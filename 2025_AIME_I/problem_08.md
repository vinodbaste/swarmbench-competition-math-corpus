## Problem

Let $k$ be a real number such that the system has exactly one complex solution $z$. The sum of all possible values of $k$ can be written as $\frac{m}{n}$, where $m$ and $n$ are relatively prime positive integers. Find $m + n$. Here $i = \sqrt{-1}$.

## Solution 1

[asy] size(300); draw((0, 0) -- (0, 20), EndArrow(10)); label("$y$", (0, 20), NW); dot((25,20)); draw((0, 0) -- (25, 0), EndArrow(10)); label("$x$", (25, 0), SE); draw(circle((25,20),5)); label(scale(0.7)*"$(25,20)$", (25,20), S); draw((7,0) -- (3,3), blue); draw((5,3/2) -- (21,23), dashed); label("$(4+k,0)$", (7,0), S); label("$(k,3)$", (3,3), N); draw(rightanglemark((3,3),(5,3/2),(21,23), 20)); draw(rightanglemark((25,20),(21,23),(5,3/2), 20)); draw((25,20) -- (21,23)); [/asy] The complex number $z$ must satisfy the following conditions on the complex plane:

$1.$ The magnitude between $z$ and $(25,20)$ is $5.$ This can be represented by drawing a circle with center $(25,20)$ and radius $5.$

$2.$ It is equidistant from the points $(4+k,0)$ and $(k,3).$ Hence it must lie on the perpendicular bisector of the line connecting these points.

For $z$ to have one solution, the perpendicular bisector of the segment connecting the two points must be tangent to the circle. This bisector must pass the midpoint, $(2+k,\frac{3}{2}),$ and have slope $\frac{4}{3}.$ The segment connecting the point of tangency to the center of the circle has slope $\frac{-3}{4},$ meaning the points of tangency can be $(29,17)$ or $(21,23).$ Solving the equation for the slope of the perpendicular bisector gives \[\frac{\frac{3}{2}-23}{k+2-21}=\frac{4}{3}\] or \[\frac{\frac{3}{2}-17}{k+2-29}=\frac{4}{3},\] giving $k=\frac{23}{8}$ or $\frac{123}{8}$, having a sum of $\frac{73}{4} \Longrightarrow \boxed{077}.$

~nevergonnagiveup

## Solution 2 (Systematic + Algebra)

We first look at each equation, and we convert each to algebra (note that the absolute value sign of $|$ means the magnitude). Let's convert z to $A + Bi$.

Note that the first equation becomes: $(25 - A)^2 + (20 - B)^2 = 25$

Note that this is the equation of a circle centered at $(25, 20)$ with radius $5$.

And the second equation becomes: $(A-4-k)^2 + B^2 = (A - k)^2 + (B-3)^2$

You can see that the many similar terms that cancel out, simplfying, you get:

$-8(A - k) + 16 + 6B = 9$

Now we must isolate B

\[B= \frac{4}{3}(A-k) - \frac{7}{6}\]

\[B = \frac{4}{3}A - \frac{4}{3}k - \frac{7}{6}\]

This equation can be seen as a line with a $\frac{4}{3}$ slope, and a y-intercept of $- \frac{4}{3}k - \frac{7}{6}$.

Note that the question only wants one solution, so we want two tangent lines, one above the circle, and one below the circle. You can see Solution 2 for the picture.

Because the slope is $\frac{4}{3}$, the circle must have a slope coming out of center of its reciprocal, $-\frac{3}{4}$. So the points on the circle where this line with a $\frac{4}{3}$ must intersect must be $(21, 23)$ and $(29, 17)$. We can easily use point-slope form to find the equations of these lines. \[y - 23 = \frac{4}{3}(x - 21)\]

and

\[y - 17 = \frac{4}{3}(x - 29)\]

Now we must match the y-intercepts to the equations with $k$ in it. Solving the equations:

\[\frac{4}{3}(-21) + 23 = - \frac{4}{3}k - \frac{7}{6}\]

\[\frac{4}{3}(-29) + 17 = - \frac{4}{3}k - \frac{7}{6}\]

we get that $k = \frac{23}{8}$ and $k = \frac{123}{8}$ Adding them up and simplifying, we get a sum of $\frac{73}{4} \Longrightarrow \boxed{077}.$

~Marcus:)

## Solution 3 (A Little Geometry)

