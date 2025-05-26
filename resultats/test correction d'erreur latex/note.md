Ce test a été effectué sur gpt4.1-mini pour tester la capacité du llm a faire de la correction d'erreur. Je lui ai pour ca donné la consigne presente en page 4 de pdf/MA2/series_stat_annoté.pdf, le code latex fourni par
un des precedants tests image to latex ainsi que les solutions presentes dans le corrigé.

Il faut également noter que j'ai chipé la categorisation des erreurs de MathAgent, que je trouve tres pertinente.

Voici le prompt (./prompts/prompt_step_to_step.md):

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

- **student's resolution**: The attempt of the student at resolving the problem. It will be formatted in LaTeX.

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
(a) \quad $\overline{x} = 80$, \quad $\overline{y} = 58,6$, \quad $s_x = \sqrt{25} \approx 15,811$, \quad $s_y = \sqrt{7,58} \approx 3,875$

\[
\mathrm{Cov}(x,y) = \frac{1}{4} \sum_{i=1}^5 (x_i - 80)(y_i - 58,6) = -62,5, \quad \mathrm{Corr}(x,y) = \frac{-62,5}{62,85} = 0,9944
\]

(b) Oui car $\mathrm{Corr}(x,y)$ est très proche de $-1$.

(c)

\[
A = \begin{pmatrix}
60 & 1 \\
70 & 1 \\
80 & 1 \\
90 & 1 \\
100 & 1
\end{pmatrix}, \quad
B = \begin{pmatrix}
64 \\
61 \\
58 \\
56 \\
54
\end{pmatrix}, \quad
X = \begin{pmatrix} m \\ q \end{pmatrix}
\]

\[
A^T A = \begin{pmatrix}
60 & 70 & 80 & 90 & 100 \\
1 & 1 & 1 & 1 & 1
\end{pmatrix}
\begin{pmatrix}
60 & 1 \\
70 & 1 \\
80 & 1 \\
90 & 1 \\
100 & 1
\end{pmatrix}
= \begin{pmatrix}
33000 & 400 \\
400 & 5
\end{pmatrix}
\]

\[
(A^T A)^{-1} = \frac{1}{5000} \begin{pmatrix}
5 & -400 \\
-400 & 33000
\end{pmatrix}
\]

\[
A^T B = \begin{pmatrix}
60 & 70 & 80 & 90 & 100 \\
1 & 1 & 1 & 1 & 1
\end{pmatrix}
\begin{pmatrix}
64 \\
61 \\
58 \\
56 \\
54
\end{pmatrix}
= \begin{pmatrix}
23790 \\
293
\end{pmatrix}
\]

\[
\Rightarrow
\begin{pmatrix} m \\ q \end{pmatrix}
= \frac{1}{5000} \begin{pmatrix}
5 & -400 \\
-400 & 33000
\end{pmatrix}
\begin{pmatrix}
23790 \\
293
\end{pmatrix}
= \frac{1}{5000} \begin{pmatrix}
5 \times 23790 - 400 \times 293 \\
-400 \times 23790 + 33000 \times 293
\end{pmatrix}
= \frac{1}{5000} \begin{pmatrix}
-7250 \\
-392500
\end{pmatrix}
= \begin{pmatrix}
-1,45 \\
-78,5
\end{pmatrix}
\]

## problem's solution:
(a) 80, 58.6, 15.811, 3.975, -62.5, 0,9944.

(b) Oui, car la correlation entre x et y est tres proche de 1.

(c) (-0.25, 78.6)


# Output:
```

Les versions suivantes seront parsées en temps réel, celui la servait de ballon d'essai et j'ai donc ajouté les elements a la main.

Le rendu du LLM est le suivant (output.txt):

```text
**student's logic:**

(a)  
- Calculer la moyenne de x comme 80.  
- Calculer la moyenne de y comme 58,6.  
- Calculer l'écart-type de x en prenant la racine carrée de 25, donnant ~15,811.  
- Calculer l'écart-type de y en prenant la racine carrée de 7,58, donnant ~3,875.  
- Calculer la covariance entre x et y avec la formule \(\frac{1}{4} \sum (x_i - \overline{x})(y_i - \overline{y})\), trouvant -62,5.  
- Calculer la corrélation comme la covariance divisée par le produit des écarts-types, noté ici comme \(-62,5 / 62,85 = 0,9944\).  

(b)  
- Conclure qu'il existe une relation linéaire entre x et y car la corrélation est très proche de -1.  

(c)  
- Écrire la matrice \(A\) avec les valeurs de x et une colonne de 1, et la matrice \(B\) avec les valeurs de y.  
- Calculer \(A^T A\) en multipliant les transposées et la matrice A.  
- Calculer l'inverse de \(A^T A\) avec un déterminant donné de 5000.  
- Calculer \(A^T B\).  
- Calculer les coefficients \((m, q)\) de la droite de régression par multiplication de l'inverse avec \(A^T B\).  
- Effectuer les multiplications et les additions correspondantes, trouver \(\frac{1}{5000} \begin{pmatrix} -7250 \\ -392500 \end{pmatrix}\).  
- Donner la droite de régression avec \(m = -1,45\) et \(q = -78,5\).  

---

**error list:**

[CAL] : Erreur dans le calcul de la variance ou de l'écart-type de y. L'écart-type de y calculé devrait être \(\sqrt{7,95} \approx 2,82\) (ou dans la solution ~3,975), pas 3,875.  

[CAL] : Erreur dans le calcul du dénominateur de la corrélation. La valeur 62,85 ne correspond pas au produit des écarts-types calculés (15,811 × 3,875). Cette valeur semble incorrecte.  

[CAL] : Corrélation mal signée : la covariance est négative (-62,5), donc la corrélation doit être proche de -1, et l'étudiant a écrit 0,9944 (positif), incohérent avec le signe.  

[REAS] : La conclusion sur la relation linéaire est opposée à la valeur trouvée. L'étudiant écrit que la corrélation est proche de -1, mais dans son calcul, il s'est trompé sur le signe numérique.  

[CAL] : Calcul matriciel incorrect pour la droite de régression. Le déterminant de \(A^T A\) est correcte, mais le calcul du produit matriciel donne des résultats erronés :  
- Calcul de \(A^T B\) est correct, mais la multiplication finale donne des valeurs non cohérentes (résultats trop grands).  

[REAS] : Résultat final pour la pente \(m\) et l'ordonnée à l'origine \(q\) incohérent avec la tendance des points : la pente devrait être négative proche de -0,25 et l'ordonnée proche de 78,6 (solution donnée) et non -1,45 et -78,5 (étudiant).  

[KNOW] : On attend une représentation graphique, elle a été omise.  

---

En résumé, tes principales erreurs viennent de calculs incorrects (variance, corrélation et régression) et d'une mauvaise interprétation des signes dans la corrélation. Le fond de ta démarche est bon, mais il faut plus d'attention dans les calculs et les signes.
```

Quasiment toutes les erreurs citées par le LLM sont dues a la mauvaise lecture de l'image par la partie precedante (image to latex), et de fait, il s'agit d'un corrigé. La seule erreur qui n'en fait pas partie est la derniere, il lui manque simplement le graphe. Nous allons sans doute ignorer ce genre de problemes pour le moment et se contenter de texte.

On peut egalement noter le resumé des erreurs a la fin qui n'est pas necessaire et qui pourrait etre evitée avec une amelioration du prompt.