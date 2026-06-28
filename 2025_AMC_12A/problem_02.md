_The following problem is from the [2025 AMC 10A #2](https://artofproblemsolving.com/wiki/index.php?title=2025\_AMC\_10A\_Problems/Problem\_2 "2025 AMC 10A Problems/Problem 2") and [2025 AMC 12A #2](https://artofproblemsolving.com/wiki/index.php/2025\_AMC\_12A\_Problems/Problem\_2), so those problems redirect to this page._
## Problem

A box contains $10$ pounds of a nut mix that is $50$ percent peanuts, $20$ percent cashews, and $30$ percent almonds. A second nut mix contains $20$ percent peanuts, $40$ percent cashews, and $40$ percent almonds.They are all added together in one box resulting in a new nut mix that has $40$ percent peanuts. How many pounds of cashews are now in the box?

$\textbf{(A) } 3.5 \qquad\textbf{(B) } 4 \qquad\textbf{(C) } 4.5 \qquad\textbf{(D) } 5 \qquad\textbf{(E) } 6$

## Solution 1

We are given $0.2(10) = 2$ pounds of cashews in the first box.

Denote the pounds of nuts in the second nut mix as $x.$

\[5 + 0.2x = 0.4(10 + x)\]\[0.2x = 1\]\[x = 5\]

Thus, we have $5$ pounds of the second mix.

\[0.4(5) + 2 = 2 + 2 = \boxed{\text{(B) }4}\]

~pigwash

~yuvaG (Formatting)

~LucasW (Minor $\LaTeX$)

~Kirbyisdabestboiii (Very very very minor edits)

## Solution 2

Let the number of pounds of nuts in the second nut mix be $x$. Therefore, we get the equation $0.5 \cdot 10 + 0.2 \cdot x = 0.4(x+10)$. Solving it, we get $x=5$. Therefore, the amount of cashews in the two bags is $(0.2 \cdot 10) + (0.4 \cdot 5) = 4$, so our answer choice is $\boxed{\textbf{(B)} 4}$.

~iiiiiizh

~yuvaG - $\LaTeX$ Formatting;)

~Amon26(really minor edits)

~vsarg (minor edits and grammatical fixxes)

## Solution 3

The percent of peanuts in the first mix is $10\%$ away from the total percentage of peanuts, and the percent of peanuts in the second mix is $20\%$ away from the total percentage. This means the first mix has twice as many nuts as the second mix, so the second mix has $5$ pounds. $0.20 \cdot 10 + 0.40 \cdot 5 = 4$ pounds of cashews. So our answer is, $\boxed{\textbf{(B)}4}$

The weight of the second box of nut mix can be calculated by: ($0.2x + 5) / (10 + x) = 0.4$, where the numerator is equal to the weight of the peanuts, the denominator is equal to the total weight of the boxes, and $x$ is equal to the weight of the second box.

Multiplying both sides by $10 + x$, you get $0.2x + 5 = 4 + 0.4x$

Isolating the variable: $0.2x = 1$$\Rightarrow x = 5$

Calculating the weight of the cashews: $5(0.4) + 10(0.2)$$\Rightarrow 2 + 2$$\Rightarrow 4$

The answer is $\boxed{\textbf{(B) } 4}$.

~LUCKYOKXIAO

~LEONG2023-Latex

## Solution 4

Note that we can set the information given in the problem into a table shown below:

\[\renewcommand{\arraystretch}{1.5} \begin{centering} \begin{array}{| c | c | c |} \hline \text{Peanuts} & \text{Cashews} & \text{Almonds}\\ \hline 5 & 2 & 3\\ \hline \frac{2}{10}x & \frac{4}{10}x & \frac{4}{10}x\\ \hline \end{array} \end{centering}\]

We are given that the new nut mix will contain $40\%$ peanuts. Hence, $5 + \frac{2}{10}x$ is $40\%$ of the total mix which is $10 + x$. Solving the equation $5 + \frac{2}{10}x = \frac{2}{5} \cdot (10 + x)$ yields $x=5.$ Therefore, the number of cashews in the new mix is equal to $2 + \frac{2}{5} \cdot 5 = \boxed{\textbf{(B)}  4}$.

~Moonlight11

~TehSovietOnion (LaTeX)

## Solution 5

Write composition vectors as column vectors (mass fractions multiplied by mass):