[](https://artofproblemsolving.com/wiki/index.php?title=File:2025AIMEII_P8_Solution3_1.png)[](https://artofproblemsolving.com/wiki/index.php?title=File:2025AIMEII_P8_Solution3_2.png)

To solve the problem, we first locate the point $Z$. According to the conditions, we can know that:

$Z$ is on the perpendicular bisector of $(k,3)$ and $(k+4,0)$

The distance from $Z$ to circle $O(25,20)$ is ${5}$.

Therefore, $Z$ must be the 2 points of tangent of a line with the slope of $\frac{4}{3}$ with circle O (center at $(25,20)$, radius of ${5}$), corresponding to the 2 values: ${K_1}$ and ${K_2}$.

Since the question only asks for the sum of ${K_1}$ and ${K_2}$, we would not need to calculate them separately. Let the middle point of ${K_1}$ and ${K_2}$ be ${K}$ ==>${K_1}$ + ${K_2}$ = ${2K}$.

Looking at the simplified figure below. We may calculate using similarity of the triangles:

$\frac{SV}{SO}=\frac{WV}{OT}$

$SV = \frac{2.5\cdot25}{20}=\frac{25}{8}$

$KS = KV-SV = 4-\frac{25}{8} = \frac{7}{8}$

$KT = KS+ST = \frac{7}{8}+15 = \frac{127}{8}$

$K_1+K_2 = 2K = (25-\frac{127}{8})\cdot2= \frac{73}{8}\cdot2 = \frac{73}{4}$

We conclude that $m+n=\boxed{077}$.

~cassphe

## Solution 4 (Distance Formula, quick)

Let $z = a + bi.$ Then the system becomes $(25 - a)^2 + (20 - b)^2 = 25$ and $(a - 4 - k)^2 + b^2 = (a - k)^2 + (b - 3)^2$$\implies b = \frac{4}{3}a - (\frac{4}{3}k + \frac{7}{6})$. For this system to have one solution for $z,$ the line $b = \frac{4}{3}a - (\frac{4}{3}k + \frac{7}{6})$ must be tangent to the circle $(25 - a)^2 + (20 - b)^2 = 25$. For a line to be tangent to a circle, the distance between the line and center must be equal to the length of the radius, which is $5$. The center of the circle is $(a,b) \rightarrow (25,20),$ and we can express the line as $8a - 6b - (8k + 7) = 0.$ So we have: \[d = \frac{|Ax_0 + By_0 + C|}{\sqrt{A^2 + B^2}} = \frac{|8(25) - 6(20) -(8k + 7)|}{\sqrt{8^2 + 6^2}} =  \frac{|73 - 8k|}{10} = 5 \implies |73 - 8k| = 50\]\[k = \frac{23}{8}, \frac{123}{8}.\]$\frac{m}{n}$ is $\frac{146}{8} = \frac{73}{4}.$ The requested sum is $73 + 4 = \boxed{77}.$

~[grogg007](https://artofproblemsolving.com/wiki/index.php?title=User:Grogg007 "User:Grogg007"), Mathycoder & MathKing555 also previously mentioned a similar approach

## Solution 5 (Educated Guess)

Letting $z=a+bi$, the given equations become $(a-25)^2+(b-20)^2 = 25$ and $(a-4-k)^2+b^2 = (a-k)^2+(b-3)^2$. Expanding the second equation and canceling like terms yields $16-8a+8k=-6b+9$. Rearrange and solve for $k$ to get $k=\frac{8a-6b-7}{8}$.

The equation $(a-25)^2+(b-20)^2 = 25$ is a circle with center $(25, 20)$ and radius $5$. As explained in Solution 1, $|z - 4 - k| = |z - 3i - k|$ represents the perpendicular bisector of the line segment formed by connecting points $(4+k, 0)$ and $(k, 3)$. The $2$ tangent points hit on the circle by the perpendicular bisector with be diametrically opposite.

Experiment with plugging in diametrically opposite pairs of points such as $(a, b)={(20, 15), (20, 25)}$ and $(a, b)={(29, 17), (21, 23)}$, which can be found using $3-4-5$ right triangles, into the previously found formula $k=\frac{8a-6b-7}{8}$. Observe that when the resulting $k$-values from each pair are added together, the value $\frac{146}{8}=\frac{73}{4}$ is obtained every time. If one assumes that this holds true for each pair of points, then it also holds true for the $2$ desired points, and the answer is $73+4=\boxed{077}$.

~Christian
