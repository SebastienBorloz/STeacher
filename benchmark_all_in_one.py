import os
from LLM import *
from utilities import read_file, parse_prompt
import json
import time

class all_in_one_tester:
	def __init__(self, LLM, base_path = "./exercise_resolution_dataset_aio"):
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
				# need to create the element to append it, but a simple 'current_level["image_path"] = []' would reset the array on every item
				try:
					t1 = current_level["image_path"][0]
				except:
					current_level["image_path"] = []

				try:
					if filename.endswith('.png'):
						current_level["image_path"].append(file_path)
					elif filename.endswith('.tex'):
						with open(file_path, 'r', encoding='utf-8') as f:
							current_level[filename] = f.read()
					elif filename.endswith('.json'):
						with open(file_path, 'r', encoding='utf-8') as f:
							current_level[filename] = json.load(f)
				except Exception as e:
					print(f"Error loading {file_path}: {str(e)}")
					current_level[filename] = None
		
		self.dataset = dataset_dict


	def get_llm_answer(self, prompt, image, temperature):
		return self.LLM.ask_LLM_txt_and_imgs(prompt, image, temperature)


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
						parsed_prompt = parse_prompt(txt = prompt, exercise=test["consigne.tex"], ex_num=ex_num, solution=test["solution.tex"])
						img_paths = test["image_path"]
						imgs = []
						for i in img_paths:
							imgs.append(img_to_b64(i))

						resp, usage = self.get_llm_answer(parsed_prompt, imgs, temperature)

						# for a result report json
						results[category][student][ex_num]["consigne"] = test["consigne.tex"]
						results[category][student][ex_num]["images"] = test["image_path"]
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
    # OpenAIClient("gpt-4.1"), 
    # OpenAIClient("gpt-4o"),
    # AnthropicClient("claude-opus-4-20250514"),
    # AnthropicClient("claude-sonnet-4-20250514"),
    # AnthropicClient("claude-3-7-sonnet-20250219"),
    # AnthropicClient("claude-3-5-haiku-20241022"),
    # InfNetClient("meta-llama/llama-3.2-11b-instruct"),
    # InfNetClient("qwen/qwen2.5-7b-instruct"),
    # InfNetClient("deepseek/deepseek-vl2-small"),
    # GrokClient("grok-2-vision-1212"),
    # GeminiClient("gemini-2.5-pro-preview-06-05", "low"),
	# GeminiClient("gemini-2.5-pro-preview-06-05", "medium"),
	# GeminiClient("gemini-2.5-pro-preview-06-05", "high"),
    GeminiClient("gemini-2.5-flash-preview-05-20"),
    # GeminiClient("gemini-2.0-flash"),
]

prompt = read_file("./prompts/all_in_one_with_context.md")


def run_benchmark(LLM):
	try:
		test = all_in_one_tester(LLM=LLM)
		test.benchmark(0, prompt)
		print("yay")
	except Exception as e:
		print(f"Error with {LLM.model}: {e}")


# Use ThreadPoolExecutor to run benchmarks in parallel
if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=min(10, len(LLMs))) as executor:
        executor.map(run_benchmark, LLMs)