Initial mass vector (peanuts, cashews, almonds) for 10 lb: \[\mathbf{v}_0 = 10 \begin{pmatrix} 0.50 \\ 0.20 \\ 0.30 \end{pmatrix} = \begin{pmatrix} 5 \\ 2 \\ 3 \end{pmatrix}.\] Added mix per unit mass: \[\mathbf{u} = \begin{pmatrix} 0.20 \\ 0.40 \\ 0.40 \end{pmatrix}.\] After adding lb, total mass vector is \[\mathbf{v}(x) = \mathbf{v}_0 + x \mathbf{u} = \begin{pmatrix} 5 \\ 2 \\ 3 \end{pmatrix} + x \begin{pmatrix} 0.2 \\ 0.4 \\ 0.4 \end{pmatrix}.\] Peanut fraction requirement: \[\frac{\mathbf{e}_1^\top \mathbf{v}(x)}{\mathbf{1}^\top \mathbf{v}(x)} = 0.4,\] where and . This is exactly the same scalar equation, \[\frac{5 + 0.2x}{10 + x} = 0.4,\] leading to and hence \[\mathbf{v}(5) = \begin{pmatrix} 5 \\ 2 \\ 3 \end{pmatrix} + 5 \begin{pmatrix} 0.2 \\ 0.4 \\ 0.4 \end{pmatrix} = \begin{pmatrix} 6 \\ 4 \\ 5 \end{pmatrix}.\] Thus cashews lb.

## Solution 6: Very easy algebra and straightforward!

Set up the ratios for the initial and the additional mixtures. The ratio of Peanuts:Cashews:Almonds (denoted as P:C:A) would initially be $5x:2x:3x$ for some factor $x$. Then for the second mixture it would be $2x:4x:4x$. If we add these we get 7x:6x:7x. Now we know that the percentage of peanuts is 40\%. But we also know that the number of pounds of peanuts and almonds is the same. $40\%+40\%=80\%$ and so the number of cashews makes up $20\%$ of the mixture. If you divide the factor $x$ by the whole ratio you get $7:6:7$ . These values sum to $20$ and $20\%$ of $20$ is $4$.

## See Also

**[2025 AMC 10A](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A "2025 AMC 10A")** (**[Problems](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems "2025 AMC 10A Problems")** • **[Answer Key](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Answer_Key "2025 AMC 10A Answer Key")** • [Resources](https://artofproblemsolving.com/community/c13))
Preceded by

**[Problem 1](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_1 "2025 AMC 10A Problems/Problem 1")**Followed by

**[Problem 3](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_3 "2025 AMC 10A Problems/Problem 3")**
[1](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_1 "2025 AMC 10A Problems/Problem 1")**•**[2](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_2 "2025 AMC 10A Problems/Problem 2")**•**[3](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_3 "2025 AMC 10A Problems/Problem 3")**•**[4](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_4 "2025 AMC 10A Problems/Problem 4")**•**[5](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_5 "2025 AMC 10A Problems/Problem 5")**•**[6](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_6 "2025 AMC 10A Problems/Problem 6")**•**[7](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_7 "2025 AMC 10A Problems/Problem 7")**•**[8](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_8 "2025 AMC 10A Problems/Problem 8")**•**[9](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_9 "2025 AMC 10A Problems/Problem 9")**•**[10](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_10 "2025 AMC 10A Problems/Problem 10")**•**[11](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_11 "2025 AMC 10A Problems/Problem 11")**•**[12](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_12 "2025 AMC 10A Problems/Problem 12")**•**[13](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_13 "2025 AMC 10A Problems/Problem 13")**•**[14](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_14 "2025 AMC 10A Problems/Problem 14")**•**[15](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_15 "2025 AMC 10A Problems/Problem 15")**•**[16](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_16 "2025 AMC 10A Problems/Problem 16")**•**[17](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_17 "2025 AMC 10A Problems/Problem 17")**•**[18](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_18 "2025 AMC 10A Problems/Problem 18")**•**[19](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_19 "2025 AMC 10A Problems/Problem 19")**•**[20](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_20 "2025 AMC 10A Problems/Problem 20")**•**[21](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_21 "2025 AMC 10A Problems/Problem 21")**•**[22](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_22 "2025 AMC 10A Problems/Problem 22")**•**[23](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_23 "2025 AMC 10A Problems/Problem 23")**•**[24](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_24 "2025 AMC 10A Problems/Problem 24")**•**[25](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_25 "2025 AMC 10A Problems/Problem 25")
**[All AMC 10 Problems and Solutions](https://artofproblemsolving.com/wiki/index.php?title=AMC_10_Problems_and_Solutions "AMC 10 Problems and Solutions")**

[](https://artofproblemsolving.com/wiki/index.php?title=File:AMC_Logo.png)
