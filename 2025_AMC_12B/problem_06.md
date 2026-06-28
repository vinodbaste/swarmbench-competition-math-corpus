_The following problem is from the [2025 AMC 10B #8](https://artofproblemsolving.com/wiki/index.php?title=2025\_AMC\_10B\_Problems/Problem\_8 "2025 AMC 10B Problems/Problem 8") and [2025 AMC 12B #6](https://artofproblemsolving.com/wiki/index.php/2025\_AMC\_12B\_Problems/Problem\_6), so those problems redirect to this page._
## Problem

Emmy says to Max, "I ordered 36 math club sweatshirts today." Max asks, "How much did each shirt cost?" Emmy responds, "I'll give you a hint. The total cost was $\$ \underline A~\underline B~\underline B.\underline B~\underline A$, where $A$ and $B$ are digits and $A \neq 0$." After a pause, Max says, "That was a good price." What is $A + B$?

$\textbf{(A)}~7 \qquad \textbf{(B)}~8 \qquad \textbf{(C)}~11 \qquad \textbf{(D)}~14 \qquad \textbf{(E)}~15$

## Solution 1

The problem is essentially telling us that $\underline A~\underline B~\underline B.\underline B~\underline A$ is divisible by $36$, so it is divisible by $9$. Then, by the divisibility by $9$ condition, \[A+B+B+B+A=2A+3B\equiv 0\pmod{9}\] This means that $A$ must be divisible by $3$, or otherwise $2A+3B$ would not be divisible by $3$ and thus $9$. Since $A\ne0$, we must have one of $A=3,6,9$.

But $A$ must be even or else the entire number would not be even and thus would not be divisible by $4$. Hence $A=6$. Then, $2\cdot 6+3B\equiv 0\pmod{9}$, so $4+B\equiv 0\pmod{3}$, and thus $B\equiv 2\pmod{3}$. This yields $B=2,5,8$, of which $B=5$ is the only number that allows $\underline A~\underline B~\underline B.\underline B~\underline A$ to be divisible by $4$. Thus the answer is $6+5=\boxed{\textbf{(C)}~11}$.

~ [eevee9406](https://artofproblemsolving.com/wiki/index.php/User:Eevee9406)

## Solution 2 (Trial and Error)

A number is divisible by $36$ if it divisible by $4$, and $9$. The divisibility rule for $4$ requires the last 2 digits to also be a multiple of $4$. The divisibility rule for 9 requires the sum of all digits to be divisible by $9$. Using the first condition $A+B$ is a multiple of 4. We can list out all possibilities for this, since both $A$ and $B$ are digits. The possibilities are $(1,2),(1,6),...(9,6)$ for $A$, and $B$ respectively. There are a total of $2$ digits that are $A$'s and $3$ that are $B$'s. So if the digits sum to $9$, then $2A+3B$ is a multiple of 9. We can try plugging in numbers from our list earlier into the equation $2A+3B$ to find what values set the expression equal to a multiple of $9$. By trying numbers $A=6$, and $B=5$. So then $A+B$ yields

$6+5=\boxed{\textbf{(C)}~11}$.

~NumberNinja1234

## See Also

**[2025 AMC 10B](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B "2025 AMC 10B")** (**[Problems](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems "2025 AMC 10B Problems")** • **[Answer Key](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Answer_Key "2025 AMC 10B Answer Key")** • [Resources](https://artofproblemsolving.com/community/c13))
Preceded by

**[Problem 7](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_7 "2025 AMC 10B Problems/Problem 7")**Followed by

**[Problem 9](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_9 "2025 AMC 10B Problems/Problem 9")**
[1](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_1 "2025 AMC 10B Problems/Problem 1")**•**[2](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_2 "2025 AMC 10B Problems/Problem 2")**•**[3](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_3 "2025 AMC 10B Problems/Problem 3")**•**[4](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_4 "2025 AMC 10B Problems/Problem 4")**•**[5](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_5 "2025 AMC 10B Problems/Problem 5")**•**[6](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_6 "2025 AMC 10B Problems/Problem 6")**•**[7](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_7 "2025 AMC 10B Problems/Problem 7")**•**[8](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_8 "2025 AMC 10B Problems/Problem 8")**•**[9](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_9 "2025 AMC 10B Problems/Problem 9")**•**[10](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_10 "2025 AMC 10B Problems/Problem 10")**•**[11](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_11 "2025 AMC 10B Problems/Problem 11")**•**[12](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_12 "2025 AMC 10B Problems/Problem 12")**•**[13](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_13 "2025 AMC 10B Problems/Problem 13")**•**[14](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_14 "2025 AMC 10B Problems/Problem 14")**•**[15](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_15 "2025 AMC 10B Problems/Problem 15")**•**[16](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_16 "2025 AMC 10B Problems/Problem 16")**•**[17](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_17 "2025 AMC 10B Problems/Problem 17")**•**[18](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_18 "2025 AMC 10B Problems/Problem 18")**•**[19](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_19 "2025 AMC 10B Problems/Problem 19")**•**[20](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_20 "2025 AMC 10B Problems/Problem 20")**•**[21](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_21 "2025 AMC 10B Problems/Problem 21")**•**[22](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_22 "2025 AMC 10B Problems/Problem 22")**•**[23](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_23 "2025 AMC 10B Problems/Problem 23")**•**[24](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_24 "2025 AMC 10B Problems/Problem 24")**•**[25](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_25 "2025 AMC 10B Problems/Problem 25")
**[All AMC 10 Problems and Solutions](https://artofproblemsolving.com/wiki/index.php?title=AMC_10_Problems_and_Solutions "AMC 10 Problems and Solutions")**

[](https://artofproblemsolving.com/wiki/index.php?title=File:AMC_Logo.png)
