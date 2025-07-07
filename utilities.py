import base64
import os

def read_file(file_path):
	"""
    Reads a text file and outputs its content

    Parameters
    ----------
    file_path : string
        Path of the file you want to read.
		

    Returns
    -------
    string
        The content of the file.
    """
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
	"""
    Replaces all parameters in {} in an input text with the input parameters of this function.

    Parameters
    ----------
    file_path : string
        First possible way of giving the text to parse, through a text file to read, will have priority if the two options are used.
    txt : string
        Second possible way of giving the text to parse, already in a string.
	**params: string
		texts to place in the inputed text, for example: 
		with the prompt being "I have just seen a {object}!", you should have an object parameter, 
		like object="bird". The output of the function will then be "I have just seen a bird!"
		

    Returns
    -------
    string
        The inputed text with params instead of the {} blocs in the text.
    """
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
	"""
	Reads an image and returns it as a b64 formatted string.

	Parameters
	----------
	img_path : string
		Path of the image you want to read.
		

	Returns
	-------
	string
		The b64 encoded image.
	"""
	with open(img_path, "rb") as image_file:
		b64_image = base64.b64encode(image_file.read()).decode("utf-8")
	return b64_image

