import os
from LLM import *
from utilities import read_file, parse_prompt
import json
import time

class error_finding_tester:
	def __init__(self, LLM, base_path = "./exercise_resolution_dataset"):
		self.LLM = LLM
		
		if self.LLM.model.find("/") != -1:
			self.model_name = LLM.model.split("/")[-1]
		else:
			self.model_name = LLM.model
		self.load_dataset_to_dict(base_path)
	


	def load_dataset_to_dict(self, root_dir):
		"""
		Loads the dataset structure into a nested dictionary.
		
		Args:
			root_dir (str): Path to the root directory of the dataset
		
		Returns:
			dict: Nested dictionary containing all files and their content
		"""
		dataset_dict = {}
		
		# Walk through the directory structure
		for dirpath, dirnames, filenames in os.walk(root_dir):
			# Split the path into components
			path_parts = dirpath.split(os.sep)
			
			# Skip the root directory itself
			if dirpath == root_dir:
				continue
				
			# Start building the nested structure
			current_level = dataset_dict
			for part in path_parts[len(root_dir.split(os.sep)):]:
				if part not in current_level:
					current_level[part] = {}
				current_level = current_level[part]
			
			# Add files to the current level
			for filename in filenames:
				file_path = os.path.join(dirpath, filename)
				try:
					if filename.endswith('.json'):
						with open(file_path, 'r', encoding='utf-8') as f:
							current_level[filename] = json.load(f)
					else:
						with open(file_path, 'r', encoding='utf-8') as f:
							current_level[filename] = f.read()
				except Exception as e:
					print(f"Error loading {file_path}: {str(e)}")
					current_level[filename] = None
		
		self.dataset = dataset_dict


	def get_llm_answer(self, prompt, temperature):
		return self.LLM.ask_LLM_txt(prompt, temperature)


	def benchmark(self, temperature, prompt):
		results = {}
		for category in self.dataset:
			results[category] = {}
			for student in range(1, len(self.dataset[category])+1):
				student = str(student)
				results[category][student] = {}
				for ex_num in range(1, len(self.dataset[category][student])+1):
					ex_num = str(ex_num)
					try:
						results[category][student][ex_num] = {}
						test = self.dataset[category][student][ex_num]
						parsed_prompt = parse_prompt(txt=prompt,exercise=test["consigne.tex"], student_res=test["student.tex"], solution=test["solution.tex"])
						resp, usage = self.get_llm_answer(parsed_prompt, temperature)

						# for a result report json
						results[category][student][ex_num]["consigne"] = test["consigne.tex"]
						results[category][student][ex_num]["student"] = test["student.tex"]
						results[category][student][ex_num]["solution"] = test["solution.tex"]
						results[category][student][ex_num]["prompt"] = prompt
						results[category][student][ex_num]["response"] = resp
						results[category][student][ex_num]["errors"] = test["errors.json"]

						print(f"fini {category}:{student}:{ex_num} for {self.LLM.model}")
						print(usage)
						time.sleep(1)
					except Exception as e:
						print(f"Error with {self.LLM.model}, test {category}:{ex_num}: {e}")
						time.sleep(1)

		try:
			with open(f"./benchmark_results/{self.model_name}-{self.LLM.reasoning_effort}.json", "w") as f:
				json.dump(results, f, indent=4)

		except:
			with open(f"./benchmark_results/{self.model_name}.json", "w") as f:
				json.dump(results, f, indent=4)



# ===============================================================================================================================
# main benchmark

import concurrent.futures

LLMs = [
    OpenAIClient("gpt-4.1"), 
    OpenAIClient("gpt-4o"),
    AnthropicClient("claude-opus-4-20250514"),
    AnthropicClient("claude-sonnet-4-20250514"),
    AnthropicClient("claude-3-7-sonnet-20250219"),
    AnthropicClient("claude-3-5-haiku-20241022"),
    InfNetClient("meta-llama/llama-3.2-11b-instruct"),
    InfNetClient("qwen/qwen2.5-7b-instruct"),
    InfNetClient("deepseek/deepseek-vl2-small"),
    GrokClient("grok-2-vision-1212"),
    GeminiClient("gemini-2.5-pro-preview-06-05", "low"),
	GeminiClient("gemini-2.5-pro-preview-06-05", "medium"),
	GeminiClient("gemini-2.5-pro-preview-06-05", "high"),
    GeminiClient("gemini-2.5-flash-preview-05-20"),
    GeminiClient("gemini-2.0-flash"),
]

prompt = read_file("./prompts/error_finding_v3+correc.md")


def run_benchmark(LLM):
    try:
        test = error_finding_tester(LLM=LLM)
        test.benchmark(0, prompt)
    except Exception as e:
        print(f"Error with {LLM.model}: {e}")


# Use ThreadPoolExecutor to run benchmarks in parallel
if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=min(10, len(LLMs))) as executor:
        executor.map(run_benchmark, LLMs)


# ===============================================================================================================================
# single test

# LLMs = [
#     OpenAIClient("gpt-4.1"), 
#     OpenAIClient("gpt-4o"),
#     AnthropicClient("claude-opus-4-20250514"),
#     AnthropicClient("claude-sonnet-4-20250514"),
#     AnthropicClient("claude-3-7-sonnet-20250219"),
#     AnthropicClient("claude-3-5-haiku-20241022"),
#     InfNetClient("meta-llama/llama-3.2-11b-instruct"),
#     InfNetClient("qwen/qwen2.5-7b-instruct"),
#     InfNetClient("deepseek/deepseek-vl2-small"),
#     GrokClient("grok-2-vision-1212"),
#     GeminiClient("gemini-2.5-pro-preview-06-05", "low"),
# 	GeminiClient("gemini-2.5-pro-preview-06-05", "medium"),
# 	GeminiClient("gemini-2.5-pro-preview-06-05", "high"),
#     GeminiClient("gemini-2.5-flash-preview-05-20"),
#     GeminiClient("gemini-2.0-flash"),
# ]

# LLM = InfNetClient("deepseek/deepseek-vl2")
# difficulty = "intermediate"
# test_num = 6

# prompt = read_file("./prompts/latex_gen_v3.md")


# results = {}
# results[difficulty] = {}

# try:
# 	results[difficulty][test_num] = {}
# 	tester = error_finding_tester(LLM=LLM)
# 	test = tester.dataset[difficulty][test_num]

# 	img_path = test["image_path"]
# 	b64_img = img_to_b64(img_path)

# 	resp, usage = tester.get_llm_answer(prompt, b64_img, 0)
# 	y = test["expected_output"]
# 	dist, clean_resp, clean_sol = tester.evaluate_response(resp, y)

# 	# for a result report json
# 	results[difficulty][test_num]["image"] = test["image_path"]
# 	results[difficulty][test_num]["prompt"] = prompt
# 	results[difficulty][test_num]["score"] = dist
# 	results[difficulty][test_num]["response"] = resp
# 	results[difficulty][test_num]["clean_response"] = clean_resp
# 	results[difficulty][test_num]["solution"] = test["expected_output"]
# 	results[difficulty][test_num]["clean_solution"] = clean_sol
# 	#results[difficulty][test_num]["usage"] = usage
# 	print(f"fini {difficulty}:{test_num} for {tester.LLM.model}")
# 	print(usage)

# 	with open(f"./single_test_{tester.model_name}.json", "w") as f:
# 		json.dump(results, f, indent=4)

# except Exception as e:
# 	print(f"Error: {e}")