_The following problem is from the [2024 AMC 10A #18](https://artofproblemsolving.com/wiki/index.php/2024\_AMC\_12A\_Problems/Problem\_11) and [2024 AMC 12A #11](https://artofproblemsolving.com/wiki/index.php?title=2024\_AMC\_12A\_Problems/Problem\_11 "2024 AMC 12A Problems/Problem 11"), so those problems redirect to this page._
## Problem

There are exactly $K$ positive integers $b$ with $5 \leq b \leq 2024$ such that the base-$b$ integer $2024_b$ is divisible by $16$ (where $16$ is in base ten). What is the sum of the digits of $K$?

$\textbf{(A) }16\qquad\textbf{(B) }17\qquad\textbf{(C) }18\qquad\textbf{(D) }20\qquad\textbf{(E) }21$

## Solution 1

$2024_b = 2b^3+2b+4\equiv 0\pmod{16}\implies b^3+b+2\equiv 0\pmod 8$. If $b$ is even, then $b+2\equiv 0\pmod 8\implies b\equiv 6\pmod 8$. If $b$ is odd, then $b^2\equiv 1\pmod 8$* $\implies b^3+b+2\equiv 2b+2\pmod 8$ so $2b+2\equiv 0\pmod 8\implies b+1\equiv 0\pmod 4\implies b\equiv 3,7\pmod 8$. Now $8\mid 2024$ so $\frac38\cdot 2024=759$ but one of the answers we got from that, $3$, is too small, so $759 - 1 = 758\implies\boxed{\textbf{(D) }20}$.

~OronSH ~[mathkiddus](https://artofproblemsolving.com/wiki/index.php?title=User:Mathkiddus "User:Mathkiddus") ~andliu766 ~megaboy6679 ~trevian1(minor edit for clarity) ~Ebai ($b^2\equiv 1\pmod 8$ remark)

## Solution 2

Clearly, $b$ is either even or odd. If $b$ is even, let $b=2a$.

Thus, one solution is $b=2(4x+3)=8x+6$ for some integer $x$, or $b\equiv6\pmod8$.

What if $b$ is odd? Then let $b=2a+1$:

This simply states that $a$ is odd. Thus, the other solution is $b=2(2x+1)+1=4x+3$ for some integer $x$, or $b\equiv3\pmod4$.

We now simply must count the number of integers between $5$ and $2024$, inclusive, that are $6$ mod $8$ or $3$ mod $4$. Note that the former case comprises even numbers only while the latter is only odd; thus, there is no overlap and we can safely count the number of each and add them.

In the former case, we have the numbers $6,14,22,30,\dots,2022$; this list is equivalent to $8,16,24,32,\dots,2024\cong1,2,3,4,\dots,253$, which comprises $253$ numbers. In the latter case, we have the numbers $7,11,15,19,\dots,2023\cong4,8,12,16,\dots,2020\cong1,2,3,4,\dots,505$, which comprises $505$ numbers. There are $758$ numbers in total, so our answer is $7+5+8=\boxed{\textbf{(D) 20}}$.

~Technodoggo

## Solution 3

Note that $2024_b=2b^3+2b+4$ is to be divisible by $16$, which means that $b^3+b+2$ is divisible by $8$.

If $b=0$, then $b^3+b+2 \equiv (0)^3 + (0) + 2 \equiv 2$ is not divisible by $8$.

If $b=1$, then $b^3+b+2 \equiv (1)^3 + (1) + 2  \equiv 4$ is not divisible by $8$.

If $b=2$, then $b^3+b+2 \equiv (2)^3 + (2) + 2  \equiv 4$ is not divisible by $8$.

If $b=3$, then $b^3+b+2 \equiv (3)^3 + (3) + 2  \equiv (8+1)\cdot3 + (3) + 2 \equiv 0$ is divisible by $8$.

If $b=4$, then $b^3+b+2 \equiv (4)^3 + (4) + 2 \equiv 0 + 4 + 2 \equiv 6$ is not divisible by $8$.

If $b=5$, then $b^3+b+2 \equiv (-3)^3 + (-3) + 2 \equiv  (8+1)\cdot 3 + (-3) + 2 \equiv 2$ is not divisible by $8$.

If $b=6$, then $b^3+b+2 \equiv (-2)^3 + (-2) + 2 \equiv -8 + (-2) + 2 \equiv 0$ is divisible by $8$.

If $b=7$, then $b^3+b+2 \equiv (-1)^3 + (-1) + 2 \equiv -1 + (-1) + 2 \equiv 0$ is divisible by $8$.

Therefore, for every $8$ values of $b$, $3$ of them will make $b^3+b+2$ divisible by $8$. Therefore, since $2024$ is divisible by $8$, $\dfrac{3}{8}\cdot2024=759$ values of $b$, but this includes $b=3$, which does not satisfy the given inequality. Therefore, the answer is \[759-1=758\rightarrow7+5+8=\boxed{\text{(D) }20}\] ~Tacos_are_yummy_1

More detail by ~[luckuso](https://artofproblemsolving.com/wiki/index.php/User:Cyantist)

## Solution 4

$2024_b=2\ast\ b^3+2\ast\ b+4\ \\ {2024}_{\left(b+8\right)}=2\ast\left(b+8\right)^3+2\ast\left(b+8\right)+4$${2024}_{\left(b+8\right)}-{2024}_b=2*\left(8\right)*\left(b^2+8b+64\right)+2*8\ =16*\left(b^2+8b+64\right)+16$

We need $b\ \equiv3\ (mod\ 8)\ \ or\ b\ \equiv6\ (mod\ 8)\ \ or\ b\ \equiv7\ (mod\ 8) \\ \lfloor(2024-3)/8\rfloor+\lfloor(2024-6)/8\rfloor+\lfloor(2024-7)/8\rfloor+3=759$ take away one because $b=3$ is out of range, so $758\Rightarrow7+8+5=\boxed{\text{(D) }20}$

### Solution 4.1: Alternate Ending

One can arrange 2024 into different "blocks" consisting of 8 numbers each, particularly , ...

These just represent different class residues. So, you can just divide 2024 by 8 blocks giving us 253 total blocks with 0 extra semi-blocks.

We see that , , and all appear exactly 253 times each, so we have different values of .

However, we must not include , as the bases range from , therefore we have cases.

Our answer is $\boxed{\text{(D) }20}$.

~Pinotation (I did not do the solution above this remark)

## Solution 5 (Factoring)

Start similar to other solutions.

\[b^3+b+2 \equiv 0\pmod 8\]

Except now we notice the following:

Notice that $b+2$ and $b^2-2b+5$ have opposite parity, and when multiplied, is divisible by $8$. Thus, either $b+2$ or $b^2-2b+5$ is divisible by $8$.

$b+2$ is obvious, where $b+2 | 8$ when $b \equiv 6\pmod 8$

When testing for $b^2-2b+5 | 8$, we find $b \equiv 3, 7\pmod 8$

Proceed similar to the other solutions, $\lfloor\dfrac{3}{8} \cdot 2024\rfloor-1=759-1=758$, where $7+5+8=\boxed{\text{(D) }20}$

Also noting this is an example of a misplaced problem this would be far to easy for even P 18 of amc 10, deserved to be Q5-6

~ NSAoPS

## See Also

**[2024 AMC 10A](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A "2024 AMC 10A")** (**[Problems](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems "2024 AMC 10A Problems")** • **[Answer Key](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Answer_Key "2024 AMC 10A Answer Key")** • [Resources](https://artofproblemsolving.com/community/c13))
Preceded by

**[2024 AMC 10A Problems/Problem 17](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_17 "2024 AMC 10A Problems/Problem 17")**Followed by

**[2024 AMC 10A Problems/Problem 19](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_19 "2024 AMC 10A Problems/Problem 19")**
[1](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_1 "2024 AMC 10A Problems/Problem 1")**•**[2](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_2 "2024 AMC 10A Problems/Problem 2")**•**[3](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_3 "2024 AMC 10A Problems/Problem 3")**•**[4](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_4 "2024 AMC 10A Problems/Problem 4")**•**[5](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_5 "2024 AMC 10A Problems/Problem 5")**•**[6](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_6 "2024 AMC 10A Problems/Problem 6")**•**[7](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_7 "2024 AMC 10A Problems/Problem 7")**•**[8](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_8 "2024 AMC 10A Problems/Problem 8")**•**[9](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_9 "2024 AMC 10A Problems/Problem 9")**•**[10](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_10 "2024 AMC 10A Problems/Problem 10")**•**[11](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_11 "2024 AMC 10A Problems/Problem 11")**•**[12](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_12 "2024 AMC 10A Problems/Problem 12")**•**[13](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_13 "2024 AMC 10A Problems/Problem 13")**•**[14](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_14 "2024 AMC 10A Problems/Problem 14")**•**[15](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_15 "2024 AMC 10A Problems/Problem 15")**•**[16](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_16 "2024 AMC 10A Problems/Problem 16")**•**[17](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_17 "2024 AMC 10A Problems/Problem 17")**•**[18](https://artofproblemsolving.com/wiki/index.php/2024_AMC_12A_Problems/Problem_11)**•**[19](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_19 "2024 AMC 10A Problems/Problem 19")**•**[20](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_20 "2024 AMC 10A Problems/Problem 20")**•**[21](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_21 "2024 AMC 10A Problems/Problem 21")**•**[22](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_22 "2024 AMC 10A Problems/Problem 22")**•**[23](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_23 "2024 AMC 10A Problems/Problem 23")**•**[24](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_24 "2024 AMC 10A Problems/Problem 24")**•**[25](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_25 "2024 AMC 10A Problems/Problem 25")
**[All AMC 10 Problems and Solutions](https://artofproblemsolving.com/wiki/index.php?title=AMC_10_Problems_and_Solutions "AMC 10 Problems and Solutions")**

*   [AMC 10](https://artofproblemsolving.com/wiki/index.php?title=AMC_10 "AMC 10")
*   [AMC 10 Problems and Solutions](https://artofproblemsolving.com/wiki/index.php?title=AMC_10_Problems_and_Solutions "AMC 10 Problems and Solutions")
*   [AMC 12](https://artofproblemsolving.com/wiki/index.php?title=AMC_12 "AMC 12")
*   [AMC 12 Problems and Solutions](https://artofproblemsolving.com/wiki/index.php?title=AMC_12_Problems_and_Solutions "AMC 12 Problems and Solutions")
*   [Mathematics competitions](https://artofproblemsolving.com/wiki/index.php?title=Mathematics_competitions "Mathematics competitions")
*   [Mathematics competition resources](https://artofproblemsolving.com/wiki/index.php?title=Mathematics_competition_resources "Mathematics competition resources")

[](https://artofproblemsolving.com/wiki/index.php?title=File:AMC_Logo.png)
