## Problem

There are $n$ values of $x$ in the interval $0<x<2\pi$ where $f(x)=\sin(7\pi\cdot\sin(5x))=0$. For $t$ of these $n$ values of $x$, the graph of $y=f(x)$ is tangent to the $x$-axis. Find $n+t$.

## Solution 1

For $\sin(7\pi\cdot\sin(5x))=0$ to happen, whatever is inside the function must be of form $k\pi$. We then equate to have We know that $-1\le \sin{5x} \le 1$, so clearly $k$ takes all values $-7\le k \le 7$. Since the graph of $\sin{5x}$ has 5 periods between $0$ and $360$, each of the values $k=-6,-5,-4...-1,1,2...6$ give $10$ solutions each. $k=-7,7$ give $5$ solutions each and $k=0$ gives $9$ solutions (to verify this sketch a graph). Thus, $n=139$.

We know that the function is tangent to the x-axis if it retains the same sign on both sides of the function. This is not true for points at $k=-6,-5,-4...4,5,6$ because one side will be positive and one will be negative. However this will happen if $k=-7,7$ because the sine function "bounces back" and goes over the same values again (to clarify, because $y=\sin{5x}$ has the same values on both sides of $\sin{5x}=\frac{k}{7}$ for $k=-7,7$, as it's a maximum $\sin{5x}=\frac{7}{7}=1$ or minimum $\sin{5x}=\frac{-7}{7}=-1$, the corresponding values of $y=\sin(7\pi\cdot\sin(5x))$ also have a maximum/minimum and repeat around those $x$-values), and $t=10$ of these values exist. Thus, $n+t=\boxed{149}$.

~ [lisztepos](https://artofproblemsolving.com/wiki/index.php?title=User:Lisztepos "User:Lisztepos")

~ Clarification by Christian

## Solution 2 (Calculus)

For $f(x)=0$, we must have $7\pi\cdot\sin(5x)=k\pi$ for some integer $k$. Then $\sin(5x)=\frac{k}{7}$ always satisfies the equation. Notice that on each period of $\sin(5x)$, each $k\in\{-6,-5,\ldots,5,6\}$ is a $y$-value at two distinct points, and each $k=\pm7$ is a $y$-value at one point each. Thus each period has $13\cdot2+2\cdot1=28$ points satisfying the equation. Since the period is $\frac{2\pi}{5}$ and the domain has a length of $2\pi$, we find that $5$ periods occur in our domain if we include $x=0,2\pi$. Adding the case where $x=0$, there are a total of $28\cdot5+1=141$ roots over $x\in[0,2\pi]$. Subtracting the cases at $x=0$ and $x=2\pi$ yields $139$ total roots. This is our $n$.

Next, we take the derivative of $f(x)$; using a hideous combination of chain rules we find that

\[f'(x)=35\pi\cos(5x)\cos(7\pi\sin(5x))=0\]

Thus, for a point to be tangent to the $x$-axis, we must have either $\cos(5x)=0$ or $\cos(7\pi\sin(5x))=0$. In the first case, we know that $\sin(5x)=\frac{k}{7}$ from earlier, so $\cos(5x)=\sqrt{1-\left(\frac{k}{7}\right)^2}=0$. Then $\left(\frac{k}{7}\right)^2=1$, so $k=\pm7$. Recall that over each of the five periods, only one point will satisfy $k=7$, and only one point will satisfy $k=-7$. Thus there are $2\cdot5=10$ points in this case.

In the second case, we must have $\cos(7\pi\sin(5x))=0$. Substituting $\sin(5x)=\frac{k}{7}$ yields $\cos(k\pi)=0$. But this is impossible since $\cos(0)=1$ and $\cos(\pi)=-1$, so there are no points in this case.

As a result, $t=10+0=10$, so $n+t=139+10=\boxed{149}$.

~ [eevee9406](https://artofproblemsolving.com/wiki/index.php?title=User:Eevee9406 "User:Eevee9406")
