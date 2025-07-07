from LLM import *
from utilities import read_file
import os


LLM = GeminiClient("gemini-2.5-flash-preview-05-20")

prompt = read_file("./prompts/latex_gen_v3.md")

# Racine de l'arborescence
dir_top = "./exercise_resolution_dataset/An_sol"



# Parcourir récursivement les dossiers
for root, dirs, files in os.walk(dir_top):
	for file in files:
		if file.endswith(".png"):
			image_path = os.path.join(root, file)
			
			print(f"Started writing first draft for {image_path}...")

			try:
				# Transformer l'image
				b64_img = img_to_b64(image_path)

				# requete au LLM
				resp, usage = LLM.ask_LLM_txt_and_img(prompt, b64_img, 0)

				# Créer le chemin du fichier .txt
				base_name = os.path.splitext(file)[0]
				txt_path = os.path.join(root, f"{base_name}.txt")

				# Écrire le résultat dans le fichier texte
				with open(txt_path, "w", encoding="utf-8") as f:
					f.write(resp)
				
				print(f"Finished writing first draft for {image_path}!")

			except Exception as e:
				print(f"Failed to write for file {image_path}: {e}")