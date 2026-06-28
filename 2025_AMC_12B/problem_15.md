_The following problem is from the [2025 AMC 10B #19](https://artofproblemsolving.com/wiki/index.php?title=2025\_AMC\_10B\_Problems/Problem\_19 "2025 AMC 10B Problems/Problem 19") and [2025 AMC 12B #15](https://artofproblemsolving.com/wiki/index.php/2025\_AMC\_12B\_Problems/Problem\_15), so those problems redirect to this page._
## Problem

A container has a $1\times 1$ square bottom, a $3\times 3$ open square top, and four congruent trapezoidal sides, as shown. Starting when the container is empty, a hose that runs water at a constant rate takes $35$ minutes to fill the container up to the midline of the trapezoids.

[asy] /* Made by Mathemagician108 */ import graph3; size(200); real a = 1; real d = 0.6; real h = 0.9; triple A1 = (a,0,0); triple B1 = (0,a,0); triple C1 = (-a,0,0); triple D1 = (0,-a,0); triple A2 = (a+d,0,h); triple B2 = (0,a+d,h); triple C2 = (-(a+d),0,h); triple D2 = (0,-(a+d),h); triple A3 = (a+2*d,0,2*h); triple B3 = (0,a+2*d,2*h); triple C3 = (-(a+2*d),0,2*h); triple D3 = (0,-(a+2*d),2*h);  path3 bottom = A1--B1--C1--D1--cycle; path3 backright = A1--B1--B2--A2--cycle; path3 backleft = B1--C1--C2--B2--cycle; path3 frontleft = C1--D1--D3--C3--cycle; path3 frontright = D1--A1--A3--D3--cycle;  defaultpen(1); pen blue = rgb(202, 201, 255); pen red = rgb(255, 164, 164);  // colored surfaces draw(surface(bottom), emissive(gray)); draw(surface(backright), emissive(blue)); draw(surface(backleft), emissive(blue)); draw(surface(frontleft), emissive(red)); draw(surface(frontright), emissive(red)); // black outlines draw(A1--D1--C1); draw(A2--D2--C2); draw(A3--D3--C3, linewidth(1.4)); draw((0.32,0.68,0)--B1--(-0.32,0.68,0)); draw((1.25,0.35,h)--B2--(-1.25,0.35,h)); draw(A3--B3--C3); draw(A1--A3); draw(B1--B3); draw(C1--C3); draw(D1--D3, linewidth(1.4));  currentprojection=perspective((0,-4,3)); [/asy]

How many more minutes will it take to fill the remainder of the container?

$\text{(A) }70 \qquad \text{(B) }85 \qquad \text{(C) }90 \qquad \text{(D) }95 \qquad \text{(E) }105$

## Solution 1

Extend the edges pointing downwards to converge at a point $A$ to form a square pyramid. Consider 3 square pyramids, the large one formed by the top vertices of the original figure and $A$, the middle one formed by the medians running through the sides of the original figure and point $A$, and the smaller one formed by the bottom vertices of the original figure and point $A$. Note that all pyramids are similar since they are all essentially scaled by a certain factor.

The median length is $\frac{3+1}{2}=2$

Using side length to volume ratios, find that the volumes must have ratios $1:8:27$ Then, you get that the ratio of the volume thus filled to the volume that we must fill is equivalent to $8-1:27-8 =  7:19$. Thus, it will take $\frac{19}{7}$ more time to fill the remaining volume giving us an answer of $\frac{19}{7} * 35 = \boxed{\textbf{(D) }95}$

-Failure.net

## Solution 2 (2 min)

Note that dividing this shape along the midline gives two truncated pyramids with base areas and , and and (a truncated pyramid is a pyramid is cut at some point parallel to the base to reach a shape with bases that are squares). Using the truncated pyramid volume formula

\[V = \frac{1}{3}h\,(A_1 + A_2 + \sqrt{A_1A_2}),\]

we get volumes

\[\frac{1}{3}h(1 + 4 + \sqrt{4}) \qquad\text{and}\qquad \frac{1}{3}h(4 + 9 + \sqrt{36}).\]

Writing their ratio, we obtain

\[\frac{13 + 6}{5 + 2} = \frac{19}{7}.\]

Thus,

\[35 \cdot \frac{19}{7} = 95.\]

So the remaining time is .

-Cyrus825

## Solution 3 (Calculus)

The volume that was filled in 35 minutes can be represented as $\int_1^2 s^2 \text{d}s = \frac{1}{3}\left(2^3 - 1^3\right) = \frac{7}{3}$ where $s$ represents the side length of the horizontal cross-sectional square. Then, the volume that remains to be filled is $\int_2^3 s^2 \text{d}s = \frac{1}{3}\left(3^3 - 2^3\right) = \frac{19}{3}.$ Since the filling rate is the same, the amount of time this will take is $35 \cdot \frac{3}{7} \cdot \frac{19}{3} = \boxed{\textbf{(D) }95}$

-grape1984

## Solution 4 (Construction)

Extend the bottom of the container to form an upside down square pyramid. Then take a diagonal cross section as shown below.

[asy] size(220);  // Outer (largest) upside-down isosceles triangle pair A = (0,-4);      // bottom vertex pair B = (-3,0);      // left base point pair C = (3,0);       // right base point  draw(A--B--C--cycle);  // Middle triangle (scaled toward A) real k2 = 0.6; pair B2 = A + k2*(B - A); pair C2 = A + k2*(C - A); draw(A--B2--C2--cycle);  // Smallest triangle (scaled toward A) real k3 = 0.3; pair B3 = A + k3*(B - A); pair C3 = A + k3*(C - A); draw(A--B3--C3--cycle);  // --- Heights (altitudes) ---  // Outer triangle height pair mid1 = (B + C)/2; draw(mid1--A); label("$x_1$", midpoint(mid1--A)+(0.25,1.25));   // centered on the segment label("$3\sqrt{2}$", midpoint(mid1--A)+(3.4,2));   // centered on the segment  // Middle triangle height pair mid2 = (B2 + C2)/2; draw(mid2--A); label("$x_2$", midpoint(mid2--A)+(0.25,0.65));   // centered on the segment label("$2\sqrt{2}$", midpoint(mid2--A)+(2.3,1.2));   // centered on the segment  // Smallest triangle height pair mid3 = (B3 + C3)/2; draw(mid3--A); label("$x_3$", midpoint(mid3--A)+(0.25,0.25));   // centered on the segment label("$\sqrt{2}$", midpoint(mid3--A)+(1.2,0.6));   // centered on the segment [/asy]

You can notice that there are several similar triangles, so we write several equations. \[\frac{x_3}{x_1+x_2+x_3}=\frac{\sqrt{2}}{3\sqrt{2}}\]\[\frac{x_3}{x_2+x_3}=\frac{\sqrt{2}}{2\sqrt{2}}\]

Then solve the system to get: \[x_1=x_2=x_3=x\]

Write the volumes of the three pyramids with sides of the bases 1,2, and 3 respectively: \[V_1=\frac{x}{3}\]\[V_2=\frac{8x}{3}\]\[V_3=9x\]

The volumes of the part of the container below the midline and above it are.

\[V_2-V_1=\frac{7x}{3}\] and \[V_3-V_2=\frac{19x}{3}\]

Then the time $t$ for the top to fill up is given by \[\frac{\frac{19x}{3}}{\frac{7x}{3}}=\frac{t}{35}\] Therefore $t=\boxed{\mathbf{(D)}\ 95}$

-AARONPICK2

## Solution 5(Similar to Solution 1)

Extend the trapezoidal shape into a square pyramid. Note that we're only extending the height by another factor of the height. In other words, if the height from the $1 \times 1$ base to the midline is $h$, the height from the $2 \times 2$ base(which is the midline) to the $3 \times 3$ base(which is the finish) is also $h$. Now using this logic, the distance from the $1 \times 1$ base to the top of the pyramid is obviously also $h$. Now the problem is easy. Computing the volume of the first half of the trapezoidal shape(which takes $35$ minutes for the hose to fill) is

$\frac{1}{3} (2 \cdot 2) \cdot (2h) - \frac{1}{3} (1 \cdot 1) \cdot (h) = \frac{7h}{3}$ which takes $35$ minutes. So to fill up to the height $h$ we get

$h$ takes $35 \cdot \frac{3}{7} = 15$ minutes to fill.

Now to find the volume of the last half of he trapezoidal shape we get

$\frac{1}{3} (3 \cdot 3) \cdot (3h) - \frac{1}{3} (2 \cdot 2) \cdot (2h) = \frac{19h}{3}$ so if we plug in $h$ takes $15$ minutes to fill we get

$\frac{19h}{3}$ takes $\frac{19 \cdot 15}{3} = 19 \cdot 5 = \boxed{95}$ minutes to fill.

~ilikemath247365

## See Also

**[2025 AMC 10B](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B "2025 AMC 10B")** (**[Problems](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems "2025 AMC 10B Problems")** • **[Answer Key](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Answer_Key "2025 AMC 10B Answer Key")** • [Resources](https://artofproblemsolving.com/community/c13))
Preceded by

**[Problem 18](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_18 "2025 AMC 10B Problems/Problem 18")**Followed by

**[Problem 20](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_20 "2025 AMC 10B Problems/Problem 20")**
[1](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_1 "2025 AMC 10B Problems/Problem 1")**•**[2](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_2 "2025 AMC 10B Problems/Problem 2")**•**[3](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_3 "2025 AMC 10B Problems/Problem 3")**•**[4](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_4 "2025 AMC 10B Problems/Problem 4")**•**[5](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_5 "2025 AMC 10B Problems/Problem 5")**•**[6](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_6 "2025 AMC 10B Problems/Problem 6")**•**[7](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_7 "2025 AMC 10B Problems/Problem 7")**•**[8](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_8 "2025 AMC 10B Problems/Problem 8")**•**[9](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_9 "2025 AMC 10B Problems/Problem 9")**•**[10](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_10 "2025 AMC 10B Problems/Problem 10")**•**[11](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_11 "2025 AMC 10B Problems/Problem 11")**•**[12](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_12 "2025 AMC 10B Problems/Problem 12")**•**[13](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_13 "2025 AMC 10B Problems/Problem 13")**•**[14](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_14 "2025 AMC 10B Problems/Problem 14")**•**[15](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_15 "2025 AMC 10B Problems/Problem 15")**•**[16](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_16 "2025 AMC 10B Problems/Problem 16")**•**[17](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_17 "2025 AMC 10B Problems/Problem 17")**•**[18](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_18 "2025 AMC 10B Problems/Problem 18")**•**[19](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_19 "2025 AMC 10B Problems/Problem 19")**•**[20](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_20 "2025 AMC 10B Problems/Problem 20")**•**[21](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_21 "2025 AMC 10B Problems/Problem 21")**•**[22](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_22 "2025 AMC 10B Problems/Problem 22")**•**[23](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_23 "2025 AMC 10B Problems/Problem 23")**•**[24](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_24 "2025 AMC 10B Problems/Problem 24")**•**[25](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_25 "2025 AMC 10B Problems/Problem 25")
**[All AMC 10 Problems and Solutions](https://artofproblemsolving.com/wiki/index.php?title=AMC_10_Problems_and_Solutions "AMC 10 Problems and Solutions")**

[](https://artofproblemsolving.com/wiki/index.php?title=File:AMC_Logo.png)
