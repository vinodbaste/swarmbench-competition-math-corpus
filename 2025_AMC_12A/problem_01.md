_The following problem is from the [2025 AMC 10A #1](https://artofproblemsolving.com/wiki/index.php?title=2025\_AMC\_10A\_Problems/Problem\_1 "2025 AMC 10A Problems/Problem 1") and [2025 AMC 12A #1](https://artofproblemsolving.com/wiki/index.php/2025\_AMC\_12A\_Problems/Problem\_1), so those problems redirect to this page._
## Problem

Andy and Betsy both live in Mathville. Andy leaves Mathville on his bicycle at $1{:}30$, traveling due north at a steady $8$ miles per hour. Betsy leaves on her bicycle from the same point at $2{:}30$, traveling due east at a steady $12$ miles per hour. At what time will they be exactly the same distance from their common starting point?

$\textbf{(A) } 3{:}30 \qquad \textbf{(B) } 3{:}45 \qquad \textbf{(C) } 4{:}00 \qquad \textbf{(D) } 4{:}15 \qquad \textbf{(E) } 4{:}30$

== This page has some problems with rendering; thanks to everyone trying to fix it:)

## Solution 1

At $2{:}30$, Andy is $8$ miles ahead. For every hour that they both travel, Betsy gains $4$ miles on Andy. Therefore, it will take her $2$ more hours to be the same distance from the starting point as Andy, which occurs at $\boxed{\textbf{(E) } 4{:}30}$.

$8h = 12(h-1)$$\Rightarrow 8h = 12h - 12$$\Rightarrow 4h = 12$$\Rightarrow h = 3$

Since Andy started at $1{:}30$, the catch-up time is $4{:}30$. Answer: $\textbf{(E)}$.

Alternatively, from Betsy's perspective: $8(h+1) = 12h$$\Rightarrow 8h + 8 = 12h$$\Rightarrow h = 2$ Same result: $\textbf{(E) } 4{:}30$.

## Solution 2 (Simplest Version)

Andy goes $8$ mph, Betsy goes $12$ mph.

We know that Betsy starts 1 hour after Andy, so she will be 8 miles behind.

$12x - 8 = 8x$

$4x = 8$$\,\rightarrow\,$$x = 2$

2 hours after Betsy's start time is $\boxed{\text{4:30}}$

-XaberTooth

## Solution 3

Try the answer choices:

At $3{:}30$: Andy $=16$, Betsy $=12$ At $3{:}45$: Andy $=18$, Betsy $=15$ At $4{:}00$: Andy $=20$, Betsy $=18$ At $4{:}15$: Andy $=22$, Betsy $=21$ At $4{:}30$: Andy $=24$, Betsy $=24$ You can visualize this using a table:

Thus the correct answer is $\boxed{\textbf{(E) } 4{:}30}$.

~vgarg

~SunSine

## Solution 4

Since $\text{lcm}(8,12)=24$, the time for Andy to reach 24 miles is $24/8 = 3$ hours.

$1{:}30 + 3{:}00 = \boxed{\textbf{(E) } 4{:}30}$.

Note: Alternatively we can find that the time for Betsy to reach $24$ miles is $\frac{24}{12} = 2$ hours. So we have

\[2{:}30 + 2{:}00 = \boxed{\textbf{(E) } 4{:}30}.\]

~Boywithnuke

~minor edits by ChickensEatGrass

~minor edits by RISHADA

~Note by JerryZYang

## Solution 5

Andy goes $8x$ miles, Betsy goes $12(x-1)$ miles. Set equal:

$8x = 12(x-1)$$\Rightarrow x = 3$

Thus the answer is $\boxed{\textbf{(E) } 4{:}30}$.

~minor LaTeX edits by zoyashaikh

~minor $\LaTeX$ edits by i_am_not_suk_at_math

~minor LaTeX edits by Pipii

## Solution 6

Using constant rates:

\[\begin{array}{c|c|c} \textbf{Time} & \textbf{Andy} - 8\text{ mph} & \textbf{Betsy} - 12\text{ mph} \\ \hline \hline 1{:}30 - \text{Starting} & 0 \text{ miles} & 0 \text{ miles} \\ \hline 2{:}30 & 8 \text{ miles} & 0 \text{ miles} \\ \hline 3{:}30 & 16 \text{ miles} & 12 \text{ miles} \\ \hline  4{:}30 & 24 \text{ miles} & 24 \text{ miles} \end{array}\]

