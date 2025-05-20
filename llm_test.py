import os
from openai import OpenAI, OpenAIError
from prompt_parsing import parse_prompt,read_file

# Check if OpenAI API key is available
api_key = os.environ.get("OPENAI_KEY_R")
if not api_key:
    print("OPENAI_KEY_R environment variable is not set. Please set it to use the OpenAI API.")
    raise EnvironmentError("OPENAI_KEY_R environment variable is not set")

client = OpenAI(
    api_key=api_key
)
# MODEL = "o3-mini"
MODEL = "gpt-4.1-mini"


# finding the error
instructions = read_file("./prompts/proto_prompt_error.md")
exercise = read_file("./prompts/exercise_example.md")
print("=========================================================================================")
print(instructions + "\n\n" + exercise)
print("=========================================================================================")
response = client.responses.create(
    model=MODEL,
    instructions=instructions,
    input=exercise,
)
print("response:")
print(response.output_text)


# helping the student
instructions = read_file("./prompts/proto_prompt_helper.md")
exercise = exercise + f"{response.output_text}\n\nTutor answer: "
print("=========================================================================================")
print(instructions + "\n\n" + exercise)
print("=========================================================================================")
response = client.responses.create(
    model=MODEL,
    instructions=instructions,
    input=exercise,
)
print("response:")
print(response.output_text)

print(response)