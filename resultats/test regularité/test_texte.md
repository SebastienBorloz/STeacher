# notes
Ci-dessous sont les resultats de 10 tests fait sur l'image 1 avec le prompt suivant:

```text
In this image should be math theory, with equations and annotations in french.
Your task is to transcribe it as accurately as possible. You must not use Latex code, everything in your output has to be plain text.
If you encounter what seems to be a sign error, you must transcribe it **as is** without correcting it.
You must not translate the text.
If, the image is unreadable or if the content doesn't seem to be maths, simply say [error]: {the error you encoutered}.
for example, if you didn't receive an image, return '[error]: I was not given an image.'
```

Le but était de constater ou non une régularité dans la syntaxe employée, typiquement pour des symboles mathématiques ayant plusieurs options, comme un puissance (x^-1 ou x⁻¹)

En l'occurence, les resultats different entre les reponses, ce qui etait le resultat attendu. Il serait sans doute possible de limiter cela en specifiant dans le prompt certaines notations. Baisser la temperature pourrait avoir un impact, mais
il faudrait le mesurer sur des images differentes pour en avoir le coeur net et je manque pour le moment cruellement de données.

Il est a noter que nous n'avons pas besoin de régularité sur la syntaxe a ce point du pipeline pour le fonctionnement de l'outil directement (le LLM d'aide a l'etudiant n'aura sans doute pas de probleme a faire l'equivalence entre x^-1 et x⁻¹).

Mais cette régularité sera necessaire pour un eventuel benchmark, puisqu'il nous faut un resultat comparable a une valeur objectif.


# response (1):
Le noyau de f est Ker(f) := {x appartenant à R^n | f(x) = 0}
(= f^-1(0), la préimage de 0)
Ex1) f(x) = 0, pour tout x appartenant à R^n  --->  A = 0(m,n)
Im(f) = {0}  => Ker(f) = R^n
(z) f( (x,y) ) = ( x - y , x + y )   Im(f) = { (x - y, x + y) | x,y appartenant à R }
= E x(1 1) + y (-1 1) | x,y appartenant à R }
= R^2 car (1 1) et (-1 1) sont lin. indé.
(Rem: ce sont les colonnes de A !)

Ker(f) = { (x,y) | (x-y, x+y) = (0, 0) }
      = { x - y = 0
          x + y = 0 } <=> { x = 0
                            y = 0 }


