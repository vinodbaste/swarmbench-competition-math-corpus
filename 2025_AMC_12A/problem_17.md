## Problem

The polynomial $(z + i)(z + 2i)(z + 3i) + 10$ has three roots in the complex plane, where $i = \sqrt{-1}$. What is the area of the triangle formed by these three roots?

$\textbf{(A)}~6 \qquad \textbf{(B)}~8 \qquad \textbf{(C)}~10 \qquad \textbf{(D)}~12 \qquad \textbf{(E)}~14$

## Solution 1 (substitution)

We initially note the symmetry of the product $(z+i)(z+2i)(z+3i)$, in that the factors $(z+i)$ and $(z+3i)$ can be expressed as $(z+2i) \mp i$ respectively. Accordingly, making the substitution $w = z+2i$ enables us to apply the 'difference of two squares' identity, yielding \begin{align*}(z+i)(z+2i)(z+3i)+10 &= (w-i)(w)(w+i)+10 \\ &= w\left(w^2-i^2\right)+10 \\ &= w\left(w^2+1\right)+10 = w^3+w+10.\end{align*} Having thus eliminated the quadratic term of the given cubic polynomial, we easily observe that $-2$ is a root of this new cubic (in particular, by the [rational root theorem](https://artofproblemsolving.com/wiki/index.php?title=Rational_root_theorem "Rational root theorem"), the only possible rational roots are integers that are factors of $10$).

It follows that $w^3+w+10 = \left(w+2\right)\left(w^2-2w+5\right)$, and hence, using either the quadratic formula or completing the square, the other two roots are $1+2i$ and $1-2i$. Moreover, since our initial substitution simply shifts all points in the complex plane by $2i$ (i.e. by $2$ units vertically upward) and area is preserved under translation, the required area of the triangle in the $z$-plane is the same as that of the triangle formed by these three roots in the $w$-plane.

Now, as $1+2i$ and $1-2i$ of course have the same real part, the side of the triangle between these two vertices is simply vertical, and has length $2-(-2) = 4$. The length of the altitude to that side is the perpendicular distance from $-2$ to the vertical line $\usepackage{physics}\Re(z) = 1$, i.e. the horizontal distance from $-2$ to $1$, which is $1-(-2) = 3$. Thus the area of the triangle is $\frac{1}{2} \cdot 4 \cdot 3 = \boxed{\textbf{(A)}~6}$.

~lprado

### Solution 1.1 (alternative using shoelace formula for last step)

While the area of the triangle (once we have determined its vertices) can be straightforwardly computed using $\text{area } = \frac{1}{2} \cdot \text{base} \cdot \text{perpendicular height}$ as explained above, it is also possible to use the [shoelace formula](https://artofproblemsolving.com/wiki/index.php?title=Shoelace_Theorem "Shoelace Theorem"), a general result giving the area of any polygon in the plane in terms of the coordinates of its vertices.

Specifically, the vertices $-2$, $1+2i$, and $1-2i$ in the complex plane of course become the points $(-2,0)$, $(1,2)$, and $(1,-2)$ in the $x$-$y$ plane, so the shoelace formula gives the area of the triangle as \[\frac{1}{2} \cdot \left\lvert (-2) \cdot 2 + 1 \cdot (-2) + 1 \cdot 0 - 0 \cdot 1 - 2 \cdot 1 - (-2) \cdot (-2)\right\rvert = \frac{1}{2} \cdot \left\lvert -12\right\rvert = \boxed{\textbf{(A)}~6}.\]

### Solution 1.2 (alternative using triangle in $z$-plane for last two steps)

As an alternative to arguing that the triangle formed by the three roots for $w$ has the same area as the one originally formed by the roots for $z$, we can simply convert back to the $z$-plane using $z = w-2i$. Therefore, as the roots for $w$ are $-2$, $1+2i$, and $1-2i$, those for $z$ are $-2-2i$, $(1+2i)-2i = 1$, and $(1-2i)-2i = 1-4i$, with the vertical side of the triangle thus being that between $1$ and $1-4i$.

We can now use either of the two approaches above: for the former, the vertical side again has length $0-(-4) = 4$ and the corresponding altitude has length $1-(-2) = 3$, once again giving the area as $\frac{1}{2} \cdot 4 \cdot 3 = \boxed{\textbf{(A)}~6}$. For the latter, the shoelace formula also gives the area as \[\frac{1}{2} \cdot \left\lvert (-2) \cdot 0 + 1 \cdot (-4) + 1 \cdot (-2) - (-2) \cdot 1 - 0 \cdot 1 - (-4) \cdot (-2)\right\rvert = \frac{1}{2} \cdot \left\lvert -12\right\rvert = \boxed{\textbf{(A)}~6}.\]

~backtosq-1 ~minor edit by 526

## Solution 2 (directly finding the roots)

Expanding the given polynomial yields \begin{align*}(z+i)(z+2i)(z+3i)+10 &= \left(z^2 + 2iz + iz + 2 \cdot (-1)\right)\left(z+3i\right)+10 \\ &= \left(z^2+3iz-2\right)\left(z+3i\right)+10 \\ &= z^3 + 3iz^2 + 3iz^2 + 9 \cdot (-1)z - 2z - 6i + 10 \\ &= \left(z^3-11z+10\right)+\left(6z^2-6\right)i,\end{align*} and so any complex number $z$ will be a root if and only if it is a root of both the real part, $\left(z^3-11z+10\right)$, and the imaginary part, $\left(6z^2-6\right)$.

We immediately observe that $1$ is indeed a root of both of them, so by factoring out $(z-1)$, we obtain $(z+i)(z+2i)(z+3i)+10 = \left(z-1\right)\left(z^2+(1+6i)z+(-10+6i)\right)$, and now using the quadratic formula, we deduce that the other two roots are given by \begin{align*}z &= \frac{-(1+6i) \pm \sqrt{(1+6i)^2 - 4 \cdot 1 \cdot (-10+6i)}}{2 \cdot 1} \\ &= \frac{-1-6i \pm \sqrt{1+12i-36+40-24i}}{2} \\ &= \frac{-1-6i \pm \sqrt{5-12i}}{2}.\end{align*}

Noting that $5-12i = (3-2i)^2$ (or else by writing $5-12i = (a+bi)^2$ for some $a,b \in \mathbb{R}$, and then solving for $a$ and $b$ by comparing real and imaginary parts of both sides), the above expression reduces to $z = \frac{-1-6i+3-2i}{2} = \frac{2-8i}{2} = 1-4i$ or $z = \frac{-1-6i-3+2i}{2} = \frac{-4-4i}{2} = -2-2i$. In other words, the three roots are precisely $1$, $1-4i$, and $-2-2i$, and thus using either of the approaches in Solution 1.2 above, the area of the triangle is $\boxed{\textbf{(A)}~6}$.

~ScoutViolet and ~Pinotation

## See Also

*   [AMC 12](https://artofproblemsolving.com/wiki/index.php?title=AMC_12 "AMC 12")
*   [AMC 12 Problems and Solutions](https://artofproblemsolving.com/wiki/index.php?title=AMC_12_Problems_and_Solutions "AMC 12 Problems and Solutions")
*   [Mathematics competitions](https://artofproblemsolving.com/wiki/index.php?title=Mathematics_competitions "Mathematics competitions")
*   [Mathematics competition resources](https://artofproblemsolving.com/wiki/index.php?title=Mathematics_competition_resources "Mathematics competition resources")

[](https://artofproblemsolving.com/wiki/index.php?title=File:AMC_Logo.png)
