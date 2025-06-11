import os
from openai import OpenAI
import base64
import cv2
import numpy as np

class LLM:
    def __init__(self, model = "gpt-4.1-mini"):
        # Check if OpenAI API key is available
        api_key = os.environ.get("OPENAI_KEY_R")
        if not api_key:
            print("OPENAI_KEY_R environment variable is not set. Please set it to use the OpenAI API.")
            raise EnvironmentError("OPENAI_KEY_R environment variable is not set")

        self.client = OpenAI(
            api_key=api_key
        )
        self.model = model


    def ask_LLM(self, input, temperature=1):
        response = self.client.responses.create(
            model=self.model,
            input=input,
            temperature=temperature
        )

        print("response:")
        print(response.output_text)

        print("yay")
        return response.output_text, response.usage


    def ask_LLM_txt(self, prompt, temperature=1):
        input = [
            {
                "role": "user",
                "content": [
                    {"type": "input_text", "text": prompt},
                ],
            }
        ]

        answer, usage = self.ask_LLM(input, temperature)
        return answer, usage

    def ask_LLM_txt_and_img(self, prompt, image, temperature=1):
        input = [
            {
                "role": "user",
                "content": [
                    {"type": "input_text", "text": prompt},
                    {"type": "input_image", "image_url":  f"data:image/jpg;base64,{image}"}
                ],
            }
        ]

        answer, usage = self.ask_LLM(input, temperature)
        return answer, usage





# test = LLM()

# prompt = "In this image should be math theory, with equations and annotations in french." \
#          "Your task is to transcribe it as accurately as possible. You must not use Latex code, everything in your output has to be plain text." \
#          "If you encounter what seems to be a sign error, you must transcribe it **as is** without correcting it." \
#          "You must not translate the text." \
#          "If, the image is unreadable or if the content doesn't seem to be maths, simply say [error]: {the error you encoutered}." \
#          "for example, if you didn't receive an image, return '[error]: I was not given an image.'"

# img_path = "./images/test1_resized.jpg"

# b64_image = img_to_b64(img_path)

# input = [
#     {
#         "role": "user",
#         "content": [
#             {"type": "input_text", "text": prompt},
#             {"type": "input_image", "image_url":  f"data:image/jpg;base64,{b64_image}"}
#         ],
#     }
# ]



# out = test.ask_LLM_txt_and_img(prompt, b64_image)

# print(out)