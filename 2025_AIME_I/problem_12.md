## Problem

The set of points in $3$-dimensional coordinate space that lie in the plane $x+y+z=75$ whose coordinates satisfy the inequalities \[x-yz<y-zx<z-xy\]forms three disjoint convex regions. Exactly one of those regions has finite area. The area of this finite region can be expressed in the form $a\sqrt{b},$ where $a$ and $b$ are positive integers and $b$ is not divisible by the square of any prime. Find $a+b.$

## Solution 1

Rewriting we have $z=75-x-y.$

From the inequality $x-yz<y-zx$ we can rewrite to get, \[x-y(75-x-y)< y-x(75-x-y).\]\[76x-76y+y^2-x^2<0.\]\[(76-x-y)(x-y)<0.\]

Similarly from the inequality $y-zx<z-xy$ we rewrite to get, \[y-x(75-x-y)<(75-x-y)-xy.\]\[2y + 2xy + x^2 - 74x - 75 < 0.\]\[(x + 1)(2y + x - 75) < 0.\] Our next step is a visual which can be seen by roughly graphing the two inequalities. The first inequality is similar to a bow tie(you have to graph to see it lol) with bounds of $x-y=0$ and $76-x-y=0.$ The second one is a bow tie with edges of $x+1=0$ and $2y+x-75=0.$Here is the region of our solutions. [asy] import graph; size(400, 400); real xmin = -250, xmax = 250; real ymin = -150, ymax = 150; draw((xmin,0)--(xmax,0), black+0.8bp, Arrow); draw((0,ymin)--(0,ymax), black+0.8bp, Arrow); pair A = (38, 38),       B = (-10, -10),       C = (-227, 151),       D = (-10, 85/2),       E = (25, 25); path L1 = (xmin, xmin)--(xmax, xmax); path L2 = (xmin, 76-xmin)--(xmax, 76-xmax); path L3 = ((-10, ymin)--(-10, ymax)); path L4 = (xmin, (75-xmin)/2)--(xmax, (75-xmax)/2); fill(B--D--E--cycle, lightgreen); draw(L1, blue); draw(L2, blue); draw(L3, red); draw(L4, red); dot(A, black); label("$(38,38)$", A, NE); dot(B, black); label("$(-1,-1)$", B, SE); dot(C, black); label("$(-227,151)$", C, NW); dot(D, black); label("$(-1,38)$", D, SW); dot(E, black); label("$(25,25)$", E, SE); [/asy] It is simple to find the intersections of those which are $(-1,38,38),(25,25,25)$ and $(-1,-1,77).$ The sidelengths of this triangle are $39\sqrt{2},26\sqrt{6},13\sqrt{6}$ which is a $30-60-90$ gives us an area of \[\frac{1}{2}(39\sqrt{2})(13\sqrt{6})=507\sqrt{3}\implies\boxed{510}.\]

