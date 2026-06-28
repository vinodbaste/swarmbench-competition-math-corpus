## Problem

Let $p$ be the least prime number for which there exists a positive integer $n$ such that $n^{4}+1$ is divisible by $p^{2}$. Find the least positive integer $m$ such that $m^{4}+1$ is divisible by $p^{2}$.

## Solution 1

If , then for some integer . But or , so it is impossible. Thus is an odd prime.

There are two ways to do the first part:

**First Method using FLT.** For integer such that , we have , hence , but . By [Fermat's Little Theorem](https://artofproblemsolving.com/wiki/index.php?title=Fermat%27s_Little_Theorem "Fermat's Little Theorem"), , so

Here, mustn't be divide into or otherwise , which contradicts. So , and so . The smallest such prime is clearly .

**Second Method using orders.** Notice that the order modulo $p^2$ of $n^4$ must be $8$, so $8\mid\varphi(p^2)=p(p-1)$. Hence $8\mid p-1$, so $p\equiv 1\pmod{8}$. The smallest such prime is $p=17$. ~eevee9406

So we have to find the smallest positive integer such that . We first find the remainder of divided by by doing

So , . If , let , by the binomial theorem,

So the smallest possible , and .

If , let , by the binomial theorem,

So the smallest possible , and .

If , let , by the binomial theorem,

So the smallest possible , and .

If , let , by the binomial theorem,

So the smallest possible , and .

In conclusion, the smallest possible is .

Solution by Quantum-Phantom

## Solution 2 (Hensel's Lemma)

We know, from Solution 1, that by Fermat's Little Theorem, $p\equiv 1\pmod{8}$, and that the smallest $p$ satisfying such is $17$. Thus, we have $p^2=289$ and we are attempting to lift modulo $17$ to modulo $289$.

Given in the problem, it is established that $p^2\mid m^4 +1$ holds true, so we can guarantee that $m^4\equiv 1\pmod{289}$. Testing for roots $r_0$ modulo $17$ gives us the solutions $r_0= \pm 2$, $\pm 8$, which satisfy $r_0^4\equiv -1 \pmod{17}$.

Note that we can now use Hensel's Lemma, by defining a function $f(x)=x^4+1$, giving $f'(x)=4x^3$. We know firstly that, though $f(r_0)$ for all roots $r_0$ we found is congruent to $0\pmod{17}$, this does not hold true for $f'(r_0)$, so we guarantee that there is one lift by Hensel's Lemma to $289$ that we can perform, defined for root $r_1$ that $r_1 = r_0-\frac{f(r_0)}{f'(r_0)}\pmod{p^k}$. We now break our work into four cases:

1.   $r_0 = 2$. $f(2)=17$ and $f'(2)=32$, so $r_1=2-\frac{17}{32}\pmod{289}$, and we need to find the inverse of $32\equiv 15$ modulo $17$. By the extended Euclidean algorithm, we find that $8\cdot 15\equiv 1 \pmod{17}$, and thus $r_1=2-17\cdot 8\equiv 155 \pmod{289}$.
2.   $r_0 = -2$, or equivalent, $15$. $f(-2)=17$ and $f'(-2)=-32$, so $r_1=-2+\frac{17}{32}\pmod{289}$. We already found the inverse of $32$ modulo $17$, so this case has $r_1=-1+17\cdot 8\equiv 134 \pmod{289}$.
3.   $r_0 = 8$. $f(8)=4097$ and $f'(8)=2048$, so $r_1=-2+\frac{4097}{2048}\pmod{289}$, and we need to find the inverse of $32\equiv 8$ modulo $17$. We already know the inverse of $8$ is $15$, so we end up with $r_1=8-4097\cdot 15\equiv 110\pmod{289}$.
4.   $r_0 = -8$, or equivalent, $9$. $f(-8)=4097$ and $f'(-8)=-2048$, so $r_1=-8+\frac{4097}{2048}\pmod{289}$. We already found the inverse of $2048$ modulo $17$, so this case has $r_1=-8+4097\cdot 15\equiv 179\pmod{289}$.

Thus, out of our four values for $m$, the smallest is $\boxed{110}$. Solution by [juwushu](https://artofproblemsolving.com/wiki/index.php?title=User:Juwushu "User:Juwushu").

## Solution 3 (Easy, given specialized knowledge)

Note that $n^4 + 1 \equiv 0 \pmod{p}$ means $\text{ord}_{p}(n) = 8 \mid p-1.$ The smallest prime that does this is $17$ and $2^4 + 1 = 17$ for example. Now let $g$ be a primitive root of $17^2.$ The satisfying $n$ are of the form, $g^{\frac{p(p-1)}{8}}, g^{3\frac{p(p-1)}{8}}, g^{5\frac{p(p-1)}{8}}, g^{7\frac{p(p-1)}{8}}.$ So if we find one such $n$, then all $n$ are $n, n^3, n^5, n^7.$ Consider the $2$ from before. Note $17^2 \mid 2^{4 \cdot 17} + 1$ by LTE. Hence the possible $n$ are, $2^{17}, 2^{51}, 2^{85}, 2^{119}.$ Some modular arithmetic yields that $2^{51} \equiv \boxed{110}$ is the least value.

~Aaryabhatta1

## Solution 4 (Unfinished)

We work in the ring and use the formula \[\sqrt[4]{-1}=\pm\sqrt{\frac12}\pm\sqrt{-\frac12}.\] Since , the expression becomes , and it is easily calculated via Hensel that , thus giving an answer of .

## Solution 5

Alternative Beginning to Solution 1.

Note $n^4 + 1 \equiv 0 \pmod{p^2}$ implies $n^4 + 1 \equiv 0 \pmod{p}$, so $n^4 \equiv p-1 \pmod{p}$. Also, $p$ must satisfy $p^2 - 1 \pmod{p} \equiv n^4$. The first constraint implies the smallest values of $p$ are $p = 2,17$. However, if $p = 2$, then $p^2 - 1 \equiv 3 \pmod{4}$. However, all quartic residues (as in solution 1), are $0, 1 \pmod{4}$, so 2 is impossible. Try $p = 17$. We see that $n = 2$ satisfies the two equations, as $16 \equiv 17-1 \pmod{17}$, and $289 - 1 \pmod{289} \equiv n^4$ is a possible quartic residue, as $288 \pmod{289} \equiv -1 \pmod{289}$ which has a solution modulo 17, specifically when $n = 2$ in which we let $x = 2+17k$, which when raised to the fourth taken modulo 289, we obtain $x^4 \equiv 16 + 544k \pmod{289}$. Reduce 544 and obtain $x^4 \equiv 16 + 255k \pmod{289}$. Now, assume this takes the form $16 + 255k \equiv -1 \equiv 288 \pmod{289}$. Then, $255k \equiv 272 \pmod{289}$ must have solutions. Divide by 17, and obtain $15k \equiv 16 \pmod{17}$. The inverse of $15k$ is 8, so $k \equiv 9 \pmod{17}$. Because solutions for $k$ exist, that directly implies 288 is a valid quartic residue, so $p = 17$ is our smallest prime.

Continue as in solution 1 to obtain $\boxed{110}$.

~Pinotation