Thus the answer is $\boxed{\textbf{(E) } 4{:}30}$.

~i_am_not_suk_at_math

~minor LaTeX edits by vinceS

## Solution 7 (Calculus Overkill)

Let $D_A(t) = 8t$, $D_B(t) = 12(t-1)$ for $t \ge 1$.

Difference: $F(t) = 12(t-1) - 8t = 4t - 12$.

Set $F(t)=0$: $4t - 12 = 0$$t = 3$ hours.

$1{:}30 + 3 = 4{:}30$.

-apex304

## Solution 8 (Easy to understand, fast)(Detailed)

Let denote time in hours measured from 1:30 PM:

.

Thus at 1:30 PM, at 2:30 PM, and the physically relevant domain for both riders having left is .

Velocity/position (vectorized). Choose orthonormal basis with east and north. Define piecewise position vectors (for all ):

, \[r_B(t) = \begin{cases} (0, 0), & 0 \leq t < 1, \\ 12(t - 1) \, i, & t \geq 1, \end{cases} = (12 \max\{t - 1, 0\}, 0).\]

Define scalar distance functions (Euclidean norm / 2-norm):

, .

We seek with and . For the equality reduces to the linear equation

.

Bring like terms together:

.

Compute the difference digit-by-digit: . So

.

Divide by carefully: . Hence

.

~N0lan

## Easy Solution

## See Also

**[2025 AMC 10A](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A "2025 AMC 10A")** (**[Problems](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems "2025 AMC 10A Problems")** • **[Answer Key](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Answer_Key "2025 AMC 10A Answer Key")** • [Resources](https://artofproblemsolving.com/community/c13))
Preceded by

**First Problem**Followed by

**[Problem 2](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_2 "2025 AMC 10A Problems/Problem 2")**
[1](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_1 "2025 AMC 10A Problems/Problem 1")**•**[2](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_2 "2025 AMC 10A Problems/Problem 2")**•**[3](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_3 "2025 AMC 10A Problems/Problem 3")**•**[4](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_4 "2025 AMC 10A Problems/Problem 4")**•**[5](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_5 "2025 AMC 10A Problems/Problem 5")**•**[6](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_6 "2025 AMC 10A Problems/Problem 6")**•**[7](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_7 "2025 AMC 10A Problems/Problem 7")**•**[8](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_8 "2025 AMC 10A Problems/Problem 8")**•**[9](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_9 "2025 AMC 10A Problems/Problem 9")**•**[10](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_10 "2025 AMC 10A Problems/Problem 10")**•**[11](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_11 "2025 AMC 10A Problems/Problem 11")**•**[12](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_12 "2025 AMC 10A Problems/Problem 12")**•**[13](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_13 "2025 AMC 10A Problems/Problem 13")**•**[14](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_14 "2025 AMC 10A Problems/Problem 14")**•**[15](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_15 "2025 AMC 10A Problems/Problem 15")**•**[16](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_16 "2025 AMC 10A Problems/Problem 16")**•**[17](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_17 "2025 AMC 10A Problems/Problem 17")**•**[18](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_18 "2025 AMC 10A Problems/Problem 18")**•**[19](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_19 "2025 AMC 10A Problems/Problem 19")**•**[20](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_20 "2025 AMC 10A Problems/Problem 20")**•**[21](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_21 "2025 AMC 10A Problems/Problem 21")**•**[22](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_22 "2025 AMC 10A Problems/Problem 22")**•**[23](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_23 "2025 AMC 10A Problems/Problem 23")**•**[24](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_24 "2025 AMC 10A Problems/Problem 24")**•**[25](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_25 "2025 AMC 10A Problems/Problem 25")
**[All AMC 10 Problems and Solutions](https://artofproblemsolving.com/wiki/index.php?title=AMC_10_Problems_and_Solutions "AMC 10 Problems and Solutions")**

[](https://artofproblemsolving.com/wiki/index.php?title=File:AMC_Logo.png)
