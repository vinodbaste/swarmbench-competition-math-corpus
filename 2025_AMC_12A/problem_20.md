## Problem

The base of the pentahedron shown below is a $13 \times 8$ rectangle, and its lateral faces are two isosceles triangles with base of length $8$ and congruent sides of length $13$, and two isosceles trapezoids with bases of length $7$ and $13$ and nonparallel sides of length $13$.

[asy] /* Refined by Mathemagician108 */ import graph3; size(200); real l = 13; real w = 8; real offset = (l - 7)/2;  // 3 real midy = w/2;  // 4 real h = 12; triple O1 = (0,0,0); triple O2 = (l,0,0); triple O3 = (l,w,0); triple O4 = (0,w,0); triple T1 = (offset, midy, h); triple T2 = (l - offset, midy, h); currentprojection=orthographic((-4,-6,3)); draw(O4--O1--O2, linewidth(1)); draw(O2--O3--O4, dashed + linewidth(1)); draw(O3--T2, dashed + linewidth(1)); draw(O1--T1, linewidth(1)); draw(O4--T1, linewidth(1)); draw(O2--T2, linewidth(1)); draw(T1--T2, linewidth(1)); label("13", (O1+O2)/2, 3*-Y);  // Bottom length label("13", (O2+T2)/2, 1.5*X); label("13", (O4+T1)/2, 2*-X); label("8", (O1+O4)/2, 2*-X);   // Width label("7", (T1+T2)/2, 1.5*Z);    // Top length [/asy]

What is the volume of the pentahedron?

$\textbf{(A) } 416 \qquad \textbf{(B) } 520 \qquad \textbf{(C) }  528  \qquad  \textbf{(D) } 676 \qquad \textbf{(E) } 832$

## Solution 1 (Split Into Three Parts)

Notice that the triangular faces have a slant height of $\sqrt{13^2-4^2}=\sqrt{153}$ and that the height is therefore $\sqrt{153-(\frac{13-7}{2})^2} = 12$. Then we can split the pentahedron into a triangular prism and two pyramids. The pyramids each have a volume of $\frac{1}{3}(3)(8)(12) = 96$ and the prism has a volume of $\frac{1}{2}(8)(12)(7) = 336$. Thus the answer is $336+96 \cdot 2 = \boxed{\textbf{(C) } 528}$

~ Shadowleafy

## Solution 2

Note that the height is $12$ from the previous method. Note that as you go up, the length and width both decrease linearly and reach $0$ at the end.

So the answer is $\int_0^{12} (8 - \tfrac{2}{3}x)(13 - \tfrac{1}{2}x) dx = \boxed{\textbf{(C) } 528}$

-KapilTheAngel

## Solution (3D Pythagoras)

Let $H$ be the height of the solid. By 3D Pythagoras (recursion of 2D Pythagoras), \[\left( \frac{8}{2} \right)^2+\left( \frac{13-7}{2} \right)^2+H^2=13^2=4^2+3^2+H^2=5^2+H^2\] This gives the $5-12-13$ triple, so $H=12$. Continue as in other solutions.

~imosilver

## Solution 4(Complete Guessing)

By the Closest Answer Guessing Theorem, if any two options are really close, most of the time the greater answer choice is correct.

Proof: Left as an exercise to the reader

By the above lemma, note that the only two options that are really close to each other are $520$ and $528$. By the lemma, the answer is $\boxed{528}$.

~ilikemath247365

## Note

It just reminds about one of old aime problem {[https://artofproblemsolving.com/wiki/index.php?title=1983_AIME_Problems/Problem_11](https://artofproblemsolving.com/wiki/index.php?title=1983_AIME_Problems/Problem_11) 1983 AIME Problem 11}. ~DRA777

## See Also

*   [AMC 12](https://artofproblemsolving.com/wiki/index.php?title=AMC_12 "AMC 12")
*   [AMC 12 Problems and Solutions](https://artofproblemsolving.com/wiki/index.php?title=AMC_12_Problems_and_Solutions "AMC 12 Problems and Solutions")
*   [Mathematics competitions](https://artofproblemsolving.com/wiki/index.php?title=Mathematics_competitions "Mathematics competitions")
*   [Mathematics competition resources](https://artofproblemsolving.com/wiki/index.php?title=Mathematics_competition_resources "Mathematics competition resources")

[](https://artofproblemsolving.com/wiki/index.php?title=File:AMC_Logo.png)
