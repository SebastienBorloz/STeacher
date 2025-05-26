import os

def write_experience_report(exp_name, model, prompt, output):
	dir = f"./resultats/{exp_name}"
	try:
		os.mkdir(dir)
		print(f"Directory '{dir}' created successfully.")
	except Exception as e:
		print(f"An error occurred: {e}")

	template = '''# contexte
Ce test a été effectué sur {model}.
[contexte du test]

# inputs
Voici le prompt:

```text
{prompt}
```

Autres inputs:

# outputs
Voici le rendu du modele:

```text
{output}
```

Autres précisions output:

# analyse
[analyse de l'output]'''

	with open(f"{dir}/output.txt", "a") as f:
		f.write(output)

	final_text = template.format(model=model,prompt=prompt,output=output)

	with open(f"{dir}/note.md", "a") as f:
		f.write(final_text)

	print("tout bon")


write_experience_report("test report writer", "gpt-4.1-mini", "POMRPT?", "OUI OUI J'AI LU LE PROMPT\nAHAH")