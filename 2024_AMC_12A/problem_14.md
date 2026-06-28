_The following problem is from the [2024 AMC 10A #21](https://artofproblemsolving.com/wiki/index.php/2024\_AMC\_12A\_Problems/Problem\_14) and [2024 AMC 12A #14](https://artofproblemsolving.com/wiki/index.php?title=2024\_AMC\_12A\_Problems/Problem\_14 "2024 AMC 12A Problems/Problem 14"), so those problems redirect to this page._
## Problem

The numbers, in order, of each row and the numbers, in order, of each column of a $5 \times 5$ array of integers form an arithmetic progression of length $5$. The numbers in positions $(5, 5), \,(2,4),\,(4,3),$ and $(3, 1)$ are $0, 48, 16,$ and $12$, respectively. What number is in position $(1, 2)?$

\[\begin{bmatrix} . & ? &.&.&. \\ .&.&.&48&.\\ 12&.&.&.&.\\ .&.&16&.&.\\ .&.&.&.&0\end{bmatrix}\]$\textbf{(A) } 19 \qquad \textbf{(B) } 24 \qquad \textbf{(C) } 29 \qquad \textbf{(D) } 34 \qquad \textbf{(E) } 39$

## Solution 1 (Arithmetic Sequences)

Start from the $0$. Going up, let the common difference be $a$, and going left, let the common difference be $b$. Therefore, we have \[\begin{bmatrix} . & ? &.&.&4a \\ .&.&.&48&3a\\ 12&.&.&.&2a\\ .&.&16&.&a\\ 4b&3b&2b&b&0\end{bmatrix}\] Looking at the third column, we can see that the common difference going up is $16-2b$. We fill this in: \[\begin{bmatrix} . & ? &64-6b&.&4a \\ .&.&48-4b&48&3a\\ 12&.&32-2b&.&2a\\ .&.&16&.&a\\ 4b&3b&2b&b&0\end{bmatrix}\] Looking at the second row, $48$ has two values beside it, so we can write \[48=\dfrac{48-4b+3a}{2}\rightarrow96=48-4b+3a\rightarrow48=-4b+3a,\] and we can do the same with the third row, which gives \[32-2b=\dfrac{12+2a}{2}\rightarrow32-2b=6+a\rightarrow26=a+2b.\] Now we have the system of equations \[48=-4b+3a\]\[26=a+2b,\] and solving it gives $a=20,b=3$, therefore we can now fill in the grid with actual numbers. But before doing that, note that we're only looking for a value in the first row, and because we already have two known values in that row, we can find the common difference for that row and not focus on anything else.

Focusing only on the first row yields \[\begin{bmatrix} . & ? &46&.&80\end{bmatrix}\] This means that the common difference from right to left is $\dfrac{80-46}{2}=17$. Therefore, the desired value is $46-17=\boxed{\text{(C) }29}$ ~Tacos_are_yummy_1

## Solution 2 (Some Basic Algebra and Answer Choices)

Assume the number in position $(3, 3)$ is $x$. \[\begin{bmatrix} .&?&.&.&. \\ .&.&.&48&.\\ 12&.&x&.&.\\ .&.&16&.&.\\ .&.&.&.&0\end{bmatrix}\] Then, the integer in position $(2, 3)$ will be $2x-16$, since $2x-16$ and $16$ average out to x. (They form an arithmetic sequence). \[\begin{bmatrix} .&?&.&.&. \\ .&.&2x-16&48&.\\ 12&.&x&.&.\\ .&.&16&.&.\\ .&.&.&.&0\end{bmatrix}\] Similarly, the integer in position $(3, 2)$ is $0.5x+6$, and the integer in position $(2, 2)$ is $4x-80$. \[\begin{bmatrix} .&?&.&.&. \\ .&4x-80&2x-16&48&.\\ 12&0.5x+6&x&.&.\\ .&.&16&.&.\\ .&.&.&.&0\end{bmatrix}\] This means the number $7.5x-166$ is in position (1, 2). \[\begin{bmatrix} .&7.5x-166&.&.&. \\ .&4x-80&2x-16&48&.\\ 12&0.5x+6&x&.&.\\ .&.&16&.&.\\ .&.&.&.&0\end{bmatrix}\]

The only answer choice that makes $x$ an integer is $\boxed{\textbf{(C) }29}$

~ElaineGu

## Solution 3 (Bashy)

Let's look at the bottom-left corner. There can be $3$ possible cases for the bottom row. Either the numbers are negative, all $0$, or positive.

Let's assume all the numbers are negative. We know that the numbers in between the $?$ will be large, so we want to minimize it, because the largest answer choice is only $39$.

\[\begin{bmatrix} .&?&.&.&. \\ .&.&.&48&.\\ 12&.&.&.&.\\ .&.&16&.&.\\ -4&-3&-2&-1&0\end{bmatrix}\]

To fill in the $1$st and $3$rd column, we simply find the common differences. We get:

\[\begin{bmatrix} 28&?&70&.&. \\ 20&.&52&48&.\\ 12&.&34&.&.\\ 4&.&16&.&.\\ -4&-3&-2&-1&0\end{bmatrix}\]

Finding the $?$ , we notice that it is $49$, which is bigger than any of the other answer choices, so the bottom row can't be negative. (As the common difference for the bottom row gets larger, so does the common difference for the $1$st and $3$rd column, making the $?$ bigger, and because the smallest answer is $39$ while the minimum value for negative numbers is $49$, it can't be negative.)

