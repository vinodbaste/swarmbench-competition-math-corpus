## Problem

Six points $A, B, C, D, E,$ and $F$ lie in a straight line in that order. Suppose that $G$ is a point not on the line and that $AC=26, BD=22, CE=31, DF=33, AF=73, CG=40,$ and $DG=30.$ Find the area of $\triangle BGE.$

## Solution 1

[asy] pair A,B,C,D,E,F,G; A=(0,0); label("$A$", A, S); B=(1.5,0); label("$B$", B, S); C=(2.9,0); label("$C$", C, S); D=(4.2,0); label("$D$", D, S); E=(5.3,0); label("$E$", E, S); F=(6.5,0); label("$F$", F, S); G=(3.7,3); label("$G$", G, N);  draw(A--B--C--D--E--F); draw(C--G--D); draw(B--G--E); [/asy]

Let $AB=a$, $BC=b$, $CD=c$, $DE=d$ and $EF=e$. Then we know that $a+b+c+d+e=73$, $a+b=26$, $b+c=22$, $c+d=31$ and $d+e=33$. From this we can easily deduce $c=14$ and $a+e=34$ thus $b+c+d=39$. Using Heron's formula we can calculate the area of $\triangle{CGD}$ to be $\sqrt{(42)(28)(12)(2)}=168$, and since the base of $\triangle{BGE}$ is $\frac{39}{14}$ of that of $\triangle{CGD}$$\triangle{BGE}$ shares an altitude with $\triangle{CGD}$, we conclude they are proportional and we can calculate the area of $\triangle{BGE}$ to be $168\times \frac{39}{14}=\boxed{468}$.

~ Quick Asymptote Fix by [eevee9406](https://artofproblemsolving.com/wiki/index.php?title=User:Eevee9406 "User:Eevee9406"), edited by [aoum](https://artofproblemsolving.com/wiki/index.php?title=User:Aoum "User:Aoum")

## Solution 2 (Law of Cosines)

We need to solve for the lengths of $AB$, $BC$, $CD$, $DE$, and $EF$. Let $AB = a$, $BC = b$, $CD = c$, $DE = d$, and $EF = e$. We are given the following system of equations:

\[a + b = 26, \quad b + c = 22, \quad c + d = 31, \quad d + e = 33, \quad a + b + c + d + e = 73.\]

Substituting $a + b = 26$ and $d + e = 33$ into the equation $a + b + c + d + e = 73$, we get:

\[c = 14.\]

Thus, we have:

\[a = 18, \quad b = 8, \quad c = 14, \quad d = 17, \quad e = 16.\]

Next, consider triangle $CDG$, where $CD = 14$, $CG = 40$, and $DG = 30$. By the Law of Cosines, we have:

\[CD^2 = CG^2 + DG^2 - 2 \times CG \times DG \times \cos(\angle CGD).\]

Substituting the known values:

\[14^2 = 40^2 + 30^2 - 2 \times 40 \times 30 \times \cos(\angle CGD).\]

Simplifying:

\[196 = 1600 + 900 - 2400 \cos(\angle CGD).\]

\[2400 \cos(\angle CGD) = 2500 - 196 = 2304.\]

\[\cos(\angle CGD) = \frac{24}{25}.\]

Therefore, we can find $\sin(\angle CGD)$ using the identity $\sin^2 \theta + \cos^2 \theta = 1$:

\[\sin(\angle CGD) = \sqrt{1 - \left(\frac{24}{25}\right)^2} = \frac{7}{25}.\]

Now, the area of triangle $CDG$ is

\[\frac{1}{2} \times 40 \times 30 \times \frac{7}{25} = 168.\]

Noting that the height of triangle $CDG$ is the same as the height of triangle $BGE$, the ratio of the areas of the two triangles will be the same as the ratio of their corresponding lengths. Therefore, the answer is

\[\frac{168 \times 39}{14} = \boxed{468}.\]

(Feel free to add or correct any LaTeX and formatting)

~ Mitsuihisashi14, edited by [aoum](https://artofproblemsolving.com/wiki/index.php?title=User:Aoum "User:Aoum")
