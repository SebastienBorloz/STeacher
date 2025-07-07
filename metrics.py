import os
import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from natsort import natsorted
import jaro
import re
import random

CATEGORY_ORDER = ['easy', 'intermediate', 'hard']

class results:
	def __init__(self, data_dir):
		self.df = self._results_to_pandas(data_dir)


	def _results_to_pandas(self, data_dir):
		# Dossier contenant les JSON
		files = [f for f in os.listdir(data_dir) if f.endswith(".json")]

		# Liste pour stocker chaque ligne
		rows = []

		for file in files:
			model_name = file.replace(".json", "")
			with open(os.path.join(data_dir, file), "r") as f:
				data = json.load(f)
				for category, tests in data.items():
					for test_id, test_content in tests.items():
						row = {
							"model": model_name,
							"category": category,
							"test_id": test_id,
						}

						# Ajouter tous les champs du test à la ligne
						row.update(test_content)
						rows.append(row)


		# Créer le DataFrame final
		df_all_tests = pd.DataFrame(rows)

		# Construire un identifiant unique pour chaque test
		df_all_tests["test_key"] = df_all_tests["category"] + "_" + df_all_tests["test_id"].astype(str)

		# Ordonner les colonnes
		first_cols = ["test_key", "model", "category", "test_id"]
		other_cols = [col for col in df_all_tests.columns if col not in first_cols]
		df_all_tests = df_all_tests[first_cols + other_cols]

		return df_all_tests


	def order_df(self, df_to_sort):
		# Trier les colonnes selon l'ordre easy → intermediate → hard
		ordered_columns = []

		# Ranger d'abord par category puis par "natsorted" qui permet d'avoir d'eviter l'ordre alphabetique standard qui met le easy_10 entre easy_1 et easy_2
		for cat in CATEGORY_ORDER:
			cols = [col for col in df_to_sort.columns if col.startswith(cat)]
			ordered_columns.extend(natsorted(cols))

		return ordered_columns


	def add_metric(self, metric_function, mean_med = True):
		# Nom de la fonction de metrique
		new_line_name = metric_function.__name__

		# Appliquer la metrique
		self.df[new_line_name] = self.df.apply(
			lambda row: metric_function(row),
			axis=1
		)

		# Créer une matrice modèle × test
		self.df = self.df.pivot(index="model", columns="test_key", values=new_line_name)
		self.df = self.df[self.order_df(self.df)]

		# Ajouter colonnes moyenne et médiane si demandées
		if mean_med:
			self.df[new_line_name + "_mean"] = self.df.mean(axis=1)
			self.df[new_line_name + "_median"] = self.df.median(axis=1)


	def add_separation(self, group1, group2 = [], mean_med = True):
		# Filtrer celles qui existent bien dans les colonnes
		group_1_col = [col for col in self.df.columns if col in group1]
		
		# Colonnes restantes
		if len(group2) == 0:
			# Si groupe 2 pas spécifié, utiliser tout ce qui n'est pas dans le groupe 1
			group_2_col = [col for col in self.df.columns if col not in group1]
		else:
			group_2_col = [col for col in self.df.columns if col in group2]

		# Ajouter colonnes moyennes et médianes si demandées
		if mean_med:
			# Ajouter les deux moyennes
			self.df["group_1_mean"] = self.df[group_1_col].mean(axis=1)
			self.df["group_2_mean"] = self.df[group_2_col].mean(axis=1)

			# Ajouter les deux medianes
			self.df["group_1_median"] = self.df[group_1_col].median(axis=1)
			self.df["group_2_median"] = self.df[group_2_col].median(axis=1)


	def sort_rows(self, col, ascending=False):
		# Ranger les lignes en fonction des valeurs d'une colonne col
		self.df = self.df.sort_values(by=col, ascending=ascending)


	def display_metric(self, title, group1 = [], group2 = []):
		if len(group1) != 0:
			group_1_col = self.order_df(self.df[group1])

			if len(group2) == 0:
				# Si groupe 2 pas spécifié, utiliser tout ce qui n'est pas dans le groupe 1
				group2 = [col for col in self.df.columns if col not in group1]
			
			group_2_col = self.order_df(self.df[group2])

			an_col = [col for col in self.df.columns if col.startswith("group_")]

			ordered_col = group_1_col + group_2_col + an_col
			self.df = self.df[ordered_col]
			print(ordered_col)

		# Générer la heatmap
		plt.figure(figsize=(22, len(self.df) * 0.8))
		sns.heatmap(self.df, annot=True, fmt=".2f", cmap="RdYlGn", cbar=True)

		if len(group1) != 0:
			reds = []
			for i in group1:
				reds.append(f"{i[0]}-{i[1]}")

			ax = plt.gca()  # get current axes
			for label in ax.get_xticklabels():
				if label.get_text() in group1:
					label.set_color("red")
					label.set_fontweight("bold")


		# Titres et axes
		plt.title(title, fontsize=16)
		plt.xlabel("Tests", fontsize=12)
		plt.ylabel("Modeles", fontsize=12)
		plt.xticks(rotation=90)
		plt.tight_layout()
		plt.show()


