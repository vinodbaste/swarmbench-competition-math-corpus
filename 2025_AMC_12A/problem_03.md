_The following problem is from the [2025 AMC 10A #4](https://artofproblemsolving.com/wiki/index.php?title=2025\_AMC\_10A\_Problems/Problem\_4 "2025 AMC 10A Problems/Problem 4") and [2025 AMC 12A #3](https://artofproblemsolving.com/wiki/index.php/2025\_AMC\_12A\_Problems/Problem\_3), so those problems redirect to this page._
## Problem

A team of students is going to compete against a team of teachers in a trivia contest. The total number of students and teachers is $15$. Ash, a cousin of one of the students, wants to join the contest. If Ash plays with the students, the average age on that team will increase from $12$ to $14.$ If Ash plays with the teachers, the average age on that team will decrease from $55$ to $52$. How old is Ash?

$\textbf{(A)}~28\qquad\textbf{(B)}~29\qquad\textbf{(C)}~30\qquad\textbf{(D)}~32\qquad\textbf{(E)}~33$

## Solution 1

When Ash joins a team, the team's average is pulled towards his age. Let $A$ be Ash's age and $N$ be the number of people on the student team. This means that there are $15-N$ people in the teacher team. Let us write an expression for the change in the average for each team.

The students originally had an average of $12$, which became $14$ when Ash joined, so there was an increase of $2$. The term $A-12$ represents how much older Ash is compared to the average of the students'. If we divide this by $N+1$, which is the number of people on the student team when Ash joins, we get the average change per team member once Ash is added. Therefore, \[\frac{A-12}{N+1} = 2.\]

Similarly, for teachers, the average was originally $55$, which decreased by $3$ to become $52$ when Ash joined. Intuitively, $55-A$ represents how much younger Ash is than the average age of the teachers. Dividing this by the expression $(15-N)+1$, which is the new total number of people on the teacher team, represents the average change per team member once Ash joins. We can write the equation

\[\frac{55-A}{16-N} = 3.\]

To solve the system, multiply equation (1) by $N+1$, and similarly multiply equation (2) by $16-N$. Then add the equations together, canceling $A$, leaving equation $43=50-N$. From this we get $N=7$ and $A= \boxed{28}.$

~lprado

## Solution 2

As shown above, we get the equation \[\frac{55-A}{16-N} = 3.\] Rearranging we get \[\frac{55-A}{3} = 16-N.\] Therefore, since N must be an integer, $55-A$ must be divisible by 3. Plugging in values gets us $A= \boxed{28}.$

## Solution 3

Another way is to say that there are $S$ students and $T$ teachers and Ash's age is $A$. We can create the equations Equation $(2)$ simplifies to $A=2S+14$ and equation $(3)$ simplifies to $A=-3T+52$. Multiply equation $(2)$ by $3$ to get equation and equation $(3)$ by $-2$ to get Add (4) and (5) to get $A=6(S+T)-62$. After substituting equation (1) and simplifying, you get $A=\boxed{28}$ or answer choice $\boxed{A}$.

~Champions247 ~minor latex by Math1958

## See Also

**[2025 AMC 10A](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A "2025 AMC 10A")** (**[Problems](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems "2025 AMC 10A Problems")** • **[Answer Key](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Answer_Key "2025 AMC 10A Answer Key")** • [Resources](https://artofproblemsolving.com/community/c13))
Preceded by

**[Problem 3](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_3 "2025 AMC 10A Problems/Problem 3")**Followed by

**[Problem 5](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_5 "2025 AMC 10A Problems/Problem 5")**
[1](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_1 "2025 AMC 10A Problems/Problem 1")**•**[2](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_2 "2025 AMC 10A Problems/Problem 2")**•**[3](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_3 "2025 AMC 10A Problems/Problem 3")**•**[4](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_4 "2025 AMC 10A Problems/Problem 4")**•**[5](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_5 "2025 AMC 10A Problems/Problem 5")**•**[6](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_6 "2025 AMC 10A Problems/Problem 6")**•**[7](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_7 "2025 AMC 10A Problems/Problem 7")**•**[8](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_8 "2025 AMC 10A Problems/Problem 8")**•**[9](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_9 "2025 AMC 10A Problems/Problem 9")**•**[10](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_10 "2025 AMC 10A Problems/Problem 10")**•**[11](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_11 "2025 AMC 10A Problems/Problem 11")**•**[12](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_12 "2025 AMC 10A Problems/Problem 12")**•**[13](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_13 "2025 AMC 10A Problems/Problem 13")**•**[14](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_14 "2025 AMC 10A Problems/Problem 14")**•**[15](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_15 "2025 AMC 10A Problems/Problem 15")**•**[16](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_16 "2025 AMC 10A Problems/Problem 16")**•**[17](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_17 "2025 AMC 10A Problems/Problem 17")**•**[18](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_18 "2025 AMC 10A Problems/Problem 18")**•**[19](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_19 "2025 AMC 10A Problems/Problem 19")**•**[20](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_20 "2025 AMC 10A Problems/Problem 20")**•**[21](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_21 "2025 AMC 10A Problems/Problem 21")**•**[22](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_22 "2025 AMC 10A Problems/Problem 22")**•**[23](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_23 "2025 AMC 10A Problems/Problem 23")**•**[24](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_24 "2025 AMC 10A Problems/Problem 24")**•**[25](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_25 "2025 AMC 10A Problems/Problem 25")
**[All AMC 10 Problems and Solutions](https://artofproblemsolving.com/wiki/index.php?title=AMC_10_Problems_and_Solutions "AMC 10 Problems and Solutions")**

[](https://artofproblemsolving.com/wiki/index.php?title=File:AMC_Logo.png)
