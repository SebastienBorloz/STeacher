from typing import List, Dict
import json
import traceback
import os
import uuid
import re
import datetime

from openai import OpenAI, OpenAIError

import logging
LOG = logging.getLogger(__name__)



# Check if OpenAI API key is available
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    LOG.error("OPENAI_API_KEY environment variable is not set. Please set it to use the OpenAI API.")
    raise EnvironmentError("OPENAI_API_KEY environment variable is not set")

client = OpenAI()
# MODEL = "o3-mini"
MODEL = "gpt-4o"


def get_assistant_response(messages):
    ''' Call OpenAI's API with `messages`. '''
    try:
        LOG.info(f"Sending request to OpenAI API with {len(messages)} messages")
        
        # Filter messages to only include role and content fields
        filtered_messages = [{"role": msg["role"], "content": msg["content"]} for msg in messages]
        
        response = client.chat.completions.create(
            model=MODEL,
            messages=filtered_messages,
            temperature=0.7,  # some creativity
            max_completion_tokens=150
        )
        
        LOG.info("Successfully received response from OpenAI API")
        return response.choices[0].message.content.strip()
    except OpenAIError as e:
        LOG.error(f"OpenAI API error: {e}")
        raise
    except Exception as e:
        LOG.error(f"Error communicating with OpenAI API: {e}\n{traceback.format_exc()}")
        raise



def init_conversation(student_id: str, question_id: str):
    ''' Initialize the conversation with the system prompt and assistant's initial message'''
    LOG.info(f"Initializing conversation for student {student_id}, question {question_id}")

    # global system prompt
    with open(f"exercises/prompt.md", 'r', encoding='utf-8') as file:
        system_prompt = file.read()

    # add sample interactions (kind of like few-shot examples)
    # each example is separated by ---. 1st is assistant, then user, then assistant, etc. 
    for i in range(1, 20):
        if os.path.exists(f"exercises/sample{i}.txt"):
            with open(f"exercises/sample{i}.txt", 'r', encoding='utf-8') as file:
                interactions = file.read().split('---')                
                system_prompt += f"\n\nExample interaction {i}:\n```json\n"
                for j in range(len(interactions)):
                    message = interactions[j].strip()
                    # Add comma only if not the last item
                    ending = ",\n" if j < len(interactions) - 1 else "\n"
                    system_prompt += json.dumps({
                        "role": "assistant" if j % 2 == 0 else "user",
                        "content": message.strip(),
                    }, indent=2) + ending
                system_prompt += "```\n"

    # get a list of all exercices, the json files starting with a number, followed by an underscore
    exercise_ids = sorted([f.replace('.json', '') for f in os.listdir('exercises') if re.match(r'^\d+_', f) and f.endswith('.json')])
    print(f"Exercise IDs: {exercise_ids}")

    # read exercise data
    with open(f"exercises/{question_id}.json", 'r', encoding='utf-8') as file:
        exercise_data = json.load(file)

    # add additional prompt to the system prompt
    system_prompt += f'\n\n{exercise_data["additional_system_prompt"]}\n\n---\n\n'
    
    # add expected data to the system prompt
    system_prompt += f'''# Initial Exercice Data

This is the initial data for this exercise:

```json
{json.dumps(exercise_data["question"]["initial_data"], indent=2)}
```
    
# Expected Exercise Outcome

This exercise will be successfully completed when the student's solution matches one of these expected outcomes:

```json
{json.dumps(exercise_data["question"]["expected_data"], indent=2)}
```
'''

    LOG.debug(f"System prompt: {system_prompt}")
    
    messages = [
        {
            "role": "system", 
            "content": system_prompt, 
            "question_id": question_id, 
            "exercise_ids": exercise_ids,
            "student_id": student_id, 
            "uuid": str(uuid.uuid4()), 
            "question": exercise_data["question"]
        },
        {
            "role": "assistant", 
            "content": exercise_data["instructions"], 
            "uuid": str(uuid.uuid4())
        }
    ]

    db.save_messages(student_id, question_id, messages)
    return messages


def run_conversation(student_id: str, question_id: str, messages: List[Dict], question: str, hint: bool, data_and_formulas: Dict, pure_data: Dict):

    # Append a new user message to the conversation. In str format in 'content', and json otherwise
    messages.append({
        "uuid": str(uuid.uuid4()),
        "role": "user",
        "question": question,
        "hint": hint,
        "data_and_formulas": data_and_formulas,
        "pure_data": pure_data,
        "createdAt": str(datetime.utcnow().isoformat()),
        "content": f'''Hint requested: {hint}

# Student Question:

{question if question else 'No question asked.'}

# Student Excel data and formulas:
```json
{json.dumps(data_and_formulas, indent=2)}
```

# Student Excel data:
```json
{json.dumps(pure_data, indent=2)}
```

''',
    })

    # Ask assistant for feedback
    print(json.dumps(messages, indent=4))
    assistant_response = get_assistant_response(messages)
    print(f"Assistant response: {assistant_response}.")

    # Append assistant's response to the conversation
    messages.append({
        "uuid": str(uuid.uuid4()),
        "role": "assistant",
        "creator": MODEL,
        "content": assistant_response,
    })

    db.save_messages(student_id, question_id, messages)
    return messages


def save_feedback(student_id: str, question_id: str, messages: List[Dict], rating: int, feedback_text: str):
    '''The user has completed this exercice and given us a feedback. Just save it to the db. The ui will then move to the next exercise.'''

    LOG.info(f"Saving feedback for student {student_id}, question {question_id}, rating {rating}, feedback {feedback_text}")

    # Append user's feedback to the conversation    
    messages.append({
        "uuid": str(uuid.uuid4()),
        "role": "user",
        "createdAt": str(datetime.utcnow().isoformat()),
        "rating": rating,
        "feedback_text": feedback_text,
    })

    db.save_messages(student_id, question_id, messages)
    return messages