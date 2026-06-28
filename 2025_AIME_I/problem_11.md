## Problem
A piecewise linear function is defined by
\[f(x) = \begin{cases} x & \operatorname{if} ~ -1 \leq x < 1 \\ 2 - x & \operatorname{if} ~ 1 \leq x < 3\end{cases}\]
 and $f(x + 4) = f(x)$ for all real numbers $x$. The graph of $f(x)$ has the sawtooth pattern depicted below.

[asy]
import graph;
size(300);
Label f;
f.p=fontsize(6);
yaxis(-2,2,Ticks(f, 2.0));
xaxis(-6.5,6.5,Ticks(f, 2.0));
draw((0, 0)..(1/4,sqrt(1/136))..(1/2,sqrt(1/68))..(0.75,sqrt(0.75/34))..(1, sqrt(1/34))..(2, sqrt(2/34))..(3, sqrt(3/34))..(4, sqrt(4/34))..(5, sqrt(5/34))..(6, sqrt(6/34))..(7, sqrt(7/34))..(8, sqrt(8/34)), red);
draw((0, 0)..(1/4,-sqrt(1/136))..(0.5,-sqrt(1/68))..(0.75,-sqrt(0.75/34))..(1, -sqrt(1/34))..(2, -sqrt(2/34))..(3, -sqrt(3/34))..(4, -sqrt(4/34))..(5, -sqrt(5/34))..(6, -sqrt(6/34))..(7, -sqrt(7/34))..(8, -sqrt(8/34)), red);
draw((-7,0)--(7,0), black+0.8bp);
draw((0,-2.2)--(0,2.2), black+0.8bp);

draw((-6,-0.1)--(-6,0.1), black);
draw((-4,-0.1)--(-4,0.1), black);
draw((-2,-0.1)--(-2,0.1), black);
draw((0,-0.1)--(0,0.1), black);
draw((2,-0.1)--(2,0.1), black);
draw((4,-0.1)--(4,0.1), black);
draw((6,-0.1)--(6,0.1), black);

draw((-7,1)..(-5,-1), blue);
draw((-5,-1)--(-3,1), blue);
draw((-3,1)--(-1,-1), blue);
draw((-1,-1)--(1,1), blue);
draw((1,1)--(3,-1), blue);
draw((3,-1)--(5,1), blue);
draw((5,1)--(7,-1), blue);
[/asy]

The parabola $x = 34y^{2}$ intersects the graph of $f(x)$ at finitely many points. The sum of the $y$-coordinates of all these intersection points can be expressed in the form $\tfrac{a + b\sqrt{c}}{d}$, where $a$, $b$, $c$, and $d$ are positive integers such that $a$, $b$, $d$ have greatest common divisor equal to $1$, and $c$ is not divisible by the square of any prime. Find $a + b + c + d$.

## Video solution 1 by grogg007
https://www.youtube.com/watch?v=1c2xrdlyoUo

## Solution 1
Note that the part of $f(x)$ in the first and fourth quadrants consists of lines of the form $y = x - 4k$ and $y = 4k + 2 - x$ for integers $k \geq 0$.
Plugging in $x = 34y^2$ for $y = x - 4k$, we get $-34y^2 + y + 4k = 0,$ so the sum of the roots is $\tfrac{1}{34}$ by Vieta’s. Similarly, in the second equation, we get a sum of $-\tfrac{1}{34}.$

The top peaks of the graph form the line $y = 1$ and the bottom peaks form $y = -1.$ So the parabola will cross the positive line once it reaches the point $(34,1),$ and it will cross the negative line at $(34, -1).$
For $y = x - 4k,$ we find $k = \frac{33}{4}$ for the positive $y$ values and $k = \frac{35}{4}$ for the negative y values. Both round down to $8,$ so the parabola will stop intersecting $y = x - 4k$ entirely after $k = 8.$

Now, for $y = 4k + 2 - x,$ we find $k = \frac{33}{4}$ for the positive y values and $k = \frac{31}{4}$ for the negative y values. $\frac{33}{4}$ rounds down to $8,$ but $\frac{31}{4}$ rounds down to $7,$ so the parabola will stop intersecting the negative $y$ values of $y = 4k + 2 - x$ after $k = 7,$ but it will intersect the positive $y$ values until $k = 8.$

There are $8$ values of $k$ from $0 - 7,$ so the sum contributed by $y = 4k + 2 - x$ until $k = 7$ is $-\frac{8}{34}.$ There are $9$ values of $k$ from $0 - 8,$ so the sum contributed by $y = x - 4k$ until $k = 8$ is $\frac{9}{34}.$ Adding these together we get $\frac{1}{34}.$

Now all that's left is to figure out the positive $y$ value at $k = 8$ for the line $y = 4k + 2 - x.$ We get
\[34-34y^2 = y.\]

\[y = \frac{-1 \pm \sqrt{68^2 + 1}}{68} = \frac{-1 + 5 \sqrt{185}}{68}.\]
 Adding our $\tfrac{1}{34}$ from earlier finally gives us $\frac{1 + 5 \sqrt{185}}{68} \implies \boxed{259}$.

~grogg007, EpicBird08, mathkiddus

## Solution 2
Drawing the graph, we can use the sawtooth graph provided so nicely by MAA and draw out the parabola $x = 34y^2$. We realize that the sawtooth graph is just a bunch of lines where the positive slope lines are $y = x, y = x + 4, y = x + 8,...$. The intersections of these lines, along with the parabola are just solving the system of equations: $x = 34y^2$ and $y = x, y = x + 4, ...$. If we just take $y = x$ and $x = 34y^2$, we see that the sum of all $y$ by Vieta's is just $\frac{1}{34}$. Similarly, for $y = x + 4$, the sum of the roots by Vieta's is also $\frac{1}{34}$. So for all the positive slope lines intersecting with the parabola just gives the sum of all $y$ to continuously be $\frac{1}{34}$. Okay, now let's look at the negative slope lines. These will have equations of $y = 2 - x, y = 6 - x, y = 10 - x, ..., y = 34 - x, ...$. Similar to what we did above, we just set each of these equations along with the parabola $x = 34y^2$. The sum of all $y$ for each of these negative line intersections by Vieta's is $\frac{-1}{34}$. This keeps going for all of the lines until we reach $y = 34 - x$. Now, unfortunately, both solutions don't work as the negative solution is out of the range of $[1 , 3]$, $[5, 7]$ and so on. So we just need to take one solution for this and that being the positive one according to the graph. So we just need to solve $34 - y = 34y^2$ which means $34y^2 + y - 34 = 0$. Solving gives
\[y = \frac{-1 \pm \sqrt{68^2 + 1}}{68} = \frac{-1 + 5 \sqrt{185}}{68}.\]
So, the sums of the roots are $\frac{1}{34}$ + $\frac{-1}{34}$ + $\frac{1}{34}$ + .... + $\frac{-1}{34}$ + $\frac{1}{34}$ + $\frac{-1 + 5 \sqrt{185}}{68}.$ Nicely all the $\frac{1}{34}$ terms cancel out leaving with only one $\frac{1}{34}$ and $\frac{-1 + 5 \sqrt{185}}{68}.$ So the sum of these two is $\frac{1 + 5 \sqrt{185}}{68}.$ From there, the answer is $\boxed{259}$.

~ilikemath247365

## Video Solution
2025 AIME I #11

MathProblemSolvingSkills.com
