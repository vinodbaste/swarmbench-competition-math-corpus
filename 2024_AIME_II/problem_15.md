## Problem

Find the number of rectangles that can be formed inside a fixed regular dodecagon ($12$-gon) where each side of the rectangle lies on either a side or a diagonal of the dodecagon. The diagram below shows three of those rectangles.

[asy] /* Made by Mathemagician108 */ unitsize(0.6 inch); for(int i=0; i<360; i+=30) { dot(dir(i), 4+black); draw(dir(i)--dir(i+30)); } draw(dir(120)--dir(330)); filldraw(dir(210)--dir(240)--dir(30)--dir(60)--cycle, mediumgray, linewidth(1.5)); draw((0,0.366)--(0.366,0), linewidth(1.5)); [/asy]

## Solution 1

By Furaken

There are two kinds of such rectangles: those whose sides are parallel to some edges of the regular 12-gon (Case 1), and those whose sides are not (Case 2).

For Case 1, WLOG assume that the rectangle's sides are horizontal and vertical (don't forget to multiply by 3 at the end of Case 1). Then the rectangle's sides coincide with these segments as shown in the diagram. [asy] real r = pi/6; pair A1 = (cos(r),sin(r)); pair A2 = (cos(2r),sin(2r)); pair A3 = (cos(3r),sin(3r)); pair A4 = (cos(4r),sin(4r)); pair A5 = (cos(5r),sin(5r)); pair A6 = (cos(6r),sin(6r)); pair A7 = (cos(7r),sin(7r)); pair A8 = (cos(8r),sin(8r)); pair A9 = (cos(9r),sin(9r)); pair A10 = (cos(10r),sin(10r)); pair A11 = (cos(11r),sin(11r)); pair A12 = (cos(12r),sin(12r)); dot(A1); dot(A2); dot(A3); dot(A4); dot(A5); dot(A6); dot(A7); dot(A8); dot(A9); dot(A10); dot(A11); dot(A12); pair B1 = (0.5,0.5); pair B2 = (-0.5,0.5); pair B3 = (-0.5,-0.5); pair B4 = (0.5,-0.5); dot(B1); dot(B2); dot(B3); dot(B4); draw(A1--A5--A7--A11--cycle); draw(A2--A4--A8--A10--cycle); draw(A3--A9); draw(A6--A12); label("$A_1$", A1, NE); label("$A_2$", A2, NE); label("$A_3$", A3, N); label("$A_4$", A4, NW); label("$A_5$", A5, NW); label("$A_6$", A6, W); label("$A_7$", A7, SW); label("$A_8$", A8, SW); label("$A_9$", A9, S); label("$A_{10}$", A10, SE); label("$A_{11}$", A11, SE); label("$A_{12}$", A12, E); label("$B_1$", B1, SW); label("$B_2$", B2, SE); label("$B_3$", B3, NE); label("$B_4$", B4, NW); [/asy] We use inclusion-exclusion for this. There are 30 valid rectangles contained in $A_1A_5A_7A_{11}$, as well as 30 in $A_2A_4A_8A_{10}$. However, the 9 rectangles contained in $B_1B_2B_3B_4$ have been counted twice, so we subtract 9 and we have 51 rectangles in the diagram. Multiplying by 3, we get 153 rectangles for Case 1.

For Case 2, we have this diagram. To be honest, you can count the rectangles here in whatever way you like. [asy] real r = pi/6; pair A1 = (cos(r),sin(r)); pair A2 = (cos(2r),sin(2r)); pair A3 = (cos(3r),sin(3r)); pair A4 = (cos(4r),sin(4r)); pair A5 = (cos(5r),sin(5r)); pair A6 = (cos(6r),sin(6r)); pair A7 = (cos(7r),sin(7r)); pair A8 = (cos(8r),sin(8r)); pair A9 = (cos(9r),sin(9r)); pair A10 = (cos(10r),sin(10r)); pair A11 = (cos(11r),sin(11r)); pair A12 = (cos(12r),sin(12r)); dot(A1); dot(A2); dot(A3); dot(A4); dot(A5); dot(A6); dot(A7); dot(A8); dot(A9); dot(A10); dot(A11); dot(A12); draw(A1--A6--A7--A12--cycle); draw(A3--A4--A9--A10--cycle); draw(A2--A5--A8--A11--cycle); label("$A_1$", A1, NE); label("$A_2$", A2, NE); label("$A_3$", A3, N); label("$A_4$", A4, NW); label("$A_5$", A5, NW); label("$A_6$", A6, W); label("$A_7$", A7, SW); label("$A_8$", A8, SW); label("$A_9$", A9, S); label("$A_{10}$", A10, SE); label("$A_{11}$", A11, SE); label("$A_{12}$", A12, E); [/asy] There are 36 rectangles contained within $A_2A_5A_8A_{11}$, and 18 that use points outside $A_2A_5A_8A_{11}$. So we get a total of $3(36+18)=162$ rectangles for Case 2.