Now let's assume that all the numbers are 0. By just filling in the $1$st and $3$rd column, we find that it is:

\[\begin{bmatrix} 24 & ? &64&.&. \\ 18&.&48&48&.\\ 12&.&32&.&.\\ 6&.&16&.&.\\ 0&0&0&0&0\end{bmatrix}\]

which makes the $?=44$. $44$ is not an answer choice, so the bottom row cannot be all $0$'s.

Now, we know that the bottom row must be positive. Here's where the bashing begins. Lucky for us, the numbers must all be integers, cutting down on the number of cases we need to test. Starting with the bottom row having a common difference of $1$, we get

\[\begin{bmatrix} . & ? &.&.&. \\ 16&30&44&48&.\\ 12&21&30&39&48\\ 8&12&16&20&24\\ 4&3&2&1&0\end{bmatrix}\]

At this point we notice that the second row does not form an arithmetic progression, so we test out the next case, with the common difference being $2$. We get

\[\begin{bmatrix} . & ? &.&.&. \\ 14&27&40&48&.\\ 12&20&28&36&44\\ 10&13&16&19&22\\ 8&6&4&2&0\end{bmatrix}\]

At this point we notice that the second row does not form an arithmetic progression, so we test out the next case, with the common difference being $3$. We get

\[\begin{bmatrix} 12 & 29 &46&63&80 \\ 12&24&36&48&60\\ 12&19&26&33&40\\ 12&14&16&18&20\\ 12&9&6&3&0\end{bmatrix}\]

, giving us the answer $\boxed{\textbf{(C) }29}$

~ YTH ~Astingo for submission and final array

## Solution 4 (Arithmetic Sequences)

Let the bottom row of the grid have arithmetic difference $d$. Then the matrix becomes \[\begin{bmatrix} . & ? &.&.&4d \\ .&.&.&48&3d\\ 12&.&.&.&2d\\ .&.&16&.&d\\ .&.&.&.&0\end{bmatrix}\] Using the middle column, we have the middle item equal to $32-2d$. \[\begin{bmatrix} . & ? &.&.&4d \\ .&.&.&48&3d\\ 12&.&32-2d&.&2d\\ .&.&16&.&d\\ .&.&.&.&0\end{bmatrix}\] Filling in the middle row (which has a common difference of $10-d$) \[\begin{bmatrix} . & ? &.&.&. \\ .&.&.&48&.\\ 12&22-d&32-2d&42-3d&52-4d\\ .&.&16&.&.\\ 4d&3d&2d&d&0\end{bmatrix}\] The arithmetic sequence in the 4th column (2nd from the right) then has a common difference of $-3d-6$, so we \[\begin{bmatrix} . & ? &.&.&. \\ .&.&.&48&.\\ 12&22-d&32-2d&42-3d&52-4d\\ .&.&16&36-6d&.\\ 4d&3d&2d&30-9d&0\end{bmatrix} = \begin{bmatrix} . & ? &.&.&. \\ .&.&.&48&.\\ 12&22-d&32-2d&42-3d&52-4d\\ .&.&16&36-6d&.\\ 4d&3d&2d&d&0\end{bmatrix}\] From the cell in the 4th column, 5th row we have $30-9d=d$, or $d=3$. Finally, using the 2nd column, $\text{?} + 3d = 2(22-d)$, or $\text{?}+9=38 \Rightarrow \text{?}=\boxed{\text{(C) }29}$

~Metavaria

## Solution 5

