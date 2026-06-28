## Problem

An isosceles trapezoid has an inscribed circle tangent to each of its four sides. The radius of the circle is $3$, and the area of the trapezoid is $72$. Let the parallel sides of the trapezoid have lengths $r$ and $s$, with $r \neq s$. Find $r^2+s^2$

## Diagram

[asy] unitsize(0.5 cm);  real r = 12 + 6*sqrt(3);  real s = 12 - 6*sqrt(3);  real h = 6;    pair A = (-r/2, 0); pair B = ( r/2, 0); pair C = ( s/2, h); pair D = (-s/2, h);  draw(A--B--C--D--cycle);  pair O = (0, h/2); draw(circle(O, 3));  dot(A); label("$A$", A, SW); dot(B); label("$B$", B, SE); dot(C); label("$C$", C, NE); dot(D); label("$D$", D, NW);  dot(O); label("$O$", (0,h/2), E);  label("$r$", midpoint(A--B), S); label("$s$", midpoint(C--D), N); [/asy]

## Solution 1

To begin with, because of tangents from the circle to the bases, the height is $2\cdot3=6.$ The formula for the area of a trapezoid is $\frac{h(b_1+b_2)}{2}.$ Plugging in our known values we have \[\frac{6(r+s)}{2}=72.\]\[r+s=24.\] Next, we use Pitot's Theorem which states for tangential quadrilaterals $AB+CD=AD+BC.$ Since we are given $ABCD$ is an isosceles trapezoid we have $AD=BC=x.$ Using Pitot's we find, \[AB+CD=r+s=2x=24.\]\[x=12.\] Finally we can use the Pythagorean Theorem by dropping an altitude from D, \[\left(\frac{r - s}{2}\right)^2 + 6^2 = 12^2.\]\[\left(\frac{r-s}{2}\right)^2=108.\]\[(r-s)^2=432.\] Noting that $\frac{(r + s)^2 + (r - s)^2}{2} = r^2 + s^2$ we find, \[\frac{(24^2+432)}{2}=\boxed{504}\]

