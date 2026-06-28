## Problem

Find the number of ways to place a digit in each cell of a 2x3 grid so that the sum of the two numbers formed by reading left to right is $999$, and the sum of the three numbers formed by reading top to bottom is $99$. The grid below is an example of such an arrangement because $8+991=999$ and $9+9+81=99$.

\[\begin{array}{|c|c|c|} \hline 0 & 0 & 8 \\ \hline 9 & 9 & 1 \\ \hline \end{array}\]

## Solution 1

Consider this table:

$\begin{array}{|c|c|c|} \hline a & b & c \\ \hline d & e & f\\ \hline \end{array}$

We note that $c+f = 9$, because $c+f \leq 18$, meaning it never achieves a unit's digit sum of $9$ otherwise. Since no values are carried onto the next digit, this implies $b+e=9$ and $a+d=9$. We can then simplify our table into this:

$\begin{array}{|c|c|c|} \hline a & b & c \\ \hline 9-a & 9-b & 9-c \\ \hline \end{array}$

We want $10(a+b+c) + (9-a+9-b+9-c) = 99$, or $9(a+b+c+3) = 99$, or $a+b+c=8$. Since zeroes are allowed, we just need to apply stars and bars on $a, b, c$, to get $\tbinom{8+3-1}{3-1} = \boxed{045}$. ~akliu

## Solution 2

Like above, let's label all the entries. Now note that the conditions are now equivalent to:

$100(a + d) + 10(b + e) + (c + f) = 900 + 90 + 9, 10(a + b + c) + (d + e + f) = 99$. Note that for the first equation, it has to be that $a + d = 9$ because say $a + d = 8$. Then $10(b + e) + (c + f) = 199$ but the maximum the $LHS$ can reach is $10(18) + 18 = 180 + 18 = 198$ so this isn't possible. Therefore, $a + d = 9, b + e = 9, c + f = 9$. Now note that adding these up we get $a + b + c + d + e + f = 27$ and note that $10(a + b + c) + (d + e + f) = 99$ so let $a + b + c = x, d + e + f = y$. Note that $x + y = 27, 10x + y = 99 \implies x = 8, y = 19 \implies a + b + c = 8, d + e + f = 19$. So we have the following:

$a + d = 9, b + e = 9, c + f = 9$ and $a + b + c = 8, d + e + f = 19$. Notice after we set a triple for $(a, b, c)$ the triple for $(d, e, f)$ is uniquely and independently set based on the triple for $(a, b, c)$. Thus all we need to do is count the number of ways $a + b + c = 8$ such that $a, b, c$ are digits. We start with $0, 0, 8$ then $0, 1, 7$ and so on until $0, 8, 0$ which gives $9$ ways. Then $1, 0, 7$ to $1, 7, 0$ which gives $8$ ways. So obviously the answer is $9 + 8 + ... + 1 = \boxed{045}$.

~ilikemath247365
