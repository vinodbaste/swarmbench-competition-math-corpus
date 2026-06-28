_The following problem is from the [2025 AMC 10B #21](https://artofproblemsolving.com/wiki/index.php?title=2025\_AMC\_10B\_Problems/Problem\_21 "2025 AMC 10B Problems/Problem 21") and [2025 AMC 12B #17](https://artofproblemsolving.com/wiki/index.php/2025\_AMC\_12B\_Problems/Problem\_17), so those problems redirect to this page._
## Problem

Each of the $9$ squares in a ${3 \times 3}$ grid is to be colored red, blue, or yellow in such a way that each red square shares an edge with at least one blue square, each blue square shares an edge with at least one yellow square, and each yellow square shares an edge with at least one red square. Colorings that can be obtained from one another by rotations and/or reflections are considered the same. How many different colorings are possible?

$\textbf{(A) } 3 \qquad \textbf{(B) } 9 \qquad \textbf{(C) } 12 \qquad \textbf{(D) } 18 \qquad \textbf{(E) } 27$

## Solution 1 (Casework)

Denote $1=\text{red}$, $2=\text{blue}$, $3=\text{yellow}$. We need $1\to 2\to 3\to 1$.

WLOG place $1$ in the center $(0,0)$, $2$ on the left edge $(-1,0)$, $3$ on the top-left corner $(-1,1)$. \[\begin{bmatrix} 3 & 0 & 0 \\ 2 & 1 & 0 \\ 0 & 0 & 0 \end{bmatrix}\]$3$ must see $1$, so the top edge $(0,1)$ must also have $1$. Then, $1$ must see $2$, so the top-right corner $(1,1)$ becomes $2$, which must see $3$, so the right edge $(1,0)$ must have $3$. \[\begin{bmatrix} 3 & 1 & 2 \\ 2 & 1 & 3 \\ 0 & 0 & 0 \end{bmatrix}\] Now this bottom-right corner can vary either as $1$, $2$ or $3$. Cases on $(1,-1)$: If $1$: \[\begin{bmatrix} 3 & 1 & 2 \\ 2 & 1 & 3 \\ 3 & 2 & 1 \end{bmatrix}\] but the 3 needs a 1 and does not have it, so there are $0$ cases. If $2$: \[\begin{bmatrix} 3 & 1 & 2 \\ 2 & 1 & 3 \\ b & a & 2 \end{bmatrix}\] if $a=1$, $b$ can be $1$ or $3$. If $a=2$, $b=3$, but the 3 needs a 1 and can't get it. If $a=3$, $b=1,2$, so there are $4$ cases in total. If $3$: \[\begin{bmatrix} 3 & 1 & 2 \\ 2 & 1 & 3 \\ 2 & 1 & 3 \end{bmatrix}\] Since the 2 in the bottom left corner does not have a 3 nearby, there are $0$ cases.

WLOG the center fixes a factor of $3$, so the answer is $4\cdot 3=\boxed{\textbf{(C) } 12}$.

~imosilver - hey random question did u get silver in IMO? W if u did ,lwky nice solution =) ~edited by Alex Tu

## Solution 2 (Complex Circular Counting)

This solution is complex, but gives the answer in less than a couple minutes and saves the bearing of casework, so proceed as a last resort.

Also yes this solution is inspired from 3Blue1Brown's Olympiad Counting video.

We will find the arrangement that contains the least possible occurrences of a color and the most occurrences of a color , in which we will then use the circular gap theorem on all integers such that and .

