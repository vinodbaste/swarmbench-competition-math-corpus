## Problem

Determine, with proof, all positive integers $k$ such that\[\frac{1}{n+1} \sum_{i=0}^n \binom{n}{i}^k\]is an integer for every positive integer $n.$

## Solution 1

[https://artofproblemsolving.com/wiki/index.php/File:2025_USAMO_PROBLEM_5_1.jpg](https://artofproblemsolving.com/wiki/index.php/File:2025_USAMO_PROBLEM_5_1.jpg)

[https://artofproblemsolving.com/wiki/index.php/File:2025_USAMO_PROBLEM_5_2.jpg](https://artofproblemsolving.com/wiki/index.php/File:2025_USAMO_PROBLEM_5_2.jpg)

## Solution 2 (combinatorial via Burnside’s lemma)

Let \[X=\{(A_1,\dots,A_k):A_j\subseteq\{1,\dots,n\},\;|A_1|=\cdots=|A_k|\}.\]

Then \[|X|=\sum_{i=0}^n\binom{n}{i}^k.\]

The cyclic group $C_{n+1}$ acts on $\{1,\dots,n+1\}$ by “add 1 mod $n+1$,” and hence diagonally on $X$.

By Burnside’s lemma, \[|X/C_{n+1}|=\frac1{n+1}\sum_{g\in C_{n+1}}|\mathrm{Fix}(g)|.\]

If $g$ has order $d\mid(n+1)$ then $\mathrm{Fix}(g)$ consists of choosing each $A_j$ as a union of the $(n+1)/d$ orbits of $g$, so \[|\mathrm{Fix}(g)|=\sum_{i=0}^n\binom{d}{i}^k.\]

Thus \[(n+1)\,|X/C_{n+1}|=\sum_{d\mid(n+1)}\varphi\Bigl(\tfrac{n+1}d\Bigr)\, \sum_{i=0}^n\binom{d}{i}^k.\]

Case 1: $k=2m$ even

We prove by induction on the divisor‐lattice of $n+1$ that for every proper divisor $d<n+1$, \[d\mid\sum_{i=0}^n\binom{d}{i}^{2m}.\]

Then each term $\varphi\bigl((n+1)/d\bigr)\sum_i\binom{d}{i}^{2m}$ is divisible by $\varphi\bigl((n+1)/d\bigr)\,d$, and since \[\sum_{d\mid(n+1),\,d<n+1}\varphi\Bigl(\tfrac{n+1}d\Bigr)\,d =(n+1)-\varphi(1)\cdot1 =n+1-1,\] the entire sum on the right is congruent modulo $n+1$ to \[\varphi(1)\sum_{i=0}^n\binom{n+1}{i}^{2m} =1\cdot\sum_{i=0}^n\binom{n+1}{i}^{2m}.\]

But the left side $(n+1)\,|X/C_{n+1}|\equiv0\pmod{n+1}$, so \[n+1\;\bigm\vert\;\sum_{i=0}^n\binom{n+1}{i}^{2m}.\]

A re‐index $n+1\mapsto n$ yields \[n+1\;\bigm\vert\;\sum_{i=0}^n\binom{n}{i}^{2m},\] hence \[A_{2m}(n)=\frac1{n+1}\sum_{i=0}^n\binom{n}{i}^{2m}\in\mathbb Z.\]

Case 2: $k$ odd

Take $n=2$. Then \[A_k(2)=\frac{\binom21^k+\binom22^k+\binom23^k}{3} =\frac{1+2^k+1}{3} =\frac{2+2^k}{3}.\]

If $k$ is odd then $2^k\equiv2\pmod3$, so $2+2^k\equiv4\equiv1\pmod3$, whence \[A_k(2)\notin\mathbb Z.\]

Conclusion

$A_k(n)\in\mathbb Z\text{ for all }n\ge1\iff k\text{ even.}$

## See Also

**[2025 USAMO](https://artofproblemsolving.com/wiki/index.php?title=2025_USAMO "2025 USAMO")** (**[Problems](https://artofproblemsolving.com/wiki/index.php?title=2025_USAMO_Problems "2025 USAMO Problems")** • [Resources](http://www.artofproblemsolving.com/Forum/resources.php?c=182&cid=27&year=2025))
Preceded by

**[Problem 4](https://artofproblemsolving.com/wiki/index.php?title=2025_USAMO_Problems/Problem_4 "2025 USAMO Problems/Problem 4")**Followed by

**[Problem 6](https://artofproblemsolving.com/wiki/index.php?title=2025_USAMO_Problems/Problem_6 "2025 USAMO Problems/Problem 6")**
[1](https://artofproblemsolving.com/wiki/index.php?title=2025_USAMO_Problems/Problem_1 "2025 USAMO Problems/Problem 1")**•**[2](https://artofproblemsolving.com/wiki/index.php?title=2025_USAMO_Problems/Problem_2 "2025 USAMO Problems/Problem 2")**•**[3](https://artofproblemsolving.com/wiki/index.php?title=2025_USAMO_Problems/Problem_3 "2025 USAMO Problems/Problem 3")**•**[4](https://artofproblemsolving.com/wiki/index.php?title=2025_USAMO_Problems/Problem_4 "2025 USAMO Problems/Problem 4")**•**[5](https://artofproblemsolving.com/wiki/index.php/2025_USAMO_Problems/Problem_5)**•**[6](https://artofproblemsolving.com/wiki/index.php?title=2025_USAMO_Problems/Problem_6 "2025 USAMO Problems/Problem 6")
**[All USAMO Problems and Solutions](https://artofproblemsolving.com/wiki/index.php?title=USAMO_Problems_and_Solutions "USAMO Problems and Solutions")**

[](https://artofproblemsolving.com/wiki/index.php?title=File:AMC_Logo.png)
