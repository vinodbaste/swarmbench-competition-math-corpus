_The following problem is from the [2025 AMC 10B #23](https://artofproblemsolving.com/wiki/index.php?title=2025\_AMC\_10B\_Problems/Problem\_23 "2025 AMC 10B Problems/Problem 23") and [2025 AMC 12B #19](https://artofproblemsolving.com/wiki/index.php/2025\_AMC\_12B\_Problems/Problem\_19), so those problems redirect to this page._
## Problem

A rectangular grid of squares has $141$ rows and $91$ columns. Each square has room for two numbers. Horace and Vera each fill in the grid by putting the numbers from $1$ through $141 \times 91 = 12{,}831$ into the squares. Horace fills the grid horizontally: he puts $1$ through $91$ in order from left to right into row $1$, puts $92$ through $182$ into row $2$ in order from left to right, and continues similarly through row $141$. Vera fills the grid vertically: she puts $1$ through $141$ in order from top to bottom into column $1$, then $142$ through $282$ into column $2$ in order from top to bottom, and continues similarly through column $91$. How many squares get two copies of the same number?

$\textbf{(A)}~7 \qquad \textbf{(B)}~10 \qquad \textbf{(C)}~11 \qquad \textbf{(D)}~12 \qquad \textbf{(E)}~19$

## Note

This problem is similar to problem 16 on the 2000 AMC 12. The other problem asks for the sum of the duplicates, not the number of them. ~mathwizard123123

Yes, and it feels like this 2025 problem is a bit easier. ~heliostan

Yes, I agree. ~Cheerfulfrog

## Solution 1

Let's say $n$ is one of the numbers that got written twice in the same box. Suppose it is at column $x$ and row $y$. We will write an expression for $n$ in terms of $x$ and $y$ in two ways: from Horace's perspective and Vera's perspective.

From Horace's perspective, $n = (y-1)(141) + x$. This is because there are $y-1$ full rows before $n$, and we then need $x$ more numbers to reach $n$. Similarly, Vera will say $n = (x-1)(91) + y$.

We now have the Diophantine equation \[(y-1)(141) + x = (x-1)(91)+y\]\[141y-141+x = 91x-91+y\]\[140y=90x+50\]\[14y = 9x + 5\] One such solution is, of course, $x=y=1$. We find further solutions by adding $14$ to $x$ and $9$ to $y$. For example, the second solution is $(15,10)$. This continues until $(141,91)$ is reached. There are $\boxed{11}$ ordered pairs in this list.

~lprado

### Solution 1 (Easier way to count)

The Diophantine equation $14y-9x=5$ is in the form $ax+by = c$ has primary solution $(x_0, y_0) = (1,1)$. Also, $h = \gcd(a,b) =\gcd(14, -5) = \gcd(14,5) = 1$, and thus the solutions are of the form

\[y = 1 + 9k\]\[x = 1 + 14k\]

for some $k$.

Then, notice that because $k \ge 0$, $1 \le x \le 141$, and $1 \le y \le 91$, the largest value possible is $(x,y) = (141, 91)$, and thus

\[14k \le 140\]\[9k \le 90\].

In which $k \le 10$ in both cases. Thus there are 10 positive integers $k$ that satisfy the following. Including 0, there are $10 + 1 = \boxed{11}$.

~Pinotation

## Solution 2 (0-indexing)

For these types of problems, we essentially analyze residues, so it is more convenient to work with 0-indexing: $c=0,1,2,\dots,90$, $r=0,1,2,\dots,140$.

Then $n=91r+c+1=141c+r+1\iff 9r=14c$. We must have $(r,c)=(0,0),(14,9),(28,18),\dots,(140,90)$ so $\boxed{ \textbf{(C)}~11 }$.

~imosilver

## Solution 2 (faster ending)

After indexing to 0, we imagine a line that passes from $(0,0)$ to $(140,90)$. We know we are looking for all lattice points that lie on this line (this intuitively makes sense, because any points above the line would have column numbers far ahead of the rows, and vice versa).

Therefore, we know that the number of points must divide both $140$ and $90$. The GCD of the two is 10. We also account for point $(0,0)$, and get that $10+1=\boxed{ \textbf{(C)}~11 }$.

## Solution 3

Observe that Horaces number can be expressed as the remainder of the row number plus the column number so $H$(Horaces Number)$=91(c-1)$(column addition)$+r$(remainder of division) and do the same for Vera $V=141(r-1)+c$.The condition is $H=V$ so set the equations equal to each other. $91(c-1)+r=141(r-1)+c$ so $91c-91+r=141r-141+c$,$140r=90c+50$.This a linear Diophantine equation and the 1st solution is $(1,1)$ where the solution repeats every $lcm(90,140)=1260$ there are $11$ solutions so $\boxed{\textbf{(C)}11}$ is correct.

~~TFEA

~$\LaTeX$ by OlympiadMaster

## See Also

**[2025 AMC 10B](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B "2025 AMC 10B")** (**[Problems](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems "2025 AMC 10B Problems")** • **[Answer Key](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Answer_Key "2025 AMC 10B Answer Key")** • [Resources](https://artofproblemsolving.com/community/c13))
Preceded by

**[Problem 22](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_22 "2025 AMC 10B Problems/Problem 22")**Followed by

**[Problem 24](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_24 "2025 AMC 10B Problems/Problem 24")**
[1](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_1 "2025 AMC 10B Problems/Problem 1")**•**[2](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_2 "2025 AMC 10B Problems/Problem 2")**•**[3](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_3 "2025 AMC 10B Problems/Problem 3")**•**[4](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_4 "2025 AMC 10B Problems/Problem 4")**•**[5](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_5 "2025 AMC 10B Problems/Problem 5")**•**[6](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_6 "2025 AMC 10B Problems/Problem 6")**•**[7](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_7 "2025 AMC 10B Problems/Problem 7")**•**[8](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_8 "2025 AMC 10B Problems/Problem 8")**•**[9](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_9 "2025 AMC 10B Problems/Problem 9")**•**[10](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_10 "2025 AMC 10B Problems/Problem 10")**•**[11](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_11 "2025 AMC 10B Problems/Problem 11")**•**[12](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_12 "2025 AMC 10B Problems/Problem 12")**•**[13](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_13 "2025 AMC 10B Problems/Problem 13")**•**[14](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_14 "2025 AMC 10B Problems/Problem 14")**•**[15](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_15 "2025 AMC 10B Problems/Problem 15")**•**[16](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_16 "2025 AMC 10B Problems/Problem 16")**•**[17](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_17 "2025 AMC 10B Problems/Problem 17")**•**[18](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_18 "2025 AMC 10B Problems/Problem 18")**•**[19](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_19 "2025 AMC 10B Problems/Problem 19")**•**[20](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_20 "2025 AMC 10B Problems/Problem 20")**•**[21](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_21 "2025 AMC 10B Problems/Problem 21")**•**[22](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_22 "2025 AMC 10B Problems/Problem 22")**•**[23](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_23 "2025 AMC 10B Problems/Problem 23")**•**[24](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_24 "2025 AMC 10B Problems/Problem 24")**•**[25](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10B_Problems/Problem_25 "2025 AMC 10B Problems/Problem 25")
**[All AMC 10 Problems and Solutions](https://artofproblemsolving.com/wiki/index.php?title=AMC_10_Problems_and_Solutions "AMC 10 Problems and Solutions")**

[](https://artofproblemsolving.com/wiki/index.php?title=File:AMC_Logo.png)
