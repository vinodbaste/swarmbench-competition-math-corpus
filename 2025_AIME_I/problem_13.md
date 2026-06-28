## Problem
Alex divides a disk into four quadrants with two perpendicular diameters intersecting at the center of the disk. He draws $25$ more lines segments through the disk, drawing each segment by selecting two points at random on the perimeter of the disk in different quadrants and connecting these two points. Find the expected number of regions into which these $27$ line segments divide the disk.

## Solution 1
First, we calculate the probability that two segments intersect each other. Let the quadrants be numbered $1$ through $4$ in the normal labeling of quadrants, let the two perpendicular diameters be labeled the $x$-axis and $y$-axis, and let the two segments be $A$ and $B.$

$\textbf{Case 1:}$ Segment $A$ has endpoints in two opposite quadrants.

[asy]
pair A,B,C,D,E,F,O;
A=(1,0);B=(0,1);C=(-1,0);D=(0,-1);E=(0.5,0.86602540);F=(-0.707106,-0.707106);O=(0,0);
draw(A--C);draw(B--D);draw(circle((0,0),1));draw(E--F,blue);dot(E,blue);dot(F,blue);
[/asy]

This happens with probability $\frac{1}{3}.$ WLOG let the two quadrants be $1$ and $3.$ We do cases in which quadrants segment $B$ lies in.
* Quadrants $1$ and $2,$ $2$ and $3,$ $3$ and $4,$ and $4$ and $1$: These share one quadrant with $A,$ and it is clear that for any of them to intersect $A,$ the endpoint that shares a quadrant with an endpoint of $A$ on a certain side of that endpoint of $A$ For example, if it was quadrants $1$ and $2,$ then the point in quadrant $1$ must be closer to the $x$-axis than the endpoint of $A$ in quadrant $1.$ This happens with probability $\frac{1}{2}.$ Additionally, segment $B$ has a $\frac{1}{6}$ to have endpoints in any set of two quadrants, so this case contributes to the total probability

\[\dfrac{1}{3}\left(\dfrac{1}{6}\cdot\dfrac{1}{2}+\dfrac{1}{6}\cdot\dfrac{1}{2}+\dfrac{1}{6}\cdot\dfrac{1}{2}+\dfrac{1}{6}\cdot\dfrac{1}{2}\right)=\dfrac{1}{9}\]

* Quadrants $2$ and $4.$ This always intersects segment $A,$ so this case contributes to the total probability

\[\dfrac{1}{3}\cdot\dfrac{1}{6}=\dfrac{1}{18}\]

* Quadrants $1$ and $3.$ We will first choose the endpoints, and then choose the segments from the endpoints. Let the endpoints of the segments in quadrant $1$ be $R_1$ and $R_2,$ and the endpoints of the segments in quadrant $3$ be $S_1$ and $S_2$ such that $R_1,R_2,S_1,$ and $S_2$ are in clockwise order. Note that the probability that $A$ and $B$ intersect is the probability that $A_1$ is paired with $B_1,$ which is $\dfrac{1}{2}.$ Thus, this case contributes to the total probability

\[\dfrac{1}{3}\cdot\dfrac{1}{6}\cdot\dfrac{1}{2}=\dfrac{1}{36}.\]

$\textbf{Case 2:}$
Segment $A$ has endpoints in two adjacent quadrants.

[asy]
pair A,B,C,D,E,F,O;
A=(1,0);B=(0,1);C=(-1,0);D=(0,-1);E=(0.5,0.86602540);F=(-0.707106,0.707106);O=(0,0);
draw(A--C);draw(B--D);draw(circle((0,0),1));draw(E--F,blue);dot(E,blue);dot(F,blue);
[/asy]

This happens with probability $\frac{2}{3}.$ WLOG let the two quadrants be $1$ and $2.$ We do cases in which quadrants segment $B$ lies in.
* Quadrants $1$ and $3,$ $1$ and $4,$ $2$ and $3,$ and $2$ and $4.$ This is similar to our first case above, so this contributes to the total probability

\[\dfrac{2}{3}\left(\dfrac{1}{6}\cdot\dfrac{1}{2}+\dfrac{1}{6}\cdot\dfrac{1}{2}+\dfrac{1}{6}\cdot\dfrac{1}{2}+\dfrac{1}{6}\cdot\dfrac{1}{2}\right)=\dfrac{2}{9}\]

* Quadrants $3$ and $4.$ This cannot intersect segment $A.$
* Quadrants $1$ and $2,$ Similar to our third case above, this intersects segment $A$ with probability $\frac{1}{2},$ so this case contributes to the total probability

