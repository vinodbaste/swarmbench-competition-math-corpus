_The following problem is from the [2025 AMC 10A #24](https://artofproblemsolving.com/wiki/index.php?title=2025\_AMC\_10A\_Problems/Problem\_24 "2025 AMC 10A Problems/Problem 24") and [2025 AMC 12A #23](https://artofproblemsolving.com/wiki/index.php/2025\_AMC\_12A\_Problems/Problem\_23), so those problems redirect to this page._
## Problem

Call a positive integer _fair_ if no digit is used more than once, it has no $0$s, and no digit is adjacent to two greater digits. For example, $196, 23$ and $12463$ are fair, but $1546, 320,$ and $34321$ are not. How many fair positive integers are there?

$\textbf{(A) } 511 \qquad \textbf{(B) } 2584 \qquad \textbf{(C) } 9841 \qquad \textbf{(D) } 17711 \qquad \textbf{(E) } 19682$

## Solution 1

To satisfy the conditions, a fair integer must have no digit be a local minimum. Let's say we have $n$ distinct digits, with each digit being a number from $1$ to $9$. To create a fair integer, we begin by placing the largest digit. For the second-largest digit, we can either place this digit to the right or to the left of the string already created. We have these $2$ options for the third-largest digit, and so on. Therefore, there are $2^{n-1}$ valid permutations to create a fair integer.

We must also choose which digits will be in the permutation. If you are creating an $n$-digit long fair integer, there are $\binom{9}{n}$ ways to pick which digits will be in the number.

Therefore, for each $n \in \{1,2,\dots, 9\}$, the number of fair integers of length $n$ is: \[\binom{9}{n} \cdot 2^{n-1}.\] Summing over all $n$: \[\sum_{n=1}^9{\binom{9}{n} \cdot 2^{n-1}}=\frac{1}{2}\left(\sum_{n=0}^9{\binom{9}{n}}2^n -1\right)=\frac{1}{2}\left((1+2)^9 -1 \right) = \frac{1}{2}(19682) = \boxed{9841}.\] Note that the Binomial Theorem was used to equate \[\sum_{n=0}^9{\binom{9}{n}}2^n = (1+2)^9.\] ~lprado

## Solution 2

Note every fair number will have an increasing string of digits, a maximum digit, then a decreasing string of digits. This is because if it decreases then increases, then the digit in the middle will be less than its adjacent digits.

Let $n$ be the maximum digit. For each number $i<n$, we may either place $i$ before $n$, after $n$, or choose not to include it. Note this process will result in a unique number for every case, as the numbers before $n$ must be in increasing order, and the numbers after $n$ must be in decreasing order. Therefore, for each number $n$, we have $3^{n-1}$ cases.

Since $n \in \{1,2,\cdots9\}$, we have: \[\sum_{n=1}^9 3^{n-1}=\frac{3^9-1}{3-1}=\boxed{9841}.\]

~SilverRush

## Solution 2.5 (Cheese, Goldilocks Zone)

If you consider options D and E too large, and A and B too small, then C is your answer.

$\boxed {\text {(C) } 9841}$ Also E is twice C so C is your answer

- Ameen Patel IrvingtonHighSchoolMathGeeks -Edited by TFEA

~Minor edits by Sophia866

~ WARNING: DO NOT EVER USE! VERY VERY RISKY!

~ You could also notice that the only reasonable answers are B and C, and that since every case has a double by flipping it around(making it even) EXCEPT $1$ through $9$, meaning the answer has to be odd so C

## Solution 3 (Recursion)

Let $f(n)$ be the number of fair integers given an arbitrary set of $n$ digits. Let $a$ be the smallest of these digits. Notice that $a$ is either the first or last digit, as if it were any other digit, the two digits surrounding it would both be greater. Then, notice that if the remaining $n-1$ slots form a fair number, so does the number when $a$ is appended. Therefore, $f(n) = 2f(n-1)$. From here, we may proceed with the calculation in Solution $1$ to get the answer of $\boxed {\text {(C) } 9841}$

~ Shadowleafy

## Solution 4

For any fair integer $n$, we write some $9$-digit base-$3$ number(s) $f(n)=\left(\overline{d_1 d_2 \ldots d_9}\right)_3$ from left to right as follows:

Note that the fairness ensured one and only one of the above three cases happens.

Now if $k$ is the largest digit in $n$ then $d_k$ can be either $1$ or $2$.

An example: If $n=136852$, then $f(n)=\overline{121021010}_3$ or $\overline{121021020}_3$.

It's thus easy to see that there is a $1$-to-$2$ mapping from all fair integers to all $9$-digit base-$3$ nonzero numbers. Therefore the answer is $\frac{3^9-1}{2}$.

~ asops

## See Also

**[2025 AMC 10A](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A "2025 AMC 10A")** (**[Problems](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems "2025 AMC 10A Problems")** • **[Answer Key](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Answer_Key "2025 AMC 10A Answer Key")** • [Resources](https://artofproblemsolving.com/community/c13))
Preceded by

**[Problem 23](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_23 "2025 AMC 10A Problems/Problem 23")**Followed by

**[Problem 25](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_25 "2025 AMC 10A Problems/Problem 25")**
[1](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_1 "2025 AMC 10A Problems/Problem 1")**•**[2](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_2 "2025 AMC 10A Problems/Problem 2")**•**[3](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_3 "2025 AMC 10A Problems/Problem 3")**•**[4](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_4 "2025 AMC 10A Problems/Problem 4")**•**[5](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_5 "2025 AMC 10A Problems/Problem 5")**•**[6](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_6 "2025 AMC 10A Problems/Problem 6")**•**[7](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_7 "2025 AMC 10A Problems/Problem 7")**•**[8](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_8 "2025 AMC 10A Problems/Problem 8")**•**[9](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_9 "2025 AMC 10A Problems/Problem 9")**•**[10](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_10 "2025 AMC 10A Problems/Problem 10")**•**[11](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_11 "2025 AMC 10A Problems/Problem 11")**•**[12](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_12 "2025 AMC 10A Problems/Problem 12")**•**[13](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_13 "2025 AMC 10A Problems/Problem 13")**•**[14](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_14 "2025 AMC 10A Problems/Problem 14")**•**[15](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_15 "2025 AMC 10A Problems/Problem 15")**•**[16](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_16 "2025 AMC 10A Problems/Problem 16")**•**[17](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_17 "2025 AMC 10A Problems/Problem 17")**•**[18](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_18 "2025 AMC 10A Problems/Problem 18")**•**[19](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_19 "2025 AMC 10A Problems/Problem 19")**•**[20](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_20 "2025 AMC 10A Problems/Problem 20")**•**[21](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_21 "2025 AMC 10A Problems/Problem 21")**•**[22](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_22 "2025 AMC 10A Problems/Problem 22")**•**[23](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_23 "2025 AMC 10A Problems/Problem 23")**•**[24](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_24 "2025 AMC 10A Problems/Problem 24")**•**[25](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_25 "2025 AMC 10A Problems/Problem 25")
**[All AMC 10 Problems and Solutions](https://artofproblemsolving.com/wiki/index.php?title=AMC_10_Problems_and_Solutions "AMC 10 Problems and Solutions")**

[](https://artofproblemsolving.com/wiki/index.php?title=File:AMC_Logo.png)
