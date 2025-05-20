import os
from openai import OpenAI, OpenAIError
from prompt_parsing import parse_prompt,read_file
import base64
import cv2
import numpy as np


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


prompt = "In this image should be math theory, with equations and annotations in french." \
"Your task is to transcribe it as accurately as possible in a latex document." \
"If you encounter what seems to be a sign error, you must transcribe it **as is** without correcting it." \
"You must not translate the text." \
"If, the image is unreadable or if the content doesn't seem to be maths, simply say [error]: {the error you encoutered}." \
"for example, if you didn't receive an image, return '[error]: I was not given an image.'"

# img = cv2.imread('./images/test2.jpg')
# dim = img.shape[:2]

# big_side = max(dim)
# resized_dim = (int(dim[1]/big_side*2048), int(dim[0]/big_side*2048))

# res = cv2.resize(img, dsize=resized_dim, interpolation=cv2.INTER_CUBIC)
# cv2.imwrite("./images/test2_resized.jpg", res)


with open("./images/test2_resized.jpg", "rb") as image_file:
    b64_image = base64.b64encode(image_file.read()).decode("utf-8")


response = client.responses.create(
    model=MODEL,
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": prompt},
                {"type": "input_image", "image_url":  f"data:image/jpg;base64,{b64_image}"}
            ],
        }
    ],
)


print("response:")
print(response.output_text)

print("yay")