# notes
Ci-dessous sont les resultats de 5 tests fait sur l'image 1 avec le prompt suivant:

```text
In this image should be math theory, with equations and annotations in french.
Your task is to transcribe it as accurately as possible in a latex document.
If you encounter what seems to be a sign error, you must transcribe it **as is** without correcting it.
You must not translate the text.
If, the image is unreadable or if the content doesn't seem to be maths, simply say [error]: {the error you encoutered}.
for example, if you didn't receive an image, return '[error]: I was not given an image.'
```

Le but était de comparer la régularité dans la syntaxe employée entre le precedant test, qui faisait generer du texte et ce test-ci, qui faisait generer du latex.

En l'occurence, on observe une meilleure regularité sur la notation, ce qui est logique puisque le latex n'a pas d'alternatives sur ses notations, mais il y a des problemes de regularité ailleurs. Par exemple, l'entete des fichiers
change etonnament beaucoup (rajouts de "a4paper, 12pt" et autres) => peut etre reglé en donnant l'entete au debut du prompt.
Il change egalement la mise en page, cela devrait egalement etre reglable en donnant plus de precision au prompt.
Il faudra egalement que je verifie demain si ces codes latex sont corrects.

Il est a noter que nous n'avons pas besoin de régularité sur la syntaxe a ce point du pipeline pour le fonctionnement de l'outil directement (le LLM d'aide a l'etudiant n'aura sans doute pas de probleme a faire l'equivalence entre x^-1 et x⁻¹).

Mais cette régularité sera necessaire pour un eventuel benchmark, puisqu'il nous faut un resultat comparable a une valeur objectif.






# response (1):
```latex
\documentclass[a4paper,12pt]{article}
\usepackage{amsmath,amsfonts,amssymb}
\usepackage{geometry}
\geometry{left=2cm,right=2cm,top=2cm,bottom=2cm}

\begin{document}

Le noyau de $f$ est $\mathrm{Ker}(f) := \{\vec{x} \in \mathbb{R}^n \mid f(\vec{x})= \vec{0}\}$

$[= f^{-1}(\vec{0}),$ la préimage de $\vec{0}]$

Ex: $f(\vec{x}) = \vec{0}, \quad \forall \vec{x} \in \mathbb{R}^n \longrightarrow A = 0_{m,n}$

$\mathrm{Im}(f) := \{\vec{0}\} \quad \Rightarrow \mathrm{Ker}(f) = \mathbb{R}^n$

$\left(\begin{array}{c} x \\ y \end{array}\right) \mapsto \left(\begin{array}{c} x - y \\ x + y \end{array}\right)$ \quad $\mathrm{Im}(f) = \left\{ \left(\begin{array}{c} x - y \\ x + y \end{array}\right) \!\! \mid x,y \in \mathbb{R} \right\}$

$= \left\{ x \left(\begin{array}{c} 1 \\ 1 \end{array}\right) + y \left(\begin{array}{c} -1 \\ 1 \end{array}\right) \!\! \mid x,y \in \mathbb{R} \right\}$

$= \mathbb{R}^2$ car $\left(\begin{array}{c} 1 \\ 1 \end{array}\right)$ et $\left(\begin{array}{c} -1 \\ 1 \end{array}\right)$ sont lin. indé.

(Rem: ce sont les colonnes de $A$ !)

$\mathrm{Ker}(f) = \left\{ \left(\begin{array}{c} x \\ y \end{array}\right) \mid \left(\begin{array}{c} x - y \\ x + y \end{array}\right) = \left(\begin{array}{c} 0 \\ 0 \end{array}\right) \right\}$
$\quad \Rightarrow \left\{ \begin{array}{l} x - y = 0 \\ x + y = 0 \end{array} \right\} \Leftrightarrow \left\{ \begin{array}{l} x = 0 \\ y = 0 \end{array} \right\}$
\end{document}
```


# response (2):
```latex
\documentclass{article}
\usepackage{amsmath, amssymb}
\usepackage{amsfonts}
\usepackage{babel}

\begin{document}

Le noyau de $f$ est $\ker(f) := \{ \vec{x} \in \mathbb{R}^n \mid f(\vec{x}) = \vec{0} \}$ \\
$= f^{-1}(\vec{0}),$ la préimage de $\vec{0}$ \\
Ex : $f(\vec{x}) = \vec{0}, \forall \vec{x} \in \mathbb{R}^n \longrightarrow A = 0_{m,n}$ \\
$\mathrm{Im}(f) = \{\vec{0}\} \implies \ker(f) = \mathbb{R}^n$ \\
$\forall \begin{pmatrix} x \\ y \end{pmatrix}, f \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} x - y \\ x + y \end{pmatrix}, x,y \in \mathbb{R}$ \\
$\mathrm{Im}(f) = \left\{ \begin{pmatrix} x - y \\ x + y \end{pmatrix} \mid x,y \in \mathbb{R} \right\}$ \\
$= \left\{ x \begin{pmatrix} 1 \\ 1 \end{pmatrix} + y \begin{pmatrix} -1 \\ 1 \end{pmatrix} \mid x,y \in \mathbb{R} \right\}$ \\
$= \mathbb{R}^2$ car $\begin{pmatrix} 1 \\ 1 \end{pmatrix}$ et $\begin{pmatrix} -1 \\ 1 \end{pmatrix}$ sont lin. indé. \\
(Rem : ce sont les colonnes de $A$ !) \\
$\ker(f) = \left\{ \begin{pmatrix} x \\ y \end{pmatrix} \mid \begin{pmatrix} x - y \\ x + y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} \right\}$ \\
$\begin{cases} x - y = 0 \\ x + y = 0 \end{cases} \iff \begin{cases} x = 0 \\ y = 0 \end{cases}$

\end{document}
```


