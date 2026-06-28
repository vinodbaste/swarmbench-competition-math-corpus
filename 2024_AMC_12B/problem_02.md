_The following problem is from the [2024 AMC 10B #2](https://artofproblemsolving.com/wiki/index.php/2024\_AMC\_12B\_Problems/Problem\_2) and [2024 AMC 12B #2](https://artofproblemsolving.com/wiki/index.php?title=2024\_AMC\_12B\_Problems/Problem\_2 "2024 AMC 12B Problems/Problem 2"), so those problems redirect to this page._
## Problem

What is $10! - 7! \cdot 6!$

## Solution 1

$10! = 10 \cdot 9 \cdot 8 \cdot 7! = 720 \cdot 7!$

$6! \cdot 7! = 720 \cdot 7!$

Therefore, the equation is equal to $720 \cdot 7! - 720 \cdot 7! = \boxed{\textbf{(B) }0}$

[ONLY FOR CERTAIN CHINESE TESTPAPERS]

$0 - 5! = \boxed{\textbf{(A) }-120}$

~Aray10 (Main Solution) and RULE101 (Modifications for certain China test papers)

## Solution 2

Factoring out $7!$ gives \[7!(10\cdot9\cdot8-1\cdot6!).\] Since $10\cdot9\cdot8=6!=720$, the answer is $\boxed{\text{(B) }0}$

Factoring $6!$ also works, it just makes the expression in the parenthesis a little harder to compute.

## Solution 3

Note that $10! - 7! \cdot 6!$ must be divisible by $7$, since \[10! - 7! \cdot 6!=7!(10\cdot9\cdot8\cdot6!)=7\cdot(6!\cdot10\cdot9\cdot8\cdot6!)\] and $\boxed{\text{(B) }0}$ is the only option divisible by $7$.

## Solution 4

$10! - 7! \cdot 6!$ can be split into two parts, $10!$ and $7! \cdot 6!$. We can break the $6!$ into $(2 \cdot 4)(3 \cdot 5 \cdot 6)$ The $2 \cdot 4$ part makes $8$, and the $3 \cdot 5 \cdot 6$ part makes $90$, which is $9 \cdot 10$. We still have the 7!, and we can multiply it by $8 \cdot 9 \cdot 10$. This is clearly equivalent to $10!$, so our solution is $10! - 10! =$$\boxed{\text{(B) }0}$.

## Solution 5

$10! = 3,628,800$, $7! = 5,040$, and $6! = 720$. $5,040 \cdot 720 = 3,628,800$. Therefore, $3,628,800 - 3,628,800 = \boxed{\text{(B) }0}$.

-pepper2831

-minor edits by blakezhang
