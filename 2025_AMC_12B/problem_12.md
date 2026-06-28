## Problem

The windshield wiper on the driver's side of a large bus is depicted below. [asy] /* Made by MRENTHUSIASM */ size(200); pair A, B, C, D; A = origin; B = (3/2,3*sqrt(3)/2); C = B+(0,1.75); D = B-(0,1.75); draw(A--B,linewidth(1.1)); draw(C--D,red+linewidth(2.1)); dot(A^^B,linewidth(5)); label("$A$",A,1.5*W); label("$B$",B,1.5*E); label("$C$",C,1.5*E); label("$D$",D,1.5*E); [/asy] Arm $\overline{AB}$ pivots back and forth around point $A$, sweeping out an arc of $60^{\circ}$, symmetric about the vertical line through $A$. The wiper blade $\overline{CD}$ is attached to $B$ at its midpoint and stays vertical as the arm moves. The arm is $3$ feet long, and the wiper blade is $3.5$ feet tall. What is the area of the windshield cleaned by the wiper, in square feet, to the nearest hundredth? (Assume that the windshield is a flat vertical surface.)

$\textbf{(A) } 9.68 \qquad \textbf{(B) } 10.14 \qquad \textbf{(C) } 10.50 \qquad \textbf{(D) } 11.32 \qquad \textbf{(E) } 12.00$

## Diagram

[asy] /* Made by MRENTHUSIASM */ size(200); pair A, B, C, D, B1, C1, D1; A = origin; B = (3/2,3*sqrt(3)/2); C = B+(0,1.75); D = B-(0,1.75); B1 = (-B.x,B.y); C1 = (-C.x,C.y); D1 = (-D.x,D.y); fill(C--shift(0,1.75)*Arc(A,B,B1)--D1--shift(0,-1.75)*Arc(A,3,120,60)--cycle,palered); draw(A--B,linewidth(1.1)); draw(A--B1,dashed+linewidth(1.1)); draw(C--D,red+linewidth(2.1)); draw(C1--D1,red+dashed+linewidth(2.1)); draw(Arc(A,B,B1),dashed+linewidth(1.1),Arrows(12)); draw(shift(0,1.75)*Arc(A,B,B1),red+dashed+linewidth(2.1),Arrows(12)); draw(shift(0,-1.75)*Arc(A,B,B1),red+dashed+linewidth(2.1),Arrows(12)); dot(A^^B^^B1,linewidth(5)); label("$A$",A,1.5*W); label("$B$",B,1.5*E); label("$C$",C,1.5*E); label("$D$",D,1.5*E); label("$60^{\circ}$",A+(0,3),1.5*N); label("$3$",0.55*B,dir(-30)); Label L1 = Label("$3.5$", align=(0,0), position=MidPoint, filltype=Fill(3,3,white)); draw(C+(1,0)--D+(1,0), L=L1, arrow=Arrows(10),bar=Bars(15), linewidth(1.1)); [/asy] ~MRENTHUSIASM

## Solution 1 (Cavalieri's Principle)

The area cleaned by the wiper follows a thickened curve with vertical ends, where the curve is a $60^\circ$ arc with radius $3$. Since the sides are vertical, by Cavalieri's Principle, the area is equivalent to a rectangle with side lengths $3.5$ and the distance between the two vertical ends. Let $B'$ be the result of point $B$ at its leftmost point after it has swept $60^\circ$. Then $ABB'$ is equilateral so $BB' = AB = 3$. So the area is $3.5 \cdot 3 = \boxed{\textbf{(C) } 10.50}$.

Note: if you aren't aware of Cavalieri's Principle, you can still recognize this by slicing the top curved part of the shape and moving it to the bottom, creating a rectangle with the same area as the original shape.

## Solution 2 (Calculus)

As solution 1 kind of explains, the top and bottom of the area swept out follow the exact same path shape, so we can think of the top one as $f(x)$ and the bottom one as $f(x)-3.5$. As solution 1 points out, the width of the figure is 3. Then, the area between them is $\int_{0}^{3}[f(x)-(f(x)-3.5)]dx = \boxed{\textbf{(C) } 10.50}$.

~dg6665

## Solution 3

Using the diagram (credit - MRENTHUSIASM), we see that the line covers a certain area that we need to find. However, finding funky circle areas usually requires calculus. Using some intuition, we can see that the lune at the top of the area we need to find is the exact required area to remove and place into the bottom crescent. This transformation shifts the area into a perfect rectangle with one side length equal to the height of the blade: \[\text{Height} = 3.5\] To find the other side (the horizontal width), we continue the vertical line $\overline{CD}$ downward at its rightmost position. Then, we draw a perpendicular line from the pivot point $A$ to this extended line $\overline{CD}$, which touches our new location $F$. Let $B'$ be the leftmost position of the arm after the $60^\circ$ sweep. If we draw a perpendicular line from $B'$ touching line $\overline{AF}$ at point $G$, we realize that: \[\triangle AFC \sim \triangle AB'G \text{ by SAS}\] Because of the symmetric angles of the sweep, we know that: \[\angle CAF = \angle B'AG = 60^\circ\] This makes it a standard $30^\circ\text{-}60^\circ\text{-}90^\circ$ triangle. By the ratios of a $30^\circ\text{-}60^\circ\text{-}90^\circ$ triangle, the short leg is half the hypotenuse: \[FA = AG = 1.5\] Since the width spans symmetrically from $G$ to $F$: \[FG = 3\] Now we have our rectangle dimensions, so we just multiply them to find the total area: \[\text{Area} = 3 \times 3.5 = 10.5\] The answer is $\textbf{(C)}$.

~Randomuser456 (Note: this is what you do if you don't know Cavalieri's Principle)

## Solution 4

We just realize that the sector inside and the sector outside have equal areas so we can just imagine it as a $3.5 * 3$rectangle,which gives us $\boxed{10.5}$ (C)

~Aarav22

## See Also

[](https://artofproblemsolving.com/wiki/index.php?title=File:AMC_Logo.png)
