## Problem

On $\triangle ABC$ points $A$, $D$, $E$, and $B$ lie in that order on side $\overline{AB}$ with $AD = 4$, $DE = 16$, and $EB = 8$. Points $A$, $F$, $G$, and $C$ lie in that order on side $\overline{AC}$ with $AF = 13$, $FG = 52$, and $GC = 26$. Let $M$ be the reflection of $D$ through $F$, and let $N$ be the reflection of $G$ through $E$. Quadrilateral $DEGF$ has area $288$. Find the area of heptagon $AFNBCEM$.

[asy] unitsize(14); pair A = (0, 9), B = (-6, 0), C = (12, 0), D = (5A + 2B)/7, E = (2A + 5B)/7, F = (5A + 2C)/7, G = (2A + 5C)/7, M = 2F - D, N = 2E - G; filldraw(A--F--N--B--C--E--M--cycle, lightgray); draw(A--B--C--cycle); draw(D--M); draw(N--G); dot(A); dot(B); dot(C); dot(D); dot(E); dot(F); dot(G); dot(M); dot(N); label("$A$", A, dir(90)); label("$B$", B, dir(225)); label("$C$", C, dir(315)); label("$D$", D, dir(135)); label("$E$", E, dir(135)); label("$F$", F, dir(45)); label("$G$", G, dir(45)); label("$M$", M, dir(45)); label("$N$", N, dir(135)); [/asy]

## Solution 1

Note that the triangles outside $\triangle ABC$ have the same height as the unshaded triangles in $\triangle ABC$. Since they have the same bases, the area of the heptagon is the same as the area of triangle $ABC$. Therefore, we need to calculate the area of $\triangle ABC$. Denote the length of $DF$ as $x$ and the altitude of $A$ to $DF$ as $h$. Since $\triangle ADF \sim \triangle AEG$, $EG = 5x$ and the altitude of $DFGE$ is $4h$. The area $[DFGE] = \frac{5x + x}{2} \cdot 4h = 3x \cdot 4h = 12xh = 288 \implies xh = 24$. The area of $\triangle ABC$ is equal to $\frac{1}{2} 7x \cdot 7h = \frac{1}{2} 49xh = \frac{1}{2} 49 \cdot 24 = \frac{1}{2} 1176 = \boxed{588}$.

~alwaysgonnagiveyouup

## Solution 2

Because of reflections, and various triangles having the same bases, we can conclude that $|AFNBCEM| = |ABC|$. Through the given lengths of $4-16-8$ on the left and $13-52-26$ on the right, we conclude that the lines through $\triangle ABC$ are parallel, and the sides are in a $1:4:2$ ratio. Because these lines are parallel, we can see that $ADF,~AEG,~ABC$, are similar, and from our earlier ratio, we can give the triangles side ratios of $1:5:7$, or area ratios of $1:25:49$. Quadrilateral $DEGF$ corresponds to the $|AEG|-|ADF|$, which corresponds to the ratio $25-1=24$. Dividing $288$ by $24$, we get $12$, and finally multiplying $12 \cdot 49$ gives us our answer of $\boxed{588}$

~shreyan.chethan, cleaned up by cweu001

## Solution 3

By area lemma, we can see that the areas of the shaded areas are equivalent to the areas of the unshaded areas. Thus, we see that the desired area is equivalent to the area of the triangle $\triangle ABC$. Since $AF : FG : GC = 1 : 4 : 2$, we have $[ADF]:[AEG]:[ABC] = 1:25:49$, meaning $[ADF]:[DEGF]:[BEGC] = 1:24:24$. Thus, since $\frac{[DEGF]}{ABC} = \frac{24}{49}$, we can calculate $[ABC] = 588$.

~cweu001, cleaned up by shreyan.chethan

## Solution 4 (Vectors)

Let be given with points on segment such that lie in that order, and , , and . Similarly, points lie on segment such that lie in that order with , , and .

Note that the segment is partitioned into three parts with lengths , which simplifies to the ratio . Similarly, segment is partitioned into parts , also reducing to the ratio . This implies that the points divide and points divide in the same proportions.

Because the divisions correspond proportionally on and , the line segments and are parallel to . In particular, triangles , , and are similar by the Angle-Angle similarity criterion.

Let us introduce vector notation for convenience. Represent points by vectors respectively. Then the points on satisfy:

, , , ,

and the points on satisfy:

, . , .

The point is the reflection of about , so

, ,

and is the reflection of about , so

. .

The polygon has vertices at .

Because and are reflections of points and about points and respectively, the triangles and are congruent to and respectively. Thus, the area of polygon can be decomposed as

\[[heptagon] = [ \triangle ABC ] + [ \triangle DFM ] + [ \triangle EGN ] = [ \triangle ABC ] + [ \triangle ADF ] + [ \triangle AEG ].\]

Since , , and are similar with similarity ratios in lengths of , their areas are in the ratio

\[[ADF] : [AEG] : [ABC] = 1^2 : 5^2 : 7^2 = 1:25:49.\]

Given the quadrilateral is the region between and , its area is

\[[DEGF] = [AEG] - [ADF] = 25k - k = 24k,\]

where .

From the problem, , so

\[24k = 288 \implies k = 12.\]

Hence,

\[[ABC] = 49k = 49 \times 12 = 588.\]

Since the heptagon's area is , but recalling that and are precisely the reflected copies of and that replace these smaller triangles inside , the total area of the heptagon is exactly the area of : .

~Pinotation

## Solution 5 (area ratio)

Note that the heptagon $AFNBCEM$ has the same area as $\triangle ABC$, because both trapezoids $FNEM$ and $NBCE$ have the same bases and height as trapezoids $DEGF$ and $EBCG$ respectively, and $\triangle AFM$ has the same base and height as $\triangle ADF$.

In $\triangle ABC$, let angle $\angle BAC=\theta$.

We can see that $[DEGF]=[AEG]-[ADF]$. From this, we can say that

$288=(\frac{1}{2}AE\cdot AG \sin\theta)-(\frac{1}{2}AD\cdot AF \sin\theta)$

$288=(\frac{1}{2}\cdot 20\cdot 65 \sin(\theta)-(\frac{1}{2}\cdot 4\cdot 13 \sin\theta)$

$288=624\sin\theta$

$\sin\theta = \frac{6}{13}$

Now we can calculate the area of $\triangle ABC$.

$[ABC]=\frac{1}{2}AB\cdot AC\sin\theta$

$[ABC]=\frac{1}{2}\cdot 28\cdot 91\cdot \frac{6}{13}$

If you calculate, you get $[AFNBCEM]=[ABC]=\boxed{588}$. ~[User:Lentarot](https://artofproblemsolving.com/wiki/index.php?title=User:Lentarot "User:Lentarot") ~minor latex corrections by Glowworm