\[\dfrac{2}{3}\cdot\dfrac{1}{6}\cdot\dfrac{1}{2}=\dfrac{1}{18}.\]

Thus, the probability that two segments intersect is

\[\dfrac{1}{9}+\dfrac{1}{18}+\dfrac{1}{36}+\dfrac{2}{9}+\dfrac{1}{18}=\dfrac{17}{36}.\]

Next, we will compute the expected number of intersections of a segment with the axes. WLOG let a segment have an endpoint in quadrant $1.$ Then, it will intersect each axis with probability $\dfrac{2}{3}$ because two out of the three remaining quadrants let it intersect a specific axis, so the expected number of axes a segment intersects is $\frac{4}{3}.$

So, why do intersections matter? Because when adding a segment, it will pass through a number of regions, and for each region it passes through, it will split that region into two and add another region. The segment starts in a region, and for each intersection, it will enter another region, so the number of regions a segment passes through is $1$ more than the number of intersections with the axes and other segments. Thus, we have that by linearity of expectation the expected number of new regions created by adding a segment is

\[\dfrac{17}{36}\cdot(\text{number of segments already added})+\dfrac{4}{3}+1,\]

so the number of new regions added in total by $25$ segments again by linearity of expectation is

\[\sum_{k=0}^{24}\left(\dfrac{17}{36}k+\dfrac{7}{3}\right)=\dfrac{17}{36}\cdot \dfrac{24\cdot 25}{2}+\dfrac{25\cdot 7}{3}\]

which simplifies to $200$ as the expected number of new regions added by the $25$ segments. The axes create $4$ regions to begin with, so our answer is

\[200+4=\boxed{204}.\]

~BS2012, eevee9406 ~hashbrown2009

## Solution 2
Claim: If N line segments are drawn in the disk so that no three meet at an interior point (true with probability 1 here), then
R = 1 + N + I,
where I is the total number of interior intersection points among the segments.

Reason: When you draw a new segment that meets previous segments in k interior points, it is cut into k+1 pieces, creating k+1 new regions. Summing “+1” over all segments gives +N, and summing k over all segments counts each intersection once, giving +I.

Here N = 27, so
E[R] = 1 + 27 + E[I] = 28 + E[I].

Step 1: Intersections involving the two perpendicular diameters.
The two diameters intersect once at the center.

Now consider a random chord: endpoints are chosen uniformly on the circle, conditioned to lie in different quadrants. Thus the unordered quadrant-pair is uniform among the C(4,2)=6 pairs.

Fix one diameter (say the horizontal). A chord crosses it iff its endpoints lie in opposite half-disks, i.e. it uses one quadrant above and one below. Among the 6 quadrant-pairs, 4 have this property, so
P(chord intersects a fixed diameter) = 4/6 = 2/3.

There are 25 chords and 2 diameters, so
E[(diameter–chord intersections)] = 25 · 2 · (2/3) = 100/3.

So far:
E[I] = 1 + 100/3 + E[(chord–chord intersections)].

Step 2: Probability that two random chords intersect.
Label the four quadrant arcs cyclically A, B, C, D. A chord type is an unordered pair of distinct arcs; there are 6 types:
AB, BC, CD, DA (adjacent) and AC, BD (opposite).

Because all arcs have equal length, conditioning on “different quadrants” makes the 6 chord types equally likely; hence an ordered pair of chord types is uniform among 6² = 36 cases.

For each ordered type-pair:
• If the two chords are AB and CD (or CD and AB), or BC and DA (or DA and BC), they cannot intersect (their endpoints lie in two disjoint arcs in a non-alternating way): probability 0. That gives 4 ordered cases.
• If the two chords are AC and BD (or BD and AC), they always intersect: probability 1. That gives 2 ordered cases.
• In every other ordered case, the chords share exactly one arc (e.g. AB with AC shares A, etc.). Then, whether they intersect depends only on which of the two points on that shared arc comes first along the circle, which is equally likely. So the intersection probability is 1/2. There are 36 − 4 − 2 = 30 such ordered cases.

Therefore
P(two random chords intersect) = [2·1 + 30·(1/2) + 4·0] / 36
= (2 + 15)/36
= 17/36.

There are C(25,2) = 300 chord pairs, so
E[(chord–chord intersections)] = 300 · (17/36) = 425/3.

Step 3: Assemble.
E[I] = 1 + 100/3 + 425/3
= 1 + 525/3
= 1 + 175
= 176.

Thus
E[R] = 28 + 176 = 204.

Answer: 204.

~Gray_Wolf

## Video Solution
2025 AIME I #13

MathProblemSolvingSkills.com
