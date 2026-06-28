_The following problem is from the [2024 USAMO/5](https://artofproblemsolving.com/wiki/index.php/2024\_USAMO\_Problems/Problem\_5) and [2024 USAJMO/6](https://artofproblemsolving.com/wiki/index.php?title=2024\_USAJMO\_Problems/Problem\_6 "2024 USAJMO Problems/Problem 6"), so those problems redirect to this page._
## Problem

Point $D$ is selected inside acute triangle $ABC$ so that $\angle DAC=\angle ACB$ and $\angle BDC=90^\circ+\angle BAC$. Point $E$ is chosen on ray $BD$ so that $AE=EC$. Let $M$ be the midpoint of $BC$. Show that line $AB$ is tangent to the circumcircle of triangle $BEM$.

## Solution 1

Let $\angle DBT = \alpha$ and $\angle BEM = \beta$. Extend AD intersects BC at point T, then TC = TA, TE is perpendicular to AC

Thus, AB is the tangent of the circle BEM

Then the question is equivalent as the $\angle ABT$ is the auxillary angle of $\angle BEM$.

_ontinued_

## Solution 2

We notice that $\angle DAC = \angle ACB$, which implies symmetry about the perpendicular bisector of $\overline{AC}$. Therefore, we can extend $\overline{AD}$ to intersect the circumcircle at $Q$, and by symmetry about the perpendicular bisector, $ABQC$ is an isoceles trapezoid. Now, we realize that the midpoint condition is annoying, which really suggests that to simplify things, we take a homothety at $B$ sending $M$ to $C$, and we just need to prove that the circumcircle of $\triangle BE'C$ is tangent to line $\overline{AB}$, where $E'$ is the resultant point from a homothety at $E$. However, funnily enough, $E$ lies on the perpendicular bisector of $\overline{AC}$ because $\overline{AE}=\overline{EC}$, and the perpendicular bisector gets sent to an altitude from $Q$ under homothety, which means $E'$ is simply the intersection of $\overline{BD}$ and the altitude from $Q$ onto $\overline{BC}$! Call that point $P$. We can now ignore points $E$ and $M$. Note that we have not used the $\angle BDC$ condition yet, which means we should probably try angle chasing now. Call $\angle BAC=a, \angle ABC = b$. By angle condition, $\angle BDC = 90+a, \angle CDP = 90-a$. Now, $\angle QCA = \angle BAC = a$, so $\angle PQC = 90 - \angle ACQ = 90-a$. A miracle occurs! $\angle CDP = \angle ACQ$, so quadrilateral $QDPC$ is cyclic! $\angle ABC = \angle AQC = b$ from isoceles trapezoid, and from cyclicity $\angle DPC = 180-b = \angle BPC$. Now we have $\angle ABC = b$ and $\angle BPC = 180-b$, which looks a lot like tangency condition. We realize that it simply is the tangency condition if we extend line $\overline{AB}$ to get the supplementary angle, so we are done.

## See Also

**[2024 USAMO](https://artofproblemsolving.com/wiki/index.php?title=2024_USAMO "2024 USAMO")** (**[Problems](https://artofproblemsolving.com/wiki/index.php?title=2024_USAMO_Problems "2024 USAMO Problems")** • [Resources](http://www.artofproblemsolving.com/Forum/resources.php?c=182&cid=27&year=2024))
Preceded by

**[Problem 4](https://artofproblemsolving.com/wiki/index.php?title=2024_USAMO_Problems/Problem_4 "2024 USAMO Problems/Problem 4")**Followed by

**[Problem 6](https://artofproblemsolving.com/wiki/index.php?title=2024_USAMO_Problems/Problem_6 "2024 USAMO Problems/Problem 6")**
[1](https://artofproblemsolving.com/wiki/index.php?title=2024_USAMO_Problems/Problem_1 "2024 USAMO Problems/Problem 1")**•**[2](https://artofproblemsolving.com/wiki/index.php?title=2024_USAMO_Problems/Problem_2 "2024 USAMO Problems/Problem 2")**•**[3](https://artofproblemsolving.com/wiki/index.php?title=2024_USAMO_Problems/Problem_3 "2024 USAMO Problems/Problem 3")**•**[4](https://artofproblemsolving.com/wiki/index.php?title=2024_USAMO_Problems/Problem_4 "2024 USAMO Problems/Problem 4")**•**[5](https://artofproblemsolving.com/wiki/index.php/2024_USAMO_Problems/Problem_5)**•**[6](https://artofproblemsolving.com/wiki/index.php?title=2024_USAMO_Problems/Problem_6 "2024 USAMO Problems/Problem 6")
**[All USAMO Problems and Solutions](https://artofproblemsolving.com/wiki/index.php?title=USAMO_Problems_and_Solutions "USAMO Problems and Solutions")**

**[2024 USAJMO](https://artofproblemsolving.com/wiki/index.php?title=2024_USAJMO "2024 USAJMO")** (**[Problems](https://artofproblemsolving.com/wiki/index.php?title=2024_USAJMO_Problems "2024 USAJMO Problems")** • [Resources](http://www.artofproblemsolving.com/Forum/resources.php?c=182&cid=176&year=2024))
Preceded by

**[Problem 5](https://artofproblemsolving.com/wiki/index.php?title=2024_USAJMO_Problems/Problem_5 "2024 USAJMO Problems/Problem 5")**Followed by

**Last Problem**
[1](https://artofproblemsolving.com/wiki/index.php?title=2024_USAJMO_Problems/Problem_1 "2024 USAJMO Problems/Problem 1")**•**[2](https://artofproblemsolving.com/wiki/index.php?title=2024_USAJMO_Problems/Problem_2 "2024 USAJMO Problems/Problem 2")**•**[3](https://artofproblemsolving.com/wiki/index.php?title=2024_USAJMO_Problems/Problem_3 "2024 USAJMO Problems/Problem 3")**•**[4](https://artofproblemsolving.com/wiki/index.php?title=2024_USAJMO_Problems/Problem_4 "2024 USAJMO Problems/Problem 4")**•**[5](https://artofproblemsolving.com/wiki/index.php?title=2024_USAJMO_Problems/Problem_5 "2024 USAJMO Problems/Problem 5")**•**[6](https://artofproblemsolving.com/wiki/index.php?title=2024_USAJMO_Problems/Problem_6 "2024 USAJMO Problems/Problem 6")
**[All USAJMO Problems and Solutions](https://artofproblemsolving.com/wiki/index.php?title=USAJMO_Problems_and_Solutions "USAJMO Problems and Solutions")**

[](https://artofproblemsolving.com/wiki/index.php?title=File:AMC_Logo.png)
