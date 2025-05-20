Ces deux tests ont été faits sur l'api openai pour valider le fonctionnement de l'inclusion d'images dans les appels api. Les deux images sont test1_resized.jpg et test2_resized.jpg dans le dossier images.

Voici le prompt:

In this image should be math theory, with equations and annotations in french.
Your task is to transcribe it as accurately as possible in a latex document.
If you encounter what seems to be a sign error, you must transcribe it **as is** without correcting it.
You must not translate the text.
If, the image is unreadable or if the content doesn't seem to be maths, simply say [error]: {the error you encoutered}.
for example, if you didn't receive an image, return '[error]: I was not given an image.'


le llm a rendu un code en latex qui a ensuite été converti en pdf via pdflatex pour une meilleur lisibilité.

les resultats sont toujours aussi encourageants que sur le site (encore heureux), ce test etait sur 4.1 mini afin de limiter les couts si je faisais une betise, et meme ce modele "mini" donne deja des signes prometteurs. Il reste quelques erreurs 
qui seront interessantes a etudier avec un benchmark plus complet, mais c'est tout ce que je peux faire en attendant de recevoir une reponse de M. Richard.