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
	

#exercise_bloc = read_file("./prompts/exercise_example.md")


#txt = parse_prompt(file_path="./prompts/proto_prompt_error.md", exercise_bloc=exercise_bloc)
#print(txt)