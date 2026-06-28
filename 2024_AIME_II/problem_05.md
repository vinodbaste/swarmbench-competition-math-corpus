## Problem

Let ABCDEF be a convex equilateral hexagon in which all pairs of opposite sides are parallel. The triangle whose sides are extensions of segments AB, CD, and EF has side lengths 200, 240, and 300. Find the side length of the hexagon.

## Solution 1

[](https://artofproblemsolving.com/wiki/index.php?title=File:2024_AIME_II_5.png)

Draw a good diagram! Let $AF \cap BC$, $BC \cap DE$, and $AF \cap DE$ be K, L, and M, respectively. Let $KL=200, KM=300, ML=240$.

Notice that because of the parallel condition, all smaller triangles formed are all similar to the larger $(200,240,300)$ triangle.

Let the side length of the hexagon be $x.$

Triangle $\triangle MEF \sim \triangle MLK$, so $\frac{KL}{KM} =\frac{x}{FM} =\frac{200}{300} \implies FM=\frac{3x}{2}$.

Triangle $\triangle KAB \sim \triangle KML$, so $\frac{LM}{KM}=\frac{x}{KA} = \frac{240}{300} \implies AK=\frac{5x}{4}$.

We know $KA+AF+FM=300$, so $\frac{5}{4}x + x + \frac{3}{2}x = 300$. Solving, we get $x=\boxed{080}$.

-westwoodmonster

## Solution 2 (Fakesolve)

Draw an accurate diagram using the allowed compass and ruler: Draw a to-scale diagram of the $(200,240,300)$ triangle (e.g. 10cm-12cm-15cm). Because of the nature of these lengths and the integer answer needed, it can be assumed that the side length of the hexagon will be divisible by 10. Therefore, a trial-and-error method can be set up, wherein line segments of length $n\cdot 10$, scaled to the same scale as the triangle, can be drawn to represent the sides of the hexagon. For instance, side $BC$ would be drawn parallel to the side of the triangle of length 300, and would have endpoints on the other sides of the triangle. Using this method, it would be evident that line segments of length 80 units, scaled proportionally (4cm using the scale above), would create a perfect equilateral hexagon when drawn parallel to the sides of the triangle. $x=\boxed{080}$. - lackolith

## Note

This problem is really similar to 2021 Spring AMC 10A Problem 21. This really emphasizes the importance of studying up on past tests before taking the AMC.

-DoHumanitariansEatHumans
