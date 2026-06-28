_The following problem is from the [2024 AMC 10A #15](https://artofproblemsolving.com/wiki/index.php/2024\_AMC\_12A\_Problems/Problem\_9) and [2024 AMC 12A #9](https://artofproblemsolving.com/wiki/index.php?title=2024\_AMC\_12A\_Problems/Problem\_9 "2024 AMC 12A Problems/Problem 9"), so those problems redirect to this page._
## Problem

Let $M$ be the greatest integer such that both $M+1213$ and $M+3773$ are perfect squares. What is the units digit of $M$?

$\textbf{(A) }1\qquad\textbf{(B) }2\qquad\textbf{(C) }3\qquad\textbf{(D) }6\qquad\textbf{(E) }8$

## Solution 1

Let $M+1213=P^2$ and $M+3773=Q^2$ for some positive integers $P$ and $Q.$ We subtract the first equation from the second, then apply the difference of squares: \[(Q+P)(Q-P)=2560.\] Note that $Q+P$ and $Q-P$ have the same parity, and $Q+P>Q-P.$

We wish to maximize both $P$ and $Q,$ so we maximize $Q+P$ and minimize $Q-P.$ It follows that \begin{align*} Q+P&=1280, \\ Q-P&=2, \end{align*} from which $(P,Q)=(639,641).$

Finally, we get $M=P^2-1213=Q^2-3773\equiv1-3\equiv8\pmod{10},$ so the units digit of $M$ is $\boxed{\textbf{(E) }8}.$

~MRENTHUSIASM

~Tacos_are_yummy_1

~minor edit

## Solution 2

Ideally, we would like for the two squares to be as close as possible. The best case is that they are consecutive squares (no square numbers in between them); however, since $M+1213$ and $M+3773$ (and thus their square roots) have the same parity, they cannot be consecutive squares (which are always opposite parities). The best we can do is that $M+1213$ and $M+3773$ have one square in between them.

Let the square between $M+1213$ and $M+3773$ be $x^2$. So, we have $M+1213 = (x-1)^2$ and $M+3773 = (x+1)^2$. Subtracting the two, we have $(M+3773)-(M+1213) = (x+1)^2 - (x-1)^2$, which yields $2560 = 4x$, which leads to $x = 640$. Therefore, the two squares are $639^2$ and $641^2$, which both have units digit $1$. Since both $1213$ and $3773$ have units digit $3$, $M$ will have units digit $\boxed{\textbf{(E) }8}$.

~i_am_suk_at_math_2 (parity argument editing by Technodoggo)

## Solution 3

Let $M+1213=N^2$$\Rightarrow M+3773=(N+a)^2$

It is obvious that $a\neq1$ by parity

Thus, the minimum value of $a$ is 2 Which gives us, \[(N+a)^2-N^2=M+3773-(M+1213)\]\[4N+4=2560\]\[N=639\] Plugging this back in, \[M=N^2-1213 \space \mod \space 10\]\[M=8 \space \mod \space 10\] Hence the answer $\boxed{\textbf{(E) }8}$.

~lptoggled

- trevian1(minor edit)

## Solution 4

Let $M+1213=n^2$ and $M+3773=(n+1)^2$ for some positive integer $n$. We do this because, in order to maximize $M$, the perfect squares need to be as close to each other as possible. We find that this configuration doesn't work, as when we subtract the equations, we have $2n+1=2560$; impossible. Then we try $M+3773=(n+2)^2$. Now we would have $4n+4=2560$ which indeed works! $n=639$.

Finally, we get $M=n^2-1213$ so the units digit of $M$ is $11-3=\boxed{\textbf{(E) }8}.$

~xHypotenuse

## Solution 5 (Quadratic Residues, Answer Choices rather than finding $M$)

Every perfect square modulo 4 must end in 0 or 1 modulo 4. Reducing modulo 4 yields

\[M + 1 \pmod{4}\]\[M + 1 \pmod{4}\].

Both values $M$ yeild the same result meaning that the units digit of $M$ is unchanged through constriction. Therefore, $M \equiv 3, 0 \pmod{4}$. Analyzing the answer choices, only 3 and 8 work.

Now consider quadratic residue's modulo 7. Once again, they are either 0, 1, 2, 4 modulo 7. Reducing, we have

\[M + 2 \pmod{7}\]\[M \pmod{7}\].

If the units digit of $M$ is 3, we arise at a contradiction that $M+2 \pmod{7}$ can never satisfy a perfect square. Thus, $M \pmod{10} = \boxed{8}$.

~Pinotation

## Solution 6 (EXTREMLY FAST, 1 STEP)

Squares can only end in 0,1,4,6,5, and 9. To have x+3 (since 1213 and 3773 end in 3) end in one of those numbers and be maximized, it would be 8, because 8+3=11. The answer is $\boxed{\textbf{(E) }8}.$

~MinglePringle348

## Note

We experiment with values of $M$ to find the reason for why $M$ is maximised when $M + 1213$ and $M + 3773$ are nearly consecutive perfect squares. If $M$ is very small, $M + 1213$ and $M + 3773$ are perfect squares that are far apart. Yet, as $M$ grows, the relative distance between $M + 1213$ and $M + 3773$ decreases, so for very nearly consecutive perfect squares, $M$ is very large.

~LeonQS

(I don't know if this is trivial - when I first read the solutions, I was confused to why this was true. Maybe I didn't get enough sleep.)

## See Also

**[2024 AMC 10A](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A "2024 AMC 10A")** (**[Problems](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems "2024 AMC 10A Problems")** • **[Answer Key](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Answer_Key "2024 AMC 10A Answer Key")** • [Resources](https://artofproblemsolving.com/community/c13))
Preceded by

**[2023 AMC 10B Problems](https://artofproblemsolving.com/wiki/index.php?title=2023_AMC_10B_Problems "2023 AMC 10B Problems")**Followed by

**[2024 AMC 10B Problems](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10B_Problems "2024 AMC 10B Problems")**
[1](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_1 "2024 AMC 10A Problems/Problem 1")**•**[2](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_2 "2024 AMC 10A Problems/Problem 2")**•**[3](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_3 "2024 AMC 10A Problems/Problem 3")**•**[4](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_4 "2024 AMC 10A Problems/Problem 4")**•**[5](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_5 "2024 AMC 10A Problems/Problem 5")**•**[6](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_6 "2024 AMC 10A Problems/Problem 6")**•**[7](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_7 "2024 AMC 10A Problems/Problem 7")**•**[8](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_8 "2024 AMC 10A Problems/Problem 8")**•**[9](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_9 "2024 AMC 10A Problems/Problem 9")**•**[10](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_10 "2024 AMC 10A Problems/Problem 10")**•**[11](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_11 "2024 AMC 10A Problems/Problem 11")**•**[12](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_12 "2024 AMC 10A Problems/Problem 12")**•**[13](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_13 "2024 AMC 10A Problems/Problem 13")**•**[14](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_14 "2024 AMC 10A Problems/Problem 14")**•**[15](https://artofproblemsolving.com/wiki/index.php/2024_AMC_12A_Problems/Problem_9)**•**[16](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_16 "2024 AMC 10A Problems/Problem 16")**•**[17](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_17 "2024 AMC 10A Problems/Problem 17")**•**[18](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_18 "2024 AMC 10A Problems/Problem 18")**•**[19](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_19 "2024 AMC 10A Problems/Problem 19")**•**[20](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_20 "2024 AMC 10A Problems/Problem 20")**•**[21](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_21 "2024 AMC 10A Problems/Problem 21")**•**[22](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_22 "2024 AMC 10A Problems/Problem 22")**•**[23](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_23 "2024 AMC 10A Problems/Problem 23")**•**[24](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_24 "2024 AMC 10A Problems/Problem 24")**•**[25](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_25 "2024 AMC 10A Problems/Problem 25")
**[All AMC 10 Problems and Solutions](https://artofproblemsolving.com/wiki/index.php?title=AMC_10_Problems_and_Solutions "AMC 10 Problems and Solutions")**

*   [AMC 10](https://artofproblemsolving.com/wiki/index.php?title=AMC_10 "AMC 10")
*   [AMC 10 Problems and Solutions](https://artofproblemsolving.com/wiki/index.php?title=AMC_10_Problems_and_Solutions "AMC 10 Problems and Solutions")
*   [AMC 12](https://artofproblemsolving.com/wiki/index.php?title=AMC_12 "AMC 12")
*   [AMC 12 Problems and Solutions](https://artofproblemsolving.com/wiki/index.php?title=AMC_12_Problems_and_Solutions "AMC 12 Problems and Solutions")
*   [Mathematics competitions](https://artofproblemsolving.com/wiki/index.php?title=Mathematics_competitions "Mathematics competitions")
*   [Mathematics competition resources](https://artofproblemsolving.com/wiki/index.php?title=Mathematics_competition_resources "Mathematics competition resources")

[](https://artofproblemsolving.com/wiki/index.php?title=File:AMC_Logo.png)
