from openai import OpenAI
import anthropic
import os
from utilities import img_to_b64

# -------------------------------------------------------------------
# OpenAI
# -------------------------------------------------------------------
class OpenAIClient:
	def __init__(self, model):
		api_key = os.environ.get("OPENAI_KEY_R")
		self.client = OpenAI(api_key=api_key)
		self.model = model

	def ask_LLM(self, input, temperature=1):
		response = self.client.responses.create(
			model=self.model,
			input=input,
			temperature=temperature
		)

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
					{"type": "input_image", "image_url":  f"data:image/jpg;base64,{image}"},
					{"type": "input_text", "text": prompt}
				],
			}
		]

		answer, usage = self.ask_LLM(input, temperature)
		return answer, usage


# -------------------------------------------------------------------
# Anthropic
# -------------------------------------------------------------------
class AnthropicClient:
	def __init__(self, model):
		api_key = os.environ.get("ANTHROPIC_KEY_R")
		self.client = anthropic.Anthropic(api_key=api_key)
		self.model = model

	def ask_LLM(self, input, temperature, max_tokens):
		response = self.client.messages.create(
			model=self.model,
			messages=input,
			max_tokens=max_tokens,
			temperature=temperature
		)

		return response.content[0].text, response.usage

	def ask_LLM_txt(self, prompt, temperature=1, max_tokens=1000):
		input = [
			{
				"role": "user",
				"content": [
					{	
						"type": "text", 
	  					"text": prompt
					},
				],
			}
		]

		answer, usage = self.ask_LLM(input, temperature, max_tokens)
		return answer, usage

	def ask_LLM_txt_and_img(self, prompt, image, temperature=1, max_tokens=1000):
		input = [
			{
				"role": "user",
				"content": [
					{
						"type": "image",
						"source": {
							"type": "base64",
							"media_type": "image/png",
							"data": image,
						},
					},
					{
						"type": "text",
						"text": prompt
					}
				],
        	}
		]

		answer, usage = self.ask_LLM(input, temperature, max_tokens)
		return answer, usage

# -------------------------------------------------------------------
# Inference.net
# -------------------------------------------------------------------
class InfNetClient:
	def __init__(self, model):
		api_key = os.environ.get("INFERENCE_KEY_R")
		self.client = OpenAI(api_key=api_key, base_url="https://api.inference.net/v1")
		self.model = model

	def ask_LLM(self, input, temperature=1):
		response = self.client.chat.completions.create(
			model="deepseek/deepseek-vl2-small/fp-16",
			messages=input,
			temperature=temperature
		)

		return response.choices[0].message.content, response.usage


	def ask_LLM_txt(self, prompt, temperature=1):
		input = [
			{
				"role": "user",
				"content": [
					{"type": "text", "text": prompt},
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
					{
						"type": "image_url",
						"image_url": { "url": f"data:image/png;base64,{image}" }
					},
					{
						"type": "text",
						"text": prompt
					},
				]
			}
		]

		answer, usage = self.ask_LLM(input, temperature)
		return answer, usage


# -------------------------------------------------------------------
# xAI (Grok)
# -------------------------------------------------------------------
class GrokClient:
	def __init__(self, model):
		api_key = os.environ.get("GROK_KEY_R")
		self.client = OpenAI(api_key=api_key, base_url="https://api.x.ai/v1")
		self.model = model

	def ask_LLM(self, input, temperature):
		response = self.client.chat.completions.create(
			model=self.model,
			messages=input,
			temperature=temperature
		)
		return response.choices[0].message.content, response.usage
	
	def ask_LLM_txt(self, prompt, temperature=1):
		input = [
			{
				"role": "user", 
				"content": [
					{
						"type": "text",
						"text": prompt
					},
				]
			}
		]

		answer, usage = self.ask_LLM(input, temperature)
		return answer, usage

	def ask_LLM_txt_and_img(self, prompt, image, temperature=1):
		input = [
			{
				"role": "user", 
				"content": [
					{
						"type": "image_url",
						"image_url": { "url": f"data:image/png;base64,{image}" }
					},
					{
						"type": "text",
						"text": prompt
					},
				]
			}
		]

		answer, usage = self.ask_LLM(input, temperature)
		return answer, usage

# -------------------------------------------------------------------
# Gemini
# -------------------------------------------------------------------
class GeminiClient:
	def __init__(self, model, reasoning_effort=None):
		api_key = os.environ.get("GEMINI_KEY_R")
		self.client = OpenAI(api_key=api_key,base_url="https://generativelanguage.googleapis.com/v1beta/openai/")
		self.model = model
		self.reasoning_effort = reasoning_effort

	def ask_LLM(self, input, temperature):
		if self.reasoning_effort == None:
			response = self.client.chat.completions.create(
				model=self.model,
				messages=input,
				temperature=temperature
			)
		else:
			response = self.client.chat.completions.create(
				model=self.model,
				reasoning_effort=self.reasoning_effort,
				messages=input,
				temperature=temperature
			)
		return response.choices[0].message.content, response.usage

	def ask_LLM_txt(self, prompt, temperature=1):
		input = [
			{
				"role": "user", 
				"content": [
					{
						"type": "text",
						"text": prompt
					},
				]
			}
		]

		answer, usage = self.ask_LLM(input, temperature)
		return answer, usage

	def ask_LLM_txt_and_img(self, prompt, image, temperature=1):
		input = [
			{
				"role": "user", 
				"content": [
					{
						"type": "image_url",
						"image_url": { "url": f"data:image/png;base64,{image}" }
					},
					{
						"type": "text",
						"text": prompt
					},
				]
			}
		]

		answer, usage = self.ask_LLM(input, temperature)
		return answer, usage


# ==================================================================================================================================================
# tests

# prompt = "In this image should be math theory, with equations and annotations in french." \
#          "Your task is to transcribe it as accurately as possible. You must not use Latex code, everything in your output has to be plain text." \
#          "If you encounter what seems to be a sign error, you must transcribe it **as is** without correcting it." \
#          "You must not translate the text." \
#          "If, the image is unreadable or if the content doesn't seem to be maths, simply say [error]: {the error you encoutered}." \
#          "for example, if you didn't receive an image, return '[error]: I was not given an image.'"

# img_path = "./handwritten_dataset/easy/1.png"

# b64_image = img_to_b64(img_path)


# opain = OpenAIClient("gpt-4.1-mini")
# resp, usage = opain.ask_LLM_txt_and_img(prompt, b64_image)
# print("=======================")
# print(resp)
# print("=======================")
# print(usage)
# print("=======================")


# anthropik = AnthropicClient('claude-3-5-haiku-20241022')
# resp, usage = anthropik.ask_LLM_txt_and_img(prompt,b64_image)
# print("=======================")
# print(resp)
# print("=======================")
# print(usage)
# print("=======================")


# infnet = InfNetClient('deepseek/deepseek-vl2-small/fp-16')
# resp, usage = infnet.ask_LLM_txt_and_img("what's in the image",b64_image)
# print("=======================")
# print(resp)
# print("=======================")
# print(usage)
# print("=======================")


# grok = GrokClient('grok-2-vision-1212')
# resp, usage = grok.ask_LLM_txt_and_img("what's in the image",b64_image)
# print("=======================")
# print(resp)
# print("=======================")
# print(usage)
# print("=======================")


# gemini = GeminiClient('gemini-2.0-flash')
# resp, usage = gemini.ask_LLM_txt_and_img(prompt,b64_image)
# print("=======================")
# print(resp)
# print("=======================")
# print(usage)
# print("=======================")