# response (2):
Le noyau de f est Ker(f) := { x⃗ ∈ Rⁿ ; f(x⃗) = 0⃗ }
(= f⁻¹ (0⃗) , la preimage de 0⃗ )
Ex : (1) f(x y) = 0⃗ , ∀ x⃗ ∈ Rⁿ → A = 0ₘ,ₙ
Im(f) := { 0⃗ } → Ker(f) = Rⁿ
(2) f(x y) = (x - y, x + y)   Im(f) = { (x - y, x + y) ! x,y ∈ R }
= { x (1 1) + y (-1 1) | x, y ∈ R }
= R²  car (1 1) et (-1 1) sont lin. indé.
(Rem : ce sont les colonnes de A !)
Ker(f) = { (x y) | (x - y, x + y) = (0 0) } = 0⃗.
{ x - y = 0  
  x + y = 0  <=> { x = 0
                   y = 0 }


# response (3):
Le noyau de f est Ker(f) := {→x ∈ Rⁿ | f(→x) = →0}
(= f⁻¹(→0), la préimage de →0)
Ex(f) {f(→x) = →0, ∀→x ∈ Rⁿ} → A = 0m,n
Im(f) := {→0} ⇒ Ker(f) = Rⁿ
(z) f(x,y) = (x - y, x + y) Im(f) = {(x-y)/(x+y)! xi, y ∈ R}
= {x(1/1) + y(-1/1) | xi, y ∈ R}
= R² car (1 1) et (-1 1) sont lin. indé.
(Rem : ce sont les colonnes de A !)
:Ker(f) = {(x/y) | (x-y)/(x+y) = (0/0)} = →0, {x - y = 0
                                               x + y = 0} <=> {x=0
                                                               y=0}


# response (4):
Le noyau de f est Ker(f) := {x⃗ ∈ R^n | f(x⃗ ) = 0⃗}
(= f^-1(0⃗), la préimage de 0⃗)
Ex: f(x y) = (x - y x + y), ∀ x⃗ ∈ R^n → A = 0m,n
Im(f) := {0⃗ } → Ker(f) = R^n
(x y)  |→  (x - y x + y)  Im(f) = {(x + y) | xi, y ∈ R}
= {x (1 -1)} + y(1 1) | xi, y ∈ R}
= R^2 car (1 -1) et (1 1) sont lin. indé.
(Rem: ce sont les colonnes de A !)
Ker(f) = {(x y) | (x - y x + y) = (0 0) = 0⃗} {x -y = 0
                           x + y = 0 <=> {x = 0
                                              y = 0


# response (5):
Le noyau de f est Ker(f) := {x⃗ ∈ R^n | f(x⃗) = 0⃗}
(= f^-1(0⃗), la préimage de 0⃗)
Ex: f(x⃗) = 0⃗, ∀x⃗ ∈ R^n → A = 0_m,n
Im(f) := {0⃗} => Ker(f) = R^n

(z) f((x/y)) = (x - y , x + y)     Im(f) = {(x - y / x + y) | x,y ∈ R}
= {x (1 / 1) + y (-1 / 1) | x,y ∈ R}
= R^2 car (1 / 1) et (-1 / 1) sont lin. indé.
(Rem: ce sont les colonnes de A!)

Ker(f) = {(x/y) | (x - y / x + y) = (0/0)} = 0⃗
{x - y = 0}
{x + y = 0} <=> {x = 0
                          y = 0}


# response (6):
Le noyau de f est Ker(f) := {→x ∈ R^n | f(→x) = →0}
(= f^-1(→0), la préimage de →0)
Ex : f(→x) = →0, ∀ →x ∈ R^n  ----->  A = 0m,n

Im(f) := {→0} => Ker(f) = R^n

(z) f (x y) = (x - y)
                   (x + y)    Im(f) = {(x - y) !
                        x,y ∈ R}
    = { x (1) + y (-1)
         (1)   (-1)  | x,y ∈ R}
= R^2 car (1) et (-1) sont lin. indé.
                             (1)
(Rem : ce sont les colonnes de A !)
Ker(f) = {(x y) | (x - y)  = (0 0)} = →0.
                          (x + y)
{x - y = 0
 x + y = 0 <=> { x = 0
                       y = 0


# response (7):
Le noyau de f est Ker(f) := { x⃗ ∈ Rⁿ | f(x⃗) = 0⃗ }
(= f⁻¹(0⃗), la préimage de 0⃗)
Ex : f(x⃗) = 0⃗ , ∀x⃗ ∈ Rⁿ  ⟶ A = 0ₘ,ₙ

Im(f) := { 0⃗ } => Ker(f) = Rⁿ

(2) f(x y) = (x - y  / x + y)   Im(f) = {(x + y) | x,y ∈ R}

= {x (1) + y (-1) | x,y ∈ R}
= R² car (1) et (-1) sont lin. indé.

(Rem: ce sont les colonnes de A!)

Ker(f) = {(x y) | (x - y / x + y) = (0 0)} = 0⃗
{ x - y = 0
  x + y = 0  <=>  { x = 0
                       y = 0 }


# response (8):
Le noyau de f est Ker(f) := { x⃗ ∈ R^n | f(x⃗) = 0⃗ }

(= f⁻¹(0⃗) , la préimage de 0⃗)

Ex: f(x⃗) = 0⃗ , ∀ x⃗ ∈ R^n  --->  A = 0_m,n

Im(f) := {0⃗} => Ker(f) = R^n

(z) f(x / y) = (x - y / x + y)   Im(f) = {(x - y / x + y) | x,y ∈ R}

= {x (1 / 1) + y (-1 / 1) | x,y ∈ R}

= R^2 car (1 / 1) et (-1 / 1) sont lin. indé.

(Rem: ce sont les colonnes de A !)

Ker(f) = {(x / y) | (x - y / x + y) = (0 / 0)} = 0⃗ .   {x - y = 0 / x + y = 0} <=> {x = 0 / y = 0}


# response (9):
Le noyau de f est Ker(f) := {x̅ ∈ Rⁿ | f(x̅) = 0̅ }
(= f^-¹(0̅), la préimage de 0̅ )
Ex : f(x̅) = 0̅ , ∀ x̅ ∈ Rⁿ ---> A = 0m,n
Im(f) := {0̅} = > Ker(f) = Rⁿ
(2) f((x,y)) = (x - y, x + y) Im(f) = { (x - y, x + y) | x,y ∈ R }
= { x ( 1 1 ) + y ( -1 1 ) | x,y ∈ R }
= R² car ( 1 1 ) et ( -1 1 ) sont lin. indé.
(Rem : ce sont les colonnes de A !)
Ker(f) := { (x,y) | (x - y, x + y) = (0,0) } = 0̅
{ x - y = 0 } <=> { x = 0
{ x + y = 0    y = 0


# response (10):
Le noyau de f est Ker(f) = { x⃗ ∈ Rⁿ | f(x⃗) = 0⃗ }
(= f⁻¹(0⃗), la préimage de 0⃗)
Ex: f(x⃗) = 0⃗, ∀ x⃗ ∈ Rⁿ    →   A = 0ₘ,ₙ
Im(f) = {0⃗} → Ker(f) = Rⁿ
(2) f( (x/y) ) = (x - y / x + y)   Im(f) = { (x - y / x + y) | x,y ∈ R }
= {x(1 / 1) + y(-1 / 1) | x,y ∈ R }
= R² car (1 / 1) et (-1 / 1) sont lin. indé.
(Rem: ce sont les colonnes de A!)
Ker(f) = {(x / y) | (x - y / x + y) = (0 / 0) } = 0⃗.
{ x - y = 0
  x + y = 0 } <=> { x=0
                   y=0 }
