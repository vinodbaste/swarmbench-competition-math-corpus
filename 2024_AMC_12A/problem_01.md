_The following problem is from the [2024 AMC 10A #1](https://artofproblemsolving.com/wiki/index.php/2024\_AMC\_12A\_Problems/Problem\_1) and [2024 AMC 12A #1](https://artofproblemsolving.com/wiki/index.php?title=2024\_AMC\_12A\_Problems/Problem\_1 "2024 AMC 12A Problems/Problem 1"), so those problems redirect to this page._
## Problem

What is the value of $9901\cdot101-99\cdot10101?$

$\textbf{(A)}~2\qquad\textbf{(B)}~20\qquad\textbf{(C)}~200\qquad\textbf{(D)}~202\qquad\textbf{(E)}~2020$

## Solution 1 (Direct Computation)

The likely fastest method will be direct computation. $9901\cdot101$ evaluates to $1000001$ and $99\cdot10101$ evaluates to $999999$. The difference is $\boxed{\textbf{(A) }2}.$

Solution by [juwushu](https://artofproblemsolving.com/wiki/index.php?title=User:Juwushu "User:Juwushu").

## Solution 2 (Distributive Property)

We have \begin{align*} 9901\cdot101-99\cdot10101 &= (10000-99)\cdot101-99\cdot(10000+101) \\ &= 10000\cdot101-99\cdot101-99\cdot10000-99\cdot101 \\ &= (10000\cdot101-99\cdot10000)-2\cdot(99\cdot101) \\ &= 2\cdot10000-2\cdot9999 \\ &= \boxed{\textbf{(A) }2}. \end{align*} ~MRENTHUSIASM

## Solution 3 (Solution 1 but Distributive)

Note that $9901\cdot101=9901\cdot100+9901=990100+9901=1000001$ and $99\cdot10101=100\cdot10101-10101=1010100-10101=999999$, therefore the answer is $1000001-999999=\boxed{\textbf{(A) }2}$.

~Tacos_are_yummy_1

## Solution 4 (Modular Arithmetic)

Evaluating the given expression $\pmod{10}$ yields $1-9\equiv 2 \pmod{10}$, so the answer is either $\textbf{(A)}$ or $\textbf{(D)}$. Evaluating $\pmod{101}$ yields $0-99\equiv 2\pmod{101}$. Because answer $\textbf{(D)}$ is $202=2\cdot 101$, that cannot be the answer, so we choose choice $\boxed{\textbf{(A) }2}$.

## Solution 5 (Process of Elimination)

We simply look at the units digit of the problem we have (or take mod $10$) \[9901\cdot101-99\cdot10101 \equiv 1\cdot1 - 9\cdot1 = 2 \mod{10}.\] Since the only answers with $2$ in the units digit are $\textbf{(A)}$ and $\textbf{(D)}$, we can then continue if you are desperate to use guess and check or an actually valid method to find the answer is $\boxed{\textbf{(A) }2}$.

~[mathkiddus](https://artofproblemsolving.com/wiki/index.php?title=User:Mathkiddus "User:Mathkiddus")

## Solution 6 (Faster Distribution)

Observe that $9901=9900+1=99\cdot100+1$ and $10101=10100+1=101\cdot100+1$\begin{align*} \Rightarrow9901\cdot101-99\cdot10101 & = ((9900\cdot101)+(1\cdot101))-((99\cdot10100)+(99\cdot1)) \\ &=(99\cdot100\cdot101)+101-(99\cdot100\cdot101)-99 \\ &=101-99 \\ &=\boxed{\textbf{(A) }2}. \end{align*}

~laythe_enjoyer211

## Solution 7 (Cubes)

Let $x=100$. Then, we have Then, the answer can be rewritten as $(x^3+1)-(x^3-1)= \boxed{\textbf{(A) }2}.$

~erics118

## Solution 8 (Super Fast)

It's not hard to observe and express $9901$ into $99\cdot100+1$, and $10101$ into $101\cdot100+1$.

We then simplify the original expression into $(99\cdot100+1)\cdot101-99\cdot(101\cdot100+1)$, which could then be simplified into $99\cdot100\cdot101+101-99\cdot100\cdot101-99$, which we can get the answer of $101-99=\boxed{\textbf{(A) }2}$.

~RULE101

## Solution 9 (Estimation) *🔥VERY FAST🔥*

Notice that the answer choices are significantly different in value. This allows us to estimate the answer. $9901$ is about $10000$, and $101$ is about $100$. $99$ is about $100$, and $10101$ is about $10000$. Computing, we get $10000 \cdot 100-100 \cdot 10000 = 0$. The closest answer to this estimation is $\boxed{\textbf{(A) }2}$.

## Solution 10

We can see that the units digit of the expression is $1 - 9 \Rightarrow 11 - 9 \Rightarrow 2$, elimination options B, C, and E. Next, notice that $(9901)(101)$ is divisible by 101 while $(99)(10101)$ is not divisible by 101 (to see this, notice that 101 is prime, and $10101 = 10100 + 1$, so is not divisible by 101). This means that the final answer is not divisible by 101, eliminating $\textbf{(D)}$, so the answer is $\boxed{\textbf{(A) }2}$.

## See Also

**[2024 AMC 10A](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A "2024 AMC 10A")** (**[Problems](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems "2024 AMC 10A Problems")** • **[Answer Key](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Answer_Key "2024 AMC 10A Answer Key")** • [Resources](https://artofproblemsolving.com/community/c13))
Preceded by

**[2023 AMC 10B Problems](https://artofproblemsolving.com/wiki/index.php?title=2023_AMC_10B_Problems "2023 AMC 10B Problems")**Followed by

**[2024 AMC 10B Problems](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10B_Problems "2024 AMC 10B Problems")**
[1](https://artofproblemsolving.com/wiki/index.php/2024_AMC_12A_Problems/Problem_1)**•**[2](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_2 "2024 AMC 10A Problems/Problem 2")**•**[3](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_3 "2024 AMC 10A Problems/Problem 3")**•**[4](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_4 "2024 AMC 10A Problems/Problem 4")**•**[5](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_5 "2024 AMC 10A Problems/Problem 5")**•**[6](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_6 "2024 AMC 10A Problems/Problem 6")**•**[7](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_7 "2024 AMC 10A Problems/Problem 7")**•**[8](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_8 "2024 AMC 10A Problems/Problem 8")**•**[9](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_9 "2024 AMC 10A Problems/Problem 9")**•**[10](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_10 "2024 AMC 10A Problems/Problem 10")**•**[11](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_11 "2024 AMC 10A Problems/Problem 11")**•**[12](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_12 "2024 AMC 10A Problems/Problem 12")**•**[13](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_13 "2024 AMC 10A Problems/Problem 13")**•**[14](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_14 "2024 AMC 10A Problems/Problem 14")**•**[15](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_15 "2024 AMC 10A Problems/Problem 15")**•**[16](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_16 "2024 AMC 10A Problems/Problem 16")**•**[17](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_17 "2024 AMC 10A Problems/Problem 17")**•**[18](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_18 "2024 AMC 10A Problems/Problem 18")**•**[19](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_19 "2024 AMC 10A Problems/Problem 19")**•**[20](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_20 "2024 AMC 10A Problems/Problem 20")**•**[21](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_21 "2024 AMC 10A Problems/Problem 21")**•**[22](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_22 "2024 AMC 10A Problems/Problem 22")**•**[23](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_23 "2024 AMC 10A Problems/Problem 23")**•**[24](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_24 "2024 AMC 10A Problems/Problem 24")**•**[25](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_25 "2024 AMC 10A Problems/Problem 25")
**[All AMC 10 Problems and Solutions](https://artofproblemsolving.com/wiki/index.php?title=AMC_10_Problems_and_Solutions "AMC 10 Problems and Solutions")**

*   [AMC 10](https://artofproblemsolving.com/wiki/index.php?title=AMC_10 "AMC 10")
*   [AMC 10 Problems and Solutions](https://artofproblemsolving.com/wiki/index.php?title=AMC_10_Problems_and_Solutions "AMC 10 Problems and Solutions")
*   [Mathematics competitions](https://artofproblemsolving.com/wiki/index.php?title=Mathematics_competitions "Mathematics competitions")
*   [Mathematics competition resources](https://artofproblemsolving.com/wiki/index.php?title=Mathematics_competition_resources "Mathematics competition resources")

[](https://artofproblemsolving.com/wiki/index.php?title=File:AMC_Logo.png)
