import jaro
import os
from LLM import *
from utilities import read_file
import json
import time

class handwritten_tester:
	def __init__(self, LLM, base_path = "./handwritten_dataset"):
		self.LLM = LLM
		
		if self.LLM.model.find("/") != -1:
			self.model_name = LLM.model.split("/")[-1]
		else:
			self.model_name = LLM.model
		self.load_dataset(base_path)
	

	def load_dataset(self, base_path):
		dataset = {}

		for difficulty in ['easy', 'intermediate', 'hard']:
			difficulty_path = os.path.join(base_path, difficulty)
			if not os.path.isdir(difficulty_path):
				continue

			samples = {}
			for filename in sorted(os.listdir(difficulty_path)):
				file_id, ext = os.path.splitext(filename)
				if ext not in ['.png', '.txt']:
					continue

				file_path = os.path.join(difficulty_path, filename)
				if file_id not in samples:
					samples[file_id] = {}

				if ext == '.png':
					samples[file_id]['image_path'] = file_path
				elif ext == '.txt':
					with open(file_path, 'r', encoding='utf-8') as f:
						samples[file_id]['expected_output'] = f.read().strip()

			dataset[difficulty] = list(samples.values())

		self.dataset = dataset


	def get_llm_answer(self, prompt, image, temperature):
		return self.LLM.ask_LLM_txt_and_img(prompt, image, temperature)


	def _replace_element_from_2s(self, response, solution, element, replacement=""):
		resp_clear = response.replace(element, replacement)
		sol_clear = solution.replace(element, replacement)
		return resp_clear, sol_clear


	def evaluate_response(self, response, solution):
		try:
			response = response.split(r"\begin{document}")[1]
			response = response.split(r"\end{document}")[0]
		except:
			response = response

		try:	
			solution = solution.split(r"\begin{document}")[1]
			solution = solution.split(r"\end{document}")[0]
		except:
			solution = solution	
		
		response, solution = self._replace_element_from_2s(response,solution, r"\quad")
		response, solution = self._replace_element_from_2s(response,solution, r" ")
		response, solution = self._replace_element_from_2s(response,solution, "\n")
		response, solution = self._replace_element_from_2s(response,solution, r"\left|", "|")
		response, solution = self._replace_element_from_2s(response,solution, r"\right|", "|")
		response, solution = self._replace_element_from_2s(response,solution, r"\left(", "(")
		response, solution = self._replace_element_from_2s(response,solution, r"\left)", ")") 
		response, solution = self._replace_element_from_2s(response,solution, r"\Rightarrow", r"\implies")
		response, solution = self._replace_element_from_2s(response,solution, r"\times", r"\cdot")

		#print("clear response: \n", response)
		#print("clear solution: \n", solution)
		dist = jaro.jaro_winkler_metric(response, solution)

		return dist, response, solution
	

	def benchmark(self, difs, temperature, prompt):
		results = {}
		for difficulty in self.dataset:
			if difficulty in difs:
				results[difficulty] = {}
				for test_num in range(len(self.dataset[difficulty])):
					try:
						results[difficulty][test_num] = {}
						test = self.dataset[difficulty][test_num]

						img_path = test["image_path"]
						b64_img = img_to_b64(img_path)
						resp, usage = self.get_llm_answer(prompt, b64_img, temperature)
						y = test["expected_output"]
						dist, clean_resp, clean_sol = self.evaluate_response(resp, y)

						# for a result report json
						results[difficulty][test_num]["image"] = test["image_path"]
						results[difficulty][test_num]["prompt"] = prompt
						results[difficulty][test_num]["score"] = dist
						results[difficulty][test_num]["response"] = resp
						results[difficulty][test_num]["clean_response"] = clean_resp
						results[difficulty][test_num]["solution"] = test["expected_output"]
						results[difficulty][test_num]["clean_solution"] = clean_sol
						#results[difficulty][test_num]["usage"] = usage
						print(f"fini {difficulty}:{test_num} for {self.LLM.model}")
						print(usage)
						time.sleep(2)
					except Exception as e:
						print(f"Error with {self.LLM.model}, test {difficulty}:{test_num}: {e}")
						time.sleep(2)

		try:
			with open(f"./benchmark_results/{self.model_name}-{self.LLM.reasoning_effort}.json", "w") as f:
				json.dump(results, f, indent=4)

		except:
			with open(f"./benchmark_results/{self.model_name}.json", "w") as f:
				json.dump(results, f, indent=4)


# ===============================================================================================================================

# LLMs = [
# 	OpenAIClient("gpt-4.1-mini"), 
# 	OpenAIClient("gpt-4.1"), 
# 	OpenAIClient("gpt-4o"),
# 	AnthropicClient("claude-opus-4-20250514"),
# 	AnthropicClient("claude-sonnet-4-20250514"),
# 	AnthropicClient("claude-3-7-sonnet-20250219"),
# 	AnthropicClient("claude-3-5-haiku-20241022"),
# 	InfNetClient("meta-llama/llama-3.2-11b-instruct"),
# 	InfNetClient("qwen/qwen2.5-7b-instruct"),
# 	InfNetClient("deepseek/deepseek-vl2-small"),
# 	GrokClient("grok-2-vision-1212"),
# 	GeminiClient("gemini-2.5-pro-preview-06-05"),
# 	GeminiClient("gemini-2.5-flash-preview-05-20"),
# 	GeminiClient("gemini-2.0-flash"),
# ]

# foired = []

# for LLM in LLMs:
# 	try:
# 		test = handwritten_tester(LLM=LLM)
# 		prompt = read_file("./prompts/latex_gen_v3.md")
# 		test.benchmark(["easy", "intermediate", "hard"],0,prompt)
# 	except:
# 		foired.append(LLM.model)
# 		print(f"y a eu un probleme avec le {LLM.model} chef")

# print("on a fini chef, vla les modeles qui ont foiré:")
# print(foired)




import concurrent.futures

LLMs = [
    # OpenAIClient("gpt-4.1"), 
    # OpenAIClient("gpt-4o"),
    AnthropicClient("claude-opus-4-20250514"),
    AnthropicClient("claude-sonnet-4-20250514"),
    AnthropicClient("claude-3-7-sonnet-20250219"),
    AnthropicClient("claude-3-5-haiku-20241022"),
    # InfNetClient("meta-llama/llama-3.2-11b-instruct"),
    # InfNetClient("qwen/qwen2.5-7b-instruct"),
    # InfNetClient("deepseek/deepseek-vl2-small"),
    # GrokClient("grok-2-vision-1212"),
    # GeminiClient("gemini-2.5-pro-preview-06-05", "low"),
	# GeminiClient("gemini-2.5-pro-preview-06-05", "medium"),
	# GeminiClient("gemini-2.5-pro-preview-06-05", "high"),
    # GeminiClient("gemini-2.5-flash-preview-05-20"),
    # GeminiClient("gemini-2.0-flash"),
]

prompt = read_file("./prompts/latex_gen_v3.md")

def run_benchmark(LLM):
    try:
        test = handwritten_tester(LLM=LLM)
        test.benchmark(["easy", "intermediate", "hard"], 0, prompt)
    except Exception as e:
        print(f"Error with {LLM.model}: {e}")

#run_benchmark(GeminiClient("gemini-2.5-pro-preview-06-05", "medium"))

# Use ThreadPoolExecutor to run benchmarks in parallel
if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=min(10, len(LLMs))) as executor:
        executor.map(run_benchmark, LLMs)