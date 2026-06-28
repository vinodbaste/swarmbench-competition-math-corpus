## Problem

Circle $\omega_1$ with radius $6$ centered at point $A$ is internally tangent at point $B$ to circle $\omega_2$ with radius $15$. Points $C$ and $D$ lie on $\omega_2$ such that $\overline{BC}$ is a diameter of $\omega_2$ and ${\overline{BC} \perp \overline{AD}}$. The rectangle $EFGH$ is inscribed in $\omega_1$ such that $\overline{EF} \perp \overline{BC}$, $C$ is closer to $\overline{GH}$ than to $\overline{EF}$, and $D$ is closer to $\overline{FG}$ than to $\overline{EH}$, as shown. Triangles $\triangle {DGF}$ and $\triangle {CHG}$ have equal areas. The area of rectangle $EFGH$ is $\frac{m}{n}$, where $m$ and $n$ are relatively prime positive integers. Find $m+n$.

[asy] size(5cm); defaultpen(fontsize(10pt));  pair A = (9, 0), B = (15, 0), C = (-15, 0), D = (9, 12), E = (9+12/sqrt(5), -6/sqrt(5)), F = (9+12/sqrt(5), 6/sqrt(5)), G = (9-12/sqrt(5), 6/sqrt(5)), H = (9-12/sqrt(5), -6/sqrt(5)); filldraw(G--H--C--cycle, lightgray); filldraw(D--G--F--cycle, lightgray); draw(B--C); draw(A--D); draw(E--F--G--H--cycle); draw(circle(origin, 15)); draw(circle(A, 6));  dot(A); dot(B); dot(C); dot(D); dot(E); dot(F); dot(G); dot(H);  label("$A$", A, (.8, -.8)); label("$B$", B, (.8, 0)); label("$C$", C, (-.8, 0)); label("$D$", D, (.4, .8)); label("$E$", E, (.8, -.8)); label("$F$", F, (.8, .8)); label("$G$", G, (-.8, .8)); label("$H$", H, (-.8, -.8)); label("$\omega_1$", (9, -5)); label("$\omega_2$", (-1, -13.5)); [/asy]

## Solution 1 (Thorough)

Let $GH=2x$ and $GF=2y$. Notice that since $\overline{BC}$ is perpendicular to $\overline{GH}$ (can be proven using basic angle chasing) and $\overline{BC}$ is an extension of a diameter of $\omega_1$, then $\overline{CB}$ is the perpendicular bisector of $\overline{GH}$. Similarly, since $\overline{AD}$ is perpendicular to $\overline{GF}$ (also provable using basic angle chasing) and $\overline{AD}$ is part of a diameter of $\omega_1$, then $\overline{AD}$ is the perpendicular bisector of $\overline{GF}$.

From the [Pythagorean Theorem](https://artofproblemsolving.com/wiki/index.php?title=Pythagorean_Theorem "Pythagorean Theorem") on $\triangle GFH$, we have $(2x)^2+(2y)^2=12^2$, so $x^2+y^2=36$. To find our second equation for our system, we utilize the triangles given.

Let $I=\overline{GH}\cap\overline{CB}$. Then we know that $GFBI$ is also a rectangle since all of its angles can be shown to be right using basic angle chasing, so $FG=IB$. We also know that $CI+IB=2\cdot 15=30$. $IA=y$ and $AB=6$, so $CI=30-y-6=24-y$. Notice that $CI$ is a height of $\triangle CHG$, so its area is $\frac{1}{2}(2x)(24-y)=x(24-y)$.

Next, extend $\overline{DA}$ past $A$ to intersect $\omega_2$ again at $D'$. Since $\overline{BC}$ is given to be a diameter of $\omega_2$ and $\overline{BC}\perp\overline{AD}$, then $\overline{BC}$ is the perpendicular bisector of $\overline{DD'}$; thus $DA=D'A$. By Power of a Point, we know that $CA\cdot AB=DA\cdot AD'$. $CA=30-6=24$ and $AB=6$, so $DA\cdot AD'=(DA)^2=24\cdot6=144$ and $DA=D'A=12$.

