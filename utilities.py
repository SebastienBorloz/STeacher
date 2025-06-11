import base64
import os

def read_file(file_path):
	try:
		with open(file_path, 'r', encoding='utf-8') as file_path:
			input = file_path.read()
		#print(f"{file_path} read successfully!")
		return input
	except FileNotFoundError:
		print(f"Error: The file '{file_path}' was not found.")
		return ""
	except Exception as e:
		print(f"An error occurred: {e}")
		return ""

def parse_prompt(file_path=None, txt=None, **params):
	input = ""
	if file_path != None:
		try:
			with open(file_path, 'r', encoding='utf-8') as file_path:
				input = file_path.read()
			print(f"{file_path} read successfully!")
		except FileNotFoundError:
			print(f"Error: The file '{file_path}' was not found.")
			return ""
		except Exception as e:
			print(f"An error occurred: {e}")
			return ""
	elif txt != None:
		input = txt
	else:
		print("Error: no input file or string was given.")

	try:
		return input.format(**params)
	except KeyError as e:
		raise KeyError(f"Missing variable for placeholder: {e}")
	

def img_to_b64(img_path):
    with open(img_path, "rb") as image_file:
        b64_image = base64.b64encode(image_file.read()).decode("utf-8")
    return b64_image


def write_experience_report(exp_name, model, prompt, output):
	dir = f"./resultats/{exp_name}"
	try:
		os.mkdir(dir)
		print(f"Directory '{dir}' created successfully.")
	except Exception as e:
		print(f"An error occurred: {e}")

	template = '''# contexte
Ce test a été effectué sur {model}.
[contexte du test]

# inputs
Voici le prompt:

```text
{prompt}
```

Autres inputs:

# outputs
Voici le rendu du modele:

```text
{output}
```

Autres précisions output:

# analyse
[analyse de l'output]'''

	with open(f"{dir}/output.txt", "a") as f:
		f.write(output)

	final_text = template.format(model=model,prompt=prompt,output=output)

	with open(f"{dir}/note.md", "a") as f:
		f.write(final_text)

	print("tout bon le rapport")






#exercise_bloc = read_file("./prompts/exercise_example.md")

#txt = parse_prompt(file_path="./prompts/proto_prompt_error.md", exercise_bloc=exercise_bloc)
#print(txt)