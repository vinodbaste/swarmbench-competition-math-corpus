_The following problem is from the [2024 AMC 10A #23](https://artofproblemsolving.com/wiki/index.php/2024\_AMC\_12A\_Problems/Problem\_17) and [2024 AMC 12A #17](https://artofproblemsolving.com/wiki/index.php?title=2024\_AMC\_12A\_Problems/Problem\_17 "2024 AMC 12A Problems/Problem 17"), so those problems redirect to this page._
## Problem

Integers $a$, $b$, and $c$ satisfy $ab + c = 100$, $bc + a = 87$, and $ca + b = 60$. What is $ab + bc + ca$?

$\textbf{(A) }212 \qquad \textbf{(B) }247 \qquad \textbf{(C) }258 \qquad \textbf{(D) }276 \qquad \textbf{(E) }284 \qquad$

## Solution 1

Subtracting the first two equations yields $(a-c)(b-1)=13$. Notice that both factors are integers, so $b-1$ could equal one of $13,1,-1,-13$ and $b=14,2,0,-12$. We consider each case separately:

For $b=0$, from the second equation, we see that $a=87$. Then $87c=60$, which is not possible as $c$ is an integer, so this case is invalid.

For $b=2$, we have $2c+a=87$ and $ca=58$, which by experimentation on the factors of $58$ has no solution, so this is also invalid.

For $b=14$, we have $14c+a=87$ and $ca=46$, which by experimentation on the factors of $46$ has no solution, so this is also invalid.

Thus, we must have $b=-12$, so $a=12c+87$ and $ca=72$. Thus $c(12c+87)=72$, so $c(4c+29)=24$. We can simply trial and error this to find that $c=-8$ so then $a=-9$. The answer is then $(-9)(-12)+(-12)(-8)+(-8)(-9)=108+96+72=\boxed{\textbf{(D) }276}$.

By Antony Huang ~Very Minor Edit by lucassf12

## Solution 2

Adding up first two equations: \[(a+c)(b+1)=187\]\[b+1=\pm 11,\pm 17\]\[b=-12,10,-18,16\]

Subtracting equation 1 from equation 2: \[(a-c)(b-1)=13\]\[b-1=\pm 1,\pm 13\]\[b=0,2,-12,14\]

\[\Rightarrow b=-12\]

Which implies that $a+c=-17$ from $(a+c)(b+1)=187$

Giving us that $a+b+c=-29$

Therefore, $ab+bc+ac=100+87+60-(a+b+c)=\boxed{\text{(D) }276}$

~lptoggled

## Solution 3 (Guess and check)

The idea is that you could guess values for $c$, since then $a$ and $b$ are factors of $100 - c$. The important thing to realize is that $a$, $b$, and $c$ are all negative. Then, this can be solved in a few minutes, giving the solution $(-9, -12, -8)$, which gives the answer $\boxed{\textbf{(D)} 276}$ ~andliu766

## Solution 4

\begin{align} ab + c &= 100 \\ bc + a &= 87 \\ ca + b &= 60 \end{align}

\[(1) + (2) \implies  ab + c +bc + a = (a+c)(b+1)=187\implies b+1=\pm 11,\pm 17\]

\[(1) - (2) \implies ab + c - bc - a = (a-c)(b-1)=13\implies b-1=\pm 1,\pm 13\]

Note that $(b+1)-(b-1)=2$, and the only possible pair of results that yields this is $b-1=-13$ and $b+1=-11$, so $a+c=-17$.

Therefore,

\[ab+ba+ac=ab + c +bc + a + ca + b -(a+b+c) = (1)+(2)+(3) - (a+b+c) = 100+87+60-(a+b+c)=\boxed{\textbf{(D) }276}.\] ~[luckuso](https://artofproblemsolving.com/wiki/index.php/User:Cyantist), yuvag, Technodoggo (LaTeX credits to the latter two and editing to the latter)

## Solution 5

\begin{align} ab + c &= 100 \\ bc + a &= 87 \\ ca + b &= 60 \end{align}

There are $3$ ordered triplets of $(a,b,c)$: $(5,14,4)$, $(-3,-12,-3)$, $(-9,-12,-8)$.

However, only the last ordered triplet meets all three equations.

Therefore, $ab+ba+ac= -9\cdot-12+-12\cdot-8+-8\cdot-9 = \boxed{\textbf{(D) }276}.$

~[luckuso](https://artofproblemsolving.com/wiki/index.php/User:Cyantist), megaboy6679 (formatting), Technodoggo (LaTeX optimization/clarity adjustments)

## Solution 6 (Elimination)

Before we start, keep in mind that the problem is asking for the sum . This is nothing but , or ).

To solve the problem, we systematically test the options using elimination:

Let's first check options A and B, since they only happen when a,b, and c sum to 35 or 0. We begin by testing three positive values, but none satisfy the equation when there is a plus sign. For example, satisfies , but does not satisfy , or . If , then not all of the numbers can be positive or negative, so this would not work. From this observation, we conclude that the answer cannot be or .

Now let's test the next option, option C. Option states . If true, then:

This sum is too large. Furthermore, if all three numbers are negative, the solution still fails. For example, testing confirms the equation is not satisfied, as we get results that are too small. Thus, we eliminate option .

Finally, let's test the last two options: D and E. For option , the sum would be:

Testing values such as , the resulting sums , , and are far too large to satisfy the equation. Therefore, is also eliminated.

Once we have this answer, we still need to verify it by testing out numbers: Finally, we test option . Using , we get that . Also note that a, b, and c all have to be different, because the sums from the three equations are all different. We want to get the three closest values of a, b, and c such that they are all different, and the sum . The values are the closest three numbers. When we try them, they satisfy all three equations. So, the correct answer is: $ab+ba+ac= -9\cdot-12+-12\cdot-8+-8\cdot-9 = \boxed{\textbf{(D) }276}.$

~pimathmonkey

## See Also

**[2024 AMC 10A](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A "2024 AMC 10A")** (**[Problems](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems "2024 AMC 10A Problems")** • **[Answer Key](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Answer_Key "2024 AMC 10A Answer Key")** • [Resources](https://artofproblemsolving.com/community/c13))
Preceded by

**[Problem 22](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_22 "2024 AMC 10A Problems/Problem 22")**Followed by

**[Problem 24](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_24 "2024 AMC 10A Problems/Problem 24")**
[1](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_1 "2024 AMC 10A Problems/Problem 1")**•**[2](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_2 "2024 AMC 10A Problems/Problem 2")**•**[3](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_3 "2024 AMC 10A Problems/Problem 3")**•**[4](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_4 "2024 AMC 10A Problems/Problem 4")**•**[5](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_5 "2024 AMC 10A Problems/Problem 5")**•**[6](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_6 "2024 AMC 10A Problems/Problem 6")**•**[7](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_7 "2024 AMC 10A Problems/Problem 7")**•**[8](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_8 "2024 AMC 10A Problems/Problem 8")**•**[9](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_9 "2024 AMC 10A Problems/Problem 9")**•**[10](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_10 "2024 AMC 10A Problems/Problem 10")**•**[11](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_11 "2024 AMC 10A Problems/Problem 11")**•**[12](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_12 "2024 AMC 10A Problems/Problem 12")**•**[13](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_13 "2024 AMC 10A Problems/Problem 13")**•**[14](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_14 "2024 AMC 10A Problems/Problem 14")**•**[15](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_15 "2024 AMC 10A Problems/Problem 15")**•**[16](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_16 "2024 AMC 10A Problems/Problem 16")**•**[17](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_17 "2024 AMC 10A Problems/Problem 17")**•**[18](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_18 "2024 AMC 10A Problems/Problem 18")**•**[19](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_19 "2024 AMC 10A Problems/Problem 19")**•**[20](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_20 "2024 AMC 10A Problems/Problem 20")**•**[21](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_21 "2024 AMC 10A Problems/Problem 21")**•**[22](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_22 "2024 AMC 10A Problems/Problem 22")**•**[23](https://artofproblemsolving.com/wiki/index.php/2024_AMC_12A_Problems/Problem_17)**•**[24](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_24 "2024 AMC 10A Problems/Problem 24")**•**[25](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_25 "2024 AMC 10A Problems/Problem 25")
**[All AMC 10 Problems and Solutions](https://artofproblemsolving.com/wiki/index.php?title=AMC_10_Problems_and_Solutions "AMC 10 Problems and Solutions")**

*   [AMC 10](https://artofproblemsolving.com/wiki/index.php?title=AMC_10 "AMC 10")
*   [AMC 10 Problems and Solutions](https://artofproblemsolving.com/wiki/index.php?title=AMC_10_Problems_and_Solutions "AMC 10 Problems and Solutions")
*   [Mathematics competitions](https://artofproblemsolving.com/wiki/index.php?title=Mathematics_competitions "Mathematics competitions")
*   [Mathematics competition resources](https://artofproblemsolving.com/wiki/index.php?title=Mathematics_competition_resources "Mathematics competition resources")

[](https://artofproblemsolving.com/wiki/index.php?title=File:AMC_Logo.png)