Adding the two cases together, we get the answer $\boxed{315}$.

## Solution 2

Using the same diagram as Solution 1, we can get the number of rectangles from Case 1 by adding the number of rectangles of $A_2$$A_8$$A_8$$A_{10}$ and $A_1$$A_5$$A_7$$A_{11}$ and then subtracting the overlaps,

\[\binom{5}{2}\binom{3}{2} + \binom{5}{2}\binom{3}{2} - \binom{3}{2}\binom{3}{2}\]\[=51\]

We multiply this by 3 to get the total number of rectangles for Case 1, which is 153.

For Case 2, we can first get the total number of rectangles from $A_2A_3A_4A_5A_8A_9A_{10}A_{11}$ then add $A_1A_6A_7A_{12}$ and subtract by the overlaps, \[\binom{4}{2}\binom{4}{2} + \binom{6}{2} - \binom{4}{2} + \binom{6}{2} - \binom{4}{2}\]\[= 54\] Multiply that by 3 and add it to Case 1 to get $\boxed{315}$.

~pengf

## Solution 3

We put the dodecagon in the right position that there exists a side whose slope is 0. Note that finding a rectangle is equivalent to finding two pairs of lines, such that two lines in each pair are parallel and lines from different pairs are perpendicular. Now, we use this property to count the number of rectangles.

Because two pairs of lines that form a rectangle are perpendicular, we only need to use the slope of one pair, denoted as $k$, to determine the direction of the rectangle. The slope of the other pair is thus $- \frac{1}{k}$. To avoid overcounting, we do casework analysis by defining each case in term of $0 \leq k < \infty$ only (we make a convention that if $k = 0$, then $- \frac{1}{k} = \infty$).

In our counting, we will frequently quantify the distance between two vertices of the regular dodecagon. To characterize this in a straightforward way, we simply measure the number of vertices (on the minor arc) between our measured two vertices. For instance, two vertices on a side has distance 0. Distances between two vertices that are diagonals can be 1, 2, 3, 4, 5.

Case 1: $k = 0, \tan 30^\circ, \tan 60^\circ$.

We only count for $k = 0$. The number of solutions for $k = \tan 30^\circ$ and $\tan 60^\circ$ are the same.

Consider $k = 0$. We need to find a pair of horizontal segments and a pair of vertical segments to form a rectangle.

For $k = 0$, the length of each horizontal segment can only be 0, 2, 4.

Denote by $2i$ the shorter length of two parallel horizontal segments. Given $i$, the number of pairs of two parallel horizontal segments is $1 + 2 \left( 4 - 2 i \right)$.

Given $i$, to form a rectangle, the number of pairs of vertical segments is $\binom{2i + 2}{2}$.

Therefore, for $k = 0$, the number of rectangles is

The number of rectangles for $k = \tan 30^\circ$ and $\tan 60^\circ$ are the same. Therefore, the total number of rectangles in this case is $54 \cdot 3 = 162$.

Case 2: $k = \tan 15^\circ$, $\tan 45^\circ$, $\tan 75^\circ$.

The number of rectangles under all these $k$s are the same. So we only count for $k = \tan 15^\circ$.

For $k = \tan 15^\circ$, the length of each segment can only be 1, 3, 5. However, there is only one segment with length 5. So this cannot be the shorter length of two parallel segments with slope $\tan 15^\circ$.

Denote by $2i + 1$ the shorter length of two parallel segments with slope $\tan 15^\circ$. Given $i$, the number of pairs of two parallel segments is $1 + 2 \left( 3 - 2 i \right)$.

Given $i$, to form a rectangle, the number of pairs of vertical segments is $\binom{2i + 3}{2}$.

Therefore, for $k = \tan 15^\circ$, the number of rectangles is

The number of rectangles for $k = \tan 45^\circ$ and $\tan 75^\circ$ are the same. Therefore, the total number of rectangles in this case is $51 \cdot 3 = 153$.

Putting all cases together, the total number of rectangles is $162 + 153 = \boxed{\textbf{(315) }}$.

~Steven Chen and SHEN KISLAY KAI(Professor Chen Education Palace, www.professorchenedu.com)
