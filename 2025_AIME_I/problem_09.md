## Problem

The parabola with equation $y = x^2 - 4$ is rotated $60^\circ$ counterclockwise around the origin. The unique point in the fourth quadrant where the original parabola and its image intersect has $y$-coordinate $\frac{a - \sqrt{b}}{c}$, where $a$, $b$, and $c$ are positive integers, and $a$ and $c$ are relatively prime. Find $a + b + c$.

## Graph

[https://www.desmos.com/calculator/ci3vodl4vs](https://www.desmos.com/calculator/ci3vodl4vs)

## Solution 1

We need to relate the rotation to something simpler because substituting the equation of the rotated parabola into the original will give us a quartic. [asy] size(300); import graph;  // View window real L = 6;  // Original parabola y = x^2 - 4 real f(real x){ return x^2 - 4; }  // Rotation by +60 degrees about the origin pair rot60(pair P){   real ang = pi/3;   return (P.x*cos(ang) - P.y*sin(ang), P.x*sin(ang) + P.y*cos(ang)); }  // Axes draw((-L,0)--(L,0), gray(0.65), Arrows(4)); draw((0,-L)--(0,L), gray(0.65), Arrows(4));  // Plot original parabola real xmin=-3.5, xmax=3.5; path parab = graph(f, xmin, xmax); draw(parab, blue+1.2bp);  // Build rotated parabola by sampling, then connecting smoothly int N=220; pair[] pts; for(int i=0; i<=N; ++i){   real x = xmin + (xmax - xmin)*i/N;   pts.push(rot60((x, f(x)))); } path rpar = pts[0]; for(int i=1; i<=N; ++i) rpar = rpar..pts[i]; draw(rpar, red+1.2bp);  // Line y = -sqrt(3) x draw((-L,  sqrt(3)*L)--(L, -sqrt(3)*L), rgb(0,0.45,0)+1.2bp);  // Vertices pair v1 = (0,-4);              // original vertex pair v2 = rot60(v1);           // rotated vertex dot(v1, blue+4bp); dot(v2, red+4bp); [/asy]

Notice that the vertices of the original parabola and its image are symmetrical about the angle bisector of the 60 degree rotation (shown in green).

The equation of this line is $y = -\tan60^\circ \cdot y = -\sqrt{3}x.$ This means that the point lying on this line and the original parabola must be the intersection of the new and original images since it won't change position with the rotation.

We substitute $y = x^2 - 4:$\[x^2 - 4 = -\sqrt{3}x\]\[x = \frac{-\sqrt{3} + \sqrt{19}}{2}.\]

Then $y = (\frac{-\sqrt{3} + \sqrt{19}}{2})^2 - 4 = \frac{3 - \sqrt{57}}{2}.$$57 + 3 + 2 = \boxed{62}.$

~[grogg007](https://artofproblemsolving.com/wiki/index.php?title=User:Grogg007 "User:Grogg007"), ~[mathkiddus](https://artofproblemsolving.com/wiki/index.php?title=User:Mathkiddus "User:Mathkiddus"), ~[athreyay](https://artofproblemsolving.com/wiki/index.php?title=User:Athreyay "User:Athreyay")

## Solution 2 (Similar to Solution 1)

Note that this question is equivalent to finding a point $B$ in the fourth quadrant, such that when a point $A$ on the graph of $y = x^2 - 4$ is rotated $60^\circ$ counterclockwise around the origin, it lands on $B$, which is also on the graph.

The first thing to note is that point $A$ and $B$ must be equidistant to the origin. If we express the coordinates of $A$ as $(a, b)$, and the coordinates of $B$ as $(x, y)$, we have: \[\|OA\| = \|OB\|\] which means that: \[\sqrt{a^2 + b^2} = \sqrt{x^2 + y^2}\] Since $b = a^2 - 4$ and $y = x^2 - 4$, we have $a^2 = b + 4$ and $x^2 = y + 4$, substituting this into the previous equation and squaring both sides yields: \[2a^2 + 4 = 2x^2 + 4\] Meaning that $a^2 = x^2$, since $A$ and $B$ clearly cannot coincide, we must have $a = -x$, since $y = x^2 - 4$ is an even function, this means that point $A$ and $B$ are just reflections of each other over the y axis. The angle between $\overline{OA}$ and $\overline{OB}$ is $60^\circ$ and $A$ and $B$ is symmetrical, the y axis should bisect the angle \angle AOB, i.e., the angle between $\overline{OB}$ and the y axis is: \[\frac{60^\circ}{2} = 30^\circ\] Therefore the point $B$ must lie on the line \[y = -\sqrt{3}x\]

We have: \[\begin{cases}y = x^2 - 4 \\ y = -\sqrt{3}x \end{cases}\]\[x^2 - 4 = -\sqrt{3}x\] Using the quadratic formula and keeping in mind that the x value is positive (since $B$ is in the fourth quadrant) yields $x = \frac{\sqrt{19} - \sqrt{3}}{2}$.

Substituting into \[y = -\sqrt{3}x\] We get \[y=\frac{3-\sqrt{57}}{2}\implies \boxed{062}.\]

The last part of this solution is essentially Solution 1.

~[IDKHowtoaddsolution](https://artofproblemsolving.com/wiki/index.php?title=User:IDKHowtoaddsolution&action=edit&redlink=1 "User:IDKHowtoaddsolution (page does not exist)")

The last part of this solution is essentially Solution 1.

## Solution 3 (clarification needed): Rotation

Rotate the point $(x,y)$$60^\circ$ counterclockwise about the origin. To find the resulting point $(x',y')$, use polar coordinates. Let $x=r \cos\theta$ and $y=r \sin\theta$, so $(x',y')=(r \cos({\theta+60^\circ}), r \sin({\theta+60^\circ}))$. Expanding using the angle addition identities and simplifying gives $(x',y')=\left(\frac{r\cos\theta-r\sqrt{3}\sin\theta}{2}, \frac{r\sin\theta+r\sqrt{3}\cos\theta}{2}\right)$. Substituting back in $x=r \cos\theta$ and $y=r \sin\theta$ yields $(x',y')=\left(\frac{x-y\sqrt{3}}{2}, \frac{x\sqrt{3}+y}{2}\right)$.

To rewrite $(x',y')$ completely in terms of $x$, substitute $y=x^2-4$ to get $(x',y')=\left(\frac{x-(x^2-4)\sqrt{3}}{2}, \frac{x\sqrt{3}+(x^2-4)}{2}\right)$.)

We now have the coordinates for each point on the rotated parabola: $(x',y')=\left(\frac{x-(x^2-4)\sqrt{3}}{2}, \frac{x\sqrt{3}+(x^2-4)}{2}\right)$. Set the $y$-coordinates for both the original and rotated parabola equal to each other: $\frac{x\sqrt{3}+(x^2-4)}{2}=x^2-4$. Rearranging gives the quadratic $x^2-\sqrt{3}x-4=0$, and applying the Quadratic Formula yields the solutions $x=\frac{\sqrt{3}\pm\sqrt{19}}{2}$.

Taking the solution $x=\frac{\sqrt{3}-\sqrt{19}}{2}$ (IDK why though, the $x$-value is negative when it should be positive, clarification needed) (due to the way we set up the equation, we are finding the $x$ value of the point that maps to the intersection point after rotation. $-x$ is the $x$ value for the intersection point ~Towerrocks) and substituting it into $y=x^2-4$ gives $y=\left(\frac{\sqrt{3}-\sqrt{19}}{2}\right)^2-4=\frac{22-2\sqrt{57}}{4}-4=\frac{6-2\sqrt{57}}{4}=\frac{3-\sqrt{57}}{2}$. Therefore, our answer is $a+b+c=3+57+2=\boxed{062}$.

Note: It may be possible to solve the problem by substituting the coordinates $(x',y')=\left(\frac{x-y\sqrt{3}}{2}, \frac{x\sqrt{3}+y}{2}\right)$ into the equation $y=x^2-4$ to obtain the systems of equations $\frac{x\sqrt{3}+y}{2}=\left(\frac{x-y\sqrt{3}}{2}\right)^2-4, y=x^2-4$.

~Christian