Denote $J=\overline{DA}\cap\overline{GF}$. We know that $DJ=DA-AJ=12-x$ (recall that $GI=IH=x$, and it can be shown that $GIAJ$ is a rectangle). $\overline{DJ}$ is the height of $\triangle DGF$, so its area is $\frac{1}{2}(2y)(12-x)=y(12-x)$.

We are given that $[DGF]=[CHG]$ ($[ABC]$ denotes the area of figure $ABC$). As a result, $x(24-y)=y(12-x)$. This can be simplified to $y=2x$. Substituting this into the Pythagorean equation yields $5x^2=36$ and $x=\frac{6}{\sqrt{5}}$. Then $y=\frac{12}{\sqrt{5}}$.

$[EFGH]=2x\cdot2y=2\cdot\frac{6}{\sqrt{5}}\cdot2\cdot\frac{12}{\sqrt{5}}=\frac{288}{5}$, so the answer is $288+5=\boxed{293}$.

~ [eevee9406](https://artofproblemsolving.com/wiki/index.php/User:Eevee9406)

~ Edited by [aoum](https://artofproblemsolving.com/wiki/index.php/User:Aoum)

## Solution 2 (Faster)

Denote the intersection of $BC$ and $w_1$ as $P$, the intersection of $BC$ and $GH$ be $Q$, and the center of $w_2$ to be $O$. Additionally, let $EF = GH = a, FG = EH = b$. We have that $CP = 18$ and $PQ = 6-\frac{b}{2}$. Considering right triangle $OAD$, $AD = 12$. Letting $R$ be the intersection of $AD$ and $FG$, $DR = 12 - \frac{a}{2}$. Using the equivalent area ratios: \[\frac{a(24-\frac{b}{2})}{2} = \frac{(12-\frac{a}{2})b}{2}\]

This equation gives $b=2a$. Using the [Pythagorean Theorem](https://artofproblemsolving.com/wiki/index.php?title=Pythagorean_Theorem "Pythagorean Theorem") on triangle $GHE$ gives that $a^2+b^2 = 144$. Plugging the reuslt $b=2a$ into this equation gives that the area of the triangle is $\frac{288}{5} \to \boxed{293}$.

~ Vivdax

~ Edited by [aoum](https://artofproblemsolving.com/wiki/index.php/User:Aoum)

~ Additional edits by fermat_sLastAMC

## Solution 3 (Not Recommended)

You can use your ruler to check that $GF=2GH.$ Then, we have $GF^2+GH^2=36,$ and we solve the system of equations to get $\frac{288}{5},$ so the answer is $\boxed{293}.$

Note: This method is not recommended as the diagrams are not necessarily drawn to scale. However, it can be used in emergency situations or to verify the answer.

~derekwang2048

## Solution 4 (Almost no Algebra)

If we draw segments connecting $A$ to $F, G,$ and $H,$ we can easily verify that all of the right triangles created are congruent. Thus, triangles $AGF$ and $AGH$ have equal areas, which means, by the given conditions, that kites $AGCH$ and $AGDF$ have equal areas. Thus, by the area formula for kites,

\[\frac{1}{2}(AD)(GF)=\frac{1}{2}(AC)(GH),\] or \[(AD)(GF)=(24)(GH).\]

Also, if we extend $AD$ to the other side of the large circle, the chord length formula gives

\[(AD)(AD)=(AC)(AB),\] so \[(AD)(AD)=(24)(6).\]

Squaring the second equation above gives \[(AD)(AD)(GF)(GF)=(24)(24)(GH)(GH).\] Dividing by the fourth equation gives \[(GF)^2=4(GH)^2.\] Since we know, by the Pythagorean Theorem, that $(GF)^2+(GH)^2=144,$ we can substitute to determine that $5(GH)^2=144.$

The desired area is $(GF)(GH)=2(GH)^2=\frac{2}{5}(144),$ which is $\frac{288}{5},$ so the answer is $\boxed{293}.$

~ Edited by Christian, but IDK the original author