We subtract $12$ from each element of the array and denote $a_{i,j}$ the number in position $(i,j), a_{3,1} = 0, a_{4,3} = 4,  a_{2,4} = 36,  a_{5,5} = - 12.$ Denoting $a_{3,2} = x \implies$ that in third row we get $(0, x, 2x, 3x, 4x).$ We use the property of an arithmetic progression and get \[a_{4,4} = 2a_{3,4} - a_{2,4} = 6x - 36,\]\[a_{4,5} = 2 a_{4,4}- a_{3,4} = 12x - 76,\]\[a_{5,5} = 2 a_{4,5}- a_{3,5} \implies  - 12 = 2(2x - 76) - 4x \implies x = 7 = a_{3,2},  a_{3,3}=14.\]\[\begin{bmatrix} .&.&.&.&. \\ .&.&.&36&.\\ 0&x&2x&3x&4x\\ .&.&4&6x-36&12x-76\\ .&.&.&.&-12\end{bmatrix}\]\[a_{2,3} = 2 a_{3,3}- a_{4,4} = 2 \cdot 14 - 4 = 24,\]\[a_{2,2} = 2 a_{2,3}- a_{2,4} = 2 \cdot 24 - 36 = 12,\]\[a_{1,2} = 2 a_{2,2}- a_{3,2} = 2 \cdot 12 - 7 = 17.\]

\[\begin{bmatrix} .&17&.&&.& \\ .&12&24&36&.\\ 0&7&14&.&.\\ .&.&.&.&.\\ .&.&.&.&.\end{bmatrix}\] We add $12$ and get the number in position $(1,2)$ as $17 + 12 = 29.$

**vladimir.shelomovskii@gmail.com, vvsss**

## See Also

**[2024 AMC 10A](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A "2024 AMC 10A")** (**[Problems](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems "2024 AMC 10A Problems")** • **[Answer Key](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Answer_Key "2024 AMC 10A Answer Key")** • [Resources](https://artofproblemsolving.com/community/c13))
Preceded by

**[Problem 20](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_20 "2024 AMC 10A Problems/Problem 20")**Followed by

**[Problem 22](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_22 "2024 AMC 10A Problems/Problem 22")**
[1](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_1 "2024 AMC 10A Problems/Problem 1")**•**[2](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_2 "2024 AMC 10A Problems/Problem 2")**•**[3](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_3 "2024 AMC 10A Problems/Problem 3")**•**[4](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_4 "2024 AMC 10A Problems/Problem 4")**•**[5](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_5 "2024 AMC 10A Problems/Problem 5")**•**[6](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_6 "2024 AMC 10A Problems/Problem 6")**•**[7](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_7 "2024 AMC 10A Problems/Problem 7")**•**[8](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_8 "2024 AMC 10A Problems/Problem 8")**•**[9](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_9 "2024 AMC 10A Problems/Problem 9")**•**[10](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_10 "2024 AMC 10A Problems/Problem 10")**•**[11](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_11 "2024 AMC 10A Problems/Problem 11")**•**[12](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_12 "2024 AMC 10A Problems/Problem 12")**•**[13](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_13 "2024 AMC 10A Problems/Problem 13")**•**[14](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_14 "2024 AMC 10A Problems/Problem 14")**•**[15](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_15 "2024 AMC 10A Problems/Problem 15")**•**[16](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_16 "2024 AMC 10A Problems/Problem 16")**•**[17](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_17 "2024 AMC 10A Problems/Problem 17")**•**[18](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_18 "2024 AMC 10A Problems/Problem 18")**•**[19](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_19 "2024 AMC 10A Problems/Problem 19")**•**[20](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_20 "2024 AMC 10A Problems/Problem 20")**•**[21](https://artofproblemsolving.com/wiki/index.php/2024_AMC_12A_Problems/Problem_14)**•**[22](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_22 "2024 AMC 10A Problems/Problem 22")**•**[23](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_23 "2024 AMC 10A Problems/Problem 23")**•**[24](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_24 "2024 AMC 10A Problems/Problem 24")**•**[25](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_25 "2024 AMC 10A Problems/Problem 25")
**[All AMC 10 Problems and Solutions](https://artofproblemsolving.com/wiki/index.php?title=AMC_10_Problems_and_Solutions "AMC 10 Problems and Solutions")**

*   [AMC 10](https://artofproblemsolving.com/wiki/index.php?title=AMC_10 "AMC 10")
*   [AMC 10 Problems and Solutions](https://artofproblemsolving.com/wiki/index.php?title=AMC_10_Problems_and_Solutions "AMC 10 Problems and Solutions")
*   [Mathematics competitions](https://artofproblemsolving.com/wiki/index.php?title=Mathematics_competitions "Mathematics competitions")
*   [Mathematics competition resources](https://artofproblemsolving.com/wiki/index.php?title=Mathematics_competition_resources "Mathematics competition resources")

[](https://artofproblemsolving.com/wiki/index.php?title=File:AMC_Logo.png)
