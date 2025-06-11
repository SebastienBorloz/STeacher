class LLM:
	def __init__(self, input_price, cached_input_price, output_price):
		self.input_price = input_price
		self.cached_input_price = cached_input_price
		self.output_price = output_price

	def get_price(self, input_tokens, cached_input_tokens, output_tokens):
		in_price = input_tokens * self.input_price / 1000000
		ca_price = cached_input_tokens * self.cached_input_price / 1000000
		ou_price = output_tokens * self.output_price / 1000000
		return in_price + ca_price + ou_price

class LLM_use:
	def __init__(self, LLM, fix_tokens, changing_part_tokens, expected_output_tokens):
		self.LLM = LLM
		self.fix_tokens = fix_tokens
		self.changing_part_tokens = changing_part_tokens
		self.expected_output_tokens = expected_output_tokens

	def get_query_price(self, iterations):
		first_cost = self.LLM.get_price(self.fix_tokens + self.changing_part_tokens, 0, self.expected_output_tokens)
		total_cost = first_cost
		cache_tokens = self.fix_tokens + self.changing_part_tokens + self.expected_output_tokens
		for i in range(iterations - 1):
			iteration_cost = self.LLM.get_price(self.changing_part_tokens, cache_tokens, self.expected_output_tokens)
			cache_tokens += self.changing_part_tokens + self.expected_output_tokens
			total_cost += iteration_cost
		return total_cost


# models
gpt4_1 = LLM(2, 0.5, 8)
gpt4o = LLM(2.5, 1.25, 10)
gpt4o_mini = LLM(0.15, 0.075, 0.6)
gpt4_1_mini = LLM(0.4, 0.1, 1.6)
deepseek = LLM(0.55, 0.14, 2.19)


# exercisess parameters
est_questions_to_llm_per_exercise = 3
est_code_executions_per_exercise = 5
number_of_exercises = 20
est_n_students = 250


# verification du code
model = gpt4o_mini
code_verif = LLM_use(model,370,0,1)
code_verif_cost = est_code_executions_per_exercise * code_verif.get_query_price(1)
cost_verif_per_student = code_verif_cost * number_of_exercises
total_verif_cost = cost_verif_per_student * est_n_students
print("cout de verification: ", total_verif_cost)


# lecture de photo
model = gpt4_1_mini
code_verif = LLM_use(model,765,0,300)
code_verif_cost = est_code_executions_per_exercise * code_verif.get_query_price(1)
cost_verif_per_student = code_verif_cost * number_of_exercises
total_photo_cost = cost_verif_per_student * est_n_students
print("cout de lecture de photo: ", total_photo_cost)


# evaluation rubrique
model = gpt4_1_mini
code_verif = LLM_use(model,870,0,570)
rubrique_cost = est_code_executions_per_exercise * code_verif.get_query_price(1)
cost_rubrique_per_student = rubrique_cost * number_of_exercises
total_rubrique_cost = cost_rubrique_per_student * est_n_students
print("cout d'evaluation rubrique: ", total_rubrique_cost)


# LLM aide a l'etudiant
model = gpt4_1_mini
code_verif = LLM_use(model,1250,50,100)
student_help_cost = code_verif.get_query_price(est_questions_to_llm_per_exercise)
cost_student_help_per_student = student_help_cost * number_of_exercises
total_student_help_cost = cost_student_help_per_student * est_n_students
print("cout d'aide a l'etudiant: ", total_student_help_cost)


# calculs finaux
total_estimated_cost = total_student_help_cost + total_verif_cost + total_rubrique_cost + total_photo_cost

print("cout total: ", total_estimated_cost)