~[mathkiddus](https://artofproblemsolving.com/wiki/index.php?title=User:Mathkiddus "User:Mathkiddus")~plang2008~hashbrown2009

## Solution 2

Consider $x-yz<y-zx<z-xy$. From $x-yz<y-zx$, we find $z(y-x)>x-y$. Thus, if $x>y$, then $z<-1$, and if $x<y$, then $z>-1$. Similarly, taking another pair of the inequalities yields $y>-1$ when $z>x$ and $y<-1$ when $x>z$. Finally, taking the third pair yields $x>-1$ if $z>y$ and $x<-1$ if $z<y$.

Consider the first two resultant pairs of inequalities. Taking them pairwise (one from the first set and one from the second set) results in four cases:

1. Combining $z<-1$ if $x>y$ and $y>-1$ if $z>x$ yields $-1>z>x>y>-1$, a contradiction.

2. Combining $z<-1$ if $x>y$ and $y<-1$ if $z<x$ yields $x,-1>y,z$.

3. Combining $z>-1$ if $x<y$ and $y>-1$ if $z>x$ yields $y,z>-1,x$.

4. Combining $z>-1$ if $x<y$ and $y<-1$ if $z<x$ yields $-1>y>x>z>-1$, a contradiction.

Now we have only two satisfactory inequalities. We now consider the third pair of inequalities ($x>-1$ if $z>y$ and $x<-1$ if $z<y$). Taking the two sets pairwise:

1. Combining $x,-1>y,z$ and $x>-1$ if $z>y$ yields $x>-1>z>y$. Consider some valid $x,y,z$ that satisfy $x+y+z=75$ and $x>-1>z>y$. We can infinitely increase $x$ while decreasing $y$ by the same amount, leading to another valid triple, so this case is infinite and we do not consider this case (for instance, if $x=100,y=-13,z=-12$, then $x=100+a,y=-13-a,z=-12$ is a valid triple for all nonnegative $a$).

2. Combining $y,z>-1,x$ and $x>-1$ if $z>y$ yields $z>y>x>-1$. This case is finite due to the lower bound.

3. Combining $x,-1>y,z$ and $x<-1$ if $z<y$ yields $-1>x>y>z$. There are no possible solutions since $x,y,z$ are negative from this inequality, but at least one must be positive to satisfy $x+y+z=75$, a contradiction.

4. Combining $y,z>-1,x$ and $x<-1$ if $z<y$ yields $y>z>-1>x$. By the same argument as in Case 1, this is an infinite case.

Thus we are tasked with finding the area of the figure formed by all triples $x,y,z$ satisfying $x+y+z=75$ and $z>y>x>-1$. We consider edge cases, so we maximize each variable by the largest amount possible to find three triples $(77,-1,-1),(38,38,-1),(25,25,25)$. We assume that these are the only edge cases (so the figure forms a triangle), and we can use the [Distance formula](https://artofproblemsolving.com/wiki/index.php?title=Distance_formula "Distance formula"). We find that the three side lengths of our triangle are $39\sqrt{2},13\sqrt{6},26\sqrt{6}$. These side lengths just so happen to form a $30-60-90$ triangle with legs $13\sqrt{6}$ and $39\sqrt{2}$, so the area of the triangle is

\[\frac{1}{2}\cdot13\sqrt{6}\cdot39\sqrt{2}=507\sqrt{3}\]

Thus the answer is $507+3=\boxed{510}$. ~eevee9406

## Solution 3

Decomposing the inequality chain: \[x-yz<y-zx \quad \text{and} \quad y-zx<z-xy\] which is equivalent to \[(x-y)(z+1)<0 \quad \text{and} \quad (y-z)(x+1)<0\] Substituting $z$ with $z=75-x-y$ and simplifying yields \[(x-y)(x+y-76)>0 \quad \text{and} \quad (x+2y-75)(x+1)<0\] See that the solution to the first inequality is \[x-y>0, \, x+y-76>0 \quad \text{(I)} \quad \text{or} \quad x-y<0, \, x+y-76<0 \quad \text{(II)}\] Applying a similar method results in the solution to the second: \[x+2y-75>0, \, x+1<0 \quad \text{(III)} \quad \text{or} \quad x+2y-75<0, \, x+1>0 \quad \text{(IV)}\] Trying each grouping (i.e. let $\text{(I)}$ and $\text{(III)}$, $\text{(I)}$ and $\text{(IV)}$, $\text{(II)}$ and $\text{(III)}$, or $\text{(II)}$ and $\text{(IV)}$ be satisfied at the same time) and graphing shows that when $\text{(II)}$ and $\text{(IV)}$ are both satisfied, a triangle whose vertices are $(-1,38)$, $(-1,-1)$, and $(25,25)$ is formed. Further calculations show that the area of the triangle is $507$. However, this is not the final answer. We have projected the original shape to the $xy$-plane by substituting $z$. We know that for a surface defined by the equation $z=f(x,y)$, the area element $dS$ for this surface is given by \[dS=\sqrt{1+(f_x)^2+(f_y)^2}dxdy\] where $f_x$ and $f_y$ are the partial derivatives of the function $f(x,y)$ with respect to $x$ and $y$. For the plane $x+y+z=75$ where $f(x,y)=75-x-y$, computation gives \[f_x=-1, f_y=-1\] Substituting these into the original equation to get \[dS=\sqrt{3}dxdy\] This implies that to find the area of the original shape, we have to multiply the area of its projection on the $xy$-plane by $\sqrt{3}$. Therefore, the area of the original shape is $507\sqrt{3}$, with final answer $\boxed{510}$.

~[Bloggish](https://artofproblemsolving.com/wiki/index.php?title=User:Bloggish "User:Bloggish")

## Supplementary Graph

[asy] import three; unitsize(1cm); size(300); currentprojection=orthographic(-1/3,-1,-1/2); //basic coordinates to origin (-1,-1,-1) draw((-1,-1,-1)--(-1,-1,100)); draw((-1,-1,-1)--(-1,100,-1)); draw((-1,-1,-1)--(100,-1,-1)); label("$X$",(100,-1,-1), SW); label("$Y$",(-1,100,-1), SW); label("$Z$",(-1,-1,100), SW);  // X+Y+Z=75 space over original (-1,-1,-1） draw((-1,-1,77)--(-1,77,-1),red); draw((77,-1,-1)--(-1,77,-1),red); draw((77,-1,-1)--(-1,-1,77),red); // draw((-1,38,38)--(77,-1,-1),red); draw((-1,-1,77)--(38,38,-1),red); //label label("$(-1,-1,77)$",(-1,-1,77), NW); label("$(-1,77,-1)$",(-1,77,-1), NW); label("$(77,-1,-1)$",(77,-1,-1), NE); label("$(25,25,25)$",(25,25,25), NE); label("$(-1,-1,-1)$",(-1,-1,-1),NW); label("$(-1,38,38)$",(-1,38,38),NW); label("$(38,38,-1)$",(38,38,-1),SE); //the target area in blue draw((-1,-1,77)--(25,25,25),blue); draw((-1,-1,77)--(-1,38,38),blue); draw((25,25,25)--(-1,38,38),blue); [/asy]

This is the real graph of the 3D space in coordinates. The area in BLUE is the space that satisfied the conditions, and it is 1/6 of a regular triangle.

~cassphe

## Fakesolve: Fast but Flawed

Visualize or draw a $3$-dimensional graph of the following planes: $x+y+z=75$, $x=-1$, $y=-1$, $z=-1$, $x=y$, $y=z$, and $z=x$. The last $6$ planes (which be derived by solving for the zeroes of the inequalities $x-yz<y-zx$, $y-zx<z-xy$, $x-yz<z-xy$) form the plane $x+y+z=75$ into an triangle (which is equilateral by symmetry) with all $3$ of its medians cutting through it.

The vertices of the large equilateral triangle can be found by considering its smaller medial triangle formed by connecting the midpoints of the equilateral triangle. The coordinates of the medial triangle are formed by the intersections of the planes $x+y+z=75$, $x=y$, $z=-1$; $x+y+z=75$, $y=z$, $x=-1$; and $x+y+z=75$, $z=x$, $y=-1$. Solving these systems of equations gives the vertices $(38, 38, -1)$, $(-1, 38, 38)$, and $(38, -1, 38)$, respectively. Applying the Distance Formula, we get the side length of the medial triangle as $\sqrt{(x_2-x_1)^2+(y_2-y_1)^2+(z_2-z_1)^2}=\sqrt{(-1-38)^2+(38-38)^2+(38-(-1))^2}=39\sqrt{2}$.

Then, the area of the original equilateral triangle is $4\cdot\frac{(39\sqrt{2})^2\cdot\sqrt{3}}{4}=3042\sqrt{3}$. Since the original equilateral triangle is divided into $6$ congruent $30-60-90$ right triangles, each of these triangles has area $3042\sqrt{3}/6=507\sqrt{3}$. Assuming that the desired convex region includes at least $1$ of these $30-60-90$ right triangles, the possible answers are $507\sqrt{3}, 1014\sqrt{3}, 1521\sqrt{3}, ...  3042\sqrt{3}$. However, if we compare each of these possible answers to the format $a\sqrt{b}$, the only one of these answers for which $a+b$ is less than $1000$ (so it fits into the AIME answer format of $3$ digits) is $507\sqrt{3}$, yielding $a+b=507+3=\boxed{510}$.

~Christian
