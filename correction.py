from benchmark_error_finding import error_finding_tester
import json
from LLM import *

LLM = GeminiClient("gemini-2.5-pro-preview-06-05", "low")
test = error_finding_tester(LLM=LLM)

file_path = "./benchmark_results/error finder gemini/gemini-2.5-pro-preview-06-05-low.json"

with open(file_path, 'r', encoding='utf-8') as f:
	results_pre = json.load(f)


results = {}
for category in test.dataset:
	results[category] = {}
	for student in range(1, len(test.dataset[category])+1):
		student = str(student)
		results[category][student] = {}
		for ex_num in range(1, len(test.dataset[category][student])+1):
			ex_num = str(ex_num)
			try:
				prev = results_pre[category][student][ex_num]
				results[category][student][ex_num] = {}
				current_test = test.dataset[category][student][ex_num]

				# for a result report json
				results[category][student][ex_num]["consigne"] = current_test["consigne.tex"]
				results[category][student][ex_num]["student"] = current_test["student.tex"]
				results[category][student][ex_num]["solution"] = current_test["solution.tex"]
				results[category][student][ex_num]["prompt"] = prev["prompt"]
				results[category][student][ex_num]["response"] = prev["response"]
				results[category][student][ex_num]["errors"] = current_test["errors.json"]

			except Exception as e:
				print(f"Error")

	
try:
	with open(f"./benchmark_results/corrected.json", "w") as f:
		json.dump(results, f, indent=4)
except:
	with open(f"./benchmark_results/corrected.json", "w") as f:
		json.dump(results, f, indent=4)