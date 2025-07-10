# STeacher
Git du projet de bachelor "STeacher". L'objectif du travail était de créer un assistant IA pour aider les étudiants avec des exercices de mathématique:
L'étudiant prend une photo de sa feuille, la photo est passée dans le pipeline et ressort en temps que réponse d'un LLM, qui va tacher de mettre l'eleve sur la bonne piste sans lui donner la reponse.

## Pipeline
1. image to LaTeX:
Un premier prompt et la photo vont etre donnés a un LLM multimodal afin de transformer le raisonnement de l'eleve en LaTeX, un language d'écriture de rapport qui nous offre un semblant de régularité syntaxique. 

2. LaTeX to error:
Un second prompt va donner a un autre LLM le raisonnement de l'eleve ainsi que la consigne et un raisonnement juste pour l'exercice, extrait d'un corrigé. En sortie, on demande au LLM de nous donner la premiere
erreur que l'eleve a fait dans son raisonnement.

3. help to the student:
Enfin, un théorique troisième prompt va donner a un LLM toutes les informations (ou une partie) obtenues par les deux premiers prompts et lui demander de les reformuler pour l'eleve afin de l'aider a corriger
sa resolution d'exercice sans lui donner la reponse.
Ce prompt n'a pas été créé ici par manque de temps.


## Travail effectué
1. 
Il s'agit d'une tache d'OCR un peu specifique et un peu plus compliquée que de la reconnaissance, puisqu'il faut egalement reformuler le tout en LaTeX. Des tests ont été effectués sur plusieurs LLMs afin d'evaluer leur competence pour ce travail. Etant donné que la tache est assez specifique (on cherche a representer les maths enseignées a la HES), j'ai composé un dataset maison a partir:
- de notes de cours et d'exercices que j'ai ecrit a l'epoque de mes cours de maths
- de notes de cours et d'exercices que m'ont fournis des camarades de classe
- de notes de cours et d'exercices que m'ont fournis des eleves de mon responsable de bachelor
- de corrigés de series de maths que m'a fourni un de professeurs de mathematiques avec qui j'ai pu discuter du projet \
*J'en profite pour remercier ici toutes les personnes qui ont eu la gentillesse de me fournir du contenu pour mon dataset!*

2. 
La seconde tache est une tache de logique plus dure techniquement et surtout plus dure a evaluer. Si j'avais eu plus de temps, j'aurais sans doute du partir sur une solution de LLM as a judge pour comparer les erreurs "réelles" et les erreurs decrites par le LLM dans sa reponse. A defaut de pouvoir mettre cela en place, j'ai verifié quelques chiffres plus faciles a verifier, notamment si le LLM trouvait les raisonnements erronés et si la ligne ou l'erreur est annoncée est la bonne.
La aussi, pour faire mon evaluation, j'ai pu composer un dataset. Celui-ci a été créé a partir d'examens de mathématiques anonymisés afin de reunir les informations que je souhaitais pour mes experiences:
- consigne de l'exercice
- un raisonnement d'eleve pour resoudre l'exercice, erroné ou non
- un raisonnement de prof pour resoudre l'exercice qui arrive a la bonne reponse \
*La aussi, mini remerciement que pas grand monde ne verra pour la confiance que l'ont m'a accordé avec ces données*


