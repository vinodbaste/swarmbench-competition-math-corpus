## Problem

Define $f(x)=|| x|-\tfrac{1}{2}|$ and $g(x)=|| x|-\tfrac{1}{4}|$. Find the number of intersections of the graphs of \[y=4 g(f(\sin (2 \pi x))) \quad\text{ and }\quad x=4 g(f(\cos (3 \pi y))).\]

## Graph

[https://www.desmos.com/calculator/wml09giaun](https://www.desmos.com/calculator/wml09giaun)

## Solution 1

If we graph $4g(f(x))$, we see it forms a sawtooth graph that oscillates between $0$ and $1$ (for values of $x$ between $-1$ and $1$, which is true because the arguments are between $-1$ and $1$). Thus by precariously drawing the graph of the two functions in the square bounded by $(0,0)$, $(0,1)$, $(1,1)$, and $(1,0)$, and hand-counting each of the intersections, we get $\boxed{385}$

While this solution might seem unreliable (it probably is), the only parts where counting the intersection might be tricky is near $(1,1)$. Make sure to count them as two points and not one, or you'll get $384$.

## Note 1

The answer should be 385 since there are 16 intersections in each of 24 smaller boxes of dimensions 1/6 x 1/4 and then another one at the corner (1,1).

## Solution 2

We will denote $h(x)=4g(f(x))$ for simplicity. Denote $p(x)$ as the first equation and $q(y)$ as the graph of the second. We notice that both $f(x)$ and $g(x)$ oscillate between 0 and 1. The intersections are thus all in the square $(0,0)$, $(0,1)$, $(1,1)$, and $(1,0)$. Every $p(x)$ wave going up and down crosses every $q(y)$ wave. Now, we need to find the number of times each wave touches 0 and 1.

We notice that $h(x)=0$ occurs at $x=-\frac{3}{4}, -\frac{1}{4}, \frac{1}{4}, \frac{3}{4}$, and $h(x)=1$ occurs at $x=-1, -\frac{1}{2}, 0,\frac{1}{2},1$. A sinusoid passes through each point twice during each period, but it only passes through the extrema once. $p(x)$ has 1 period between 0 and 1, giving 8 solutions for $p(x)=0$ and 9 solutions for $p(x)=1$, or 16 up and down waves. $q(y)$ has 1.5 periods, giving 12 solutions for $q(y)=0$ and 13 solutions for $q(y)=1$, or 24 up and down waves. This amounts to $16\cdot24=384$ intersections.

However, we have to be very careful when counting around $(1, 1)$. At this point, $q(y)$ has an infinite downwards slope and $p(x)$ is slanted, giving us an extra intersection; thus, we need to add 1 to our answer to get $\boxed{385}$.

~Xyco

## Solution 3 (Rigorous analysis of why there are two solutions near (1,1))

We can easily see that only $x, y \in \left[0,1 \right]$ may satisfy both functions. We call function $y = 4g \left( f \left( \sin \left( 2 \pi x \right) \right) \right)$ as Function 1 and function $x = 4g \left( f \left( \cos \left( 3 \pi y \right) \right) \right)$ as Function 2.

For Function 1, in each interval $\left[ \frac{i}{4} , \frac{i+1}{4} \right]$ with $i \in \left\{ 0, 1, \cdots, 3 \right\}$, Function 1's value oscillates between 0 and 1. It attains 1 at $x = \frac{i}{4}$, $\frac{i+1}{4}$ and another point between these two. Between two consecutive points whose functional values are 1, the function first decreases from 1 to 0 and then increases from 0 to 1. So the graph of this function in this interval consists of 4 monotonic pieces.

For Function 2, in each interval $\left[ \frac{i}{6} , \frac{i+1}{6} \right]$ with $i \in \left\{ 0, 1, \cdots, 5 \right\}$, Function 2's value oscillates between 0 and 1. It attains 1 at $y = \frac{i}{6}$, $\frac{i+1}{6}$ and another point between these two. Between two consecutive points whose functional values are 1, the function first decreases from 1 to 0 and then increases from 0 to 1. So the graph of this function in this interval consists of 4 monotonic curves.

Consider any region $\left[ \frac{i}{4} , \frac{i+1}{4} \right] \times \left[ \frac{j}{6} , \frac{j+1}{6} \right]$ with $i \in \left\{ 0, 1, \cdots, 3 \right\}$ and $j \in \left\{0, 1, \cdots , 5 \right\}$ but $\left( i, j \right) \neq \left( 3, 5 \right)$. Both functions have four monotonic pieces. Because Function 1's each monotonic piece can take any value in $\left[ \frac{j}{6} , \frac{j+1}{6} \right]$ and Function 2' each monotonic piece can take any value in $\left[ \frac{i}{4} , \frac{i+1}{4} \right]$, Function 1's each monotonic piece intersects with Function 2's each monotonic piece. Therefore, in the interval $\left[ \frac{i}{4} , \frac{i+1}{4} \right] \times \left[ \frac{j}{6} , \frac{j+1}{6} \right]$, the number of intersecting points is $4 \cdot 4 = 16$.

Next, we prove that if an intersecting point is on a line $x = \frac{i}{4}$ for $i \in \left\{ 0, 1, \cdots, 4 \right\}$, then this point must be $\left( 1, 1 \right)$.

For $x = \frac{i}{4}$, Function 1 attains value 1. For Function 2, if $y = 1$, then $x = 1$. Therefore, the intersecting point is $\left( 1, 1 \right)$.

Similarly, we can prove that if an intersecting point is on a line $y = \frac{i}{6}$ for $i \in \left\{ 0, 1, \cdots, 6 \right\}$, then this point must be $\left( 1, 1 \right)$.

Therefore, in each region $\left[ \frac{i}{4} , \frac{i+1}{4} \right] \times \left[ \frac{j}{6} , \frac{j+1}{6} \right]$ with $i \in \left\{ 0, 1, \cdots, 3 \right\}$ and $j \in \left\{0, 1, \cdots , 5 \right\}$ but $\left( i, j \right) \neq \left( 3, 5 \right)$, all 16 intersecting points are interior. That is, no two regions share any common intersecting point.

Next, we study region $\left[ \frac{3}{4} , 1 \right] \times \left[ \frac{5}{6} , 1 \right]$. Consider any pair of monotonic pieces, where one is from Function 1 and one is from Function 2, except the pair of two monotonic pieces from two functions that attain $\left( 1 , 1 \right)$. Two pieces in each pair intersects at an interior point on the region. So the number of intersecting points is $4 \cdot 4 - 1 = 15$.

Finally, we compute the number intersection points of two functions' monotonic pieces that both attain $\left( 1, 1 \right)$.

One trivial intersection point is $\left( 1, 1 \right)$. Now, we study whether they intersect at another point.

Define $x = 1 - x'$ and $y = 1 - y'$. Thus, for positive and sufficiently small $x'$ and $y'$, Function 1 is reduced to \[ y' = 4 \sin 2 \pi x' \hspace{1cm} (1) \] and Function 2 is reduced to \[ x' = 4 \left( 1 - \cos 3 \pi y' \right) . \hspace{1cm} (2) \]

Now, we study whether there is a non-zero solution. Because we consider sufficiently small $x'$ and $y'$, to get an intuition and quick estimate, we do approximations of the above equations.

Equation (1) is approximated as \[ y' = 4 \cdot 2 \pi x' \] and Equation (2) is approximated as \[ x' = 2 \left( 3 \pi y' \right)^2  \]

To solve these equations, we get $x' = \frac{1}{8^2 \cdot 18 \pi^4}$ and $y' = \frac{1}{8 \cdot 18 \pi^3}$. Therefore, two functions' two monotonic pieces that attain $\left( 1, 1 \right)$ have two intersecting points.

Putting all analysis above, the total number of intersecting points is $16 \cdot 4 \cdot 6 + 1 = \boxed{\textbf{(385) }}$.

~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Drawing of two solutions near $\left( 1, 1 \right)$

[https://artofproblemsolving.com/wiki/index.php/File:2024_AIME_I_Problem_12,_two_solutions_near_(1,1).png](https://artofproblemsolving.com/wiki/index.php/File:2024_AIME_I_Problem_12,_two_solutions_near_(1,1).png)

~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)
