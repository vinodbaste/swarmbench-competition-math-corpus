_The following problem is from the [2024 AMC 10A #19](https://artofproblemsolving.com/wiki/index.php/2024\_AMC\_12A\_Problems/Problem\_12) and [2024 AMC 12A #12](https://artofproblemsolving.com/wiki/index.php?title=2024\_AMC\_12A\_Problems/Problem\_12 "2024 AMC 12A Problems/Problem 12"), so those problems redirect to this page._
## Problem

The first three terms of a geometric sequence are the integers $a,\,720,$ and $b,$ where $a<720<b.$ What is the sum of the digits of the least possible value of $b?$

$\textbf{(A) } 9 \qquad \textbf{(B) } 12 \qquad \textbf{(C) } 16 \qquad \textbf{(D) } 18 \qquad \textbf{(E) } 21$

## Solution 1

For a geometric sequence, we have $ab=720^2=2^8 3^4 5^2$, and we can test values for $b$. We find that $b=768$ and $a=675$ works, and we can test multiples of $5$ in between the two values. Finding that none of the multiples of 5 divide $720^2$ besides $720$ itself, we know that the answer is $7+6+8=\boxed{\textbf{(E) } 21}$.

(Note: To find the value of $b$ without bashing, we can observe that $2^8=256$, and that multiplying it by $3$ gives us $768$, which is really close to $720$. ~ YTH)

Note: The reason why $ab=720^2$ is because $b/720 = 720/a$. Rearranging this gives $ab = 720^2$

~eevee9406

Note: Another reason that $ab=720^2$ is because the $\sqrt{ab}=720$ (as the middle term in a geometric series is always the geometric mean [the geometric mean is the square root of the product of the first and last terms of the series]) and squaring on both sides results in $ab=720^2$.

~ThatPrimePunnyGuy

Note: Because it is a geometric sequence, it is clear that $a*k = 720$ and $720*k = b$. Then, $a*k = 720 = b/k$. Multiply the first and third term together and it is equal to the middle term multiplied by itself.

~RON-WEASLEY

## Solution 2

We have $720 = 2^4 \cdot 3^2 \cdot 5$. We want to find factors $x$ and $y$ where $y>x$ such that $\frac{y}{x}$ is minimized, as $720 \cdot \frac{y}{x}$ will then be the least possible value of $b$. After experimenting, we see this is achieved when $y=16$ and $x=15$, which means our value of $b$ is $720 \cdot \frac{16}{15} = 768$, so therefore our sum is $7+6+8=\boxed{\textbf{(E) } 21}$.

~i_am_suk_at_math_2

## Solution 3 (Similar to previous solutions)

To minimize the value of $b$, where it has to be an integer, and it has to be greater than 720, we can express the common ratio as $\dfrac{n+1}{n}$, where the value has to be greater than $1$, and $n$, and $n+1$ have to be factors of 720. Since the bigger the denominator gets, the smaller the value of the fraction, we essentially have to find the biggest value for $n$, where itself and $n+1$ are factors of $720$. From here, we can check whether $n(n+1) = 720$ yields an integer root, which it doesn't. So, then we check the next biggest factor of $720$, which is $360$. $n(n+1) = 360$, this doesn't have an integer root either. So, then we check the next biggest factor which is $240$, $n(n+1) = 240$, which we get $15$ as a root. This means the common ration is $\dfrac{16}{15}$. We then multiply $\dfrac{16}{15}$ times $720$ and add up the digits getting $\boxed{\textbf{(E) } 21}$.

~yuvag

## Solution 4

Let the common ratio of the geometric sequence be $\frac{x}{y}$, with $x>y$. This means that $720(\frac{x}{y})$ and $720(\frac{y}{x})$ must both be integers, therefore $x$ and $y$ are both factors of $720$. We would achieve the smallest ratio $\frac{x}{y}$ if $x$ and $y$ are consecutive, so by listing out the factors of $720$, we find that $1$, $2$, $3$, $4$, $5$, $6$, $8$, $9$, $10$, $15$, $16$ are the only consecutive factors (any factors larger than these would result in the ratio simplifying, making it larger than just using consecutive integers). $15$ and $16$ are the largest, so we find the common ratio to be $\frac{16}{15}$, making $b=720(\frac{16}{15})$ giving us $768$. The sum of its digits is $\boxed{\textbf{(E) } 21}$.

~lisztepos

~ small edit by RoyalPawn38

## Solution 5 (similar to other solutions)

We look for the smallest possible increasing ratio in the geometric sequence for $a$, $720$, and $b$. First, we find the prime factorization of $720$, which is really easy $720=2^4\cdot3^2\cdot5$. Then, we look for the closest possible fraction-ratio out of the primes, and after a quick look, it's easy to see it is $16$ and $15$. Now that we found our ratio, we multiply $720$ by $\frac{16}{15}$ to get $768$, so the sum of the digits of the least possible value of $b$ is $21$.

~hashbrown2009 ~GoldemGem4848 did the latex

NOTE: It's not 9/8 because we want it to be as close as possible to 1 ~gabrielle.esther

## See Also

**[2024 AMC 10A](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A "2024 AMC 10A")** (**[Problems](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems "2024 AMC 10A Problems")** • **[Answer Key](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Answer_Key "2024 AMC 10A Answer Key")** • [Resources](https://artofproblemsolving.com/community/c13))
Preceded by

**[Problem 18](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_18 "2024 AMC 10A Problems/Problem 18")**Followed by

**[Problem 20](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_20 "2024 AMC 10A Problems/Problem 20")**
[1](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_1 "2024 AMC 10A Problems/Problem 1")**•**[2](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_2 "2024 AMC 10A Problems/Problem 2")**•**[3](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_3 "2024 AMC 10A Problems/Problem 3")**•**[4](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_4 "2024 AMC 10A Problems/Problem 4")**•**[5](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_5 "2024 AMC 10A Problems/Problem 5")**•**[6](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_6 "2024 AMC 10A Problems/Problem 6")**•**[7](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_7 "2024 AMC 10A Problems/Problem 7")**•**[8](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_8 "2024 AMC 10A Problems/Problem 8")**•**[9](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_9 "2024 AMC 10A Problems/Problem 9")**•**[10](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_10 "2024 AMC 10A Problems/Problem 10")**•**[11](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_11 "2024 AMC 10A Problems/Problem 11")**•**[12](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_12 "2024 AMC 10A Problems/Problem 12")**•**[13](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_13 "2024 AMC 10A Problems/Problem 13")**•**[14](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_14 "2024 AMC 10A Problems/Problem 14")**•**[15](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_15 "2024 AMC 10A Problems/Problem 15")**•**[16](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_16 "2024 AMC 10A Problems/Problem 16")**•**[17](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_17 "2024 AMC 10A Problems/Problem 17")**•**[18](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_18 "2024 AMC 10A Problems/Problem 18")**•**[19](https://artofproblemsolving.com/wiki/index.php/2024_AMC_12A_Problems/Problem_12)**•**[20](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_20 "2024 AMC 10A Problems/Problem 20")**•**[21](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_21 "2024 AMC 10A Problems/Problem 21")**•**[22](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_22 "2024 AMC 10A Problems/Problem 22")**•**[23](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_23 "2024 AMC 10A Problems/Problem 23")**•**[24](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_24 "2024 AMC 10A Problems/Problem 24")**•**[25](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_25 "2024 AMC 10A Problems/Problem 25")
**[All AMC 10 Problems and Solutions](https://artofproblemsolving.com/wiki/index.php?title=AMC_10_Problems_and_Solutions "AMC 10 Problems and Solutions")**

[](https://artofproblemsolving.com/wiki/index.php?title=File:AMC_Logo.png)