## Contenu actuel du repo
Dans le dernier commit se trouve tout le contenu pertinent, à savoir:
- handwritten_dataset:
dataset de la premiere partie (OCR), j'ai essayé de separer mes samples en difficultés, avec les easy en plus petits bouts assez clairs et intermediate et hard qui contiennent des pages completes, des ecritures plus dure a lire (en tout cas pour moi) ainsi que des "formes" de cheminement plus compliquées a lire (donc l'eleve n'est pas allé de haut en bas, le raisonnement va dans d'autres directions sur la feuille)
les samples sont numérotés dans les difficultés et contiennent (avec n = l'id du sample):
	- {n}.png: une image contenant des exercices de maths ou de la théorie, peut contenir des consignes ou autres textes en caracteres imprimés.
	- {n}.txt: un equivalent LaTeX du texte contenu dans l'image {n}.png. Il peut y avoir des irregularités qui sont malheureusement intrinseques au LaTex et que j'ai tant bien que mal essayé de gerer dans mes metriques.

- exercise_resolution_dataset:
dataset de la seconde partie (detection d'erreur), j'ai ici conservé une arborescence proche de celle qui etait en place au moment de traiter les données brutes que j'ai recu, elle n'est pas optimisée principalement par manque de temps. Si le projet doit etre continué et ce dataset employé, je recommanderais de le reorganiser. Les niveaux sont les suivants: branche de maths concernée, numéro de l'eleve, numéro de l'exercice.
Les feuilles a la base de ce dataset etaient un echantillon d'examens d'analyse et d'algebre linaire, tous les echantillons d'analyse viennent de copies du meme examen d'analyse et toutes les copies d'algebre lineaire proviennent du meme examen d'algebre linéaire. J'ai essayé d'echantilloner pour avoir des bonnes, moyennes et mauvaises performances sur ~ tous les exercices de ces deux examens. Chaque echantillon contient les elements suivants:
	- consigne.tex: la consigne de l'exercice de mathematiques que l'eleve a tenté de resoudre, en format LaTeX.
	- student.tex: la resolution de l'exercice par l'eleve, en format LaTeX.
	- solution.tex: la resolution de l'exercice par l'enseignant (tirée du corrigé), en format LaTeX.
	- errors.json: un compte rendu des erreurs relevées par l'enseignant. Si le projet devait etre continué, il s'agit ici d'une partie importante a ameliorer de ce dataset: les descriptions des erreurs sont tres limitées car je n'avais ni le temps ni un souvenir suffisant de mes cours de mathematique pour les corriger moi meme efficacement et decrire les erreurs au dela de ce que le prof a bien voulu annoter. Les erreurs de signe / de report sont assez concises mais les erreurs de raisonnement, les mauvaises utilisations d'equations, etc. qui sont plus dures a voir ne sont actuellement pas (ou mal) décrites dans ces errors.json. Je les ai quand meme annotées afin d'en verifier la position, ce qui m'a fourni un debut de reponse sur la performance d'un LLM pour cette tache.

- benchmark_results:
contient les gros rapports d'experiences faits sur les benchmarks. first bench contient les resultats de la premiere partie, second bench contient les resultats de la seconde partie. individual tests contient des petits tests supplementaires faits sur la premiere partie. all in one bench contient les resultats du test du pipeline simplifié (donc on passe directement d'une image de la feuille de l'etudiant a une detection de l'erreur).

- journal de bord:
contient un calendrier avec quelques notes sur mon occupation au cours du projet ainsi que des notes personnelles prise a mesure.

- prompts:
contient les principaux prompts utilisés. Tous les tests de la premiere partie ont été faits avec le prompt latex_gen_v3.md. les prompts commencant par "error_finding" sont des variations employées pour la seconde partie. Les prompts "all_in_one" ont été employés pour tester les performances d'un LLM sur le pipeline simplifié.

- benchmark_handwritten.py:
contient le code principal pour passer un LLM a travers le benchmark de lecture de texte et generer une output selon le format trouvable dans benchmark_results.

- benchmark_error_finding.py:
contient le code principal pour passer un LLM a travers le benchmark de detection d'erreur et generer une output selon le format trouvable dans benchmark_results.

- benchmark_all_in_one.py:
contient le code principal pour passer un LLM a travers le pipeline simplifié en employant les données de la partie 2. Celui ci n'est pas reproductible car il necessite des photos des pages des examens. Ces examens ont beau etre anonymisés dans la mesure du possible, je ne les mettrai pas directement sur ce git.

- huggingface_test.py:
contient un bout de code pour faire tourner un modele huggingface en local, avait été fait pour tester un petit modele sorti en milieu de projet et presenté comme un specialiste de l'OCR.

- LLM.py:
contient les fonctions wrappers pour faire des appels sur les differentes API.

- metrics.py:
contient le necessaire pour lire les resultats du premier benchmark et de les manipuler/plotter/analyser.

- read_results_handwritten.ipynb:
jupyter notebook brouillon qui a servi a lire et analyser les resultats du premier benchmark.

- read_results_error_finding.ipynb:
jupyter notebook brouillon qui a servi a lire et analyser les resultats du second benchmark.

- requirements:
pip freeze de fin de projet, il y a sans doute quelques librairies en trop mais il devrait y avoir tout le necessaire. (Version de python employée: 3.10.13)

- utilities.py:
quelques petites fonctions utilitaires reutilisées un peu partout (lecture de fichiers, parsing, image to 64b)


## Emploi
dans les .py de benchmark (donc benchmark_error_finding.py et benchmark_handwritten.py), creer des objets LLM pour les modeles a tester et les mettre dans la liste "LLMs". choisir le prompt dans la variable "prompt" et lancer le code.
Le code fait un thread par LLM et passe le tout a travers le benchmark. Quand un LLM a fini tous les exercices, le fichier de rapport est generé dans "./benchmark_results".
