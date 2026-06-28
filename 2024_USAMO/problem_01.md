Find all integers $n \geq 3$ such that the following property holds: if we list the divisors of $n !$ in increasing order as $1=d_1<d_2<\cdots<d_k=n!$, then we have \[d_2-d_1 \leq d_3-d_2 \leq \cdots \leq d_k-d_{k-1} .\]

## Solution 2

We claim only $n = 3$ and $n = 4$ are the only two solutions. First, it is clear that both solutions work.

Next, we claim that $n < 5$. For $n \geq 5$, let $x$ be the smallest $x$ such that $x+1$ is not a factor of $n!$. Let the smallest factor larger than $x$ be $x+k$.

Now we consider $\frac{n!}{x-1}$, $\frac{n!}{x}$ and $\frac{n!}{x+k}$. Since $\frac{n!}{x-1} > \frac{n!}{x} > \frac{n!}{x+k}$, if $n$ were to satisfy the conditions, then $\frac{n!}{x-1}-\frac{n!}{x} \geq \frac{n!}{x} - \frac{n!}{x+k}$. However, note that this is not true for $x \geq 5$ and $k > 1$.

Note that the inequality is equivalent to showing $\frac{1}{x(x-1)} \geq \frac{k}{x(x+k)}$, which simplifies to $x+k \geq kx-k$, or $\frac{x}{x-2} \geq k \geq 2$. This implies $x \geq 2x-4$, $x \leq 4$, a contradiction, since the set of numbers $\{1, 2, 3, 4, 5\}$ are all factors of $n!$, and the value of $x$ must exist. Hence, no solutions for $n \geq 5$.

## See Also

**[2024 USAMO](https://artofproblemsolving.com/wiki/index.php?title=2024_USAMO "2024 USAMO")** (**[Problems](https://artofproblemsolving.com/wiki/index.php?title=2024_USAMO_Problems "2024 USAMO Problems")** • [Resources](http://www.artofproblemsolving.com/Forum/resources.php?c=182&cid=27&year=2024))
Preceded by

**First Question**Followed by

**[Problem 2](https://artofproblemsolving.com/wiki/index.php?title=2024_USAMO_Problems/Problem_2 "2024 USAMO Problems/Problem 2")**
[1](https://artofproblemsolving.com/wiki/index.php/2024_USAMO_Problems/Problem_1)**•**[2](https://artofproblemsolving.com/wiki/index.php?title=2024_USAMO_Problems/Problem_2 "2024 USAMO Problems/Problem 2")**•**[3](https://artofproblemsolving.com/wiki/index.php?title=2024_USAMO_Problems/Problem_3 "2024 USAMO Problems/Problem 3")**•**[4](https://artofproblemsolving.com/wiki/index.php?title=2024_USAMO_Problems/Problem_4 "2024 USAMO Problems/Problem 4")**•**[5](https://artofproblemsolving.com/wiki/index.php?title=2024_USAMO_Problems/Problem_5 "2024 USAMO Problems/Problem 5")**•**[6](https://artofproblemsolving.com/wiki/index.php?title=2024_USAMO_Problems/Problem_6 "2024 USAMO Problems/Problem 6")
**[All USAMO Problems and Solutions](https://artofproblemsolving.com/wiki/index.php?title=USAMO_Problems_and_Solutions "USAMO Problems and Solutions")**

[](https://artofproblemsolving.com/wiki/index.php?title=File:AMC_Logo.png)
