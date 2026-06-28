## Problem

Alice the architect and Bob the builder play a game. First, Alice chooses two points $P$ and $Q$ in the plane and a subset $\mathcal{S}$ of the plane, which are announced to Bob. Next, Bob marks infinitely many points in the plane, designating each a city. He may not place two cities within distance at most one unit of each other, and no three cities he places may be collinear. Finally, roads are constructed between the cities as follows: for each pair $A,\,B$ of cities, they are connected with a road along the line segment $AB$ if and only if the following condition holds: For every city $C$ distinct from $A$ and $B$, there exists $R\in\mathcal{S}$ such that $\triangle PQR$ is directly similar to either $\triangle ABC$ or $\triangle BAC$. Alice wins the game if (i) the resulting roads allow for travel between any pair of cities via a finite sequence of roads and (ii) no two roads cross. Otherwise, Bob wins. Determine, with proof, which player has a winning strategy.

Note: $\triangle UVW$ is directly similar to $\triangle XYZ$ if there exists a sequence of rotations, translations, and dilations sending $U$ to $X$, $V$ to $Y$, and $W$ to $Z$.

## Solution 1

Alice has a winning strategy: Choose $\mathcal S$ to be the set of of points strictly outside the disk with diameter $PQ$. Then two cities $A$ and $B$ have a road between them if and only if every other city is outside the closed disk with diameter $AB$. Note that this condition is equivalent to the angle $\angle ACB$ being acute for every other city $C$. We need to prove that no matter how Bob chooses cities,

1.   No roads cross, and
2.   All cities are connected.

We first prove (1). Suppose for the sake of contradiction that there are roads between $A$ and $C$ and between $B$ and $D$, and that these roads cross. Then $ABCD$ is a convex quadrilateral, because its diagonals intersect. Now, recall our condition for the existence of roads between $A$ and $C$ and between $B$ and $D$: We must have that the angles $\angle ABC$, $\angle BCD$, $\angle CDA$, and $\angle DAB$ are all acute. Because $ABCD$ is a convex quadrilateral, these angles are the interior angles. Then the sum of the interior angles of $ABCD$ is less than $360^\circ$, a contradiction with the fact that the sum of the interior angles of a quadrilateral is always $360^\circ$. $\rightarrow \leftarrow$

We next prove (2). We use induction on the Euclidean distance between cities. Our base case is that two cities are less than $1$ away from each other. If this is the case, then they are the same city, and so the empty path connects them. Now, suppose for the sake of induction that any two cities less than $\sqrt n$ away from each other have a finite path between them. We will show the same is true for $\sqrt{n + 1}$. Consider any two distinct cities $A$ and $B$ less than $\sqrt{n + 1}$ away from each other. If there is a road between them, we are done. Otherwise, there must be some third city $C$ for which $\angle ACB \geq 90^\circ$. [asy] import markers; size(12cm);  pair A = (-1,0); pair B = (1,0); pair O = (0,0);  // Point C in the upper-left of the disk pair C = dir(120) * 0.8;  draw(circle(O,1)); draw(A--B, dashed); draw(A--C); draw(C--B);  label("less than $\sqrt{n+1}$", A--B, S);  markangle(radius=10, A, C, B);  dot(A); dot(B); dot(C); label("$A$", A, W); label("$B$", B, E); label("$C$", C, N); [/asy]

By the Law of Cosines, we get that \[\overline{AB}^2 \geq \overline{AC}^2 + \overline{CB}^2.\] Because no two cities are closer than $1$ away from each other, both $\overline{AC}$ and $\overline{CB}$ are at least $1$. So, \[\overline{AC}^2 \leq \overline{AB}^2 - \overline{CB}^2 < (n + 1) - 1 = n.\] Hence, by the inductive hypothesis, there is a finite path from $A$ to $C$. Likewise, there is a finite path from $C$ to $B$. Joining these paths together, we get a finite path from $A$ to $B$, as desired.

Hence, any two cities, no matter their distance apart, have a finite path connecting them. $\square$

Note: The graph of roads constructed by Alice's choice of $\mathcal S$ is called the [Gabriel graph](https://en.wikipedia.org/wiki/Gabriel_graph).

## Aside

It may be tempting to choose $S$ so that the graph of roads is the [relative neighborhood graph](https://en.wikipedia.org/wiki/Relative_neighborhood_graph). This can be done by choosing $S$ to be all points outside of the intersection of the disks centered at $A$ and $B$ with radii $\overline{AB}$. However, this only works for finite sets of cities. When the set of cities is infinite, it is possible that the graph won't be connected. For example, consider the infinite set of cities at $A_n = (2n, 0)$ and $B_n = (2n + 1, \sqrt3)$ for positive integers $n$. Then perturb these cities slightly so that \[\overline{B_1A_1} > \overline{A_1A_2} > \overline{A_2B_1} > \overline{B_1B_2} > \overline{B_2A_2} > \overline{A_2A_3} > \overline{A_3B_2} > \overline{B_2B_3} > \overline{B_3A_3} > \cdots.\] In this case, there are never any connections between any of the $\{A_n\}$ and the $\{B_n\}$, so the relative neighborhood graph is disconnected.

## See Also

**[2025 USAMO](https://artofproblemsolving.com/wiki/index.php?title=2025_USAMO "2025 USAMO")** (**[Problems](https://artofproblemsolving.com/wiki/index.php?title=2025_USAMO_Problems "2025 USAMO Problems")** • [Resources](http://www.artofproblemsolving.com/Forum/resources.php?c=182&cid=27&year=2025))
Preceded by

**[Problem 2](https://artofproblemsolving.com/wiki/index.php?title=2025_USAMO_Problems/Problem_2 "2025 USAMO Problems/Problem 2")**Followed by

**[Problem 4](https://artofproblemsolving.com/wiki/index.php?title=2025_USAMO_Problems/Problem_4 "2025 USAMO Problems/Problem 4")**
[1](https://artofproblemsolving.com/wiki/index.php?title=2025_USAMO_Problems/Problem_1 "2025 USAMO Problems/Problem 1")**•**[2](https://artofproblemsolving.com/wiki/index.php?title=2025_USAMO_Problems/Problem_2 "2025 USAMO Problems/Problem 2")**•**[3](https://artofproblemsolving.com/wiki/index.php/2025_USAMO_Problems/Problem_3)**•**[4](https://artofproblemsolving.com/wiki/index.php?title=2025_USAMO_Problems/Problem_4 "2025 USAMO Problems/Problem 4")**•**[5](https://artofproblemsolving.com/wiki/index.php?title=2025_USAMO_Problems/Problem_5 "2025 USAMO Problems/Problem 5")**•**[6](https://artofproblemsolving.com/wiki/index.php?title=2025_USAMO_Problems/Problem_6 "2025 USAMO Problems/Problem 6")
**[All USAMO Problems and Solutions](https://artofproblemsolving.com/wiki/index.php?title=USAMO_Problems_and_Solutions "USAMO Problems and Solutions")**

[](https://artofproblemsolving.com/wiki/index.php?title=File:AMC_Logo.png)
