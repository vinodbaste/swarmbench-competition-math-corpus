_The following problem is from the [2025 USAMO #1](https://artofproblemsolving.com/wiki/index.php/2025\_USAMO\_Problems/Problem\_1) and [2025 USAJMO #2](https://artofproblemsolving.com/wiki/index.php?title=2025\_USAJMO\_Problems/Problem\_2 "2025 USAJMO Problems/Problem 2"), so those problems redirect to this page._
## Problem

Let $k$ and $d$ be positive integers. Prove that there exists a positive integer $N$ such that for every odd integer $n>N$, the digits in the base-$2n$ representation of $n^k$ are all greater than $d$.

## Solution 1

We define a remainder operation $\,a \bmod b\,$ to be the remainder when $a$ is divided by $b$. Also, let $\lfloor x\rfloor$ be the usual floor function.

Base-$(2n)$ Representation: \[n^k \;=\; a_{k-1}\,(2n)^{k-1} \;+\; a_{k-2}\,(2n)^{k-2} \;+\;\dots\;+\;a_1\,(2n)\;+\;a_0,\] where each $a_i$ satisfies $0 \le a_i < 2n.$ Hence, the base-$(2n)$ representation of $n^k$ is $a_{k-1}\,a_{k-2}\,\dots\,a_1\,a_0.$

Leading Digit: \[a_{k-1}  \;=\;  \left\lfloor  \dfrac{n^k}{(2n)^{k-1}} \right\rfloor \;=\; \left\lfloor \dfrac{n}{2^{k-1}} \right\rfloor.\]

General Digit Formula: For $0 \le i < k,$\[a_i  \;=\; \left\lfloor  \dfrac{\,n^k \bmod (2n)^{\,i+1}}{(2n)^i} \right\rfloor.\]

Because $n$ is odd, one can show \[n^k \bmod (2n)^{\,i+1} \;\ge\; n^{\,i+1},\] which implies \[a_i  \;\ge\; \left\lfloor \dfrac{n^{\,i+1}}{(2n)^i} \right\rfloor \;=\; \left\lfloor \dfrac{n}{2^i} \right\rfloor \;\ge\; 2^{\,k-1-i} \left\lfloor \dfrac{n}{2^{\,k-1}} \right\rfloor.\]

As $n$ grows large, $\bigl\lfloor n / 2^{\,k-1}\bigr\rfloor$ becomes arbitrarily big, so each digit $a_i$ eventually exceeds any fixed $d.$ Hence there exists an integer $N$ such that for all odd $n > N,$ the digits $a_i$ in the base-$(2n)$ representation of $n^k$ are all $> d.$

## See Also

**[2025 USAMO](https://artofproblemsolving.com/wiki/index.php?title=2025_USAMO "2025 USAMO")** (**[Problems](https://artofproblemsolving.com/wiki/index.php?title=2025_USAMO_Problems "2025 USAMO Problems")** • [Resources](http://www.artofproblemsolving.com/Forum/resources.php?c=182&cid=27&year=2025))
Preceded by

**First Question**Followed by

**[Problem 2](https://artofproblemsolving.com/wiki/index.php?title=2025_USAMO_Problems/Problem_2 "2025 USAMO Problems/Problem 2")**
[1](https://artofproblemsolving.com/wiki/index.php/2025_USAMO_Problems/Problem_1)**•**[2](https://artofproblemsolving.com/wiki/index.php?title=2025_USAMO_Problems/Problem_2 "2025 USAMO Problems/Problem 2")**•**[3](https://artofproblemsolving.com/wiki/index.php?title=2025_USAMO_Problems/Problem_3 "2025 USAMO Problems/Problem 3")**•**[4](https://artofproblemsolving.com/wiki/index.php?title=2025_USAMO_Problems/Problem_4 "2025 USAMO Problems/Problem 4")**•**[5](https://artofproblemsolving.com/wiki/index.php?title=2025_USAMO_Problems/Problem_5 "2025 USAMO Problems/Problem 5")**•**[6](https://artofproblemsolving.com/wiki/index.php?title=2025_USAMO_Problems/Problem_6 "2025 USAMO Problems/Problem 6")
**[All USAMO Problems and Solutions](https://artofproblemsolving.com/wiki/index.php?title=USAMO_Problems_and_Solutions "USAMO Problems and Solutions")**

**[2025 USAJMO](https://artofproblemsolving.com/wiki/index.php?title=2025_USAJMO "2025 USAJMO")** (**[Problems](https://artofproblemsolving.com/wiki/index.php?title=2025_USAJMO_Problems "2025 USAJMO Problems")** • [Resources](http://www.artofproblemsolving.com/Forum/resources.php?c=182&cid=176&year=2025))
Preceded by

**[Problem 1](https://artofproblemsolving.com/wiki/index.php?title=2025_USAJMO_Problems/Problem_1 "2025 USAJMO Problems/Problem 1")**Followed by

**[Problem 3](https://artofproblemsolving.com/wiki/index.php?title=2025_USAJMO_Problems/Problem_3 "2025 USAJMO Problems/Problem 3")**
[1](https://artofproblemsolving.com/wiki/index.php?title=2025_USAJMO_Problems/Problem_1 "2025 USAJMO Problems/Problem 1")**•**[2](https://artofproblemsolving.com/wiki/index.php?title=2025_USAJMO_Problems/Problem_2 "2025 USAJMO Problems/Problem 2")**•**[3](https://artofproblemsolving.com/wiki/index.php?title=2025_USAJMO_Problems/Problem_3 "2025 USAJMO Problems/Problem 3")**•**[4](https://artofproblemsolving.com/wiki/index.php?title=2025_USAJMO_Problems/Problem_4 "2025 USAJMO Problems/Problem 4")**•**[5](https://artofproblemsolving.com/wiki/index.php?title=2025_USAJMO_Problems/Problem_5 "2025 USAJMO Problems/Problem 5")**•**[6](https://artofproblemsolving.com/wiki/index.php?title=2025_USAJMO_Problems/Problem_6 "2025 USAJMO Problems/Problem 6")
**[All USAJMO Problems and Solutions](https://artofproblemsolving.com/wiki/index.php?title=USAJMO_Problems_and_Solutions "USAJMO Problems and Solutions")**

[](https://artofproblemsolving.com/wiki/index.php?title=File:AMC_Logo.png)