The average number of colors is simply (9 slots divided by 3 colors). So we see that the interval contains . We also have that the minimal number of colors is clearly 1 (it doesn't take much to show a case that contains only one color). The challenge is to find the maximal number, which is .

We see that there must be at least one of each color, so can be a maximum of 6. However, we can see that 6 clearly cannot be , as if we have a configuration of 6 colors, that would mean that through the constraints in the problem, the other three colors are already uniquely determined. However, now there is no slots in the grid, and we cannot satisfy all the requirements, so .

However, we also find that , as the four colors, say blue already determine 2 other colors, say yellow, which determine another 2 colors, say red. However, now there is one color left! This color must be blue (as there are 5), but if there is one blue an no yellow to satisfy the condition, then the case is simply impossible. Therefore, .

We can try to do the same thing for 4, but we will see that satisfies the prerequisites.

Therefore, and , in which we then use the circular gap theorem

\[C_n A = \frac{n}{k} \binom{n-k-1}{k-1}\]

For , and

And so, we do so!

For , (note that every $\binom{n}{0}=1$)

For ,

For ,

For ,

Our answer is just the sum of all four of these, which is or $\boxed{\textbf{(C) } 12}$

~Pinotation

btw the actual theorem name for isn't actually the Circular Gap Theorem. I just call it that because I honestly don't know the name of it. It is a pretty neat theorem however, and I first learned it from this AIME problem here: [1983 AIME Q7 Sol. 9](https://artofproblemsolving.com/wiki/index.php?title=1983_AIME_Problems/Problem_7).

It is apparently a closed form for the number of ways to write $n$ as the sum of $k$ positive circular cycles for $n \ge 2$, and for $0<n \le 1$, the value is just 1.

## Solution 3 (Alternative Casework)

We begin by WLOG-ing the center box as red, denoted R. \[\begin{tabular}{|c|c|c|} \hline  &  &  \\ \hline  & R &  \\ \hline  &  &  \\ \hline \end{tabular}\] We will then consider the upper edge box, for now we'll assume it to be blue (it will be clear later) \[\begin{tabular}{|c|c|c|} \hline  & B &  \\ \hline  & R &  \\ \hline  &  &  \\ \hline \end{tabular}\] Now we consider the upper right box, which is forced to be yellow as it would be redundant due to reflection through the middle column. \[\begin{tabular}{|c|c|c|} \hline  & B & Y \\ \hline  & R &  \\ \hline  &  &  \\ \hline \end{tabular}\] Now, working in a clockwise direction, the right edge box is forced to be red, the bottom corner therefore is forced to be blue, and the bottom edge is forced to be yellow. \[\begin{tabular}{|c|c|c|} \hline  & B & Y \\ \hline  & R & R \\ \hline  & Y & B \\ \hline \end{tabular}\] Now we must consider the bottom left corner. If we set the bottom left corner to red, the left edge therefore must be blue, but then nothing can be filled in for the top left box (red causes left edge to violate the blue -> yellow rule, blue fails for a multitude of reasons, and yellow violates the yellow -> red rule). \[\begin{tabular}{|c|c|c|} \hline ? & B & Y \\ \hline B & R & R \\ \hline R & Y & B \\ \hline \end{tabular}\] Yellow also doesn't work, since we get: \[\begin{tabular}{|c|c|c|} \hline B & B & Y \\ \hline R & R & R \\ \hline Y & Y & B \\ \hline \end{tabular}\] but then the blue top-left corner has no adjacent yellow box. On the other hand, blue does give $4$ valid configurations:

Either $(1)$: \[\begin{tabular}{|c|c|c|} \hline R & B & Y \\ \hline R & R & R \\ \hline B & Y & B \\ \hline \end{tabular}\] or $(2)$: \[\begin{tabular}{|c|c|c|} \hline Y & B & Y \\ \hline R & R & R \\ \hline B & Y & B \\ \hline \end{tabular}\] or $(3)$: \[\begin{tabular}{|c|c|c|} \hline R & B & Y \\ \hline Y & R & R \\ \hline B & Y & B \\ \hline \end{tabular}\] or $(4)$: \[\begin{tabular}{|c|c|c|} \hline B & B & Y \\ \hline Y & R & R \\ \hline B & Y & B \\ \hline \end{tabular}\]

We can now explain why it's valid to assume that the upper edge box is blue: if it were yellow instead, the grid would simply be the reflection of one of the above configurations through the middle row, precisely because the bottom edge box is yellow (as this would then become the upper edge box under the reflection). If the upper edge box were red, either the upper-left or the upper-right box would have to be blue, and so by reflection through the middle column (just like above), we can assume that the upper-right box specifically is blue. Again similarly to above, we can now fill in the rest of the entire grid, giving one of the following $5$ configurations:

Either $(A)$: \[\begin{tabular}{|c|c|c|} \hline Y & R & B \\ \hline B & R & Y \\ \hline R & R & B \\ \hline \end{tabular}\] or $(B)$: \[\begin{tabular}{|c|c|c|} \hline R & R & B \\ \hline B & R & Y \\ \hline Y & R & B \\ \hline \end{tabular}\] or $(C)$: \[\begin{tabular}{|c|c|c|} \hline Y & R & B \\ \hline B & R & Y \\ \hline Y & R & B \\ \hline \end{tabular}\] or $(D)$: \[\begin{tabular}{|c|c|c|} \hline Y & R & B \\ \hline B & R & Y \\ \hline R & Y & B \\ \hline \end{tabular}\] or $(E)$: \[\begin{tabular}{|c|c|c|} \hline Y & R & B \\ \hline B & R & Y \\ \hline B & Y & B \\ \hline \end{tabular}\] But $(B)$ is simply the reflection of $(A)$ in the bottom row, so we can eliminate it. After that, we observe that $(A)$ is a rotation of $(1)$ above, $(C)$ is a rotation of $(2)$, $(D)$ is a rotation of $(3)$, and $(E)$ is a rotation of $(4)$, so we can in fact eliminate all of these too.

Accordingly, having taken the central box as red, there are $4$ distinct possible configurations (precisely $(1)$ to $(4)$ above), and by symmetry, that number of possible configurations will clearly be the same if the central box is blue or yellow instead. Thus there are $3$ possible choices for the central box, followed by $4$ ways to complete the grid in each of these cases, so the total number of possible grids is $3 \cdot 4 = \boxed{\textbf{(C) } 12}$.

~hi-person, edited substantially by SevenOptimus to fix mistakes

## See Also

**[2025 AMC 10B](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B "2025 AMC 10B")** (**[Problems](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems "2025 AMC 10B Problems")** • **[Answer Key](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Answer_Key "2025 AMC 10B Answer Key")** • [Resources](https://artofproblemsolving.com/community/c13))
Preceded by

**[Problem 20](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_20 "2025 AMC 10B Problems/Problem 20")**Followed by

**[Problem 22](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_22 "2025 AMC 10B Problems/Problem 22")**
[1](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_1 "2025 AMC 10B Problems/Problem 1")**•**[2](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_2 "2025 AMC 10B Problems/Problem 2")**•**[3](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_3 "2025 AMC 10B Problems/Problem 3")**•**[4](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_4 "2025 AMC 10B Problems/Problem 4")**•**[5](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_5 "2025 AMC 10B Problems/Problem 5")**•**[6](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_6 "2025 AMC 10B Problems/Problem 6")**•**[7](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_7 "2025 AMC 10B Problems/Problem 7")**•**[8](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_8 "2025 AMC 10B Problems/Problem 8")**•**[9](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_9 "2025 AMC 10B Problems/Problem 9")**•**[10](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_10 "2025 AMC 10B Problems/Problem 10")**•**[11](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_11 "2025 AMC 10B Problems/Problem 11")**•**[12](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_12 "2025 AMC 10B Problems/Problem 12")**•**[13](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_13 "2025 AMC 10B Problems/Problem 13")**•**[14](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_14 "2025 AMC 10B Problems/Problem 14")**•**[15](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_15 "2025 AMC 10B Problems/Problem 15")**•**[16](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_16 "2025 AMC 10B Problems/Problem 16")**•**[17](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_17 "2025 AMC 10B Problems/Problem 17")**•**[18](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_18 "2025 AMC 10B Problems/Problem 18")**•**[19](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_19 "2025 AMC 10B Problems/Problem 19")**•**[20](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_20 "2025 AMC 10B Problems/Problem 20")**•**[21](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_21 "2025 AMC 10B Problems/Problem 21")**•**[22](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_22 "2025 AMC 10B Problems/Problem 22")**•**[23](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_23 "2025 AMC 10B Problems/Problem 23")**•**[24](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_24 "2025 AMC 10B Problems/Problem 24")**•**[25](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_25 "2025 AMC 10B Problems/Problem 25")
**[All AMC 10 Problems and Solutions](https://artofproblemsolving.com/wiki/index.php?title=AMC_10_Problems_and_Solutions "AMC 10 Problems and Solutions")**

[](https://artofproblemsolving.com/wiki/index.php?title=File:AMC_Logo.png)
