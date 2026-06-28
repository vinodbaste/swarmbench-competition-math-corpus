_The following problem is from the [2025 AMC 10A #21](https://artofproblemsolving.com/wiki/index.php?title=2025\_AMC\_10A\_Problems/Problem\_21 "2025 AMC 10A Problems/Problem 21") and [2025 AMC 12A #15](https://artofproblemsolving.com/wiki/index.php/2025\_AMC\_12A\_Problems/Problem\_15), so those problems redirect to this page._
## Problem

A set of numbers is called _sum-free_ if whenever $x$ and $y$ are (not necessarily distinct) elements of the set, $x+y$ is not an element of the set. For example, $\{1,4,6\}$ and the empty set are sum-free, but $\{1,4,5\}$ is not. What is the greatest possible number of elements in a sum-free subset of $\{1,2,3,...,20\}$?

$\textbf{(A) } 8 \qquad\textbf{(B) } 9 \qquad\textbf{(C) } 10 \qquad\textbf{(D) } 11 \qquad\textbf{(E) } 12$

## Solution 1

Let our subset be $\{11,12,13,...,20\}.$ If we add any element from the set $\{1,2,3,...,10\}$ to our current subset, we will have to remove at least one element from our subset. Hence, the maximum size of our subset is $\boxed{\text{(C) }10}$.

~Tacos_are_yummy_1

~nithins minor edit

## Solution 2 (Quicksolve)

Notice that an odd number plus an odd number always results in an even number. Consider the subset of all odd numbers $S = \{1, 3, 5, ..., 19\}$. The addition of any even number will result in a violation of the rules, so the maximum number of elements in this subset is $\boxed{\text{(C) }10}$.

~Kevin Wang

~nithins minor edit

## Note (Those who know)

This problem is essentially the same as [2022 AMC 10B Problem 14](https://artofproblemsolving.com/wiki/index.php?title=2022_AMC_10B_Problems/Problem_14).

~metrixgo

## Solution 3

Let $S = \{1, 2, 3, ..., 20\}$. We are looking for the largest possible sum-free subset $A \subseteq S$.

First, we show that a sum-free set of size 10 is possible. Consider the set $A_1 = \{11, 12, ..., 20\}$. The smallest possible sum of two elements (not necessarily distinct) from this set is $11 + 11 = 22$. Since $22 > 20$, no sum of two elements from $A_1$ can be in $A_1$. The size of $A_1$ is $20 - 11 + 1 = 10$. Thus, a sum-free set of size 10 exists.

Next, we prove that no sum-free set $A \subseteq S$ can have 11 or more elements. Let $m$ be the largest element in $A$. Since $A$ is sum-free and $m \in A$, for any $x \in A$, we must have $m-x \notin A$ (unless $x = m-x$, in which case $x \notin A$). This is because if both $x$ and $m-x$ were in $A$, their sum $x + (m-x) = m$ would be in $A$, which is a contradiction.

We can partition the set $\{1, 2, ..., m\}$ into pairs that sum to $m$, plus any leftover elements.

Case 1: $m$ is even. Let $m = 2k$. The numbers in $\{1, ..., m\}$ can be grouped as: $\{ (1, 2k-1), (2, 2k-2), ..., (k-1, k+1) \}$ along with the numbers $k$ and $m=2k$.

The maximum number of elements $A$ can contain from $\{1, ..., m\}$ is $1 + 0 + (k-1) = k = m/2$. Since $m \le 20$, the maximum size of $A$ is $m/2 \le 20/2 = 10$.

Case 2: $m$ is odd. Let $m = 2k-1$. The numbers in $\{1, ..., m\}$ can be grouped as: $\{ (1, 2k-2), (2, 2k-3), ..., (k-1, k) \}$ along with $m=2k-1$.

The maximum number of elements $A$ can contain from $\{1, ..., m\}$ is $1 + (k-1) = k$. Since $m = 2k-1$, we have $k = (m+1)/2$. The largest possible odd $m$ is 19. If $m=19$, $k = (19+1)/2 = 10$. So the maximum size of $A$ is $(m+1)/2 \le (19+1)/2 = \boxed{\textbf{(C) } 10}$.

In all cases, a sum-free subset of $S$ can have at most 10 elements. Since we found a set with 10 elements, the greatest possible number of elements is $10$.

## Solution 4 (Another quicksolve)

Note that selecting integers from $\{11, 12, ..., 20\}$ also satisfy the constraints of the problem. The minimum sum of any two members of the set is $11 + 11 = 22$ which is greater than any of the elements.

## Solution 5 (with quick proof)

As all of the above solutions point out, the set $\{11, ..., 20\}$ satisfies the required condition, and so the greatest size of a sum-free set is no less than 10. How do we know that 11 isn't possible? Induction is our friend here.

We want to prove that the set $\{1, ..., 2n\}$ has a sum-free set of size no more than $n$. It is obvious for $n=1$. Suppose it is true for $n-1$. Now let $S$ be a sum-free subset of $\{1, ..., 2n\}$ and that it has at least $n+1$ elements. The intersection of $S$ and $\{1, ..., 2n-2\}$ is sum-free, so it has no more than $n-1$ elements. So we must include both $2n-1$ and $2n$ into $S$. If so, then $1$ and $n$ cannot belong to $S$.

We are now searching for $n-1$ more elements. But we can make $n-2$ 'pigeonholes': $\{2, 2n-2\}, \{3, 2n-3\}, ..., \{n-1, n+1\}$, seeing that they can provide no more than $n-2$ elements because each pigeonhole will have a sum of $2n$.

## See Also

**[2025 AMC 10A](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A "2025 AMC 10A")** (**[Problems](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems "2025 AMC 10A Problems")** • **[Answer Key](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Answer_Key "2025 AMC 10A Answer Key")** • [Resources](https://artofproblemsolving.com/community/c13))
Preceded by

**[Problem 20](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_20 "2025 AMC 10A Problems/Problem 20")**Followed by

**[Problem 22](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_22 "2025 AMC 10A Problems/Problem 22")**
[1](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_1 "2025 AMC 10A Problems/Problem 1")**•**[2](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_2 "2025 AMC 10A Problems/Problem 2")**•**[3](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_3 "2025 AMC 10A Problems/Problem 3")**•**[4](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_4 "2025 AMC 10A Problems/Problem 4")**•**[5](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_5 "2025 AMC 10A Problems/Problem 5")**•**[6](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_6 "2025 AMC 10A Problems/Problem 6")**•**[7](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_7 "2025 AMC 10A Problems/Problem 7")**•**[8](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_8 "2025 AMC 10A Problems/Problem 8")**•**[9](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_9 "2025 AMC 10A Problems/Problem 9")**•**[10](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_10 "2025 AMC 10A Problems/Problem 10")**•**[11](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_11 "2025 AMC 10A Problems/Problem 11")**•**[12](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_12 "2025 AMC 10A Problems/Problem 12")**•**[13](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_13 "2025 AMC 10A Problems/Problem 13")**•**[14](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_14 "2025 AMC 10A Problems/Problem 14")**•**[15](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_15 "2025 AMC 10A Problems/Problem 15")**•**[16](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_16 "2025 AMC 10A Problems/Problem 16")**•**[17](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_17 "2025 AMC 10A Problems/Problem 17")**•**[18](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_18 "2025 AMC 10A Problems/Problem 18")**•**[19](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_19 "2025 AMC 10A Problems/Problem 19")**•**[20](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_20 "2025 AMC 10A Problems/Problem 20")**•**[21](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_21 "2025 AMC 10A Problems/Problem 21")**•**[22](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_22 "2025 AMC 10A Problems/Problem 22")**•**[23](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_23 "2025 AMC 10A Problems/Problem 23")**•**[24](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_24 "2025 AMC 10A Problems/Problem 24")**•**[25](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_25 "2025 AMC 10A Problems/Problem 25")
**[All AMC 10 Problems and Solutions](https://artofproblemsolving.com/wiki/index.php?title=AMC_10_Problems_and_Solutions "AMC 10 Problems and Solutions")**

[](https://artofproblemsolving.com/wiki/index.php?title=File:AMC_Logo.png)
