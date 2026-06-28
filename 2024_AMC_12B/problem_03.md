_The following problem is from the [2024 AMC 10B #3](https://artofproblemsolving.com/wiki/index.php/2024\_AMC\_12B\_Problems/Problem\_3) and [2024 AMC 12B #3](https://artofproblemsolving.com/wiki/index.php?title=2024\_AMC\_12B\_Problems/Problem\_3 "2024 AMC 12B Problems/Problem 3"), so those problems redirect to this page._
## Problem

For how many integer values of $x$ is $|2x| \leq 7 \pi$

$\textbf{(A) } 16 \qquad\textbf{(B) } 17 \qquad\textbf{(C) } 19 \qquad\textbf{(D) } 20 \qquad\textbf{(E) } 21$

### Modified Problem in Certain China Testpapers

For how many integer values of $x$ is $|2x| \leq 6 \pi$

$\textbf{(A) } 16 \qquad\textbf{(B) } 17 \qquad\textbf{(C) } 19 \qquad\textbf{(D) } 20 \qquad\textbf{(E) } 21$

### Solution for Certain China Testpapers

Use the fact that $\pi \approx 3.14$, and thus you can get $6\pi \approx 18.84$. We could easily see that the answer is $\{-9,-8,...,8,9\}\implies\boxed{\text{(C) }19}$

~RULE101

## Solution 1

$\pi = 3.14159\dots$ is slightly less than $\dfrac{22}{7} = 3.\overline{142857}$. So $7\pi \approx 21.9$ The inequality expands to be $-21.9 \le 2x \le 21.9$. We find that $x$ can take the integer values between $-10$ and $10$ inclusive. There are $\boxed{\text{E. }21}$ such values.

Note that if you did not know whether $\pi$ was greater than or less than $\dfrac{22}{7}$, then you might perform casework. In the case that $\pi > \dfrac{22}{7}$, the valid solutions are between $-11$ and $11$ inclusive: $23$ solutions. Since, $23$ is not an answer choice, we can be confident that $\pi < \dfrac{22}{7}$, and that $\boxed{\text{E. } 21}$ is the correct answer.

~numerophile

Test advice: If you are in the test and do not know if $\frac{22}{7}$ is bigger or smaller than $\pi$, you can use the extremely sophisticated method of just dividing $\dfrac{22}{7}$ via long division. Once you get to $3.142$ you realise that you don't need to divide further since $\pi = 3.1416$ when rounded to 4 decimal places.Therefore, you do not include $11$ and $-11$ and the answer is 21.

~Rosiefork (first time using Latex)(and a complete noob)

## Solution 2

$7\pi$ is incredibly close to $22$, but doesn't reach it. This can be both computed by using $\pi\approx3.142\implies7\cdot3.142=21.994<22$ or assumed. Therefore, including both positive and negative values, the answer is $\{-10,-9,...,9,10\}\implies\boxed{\text{(E) }21}$. ~Tacos_are_yummy_1
