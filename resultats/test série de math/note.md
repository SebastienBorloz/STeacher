Ce test a été effectué sur gpt4.1-mini pour tester les nouvellement obtenus documents fournis par M. Richard.
L'image employée est un extrait de ./pdfs/MA_2/series_stat_annoté.pdf, plus precisement la page 4.

Temperature = 0

Voici le prompt (latex_gen.md):

```text
# Task and behaviour
In this image should be math theory, with equations and annotations in french.
Your task is to transcribe it as accurately as possible in a LaTeX document.

- If you encounter what seems to be a sign error, you must transcribe it **as is** without correcting it.
- You must not translate the text.
- If the image is unreadable or if the content doesn't seem to be maths, simply say [error]: {the error you encoutered}. (for example, if you didn't receive an image, return '[error]: I was not given an image.')
- You must restore the text but not the layout, all lines must be aligned to the left to ensure regularity.

# LaTeX output
```latex
\documentclass{article}
```

Le llm a rendu un code en latex qui a ensuite été converti en pdf via pdflatex pour une meileure lisibilité.

J'ai essayé, en plus d'utiliser une nouvelle input, de prendre en compte quelques problemes des precedents retours.
Le prompt est maintenant un peu plus structuré, contient une requete de stabilité du layout ainsi qu'un debut de document latex pour essayer de stabiliser l'entete, enfin, j'ai mis la temperature a 0, la aussi pour essayer de le rendre plus stable dans sa reponse.

Assez etrangement, l'output contenait le debut d'entete que j'ai ajouté au prompt, il a au moins conservé cette ligne telle quelle. Il reste quelques erreurs et problemes. Des erreurs de lecture (petites erreurs de lecture tout au long de la page, il donne a la fin un resultat qui n'apparait pas sur la page). Et ensuite quelques problemes de format, il tente a la fin de decrire le graphe.
La question se repose de la necessité de cette etape:

Ne pourrait-on pas juste lui donner l'image et lui laisser corriger directement dessus? Il semble avoir une bonne compréhension de ce qu'il lit. Cela aurait peut-etre des meilleurs resultats. Le probleme principal de fusionner ces
deux bouts de pipeline est que l'on retire de la lisibilité. Le fait de lui faire poser le texte avant de le corriger, c'etait pouvoir s'assurer qu'il voit la meme chose que nous. D'autant que je cherche ici a créer un benchmark, ce qui est beaucoup plus dur quand l'input n'est pas dans un format clair. Le faire employer directement l'image lui permettrait également de mieux gerer les cas avec une ou plusieurs illustrations ou graphiques.

