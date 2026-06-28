_The following problem is from the [2025 AMC 10B #17](https://artofproblemsolving.com/wiki/index.php?title=2025\_AMC\_10B\_Problems/Problem\_17 "2025 AMC 10B Problems/Problem 17") and [2025 AMC 12B #14](https://artofproblemsolving.com/wiki/index.php/2025\_AMC\_12B\_Problems/Problem\_14), so those problems redirect to this page._
## Problem

Consider a decreasing sequence of positive integers \[x_1 > x_2 > \cdots > x_n\] that satisfies the following conditions:

*   The average of the first terms in the sequence is .

*   For all , the average of the first terms is less than the average of the first terms.

What is the greatest possible value of ?

$\textbf{(A)}~1013 \qquad \textbf{(B)}~1014 \qquad \textbf{(C)}~1016 \qquad \textbf{(D)}~2016 \qquad \textbf{(E)}~2025$

## Solution 1

Since the mean of the first three terms is $2025$, their sum is $2025 * 3 = 6075$. Then, incorporating the fourth term makes the mean $2025-1=2024$, so their sum must be

$2024 * 4 = 8096$, implying that the 4th term is $8096-6075=2021$ Doing the same for the 5th term,

$2023 * 5= 10115$, 5th term is

$10115-8096=2019$

Algebraically, we can model this pattern for the $k$th term = x as

$(k-1)(2029-k) + x = (k)(2028-k)$

$2029k-2029-k^2+k+x=2028k-k^2$

$x=2029-2k$

So the maximum $k\le n$ for which $x$ is positive is 1014, giving our answer $n=\boxed{\textbf{(B) }1014}$

~Failure.net

## Solution 2

The average of the first 3 terms in the sequence is 2025, which means \[\frac{x_1 + x_2 + x_3}{3} = 2025,\] so $x_1 + x_2 + x_3 = 6075$.

For $k = 4$, we have \[\frac{x_1 + x_2 + x_3 + x_4}{4} = 2025 - 1 = 2024,\] so $x_1 + x_2 + x_3 + x_4 = 8096$. We know $x_1 + x_2 + x_3 = 6075$, so \[x_4 = 8096 - 6075 = 2021.\]

For $k = 5$, we have \[\frac{x_1 + x_2 + x_3 + x_4 + x_5}{5} = 2024 - 1 = 2023.\] That means $x_1 + x_2 + x_3 + x_4 + x_5 = 10115$. We know $x_1 + x_2 + x_3 + x_4 = 8096$, so \[x_5 = 10115 - 8096 = 2019.\]

Continuing on for $k = 6, 7, 8, \ldots$, we can see that each term decreases by 2. So, \[x_6 = 2017,\ x_7 = 2015,\ x_8 = 2013,\ \text{and likewise,}\ x_3 = 2023,\ x_2 = 2025,\ x_1 = 2027.\]

To find the greatest possible value of $n$, we need to find when the numbers in this sequence become negative. The general term is \[x_n = 2027 - 2(n-1).\] We require $x_n > 0$, so \[2027 - 2(n-1) > 0.\] This simplifies to \[2027 > 2n - 2 \Rightarrow 2029 > 2n \Rightarrow n < 1014.5.\]

Thus the greatest possible integer value of $n$ is $1014$, so the answer is $\text{(B) } 1014$. ~anzhuPro

## Solution 3

Assume that the first three terms are $2026$, $2025$, and $2024$, respectively (it doesn't matter what the first 3 terms are, as long as their average is $2025$). The average of the first four terms is $2025-1=2024$, which means the fourth term is $2021$. Continuing this process, we realize that the next term is $2019$ and each subsequent term is 2 fewer. This means the $n^{th}$ term of this sequence where $n>5$ is the the ${n-1}^{th}$ term minus 2. Realizing this is an arithmetic sequence and all the terms must be positive, we get the answer, $\boxed{\textbf{(B) }1014}$

~Bros1 ~minor edit by xu27yunz

## Solution 4 (Proof of Sol. 3)

If the first k terms average to $2028-k$, note that they sum to $2028k-k^2$. Then, $k+1$ terms average to $2027-k$, so they sum to $-k^2+2026k+2027$, so the ${k+1}^{th}$ term is $(-k^2+2026k+2027)-(2028k-k^2)$, where $k \ge 3$, so ${k+1}^{th}$ term is $2027-2k$. Note that for this to be positive, $k \le 1013$, so $k+1$th term is the 1014th term, answer is 1014.

~ScoutViolet ~$Latex$ edits by Bros1

## Solution 5 (basic calculus)

From the previous solution, we derive the sum of the first $k$ terms to be equal to $2028k-k^2$. Taking a derivative of this, we get $2028-2k$. Since the only local extreme is at $k=1014$, answer must be $\boxed{\textbf{(B) }1014}$

## Solution 6

Let's pretend that $k$ does not have to be at least $4$. Then the for $k=1$ the average would be $2027$. To ensure that the next average is $2026$ the second number must be $2025$, and the pattern must continue since it's like median. Therefore you can work backwards from the last number being $1$ since it always drops by $2$ each time so you can say like $2n-1=2027$ so $n=\boxed{\textbf{(B) }1014}$

## See Also

**[2025 AMC 10B](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B "2025 AMC 10B")** (**[Problems](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems "2025 AMC 10B Problems")** • **[Answer Key](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Answer_Key "2025 AMC 10B Answer Key")** • [Resources](https://artofproblemsolving.com/community/c13))
Preceded by

**[Problem 16](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_16 "2025 AMC 10B Problems/Problem 16")**Followed by

**[Problem 18](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_18 "2025 AMC 10B Problems/Problem 18")**
[1](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_1 "2025 AMC 10B Problems/Problem 1")**•**[2](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_2 "2025 AMC 10B Problems/Problem 2")**•**[3](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_3 "2025 AMC 10B Problems/Problem 3")**•**[4](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_4 "2025 AMC 10B Problems/Problem 4")**•**[5](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_5 "2025 AMC 10B Problems/Problem 5")**•**[6](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_6 "2025 AMC 10B Problems/Problem 6")**•**[7](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_7 "2025 AMC 10B Problems/Problem 7")**•**[8](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_8 "2025 AMC 10B Problems/Problem 8")**•**[9](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_9 "2025 AMC 10B Problems/Problem 9")**•**[10](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_10 "2025 AMC 10B Problems/Problem 10")**•**[11](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_11 "2025 AMC 10B Problems/Problem 11")**•**[12](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_12 "2025 AMC 10B Problems/Problem 12")**•**[13](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_13 "2025 AMC 10B Problems/Problem 13")**•**[14](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_14 "2025 AMC 10B Problems/Problem 14")**•**[15](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_15 "2025 AMC 10B Problems/Problem 15")**•**[16](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_16 "2025 AMC 10B Problems/Problem 16")**•**[17](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_17 "2025 AMC 10B Problems/Problem 17")**•**[18](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_18 "2025 AMC 10B Problems/Problem 18")**•**[19](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_19 "2025 AMC 10B Problems/Problem 19")**•**[20](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_20 "2025 AMC 10B Problems/Problem 20")**•**[21](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_21 "2025 AMC 10B Problems/Problem 21")**•**[22](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_22 "2025 AMC 10B Problems/Problem 22")**•**[23](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_23 "2025 AMC 10B Problems/Problem 23")**•**[24](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_24 "2025 AMC 10B Problems/Problem 24")**•**[25](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_25 "2025 AMC 10B Problems/Problem 25")
**[All AMC 10 Problems and Solutions](https://artofproblemsolving.com/wiki/index.php?title=AMC_10_Problems_and_Solutions "AMC 10 Problems and Solutions")**

[](https://artofproblemsolving.com/wiki/index.php?title=File:AMC_Logo.png)