# response (3):
```latex
\documentclass{article}
\usepackage{amsmath,amssymb}

\begin{document}

Le noyau de $f$ est $\mathrm{Ker}(f) := \left\{ \vec{x} \in \mathbb{R}^n \mid f(\vec{x}) = \vec{0} \right\}$

$= f^{-1}(\vec{0})$, la préimage de $\vec{0}$

\[
\text{Ex.: } f(\vec{x}) = \vec{0}, \quad \forall \vec{x} \in \mathbb{R}^n \quad \longrightarrow \quad A = 0_{m,n}
\]

\[
\mathrm{Im}(f) := \left\{ \vec{0} \right\} \implies \mathrm{Ker}(f) = \mathbb{R}^n
\]

\[
\left(2\right) \quad f\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} x - y \\ x + y \end{pmatrix} \quad \mathrm{Im}(f) = \left\{ \begin{pmatrix} x - y \\ x + y \end{pmatrix} \mid x,y \in \mathbb{R} \right\}
\]

\[
= \left\{ x \begin{pmatrix} 1 \\ 1 \end{pmatrix} + y \begin{pmatrix} -1 \\ 1 \end{pmatrix} \mid x,y \in \mathbb{R} \right\}
\]

\[
= \mathbb{R}^2 \quad \text{car} \quad \begin{pmatrix} 1 \\ 1 \end{pmatrix} \text{ et } \begin{pmatrix} -1 \\ 1 \end{pmatrix} \text{ sont lin. indé.}
\]

(Rem: ce sont les colonnes de $A$ !)

\[
\mathrm{Ker}(f) = \left\{ \begin{pmatrix} x \\ y \end{pmatrix} \mid \begin{pmatrix} x - y \\ x + y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} \right\}
\]

\[
\begin{cases}
x - y = 0 \\
x + y = 0
\end{cases}
\iff
\begin{cases}
x = 0 \\
y = 0
\end{cases}
\]

\end{document}
```


# response (4):
```latex
\documentclass{article}
\usepackage{amsmath,amssymb}
\usepackage{amsfonts}

\begin{document}

Le noyau de $f$ est $\ker(f) := \{\vec{x} \in \mathbb{R}^n \mid f(\vec{x}) = \vec{0}\}$

$= f^{-1}(\vec{0})$, la préimage de $\vec{0}$.

Ex: $f(\vec{x}) = \vec{0}$, $\forall \vec{x} \in \mathbb{R}^n \to A = 0_{m,n}$

$\operatorname{Im}(f) := \{\vec{0}\} \implies \ker(f) = \mathbb{R}^n$

\[
f \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} x - y \\ x + y \end{pmatrix} \quad \operatorname{Im}(f) = \left\{\begin{pmatrix} x - y \\ x + y \end{pmatrix} \mid x, y \in \mathbb{R} \right\}
\]

\[
= \left\{ x \begin{pmatrix} 1 \\ 1 \end{pmatrix} + y \begin{pmatrix} -1 \\ 1 \end{pmatrix} \mid x, y \in \mathbb{R} \right\}
\]

\[
= \mathbb{R}^2 \quad \text{car} \quad \begin{pmatrix} 1 \\ 1 \end{pmatrix} \text{ et } \begin{pmatrix} -1 \\ 1 \end{pmatrix} \text{ sont lin. indé.}
\]

(Rem: ce sont les colonnes de $A$ !)

\[
\ker(f) = \left\{\begin{pmatrix} x \\ y \end{pmatrix} \mid \begin{pmatrix} x - y \\ x + y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} \right\} 
= \left\{
\begin{cases}
x - y = 0 \\
x + y = 0 
\end{cases}
\iff
\begin{cases}
x = 0 \\
y = 0 
\end{cases}
\right.
\]

\end{document}
```


# response (5):
```latex
\documentclass[a4paper,12pt]{article}
\usepackage{amsmath,amssymb}
\usepackage{amsfonts}

\begin{document}

Le noyau de \( f \) est \(\mathrm{Ker}(f) := \left\{ \vec{x} \in \mathbb{R}^n \mid f(\vec{x}) = \vec{0} \right\}\)

\[
(= f^{-1}(\vec{0}), \text{ la préimage de } \vec{0})
\]

\[
Ex.(1) \quad f(\vec{x}) = \vec{0},\, \forall \vec{x} \in \mathbb{R}^n \to A = 0_{m,n}
\]

\[
\mathrm{Im}(f) := \{\vec{0}\} \implies \mathrm{Ker}(f) = \mathbb{R}^n
\]

\[
(\forall) f\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} x - y \\ x + y \end{pmatrix} \quad \mathrm{Im}(f) = \left\{ \begin{pmatrix} x - y \\ x + y \end{pmatrix} \mid x,y \in \mathbb{R} \right\}
\]

\[
= \left\{ x \begin{pmatrix} 1 \\ 1 \end{pmatrix} + y \begin{pmatrix} -1 \\ 1 \end{pmatrix} \mid x,y \in \mathbb{R} \right\}
\]

\[
= \mathbb{R}^2, \text{ car } \begin{pmatrix} 1 \\ 1 \end{pmatrix} \text{ et } \begin{pmatrix} -1 \\ 1 \end{pmatrix} \text{ sont lin. indé.}
\]

(Rem.: ce sont les colonnes de \( A \) !)

\[
\mathrm{Ker}(f) = \left\{ \begin{pmatrix} x \\ y \end{pmatrix} \mid \begin{pmatrix} x - y \\ x + y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} \right\} 
\quad
\left\{
\begin{array}{l}
x - y = 0 \\
x + y = 0
\end{array}
\right\} 
\iff
\left\{
\begin{array}{l}
x=0 \\
y=0
\end{array}
\right.
\]

\end{document}
```
yay