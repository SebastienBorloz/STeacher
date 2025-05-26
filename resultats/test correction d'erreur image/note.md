Ce test a été effectué sur gpt4.1-mini pour tester la capacité du llm a faire de la correction d'erreur sans etapes intermediaires. Je lui ai pour ca donné la consigne presente en page 4 de pdf/MA2/series_stat_annoté.pdf, les solutions presentes dans le corrigé, ainsi qu'un png de la page complete avec le corrigé.

Il faut également noter que j'ai chipé la categorisation des erreurs de MathAgent, que je trouve tres pertinente.

Voici le prompt (./prompts/prompt_step_to_step_with_image.md):

```text
# Role and style
You are an online tutor helping students with their mathematic classes. I am a french student. You answer me as concisely as possible and in french. You use language appropriate for a bachelor's degree in engineering or at my own language level, whichever is lower.

You are currently correcting an exercise you gave to me, so you use you famed correcting strategy in two steps.

The **first step** is to understand what the student did. For every line the student wrote, you must write in plain text the logic behind it, what the student must have thought when writing said line.

Once the whole logic of the resolution is clear, you can proceed to the **second step**: finding the mistakes. They can be of different natures:
VIS (Visual Perception) => The error is due to the student misreading a visual information given to him (for example, through a graph).
CAL (Calculation) => The error is due to a miscalculation of the student at some point in the line.
REAS (Reasoning) => The error is due to a wrong step in the reasoning of the student (for example, a formula used in the wrong place).
KNOW (Knowledge) => The error is due to the student seamingly missing an information about the theory behind the exercise.
MIS (Misinterpretation) => The error is due to the student misreading a textual information given to him.

I now stand before you, expecting from you your usual method of explaining:
You will give me the result of the first step, making sure you understood what I tried to do and then give me the list of my errors and their category.

---
# Input Format
- **Exercise**: The description of the exercise given to the student

- **student's resolution**: The attempt of the student at resolving the problem, given to you as a picture of the student's sheet. The picture may also contain the description of the exercise.

- **Solution**: The solution to the problem.

### Output Format
- **student's logic**: The logic of the student's resolution. For each line of the resolution, you must write a line of explanation.

- **error list**: Every mistakes the student made during his resolution. For each error, you must give the category of the error and a short description of the precise error the student made.
Example to clarify the format:
[MIS]:
You misread the description of the exercise, it was 8 apples and not 9.

---
# Inputs
## Exercise:
L'indice d'iode (x, en gI/100g) et le nombre de cétane (y, sans dimension) ont été mesurés pour différents biodiesels. Les valeurs sont reportées dans le tableau suivant:

x | 60 | 70 | 80 | 90 | 100
y | 64 | 61 | 58 | 56 | 54

(a) Calculer la moyenne de x, la moyenne de y, la variance de x, la variance de y, la covariance(x,y) et la correlation(x,y).

(b) Y a-t-il une relation linéaire entre x et y?

(c) Déterminer l'équation de la droite de régression. Dessiner les valeurs mesurées et la droite de régression sur un même graphique.

## student's resolution:
see input picture.

## problem's solution:
(a) 80, 58.6, 15.811, 3.975, -62.5, -0,9944.

(b) Oui, car la correlation entre x et y est tres proche de -1.

(c) (-0.25, 78.6)


# Output:
```

Les versions suivantes seront parsées en temps réel, celui la servait de ballon d'essai et j'ai donc ajouté les elements a la main.

Le rendu du LLM est le suivant (output.txt):

```text
**student's logic:**

- Ligne 1 : Calcul de la moyenne de x (80) et de y (58,6), puis calcul des écarts-types (s_x ≈ 15,844 et s_y ≈ 3,875). L'étudiant a voulu calculer la variance mais a écrit l'écart-type (racine de la variance).
- Ligne 2 : Calcul de la covariance entre x et y avec la formule classique, résultat -62,5.
- Ligne 3 : Calcul du coefficient de corrélation en divisant la covariance par le produit des écarts-types, résultat 0,9344 (positif).
- Ligne 4 : Réponse à la question (b) : il affirme qu'il y a une relation linéaire car la corrélation est proche de -1 (mais il a écrit 0,9344).
- Ligne 5-7 : Construction des matrices A (avec x et 1) et B (valeurs y), puis calcul de A^T A et A^T B pour résoudre le système normal des moindres carrés.
- Ligne 8-10 : Calcul de l'inverse de A^T A, multiplication par A^T B, et obtention des coefficients m et q de la droite de régression.
- Ligne 11 : Résultat final pour m et q : m = -0,25 (approximé), q = 78,6.
- Ligne 12-13 : Tracé du graphique avec les points et la droite de régression.

---

**error list:**

[CAL] : L'écart-type a été confondu avec la variance, alors que la consigne demandait la variance (s_x et s_y sont des écarts-types, pas des variances).

[CAL] : Le coefficient de corrélation calculé est positif (0,9344), alors que la covariance est négative (-62,5), ce qui est incohérent. Le signe du coefficient de corrélation doit être négatif.

[REAS] : L'étudiant conclut qu'il y a une relation linéaire car la corrélation est proche de -1, mais il a calculé une corrélation positive (0,9344). Il y a une confusion dans l'interprétation.

[CAL] : Dans le calcul matriciel, il y a une erreur dans le calcul de A^T B (le produit matriciel semble incorrect, notamment la somme des produits).

[CAL] : Le calcul final des coefficients m et q semble erroné dans la multiplication par l'inverse, donnant un résultat approximatif mais pas correct.

[MIS] : L'étudiant n'a pas respecté la consigne de calculer la variance, la covariance et la corrélation avec précision, ce qui impacte la suite.

---

En résumé, il faut revoir les calculs de variance, covariance et corrélation, vérifier les signes, et refaire proprement le calcul matriciel pour la droite de régression.
```


Bon, je me fais un peu engueuler parce que j'ai inversé les notions de covariance et d'ecart type dans ma retranscription de la consigne, ca faisait un moment que je n'avais pas eu ces notions sous les yeux.

La notion de lignes semble etre assez compliquée a suivre, peut-etre qu'il faudra trouver un autre moyen de lui faire pointer un endroit specifique du raisonnement. Il y a cela dit une vraie faute dans cette correction, l'omission d'un - a la toute fin de la ligne 2. Il a également annoncé faux le resultat de (-0.25, 78.6) qu'il a lu juste.