def _replace_element(text, element, replacement=""):
	#if replacement == "":
	#	replacement = len(element) * " "
	text_clear = text.replace(element, replacement)
	return text_clear


def _replace_element_reg(text, element, replacement=""):
	text_clear = re.sub(element, replacement, text)
	return text_clear


def standardize_text(text):
	try:
		text = text.split(r"\begin{document}")[1]
		text = text.split(r"\end{document}")[0]
	except:
		text = text
	
	text = _replace_element(text, r" ")
	text = _replace_element(text, r"\quad")
	text = _replace_element(text, r"\qquad")
	text = _replace_element(text, "\n")
	text = _replace_element(text, r"\cancel")
	text = _replace_element(text, r"\checkmark")
	text = _replace_element(text, r"\textbf")
	text = _replace_element(text, r"\text")
	text = _replace_element(text, r"\underline")
	text = _replace_element(text, r"\boxed")
	text = _replace_element(text, r"\begin")
	text = _replace_element(text, r"\end")
	text = _replace_element(text, r"\left|", "|")
	text = _replace_element(text, r"\right|", "|")
	text = _replace_element(text, r"\mid", "|")
	text = _replace_element(text, r"\Big|", "|")
	text = _replace_element(text, r"\left(", "(")
	text = _replace_element(text, r"\right)", ")") 
	text = _replace_element(text, r"\left[", "[")
	text = _replace_element(text, r"\right]", "]") 
	text = _replace_element(text, r"\left{", "{")
	text = _replace_element(text, r"\right}", "{") 
	text = _replace_element(text, r"\Rightarrow", r"⇒")
	text = _replace_element(text, r"\implies", r"⇒")
	text = _replace_element(text, r"\times", r"*")
	text = _replace_element(text, r"\cdot", r"*")

	return text
	

def metric_standardized_text(row):	
	response = row["response"]
	solution = row["solution"]
	response = standardize_text(response)
	solution = standardize_text(solution)

	# print("=====================================================================================")
	# print("comparing:")
	# print(response+"\n\n")
	# print(solution)
	# print("=====================================================================================")

	dist = jaro.jaro_winkler_metric(response, solution)

	return dist


def metric_math_filter(row):
	def remove_anything_not_maths(txt):
		# reg = r"([\d\+\=\-\^{( ]+\w{1,3}[\d\+\=\-\^}) ]|pmatrix|\\frac|\\vec|\\sqrt|\\cdot|[\d\+\=\-\^(){}])"
		# x = re.findall(reg, txt)
		txt = _replace_element_reg(txt, "([\w',.]{10,})")
		txt = _replace_element_reg(txt, r"{+}+")
		return txt

	response = row["response"]
	solution = row["solution"]

	if type(response) == str and type(solution) == str:
		response_st = standardize_text(response)
		solution_st = standardize_text(solution)

		response = remove_anything_not_maths(response_st)
		#response = ' '.join(response)
		solution = remove_anything_not_maths(solution_st)
		#solution = ' '.join(solution)

		dist = jaro.jaro_winkler_metric(response, solution)

		if random.random() >= 0.99:
			# random choice to compare
			print("=====================================================================================")
			print(f"test: {row['model']}, {row['test_id']}")
			print("initial:")
			print(row["response"]+"\n")
			print(row["solution"])
			print("=====================================================================================")
			print("transformed:")
			print(response_st+"\n")
			print(solution_st)
			print("=====================================================================================")
			print("comparing:")
			print(response+"\n")
			print(solution)
			print("=====================================================================================")
			print("distance:")
			print(dist)
			print("=====================================================================================")
		
		return dist
	else:
		return None