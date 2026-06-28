_The following problem is from the [2024 AMC 10B #14](https://artofproblemsolving.com/wiki/index.php/2024\_AMC\_12B\_Problems/Problem\_9) and [2024 AMC 12B #9](https://artofproblemsolving.com/wiki/index.php?title=2024\_AMC\_12B\_Problems/Problem\_9 "2024 AMC 12B Problems/Problem 9"), so those problems redirect to this page._
## Problem

A dartboard is the region $B$ in the coordinate plane consisting of points $(x, y)$ such that $|x| + |y| \le 8$. A target $T$ is the region where $(x^2 + y^2 - 25)^2 \le 49$. A dart is thrown and lands at a random point in B. The probability that the dart lands in $T$ can be expressed as $\frac{m}{n} \cdot \pi$, where $m$ and $n$ are relatively prime positive integers. What is $m + n$?

$\textbf{(A) }39 \qquad \textbf{(B) }71 \qquad \textbf{(C) }73 \qquad \textbf{(D) }75 \qquad \textbf{(E) }135 \qquad$

## Diagram

[asy] // By Elephant200 // Feel free to adjust the code  size(10cm);  pair A = (8, 0); pair B = (0, 8); pair C = (-8, 0); pair D = (0, -8); draw(A--B--C--D--cycle, linewidth(1.5));  label("$(8,0)$", A, NE); label("$(0,8)$", B, NE); label("$(-8,0)$", C, NW); label("$(0,-8)$", D, SE);  filldraw(circle((0,0),4*sqrt(2)), gray, linewidth(1.5)); filldraw(circle((0,0),3*sqrt(2)), white, linewidth(1.5));  draw((-10, 0)--(10,0),EndArrow(5)); draw((10, 0)--(-10,0),EndArrow(5)); draw((0,-10)--(0,10), EndArrow(5)); draw((0,10)--(0,-10),EndArrow(5)); [/asy] ~Elephant200

## Solution 1

Inequalities of the form $|x|+|y| \le 8$ are well-known and correspond to a square in space with centre at origin and vertices at $(8, 0)$, $(-8, 0)$, $(0, 8)$, $(0, -8)$. The diagonal length of this square is clearly $16$, so it has an area of \[\frac{1}{2} \cdot 16 \cdot 16 = 128\] Now, \[(x^2 + y^2 - 25)^2 \le 49\] Converting to polar form, \[r^2 - 25 \le 7 \implies r \le \sqrt{32},\] and \[r^2 - 25 \ge -7\implies r\ge \sqrt{18}.\]

The intersection of these inequalities is the circular region $T$ for which every circle in $T$ has a radius between $\sqrt{18}$ and $\sqrt{32}$, inclusive. The area of such a region is thus $\pi(32-18)=14\pi.$ The requested probability is therefore $\frac{14\pi}{128} = \frac{7\pi}{64},$ yielding $(m,n)=(7,64).$ We have $m+n=7+64=\boxed{\textbf{(B)}\ 71}.$

-AbhiSood1234, countmath1

## Solution 2 (Calculus)

Expressing the Area of Region

Region consists of points where

In each quadrant, this can be expressed by the following functions:

First quadrant: Second quadrant: Third quadrant: Fourth quadrant:

In the first quadrant, ranges from 0 to 8, and ranges from 0 to . Thus, the area in the first quadrant is: \[\text{Area of first quadrant} = \int_0^8 \int_0^{8 - x} \, dy \, dx\]\[= \int_0^8 [y]_{y=0}^{y=8-x} \, dx = \int_0^8 (8 - x) \, dx\]\[= \left[ 8x - \frac{x^2}{2} \right]_0^8 = 64 - 32 = 32\] The total area of region is: \[\text{Area of } B = 4 \times 32 = 128\]

Expressing the Area of Region Region is defined by the inequality , which can be rewritten as: \[18 \le x^2 + y^2 \le 32\]

To find the area, we switch to polar coordinates with and , where . Here, ranges from to , and ranges from 0 to .

The area of can then be found by: \[\text{Area of } T = \int_0^{2\pi} \int_{\sqrt{18}}^{\sqrt{32}} r \, dr \, d\theta\]\[= \int_0^{2\pi} \left[ \frac{r^2}{2} \right]_{r=\sqrt{18}}^{r=\sqrt{32}} \, d\theta = \int_0^{2\pi} \left( \frac{32}{2} - \frac{18}{2} \right) \, d\theta\]\[= \int_0^{2\pi} 7 \, d\theta = 14\pi\]

The probability that a dart lands in region is the area of divided by the area of : \[P = \frac{\text{Area of } T}{\text{Area of } B} = \frac{14\pi}{128} = \frac{7\pi}{64}\]

So the probability is of the form , where and , so .

\[\boxed{\textbf{(B)}\ 71}\]

~[Athmyx](https://artofproblemsolving.com/wiki/index.php/User:Athmyx)

## Solution 3

[](https://artofproblemsolving.com/wiki/index.php?title=File:2024_AMC_12B_P09.jpeg)

~Kathan