~[mathkiddus](https://artofproblemsolving.com/wiki/index.php?title=User:Mathkiddus "User:Mathkiddus")

## Solution 2 (Trigonometry)

Draw angle bisectors from the bottom left vertex to the center of the circle. Call the angle formed $\theta$. Drawing a line from the center of the circle to the midway point of the bottom base of the trapezoid makes a right angle, and the other angle has to be $90^{\circ} - \theta$. Then draw a line segment from the center of the circle to the top left vertex, then you have a right triangle. The smaller angle of this triangle is $180^{\circ} - (180^{\circ} - \theta) = \theta$. This means $\frac{r}{2} = \frac{3}{\tan \theta} \implies r = \frac{6}{\tan \theta}$. This also means $\frac{s}{2} = 3 \tan \theta \implies s = 6 \tan \theta$. Note that $r^2 + s^2 = (r + s)^2 - 2rs.$$rs = \frac{6}{\tan \theta} \cdot 6 \tan \theta = 36 \implies 2rs = 72$. The area of the trapezoid is $72 = 6 \cdot \frac{r + s}{2} \implies r + s = 24$. $(r + s)^2 - 2rs = 576 - 72 = \boxed{504}$.

[asy] size(15cm); draw(circle((0,0), 3));  draw((-0.5 * (12 + 6sqrt(3)), -3) -- (0.5 * (12 + 6sqrt(3)), -3) -- (0.5 * (12 - 6sqrt(3)), 3) -- (-0.5 * (12 - 6sqrt(3)), 3) -- cycle); draw((0, 0) -- (-0.5 * (12 + 6*sqrt(3)),-3) -- cycle); draw((0, 0) -- (0.5 * (12 + 6*sqrt(3)),-3) -- cycle); draw((0, 0) -- (-0.5 * (12 - 6*sqrt(3)),3) -- cycle); draw((0, 0) -- (0.5 * (12 - 6*sqrt(3)),3) -- cycle); draw((0, 0) -- (0,3) -- cycle); draw((0, 0) -- (0,-3) -- cycle); draw((-0.5, -3) -- (-0.5,-2.5) -- (0.5, -2.5) -- (0.5, -3) -- cycle); draw((-0.25, 3) -- (-0.25, 2.75) -- (0.25, 2.75) -- (0.25, 3) -- cycle);  label("$\theta$", (-0.5 * (12 + 6*sqrt(3)) + 3, -3), NE); label("$\theta$", (0.5 * (12 + 6*sqrt(3)) - 3, -3), NW); label("$\theta$", (-0.5 * (12 + 6*sqrt(3)) + 3, -2), NE); label("$\theta$", (0.5 * (12 + 6*sqrt(3)) - 3, -2), NW); label("$90^{\circ} - \theta$", (0, -0.5), SW); label("$90^{\circ} - \theta$", (0, -0.5), SE); label("$90^{\circ}$", (0 - 0.1, 0), NW); label("$90^{\circ}$", (0 + 0.1, 0), NE); label("$\frac{r}{2}$", (-0.25 * (12 + 6*sqrt(3)), -3), S); label("$\frac{r}{2}$", (0.25 * (12 + 6*sqrt(3)), -3), S); label("$\theta$", (-0.1, 1.75), E); label("$\theta$", (0.1, 1.75), W); label("$\frac{s}{2}$", (-0.25 * (12 - 6*sqrt(3)), 3), N); label("$\frac{s}{2}$", (0.25 * (12 - 6*sqrt(3)), 3), N); [/asy]

-alwaysgonnagiveyouup

## Solution 3 (Fastest formula)

Denote the radius of the inscribed circle as $R$, and the parallel sides as $r$ and $s$. By formula, we get $R = 3 = \frac{1}{2} \cdot \sqrt{rs}$, where $rs = 36$. Also, by formula, $A = 72 = \frac{1}{2} \cdot \sqrt{rs} \cdot (r + s)$, where $r + s = 24$. Therefore, \begin{align*} &r^2 + s^2 = (r + s)^2 - 2rs \\ &= 24^2 - 2 \cdot 36 \\ &= \boxed{504} \end{align*}

## Solution 4(Double-angle Formula)

Let , . By the double - angle formula for tangent .

Since , .

Set . Since , we can cancel out from both sides of the equation, getting . Subtracting from both sides, we have , so .

Assume . Using the formula , then .

Substitute and into the formula: .

So the final answer is . By Airbus 320-214.

Formula reference to here: [https://en.wikipedia.org/wiki/Tangential_trapezoid](https://en.wikipedia.org/wiki/Tangential_trapezoid)

~Mitsuihisashi14

~ LaTeX by alwaysgonnagiveyouup

## Solution 5

The height of the trapezoid is clearly the diameter of the circle or $6$. We let the larger base be $r$, and the smaller one be $s$. We have by the area of a trapezoid: \[\dfrac{r+s}{2} \cdot 6 = 72 \Longrightarrow r+s = 24\]. Now, by Pitot's theorem, and letting the legs of the trapezoid be $x$, we have that $r+s = 2x = 24 \Longrightarrow x = 12$. Now, by pythag we have that $\dfrac{r-s}{2} = 6\sqrt3 \Longrightarrow r-s = 12\sqrt3$. Now, by systems of equations, we find that $r = 12+6\sqrt3$, and $s = 12-6\sqrt3$. Now, we have that $r^2 + s^2 = (12+6\sqrt3)^2+(12-6\sqrt3)^2 = \boxed{504}$

-jb2015007

## Solution 6 (Brahmagupta's)

[](https://artofproblemsolving.com/wiki/index.php?title=File:2025-AIMEI--6.png)

The area of the trapezoid is $\frac{r + s}{2} \cdot 6 = 72 \implies r + s = 24.$ Note that external tangents of a circle are equal. Let $a$ and $s - a$ be the two external tangents making up the bottom base and $b$ and $r - b$ be the two external tangents making up the top base. Since the trapezoid is isosceles, $a + b = r + s - (a + b) \implies a + b = 12.$ So the legs of the trapezoid have length $12.$ From here, we can apply Brahmagupta's Formula to the trapezoid since isosceles trapezoids are cyclic: $\sqrt{\frac{r + s}{2} \cdot \frac{r + s}{2} \cdot \frac{24 - r + s}{2} \cdot \frac{24 + r - s}{2}} = 72.$ Substituting $r + s = 24$ and solving, we get $(r - s)^2 = 432 \implies s - r = 12\sqrt{3}.$ Since we know $s + r = 24,$ we can just solve this system to get $s = 12 + 6\sqrt{3}$ and $r = 12 - 6\sqrt{3}.$ The answer is $(12 + 6\sqrt{3})^2 + (12 - 6\sqrt{3})^2 = \boxed{504}.$

~[grogg007](https://artofproblemsolving.com/wiki/index.php?title=User:Grogg007 "User:Grogg007")
