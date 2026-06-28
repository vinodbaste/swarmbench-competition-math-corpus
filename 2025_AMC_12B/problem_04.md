_The following problem is from the [2025 AMC 10B #4](https://artofproblemsolving.com/wiki/index.php?title=2025\_AMC\_10B\_Problems/Problem\_4 "2025 AMC 10B Problems/Problem 4") and [2025 AMC 12B #4](https://artofproblemsolving.com/wiki/index.php/2025\_AMC\_12B\_Problems/Problem\_4), so those problems redirect to this page._
## Problem

The value of the two-digit number $\underline{a}~\underline{b}$ in base seven equals the value of the two-digit number $\underline{b}~\underline{a}$ in base nine. What is $a+b?$

$\textbf{(A)}~7\qquad\textbf{(B)}~9\qquad\textbf{(C)}~10\qquad\textbf{(D)}~11\qquad\textbf{(E)}~14$

## Solution 1

By definition of bases, $\underline{a}~\underline{b}$ base seven is equal to $7a+b$, and $\underline{b}~\underline{a}$ base nine is equal to $9b+a$. Therefore, we must have $7a+b=9b+a$, or $6a=8b$, or $3a=4b$. But in base seven, we must have $a,b<7$. Testing cases yields $a=4,b=3$ as the only solution. Their sum is $\boxed{\textbf{(A)}~7}$.

~Note that $lcm(6,8) = 24$, which should reveal the answer a lot faster than testing.

~ [eevee9406](https://artofproblemsolving.com/wiki/index.php/User:Eevee9406)

~ CW

The first equation comes from the following idea. In base $10$, a two-digit number can be represented as $10$ times the tens digit plus the units digit, or $10^1 \cdot a + 10^0 \cdot b$. If we insert the base numbers into this expression for $\underline{a}~\underline{b}$ and $\underline{b}~\underline{a}$, we get $7^1 \cdot a + b = 9^1 \cdot b + a$. The rest of the solution is above.

Note that this method applies to any number of digits as well as decimals. ~OlympiadMaster

## Solution 2 (Answer Choices)

Since $a$ and $b$ are both digits base $7$, they must be from $0$ to $6$. Furthermore, $\underline{a}$ must be strictly greater than $b$ because two-digit representations in base $7$ exceed the values of those in base $9$. Starting from testing $\text{(A)}$, we see that the combination $(a, b) = (4, 3)$ satisfies the condition. The answer is $\boxed{\textbf{(A)}~7}$.

~megaboy6679

## Solution 3 (Not too bad- Simple Modular Arithmetic Bash)

We interpret the two-digit numbers literally:

In base 7: \[\overline{a} \ \overline{b} = 7a + b.\] In base 9: \[\overline{b} \ \overline{a} = 9b + a.\] The condition is \[7a + b = 9b + a.\] We want , but we will milk modular arithmetic as much as possible.

Start with the equation: \[7a + b = 9b + a.\] Rearrange: \[7a - a = 9b - b,\]\[6a = 8b,\]\[3a = 4b.\] This already says . But instead of finishing, we now do highly unnecessary modular analysis.

First, reduce the equation modulo 3: \[3a - 4b \equiv 0 \pmod{3}.\] Compute residues: \[3a \equiv 0 \pmod{3} \text{ always.}\]\[4b \equiv b \pmod{3}.\] So: \[0 - b \equiv 0 \pmod{3} \Rightarrow b \equiv 0 \pmod{3}.\] Thus (since digits in base 7 must be ).

Now reduce the same equation modulo 4:

Original condition . Modulo 4: \[3a \equiv 0 \pmod{4}.\] Since , the multiplicative inverse of 3 modulo 4 is 3, because \[3 \cdot 3 = 9 \equiv 1 \pmod{4}.\] Multiply both sides of \[3a \equiv 0 \pmod{4}\] by 3: \[a \equiv 0 \pmod{4}.\] Thus , because digits in base 7 satisfy .

We now have: \[a \in \{0, 4\}, b \in \{0, 3, 6\}.\] Next impose the original equation exactly, not just modularly.

Test combinations:

: \[3a = 0, 4b = 4b.\] For equality we need . That gives , but this represents the “two-digit” numbers and . Technically valid but trivial; we check the problem expectation: since it asks “What is ?”, zero is possible but let's check the other option.

: Solve \[3 \cdot 4 = 4b,\]\[12 = 4b,\]\[b = 3.\] Check that digits are valid:

is allowed in base 7.

is allowed in base 7 and base 9.

Now confirm the original equation explicitly using base values:

Left side (base 7 number ): \[7a + b = 7 \cdot 4 + 3 = 28 + 3 = 31.\] Right side (base 9 number ): \[9b + a = 9 \cdot 3 + 4 = 27 + 4 = 31.\] Equality holds.

Thus the nontrivial valid solution is \[(a, b) = (4, 3).\] Compute: \[a + b = 4 + 3 = 7.\] Final answer: .

~notvalid

## Solution 4 (Fast)

Write both integers as linear expressions and equate them \[7a+b = 9b+a\] To find solutions to this, we can put everything on one side so it equals $0$\[6a-8b=0\] Now, assuming a coordinate form $(a, b)$ you can quite easily see that $(8, 6)$ is a solution. However, this violates the fact that $a$ and $b$ are less than 7. You can see that just taking half of them gets you $(4,3)$, and that no other solution would work without exceeding, so, the answer is

$\boxed{\textbf{(A)}~7}$.

~shockfront99

## See Also

**[2025 AMC 10B](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B "2025 AMC 10B")** (**[Problems](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems "2025 AMC 10B Problems")** • **[Answer Key](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Answer_Key "2025 AMC 10B Answer Key")** • [Resources](https://artofproblemsolving.com/community/c13))
Preceded by

**[Problem 3](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_3 "2025 AMC 10B Problems/Problem 3")**Followed by

**[Problem 5](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_5 "2025 AMC 10B Problems/Problem 5")**
[1](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_1 "2025 AMC 10B Problems/Problem 1")**•**[2](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_2 "2025 AMC 10B Problems/Problem 2")**•**[3](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_3 "2025 AMC 10B Problems/Problem 3")**•**[4](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_4 "2025 AMC 10B Problems/Problem 4")**•**[5](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_5 "2025 AMC 10B Problems/Problem 5")**•**[6](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_6 "2025 AMC 10B Problems/Problem 6")**•**[7](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_7 "2025 AMC 10B Problems/Problem 7")**•**[8](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_8 "2025 AMC 10B Problems/Problem 8")**•**[9](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_9 "2025 AMC 10B Problems/Problem 9")**•**[10](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_10 "2025 AMC 10B Problems/Problem 10")**•**[11](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_11 "2025 AMC 10B Problems/Problem 11")**•**[12](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_12 "2025 AMC 10B Problems/Problem 12")**•**[13](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_13 "2025 AMC 10B Problems/Problem 13")**•**[14](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_14 "2025 AMC 10B Problems/Problem 14")**•**[15](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_15 "2025 AMC 10B Problems/Problem 15")**•**[16](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_16 "2025 AMC 10B Problems/Problem 16")**•**[17](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_17 "2025 AMC 10B Problems/Problem 17")**•**[18](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_18 "2025 AMC 10B Problems/Problem 18")**•**[19](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_19 "2025 AMC 10B Problems/Problem 19")**•**[20](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_20 "2025 AMC 10B Problems/Problem 20")**•**[21](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_21 "2025 AMC 10B Problems/Problem 21")**•**[22](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_22 "2025 AMC 10B Problems/Problem 22")**•**[23](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_23 "2025 AMC 10B Problems/Problem 23")**•**[24](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_24 "2025 AMC 10B Problems/Problem 24")**•**[25](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_25 "2025 AMC 10B Problems/Problem 25")
**[All AMC 10 Problems and Solutions](https://artofproblemsolving.com/wiki/index.php?title=AMC_10_Problems_and_Solutions "AMC 10 Problems and Solutions")**

[](https://artofproblemsolving.com/wiki/index.php?title=File:AMC_Logo.png)
