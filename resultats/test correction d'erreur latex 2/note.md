Ce test a été effectué sur gpt4.1-mini pour tester la capacité du llm a faire de la correction d'erreur. Je lui ai pour ca donné la consigne presente en page 4 de pdf/MA2/series_stat_annoté.pdf, le code latex fourni par
un des precedants tests image to latex ainsi que les solutions presentes dans le corrigé.

**Par rapport au precedant test**, j'ai pris la peine de corriger les erreurs de lecture afin d'évaluer le llm sur sa capacité a trouver les erreurs dans un latex parfait, au lieu d'un latex bourré de fautes de lecture.

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

(a) Calculer la moyenne de x, la moyenne de y, l'écart-type de x, l'écart-type de y, la covariance(x,y) et la correlation(x,y).

(b) Y a-t-il une relation linéaire entre x et y?

(c) Déterminer l'équation de la droite de régression. Dessiner les valeurs mesurées et la droite de régression sur un même graphique.

## student's resolution:
(a) \quad $\overline{x} = 80$, \quad $\overline{y} = 58,6$, \quad $s_x = \sqrt{250} \approx 15,811$, \quad $s_y = \sqrt{15,8} \approx 3,975$

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
23190 \\
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
23190 \\
293
\end{pmatrix}
= \frac{1}{5000} \begin{pmatrix}
-1250 \\
-393000
\end{pmatrix}
= \begin{pmatrix}
-0,25 \\
78,6
\end{pmatrix}
\]

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

(a)  
- Il calcule la moyenne de x (notée \(\overline{x}\)) comme étant 80.  
- Il calcule la moyenne de y (notée \(\overline{y}\)) comme étant 58,6.  
- Il calcule l'écart-type de x en utilisant \(\sqrt{250} \approx 15,811\).  
- Il calcule l'écart-type de y en utilisant \(\sqrt{15,8} \approx 3,975\).  
- Il calcule la covariance selon la formule avec la somme des produits des écarts : \(\mathrm{Cov}(x,y) = \frac{1}{4} \sum (x_i - \overline{x})(y_i - \overline{y}) = -62,5\).  
- Il calcule le coefficient de corrélation en divisant la covariance par le produit des écarts-types (62,85), mais obtient 0,9944.

(b)  
- Il conclut à l’existence d’une relation linéaire car la corrélation est très proche de \(-1\).

(c)  
- Il construit la matrice \(A\) avec les valeurs de x et un vecteur colonne de 1 pour l'ordonnée à l'origine.  
- Il construit le vecteur \(B\) avec les valeurs y.  
- Il calcule \(A^T A\) (matrice transposée fois matrice \(A\)).  
- Il calcule l'inverse \((A^T A)^{-1}\).  
- Il calcule \(A^T B\).  
- Il multiplie \((A^T A)^{-1}\) par \(A^T B\) pour obtenir le vecteur \(X = (m, q)^T\).  
- Il conclut que la droite de régression est \(y = -0,25 x + 78,6\).

---

**error list:**

[CAL] : Le calcul de la corrélation est erroné. La covariance est négative et la corrélation doit être proche de \(-0,9944\), donc le signe est incorrect (il écrit \(0,9944\) positif).  
[CAL] : Le dénominateur de la corrélation est mal calculé ou mal utilisé. Pour la corrélation, on divise par \(s_x s_y\), soit \(15,811 \times 3,975 = 62,85\), mais la valeur donnée semble fausse pour \(s_y\) (car \(\sqrt{15,8} \approx 3,975\) est correct, mais ce n’est pas cohérent avec la covariance donnée).  
[REAS] : Dans la conclusion (b), il affirme que la corrélation est proche de \(-1\), mais dans sa résolution il a mis un résultat positif \(0,9944\). Cela montre une incohérence de raisonnement par rapport au signe.  
[CAL] : L'inversion de la matrice \((A^T A)^{-1}\) est correcte, mais la multiplication finale donne \(\begin{pmatrix} -1250 \\ -393000 \end{pmatrix}\), qui divisé par 5000 donne \(\begin{pmatrix} -0,25 \\ -78,6 \end{pmatrix}\), or l’étudiant met \(q=78,6\) au lieu de \(-78,6\), erreur de signe.  
[REAS] : L’interprétation finale de la constante \(q\) dans la droite de régression est erronée (le signe doit être négatif).

En résumé, les principales erreurs sont dans la gestion des signes pour la corrélation et pour l'ordonnée à l'origine de la droite de régression, et une légère confusion dans le calcul des valeurs statistiques.
```

Le format est pour le moment un peu inconsistent, mais ce n'est un probleme que pour l'evaluation. Dans un cas du futur pipeline, tout ceci serait donné a un dernier LLM pour le reformuler comme une aide sans donner la reponse et on peut donc se permettre une certaine fluidité dans la mise en page.

Il semble essayer de faire des corrections sur des reponses justes, une fois en inventant un signe moins dans la solution et une fois avec une phrase que je ne suis pas sur de comprendre (2eme erreur). 
La premiere erreur est la seule vrai erreur du document.

