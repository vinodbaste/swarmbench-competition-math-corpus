## Problem

Let $A_1A_2\dots A_{11}$ be a non-convex $11$-gon such that

• The area of $A_iA_1A_{i+1}$ is $1$ for each $2 \le i \le 10$,

• $\cos(\angle A_iA_1A_{i+1})=\frac{12}{13}$ for each $2 \le i \le 10$,

• The perimeter of $A_1A_2\dots A_{11}$ is $20$.

If $A_1A_2+A_1A_{11}$ can be expressed as $\frac{m\sqrt{n}-p}{q}$ for positive integers $m,n,p,q$ with $n$ squarefree and $\gcd(m,p,q)=1$, find $m+n+p+q$.

## Solution 1

Set $A_1A_2 = x$ and $A_1A_3 = y$. By the first condition, we have $\frac{1}{2}xy\sin\theta = 1$, where $\theta = \angle A_2 A_1 A_3$. Since $\cos\theta = \frac{12}{13}$, we have $\sin\theta = \frac{5}{13}$, so $xy = \frac{26}{5}$. Repeating this process for $\triangle A_i A_1 A_{i+1}$, we get $A_1A_2 = A_1A_4 = \ldots A_1A_{10} = x$ and $A_1A_3 = A_1A_5 = \ldots A_1A_{11} = y$. Since the included angle of these $9$ triangles is $\theta$, the square of the third side is \[x^2 + y^2 - 2xy\cos\theta = x^2 + y^2 - \frac{52}{5}\cdot \frac{12}{13} = x^2 + y^2 - \frac{48}{5} = (x+y)^2 - 20.\] Thus the third side has length $\sqrt{(x+y)^2 - 20}.$ The perimeter is constructed from $9$ of these lengths, plus $A_{11}A_1 + A_1A_2 = x + y$, so $9\sqrt{(x+y)^2 - 20} + x + y = 20$. We seek the value of $x + y,$ so let $x + y = a$ so \begin{align*} 9\sqrt{a^2 - 20} + a &= 20\\ 81(a^2 - 20) &= 400 - 40a + a^2\\ 4a^2 + 2a - 101 &= 0 \\ a &= \frac{-2 \pm \sqrt{1620}}{8} = \frac{-1 \pm \sqrt{405}}{4} = \frac{-1 \pm 9\sqrt{5}}{4}. \end{align*} Taking the positive solution gives $m + n + p + q = 1 + 9 + 5 + 4 = \boxed{\textbf{(019)}}.$

-Benedict T (countmath1)

## Solution 2 (Very similar to Solution 1)

Let $A_1 A_2 = a_1, A_1 A_3 = a_2, ... A_1 A_{10} = a_9, A_1 A_11 a_{10}$. Now the area of each triangle is equal to half the product of two side lengths and the sine of the angle in between. This angle's cosine is given to us to be $\frac{12}{13}$. We recognize this as a $5-12-13$ triangle hence the sine of the angle will be simply $\frac{5}{13}$ (alternatively, one could use the Pythagorean Identity $\sin^2(\angle A_iA_1A_{i+1})+\cos^2(\angle A_iA_1A_{i+1})=1$). Hence each area will be $\frac{1}{2} \cdot a_n a_{n + 1} \cdot \frac{5}{13} = 1 \implies a_n a_{n+ 1} = \frac{26}{5}$. Therefore, we have:

$a_1 a_2 = \frac{26}{5}$

$a_2 a_3 = \frac{26}{5}$ . . .

$a_9 a_{10} = \frac{26}{5}$

$a_{10} a_1 = \frac{26}{5}$

Now note that the perimeter is the sum of all the other lengths. For instance, $A_2 A_3$ will be part of this perimeter which happens to be the only unknown side of $\triangle A_1 A_2 A_3$. By Law of Cosines

$(A_2 A_3)^2 = a_1^{2} + a_2^{2} - 2a_1 a_2 \frac{12}{13}$ after substituting the cosine value. We know $a_1 a_2 = \frac{26}{5}$ so substituting this in we get

$(A_2 A_3)^2 = a_1^{2} + a_2^{2} - \frac{48}{5} \implies A_2 A_3 = \sqrt{a_1^{2} + a_2^{2} - \frac{48}{5}}$. By symmetry, we conclude

$\sqrt{a_1^{2} + a_2^{2} - \frac{48}{5}} + ... + \sqrt{a_{10}^{2} + a_1^{2} - \frac{48}{5}} + a_1 + a_2 = 20$ because we need to account for $A_1 A_2 + A_1 A_{11}$ as they are actually known sides that are included in the perimeter.

Note that from the $a_1 a_2 = \frac{26}{5}$ system of equations, we can see clearly that

$a_1 = a_3$

$a_2 = a_4$ . . .

$a_8 = a_{10}$

$a_9 = a_1$

$a_{10} = a_2$

So we see that $a_{2n + 1} = a_1$ and $a_{2n} = a_2$ so we can substitute this in to get

$\sqrt{a_1^{2} + a_2^{2} - \frac{48}{5}} + ... + \sqrt{a_1^{2} + a_2^{2} - \frac{48}{5}} + a_1 + a_2 = 20$

Now the square root terms happen $9$ times as there are $11$ sides and two of them are $a_1, a_2$ given at the end of the $LHS$. So we conclude:

$9\sqrt{a_1^{2} + a_2^{2} - \frac{48}{5}} + a_1 + a_2 = 20$

Note that $a_1^{2} + a_2^{2} - \frac{48}{5} = (a_1 + a_2)^2 - 2a_1 a_2 - \frac{48}{5} = (a_1 + a_2)^2 - \frac{52 + 48}{5} = (a_1 + a_2)^2 - 20$. Note that we want to find $A_1 A_2 + A_1 A_{11} = a_1 + a_{10} = a_1 + a_2$. So we let $a_1 + a_2 = x$ to get

\[9\sqrt{x^2 - 20} + x = 20 \implies 81(x^2 - 20) = (20 - x)^2 \implies 81(x^2 - 20) = 400 - 40x + x^2 \implies 81x^2 - 1620 = 400 - 40x + x^2 \implies 80x^2 + 40x - 2020 = 0 \implies 4x^2 + 2x - 101 = 0 \implies x = \frac{-1 \pm 9\sqrt{5}}{4}\] Now take the positive value to get

$x = \frac{9\sqrt{5} - 1}{4} \implies 9 + 5 + 1 + 4 = \boxed{19}$.

~ilikemath24736

~Sylesh (Latex errors)

~ Clarifying and $\LaTeX$ edits by Christian

## Visualization Tip

The polygon can be imagined sort of like one of those Chinese fans. Congruent triangles branch out from $A_1$, the handle of the fan, forming a series of triangular ridges.

~ Christian
