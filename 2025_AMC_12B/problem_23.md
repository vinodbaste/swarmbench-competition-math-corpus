## Problem

Let $S$ be the set of all integers $z > 1$ such that for all pairs of nonnegative integers $(x, y)$ with $x < y < z$, the remainder when $2025x$ is divided by $z$ is less than the remainder when $2025y$ is divided by $z$. What is the sum of the elements of $S$?

$\textbf{(A)}~3041 \qquad \textbf{(B)}~3542 \qquad \textbf{(C)}~3750 \qquad \textbf{(D)}~4044 \qquad \textbf{(E)}~4319$

## Solution 1

Notice that there are $z$ distinct remainders modulo $z$. However, if we let $R(x)$ denote the remainder when $2025x$ is divided by $z$, we know that by the problem condition, \[R(0)<R(1)<R(2)<\cdots<R(z-1)\] But there are only $z$ distinct remainders, and each of the $z$ terms above must correspond to a distinct remainder, so we must have $R(k)=k$ for all $k=0,1,\dots,z-1$. Then $2025k\equiv k\pmod{z}$, so $2024k\equiv 0\pmod{z}$. Since $k$ can vary, this is equivalent to $2024\equiv 0\pmod{z}$, or $z\mid 2024$.

Therefore, the values $z$ that satisfy the property are the factors of $2024$, so we simply need to find the sum of the factors of $2024$ and subtract $1$ at the end since $z\ne 1$. But $2024=2^3\cdot 11\cdot 23$, so the sum of the factors minus $1$ is \[(1+2+4+8)(1+11)(1+23)-1=15\cdot12\cdot24-1=4320-1=\boxed{\textbf{(E)}~4319 }.\]

~ [eevee9406](https://artofproblemsolving.com/wiki/index.php/User:Eevee9406)

## Solution 2 (Fast)

Notice that $2025x \equiv x \pmod{z} \, \forall z \mid 2024$. Since $x<y<z$, all pairs $(x,y)$ satisfy the remainder condition when $z\mid 2024$ except for $z=1$. Recall that $2024=2^3\cdot 11 \cdot 23$, so $\sum z=(15)(12)(24)-1=\boxed{\textbf{(E)}~4319}$, which is the largest answer choice.

## Solution 3 (Rigorous)

We will show that the $z$'s sastifying the statement are actually all $z>1$ and $2025=1$$($mod $z)$.

We first provide the construction. Let the remainder of $2025$ divided by $z$ be $p$. We have $p<z$. Assume that $p\geq{1}$ in the following steps.

$2025x=px$$($mod $z)$.

$2025y=py$$($mod $z)$.

The aim of the construction is to make the the remainder of $px$ upon division by $z$ as large as possible, and to make the remainder of $py$ upon division by $z$ as small as possible.

【The Construction】

Set $x$ to be the largest positive integer satisfying $px<z$.

Set $y$ equal to $x+1$.

【Proof of why the contruction works】

$py=p(x+1)\geq{z}$.

Now calculate the remainder of $2025y$ divided by $z$. We have $p(x+1)=px+p\leq{2px}<2z$, so the remainder of $p(x+1)$ upon division by $z$ is simply $p(x+1)-z=px+p-z<px$.

The remainder of $2025x$ divided by $z$ is $px$, while the remainder of $2025y$ divided by $z$ is less than $px$. This is a success in finding a counterexample, but we have to ensure that this pair of $(x,y)$ satisfies the condition $x<y<z$.

Since $px<z$, $x<\frac{z}{p}$, $y<\frac{z}{p}+1$. If $p\geq{2}$, we have $y<\frac{z}{2}+1$, $y<\frac{z}{2}+1<z$ for all $z\geq{3}$. For $z=2$, a simple manual check of $x=0$ and $y=1$ works as this is the only possible pair.

This explains why the construction fails when $p=1$. If $p=1$ we have $x=z-1$ and $y=z$, but the condition requires $y<z$.

In fact, for $p=1$, $2025x=x$$($mod $z)$, $2025y=y$$($mod $z)$. The remainders are simply $x$ and $y$ themselves, the problem statement is automatically true for any pair of $(x,y)$ with $x<y$.

For $p=0$, $2025x=0$$($mod $z)$, $2025y=0$$($mod $z)$. The statement is always false because both remainders are always $0$.

In the end, we identify and add all the possible values of $z$ together.

$2025=kz+1$ for some positive integer $k$

$kz=2024$

$kz=2^3\times{11}\times{23}$

In the end, do not forget that $z=1$ is not included. The answer is $4320-1=4319$.

~G2JFForever

## See Also

[](https://artofproblemsolving.com/wiki/index.php?title=File:AMC_Logo.png)
