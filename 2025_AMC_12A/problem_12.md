_The following problem is from the [2025 AMC 10A #18](https://artofproblemsolving.com/wiki/index.php?title=2025\_AMC\_10A\_Problems/Problem\_18 "2025 AMC 10A Problems/Problem 18") and [2025 AMC 12A #12](https://artofproblemsolving.com/wiki/index.php/2025\_AMC\_12A\_Problems/Problem\_12), so those problems redirect to this page._
## Problem

The _harmonic mean_ of a collection of numbers is the reciprocal of the arithmetic mean of the reciprocals of the numbers in the collection. For example, the harmonic mean of $4,4,$ and $5$ is

\[\frac{1}{\frac{1}{3}(\frac{1}{4}+\frac{1}{4}+\frac{1}{5})}=\frac{30}{7}.\]

What is the harmonic mean of all the real roots of the $4050$th degree polynomial

\[\prod_{k=1}^{2025} (kx^2-4x-3)=(x^2-4x-3)(2x^2-4x-3)(3x^2-4x-3)...(2025x^2-4x-3)?\]

$\textbf{(A)}~-\frac{5}{3}\qquad\textbf{(B)}~-\frac{3}{2}\qquad\textbf{(C)}~-\frac{6}{5}\qquad\textbf{(D)}~-\frac{5}{6}\qquad\textbf{(E)}~-\frac{2}{3}$

## Solution 1

We will need to determine the sum of the reciprocals of the roots. To find the sum of the reciprocals of the roots $p,q$ of the quadratic $ax^2+bx+c$, we use Vieta's formulas. Recall that $p+q = -b/a$ and $pq = c/a$. Therefore, \[\frac{1}{p} + \frac{1}{q} = \frac{p+q}{pq} = \frac{\frac{-b}{a}}{\frac{c}{a}} = \frac{-b}{a} \cdot \frac{a}{c} = \frac{-b}{c},\] which doesn't depend on $a$.

The sum of the reciprocals of the roots of the quadratic $x^2-4x-3$ is $\frac{-(-4)}{-3} = -4/3.$ The same is true for every quadratic in the form $ax^2-4x-3$. The sum of all the reciprocals of the roots of $ax^2+bx+c$ is $2025 \cdot \left(-\frac{4}{3}\right).$

Because we have $2025$ quadratics, there are $2 \cdot 2025 = 4050$ total roots. Our answer is $\frac{1}{\frac{1}{4050}\cdot \frac{-4\cdot 2025}{3}} =\boxed{(B)\ -\dfrac{3}{2}}$.

~lprado

~some edits by i_am_not_suk_at_math, zoyashaikh, keanu31415 (minor latex edits)

## Solution 2 (similar to solution 1 but with quadratic formula)

We first find the general roots for quadratics in the form $kx^2-4x-3$. Using the quadratic formula we have Since we are asked to add the reciprocals of all $4050$ roots in the harmonic mean, we will first add the general roots in terms of $k$. We have, Thus, each pair of roots add up to $-\frac{4}{3}$, and since there are $2025$ pairs of roots, the harmonic mean of the desired expression is

~evanhliu2009

## Solution 3 (Vieta's only)

We are asked to find $\frac{4050}{\sum_{i=1}^{4050}\frac{1}{i_1}}$. By Vieta's, note that $r_1 \cdot r_2 \dots r_{4050} = -\frac{3^{2025}}{2025!} = k$ ($k$ is a constant). Then, note that we are asked to find $\frac{4050}{\sum_{i=1}^n \frac{\frac{k}{r_i}}{k}}$, and by Vieta's we get that $\sum_{i=1}^n \frac{k}{r_i} = \frac{2025 \cdot 4 \cdot 3^{2024}}{2025!}$, so substituting this in, we get \[-\frac{4050}{\frac{\frac{2025 \cdot 4 \cdot 3^{2024}}{2025!}}{\frac{3^{2025}}{2025!}}} = -\frac{4050 \cdot 3^{2025}}{4050 \cdot 3^{2024} \cdot 2} = \boxed{-\frac{3}{2}}\].

~ScoutViolet

## Solution 4 (Vieta's Formulas)

We have: \[\prod_{k = 1}^{2025} (kx^{2} - 4x - 3) = (x^{2} - 4x - 3)(2x^{2} - 4x - 3)(3x^{2} - 4x - 3) \cdots (2025x^{2} - 4x - 3)\]

So we can analyze each part of this "snake":

According to Vieta's Formulas:

For the first one: $x^{2} - 4x - 3$: We have: \[\begin{cases}  x_1+x_2=\tfrac{4}{1}\\ x_1x_2=-\tfrac{3}{1} \end{cases}\] So we have: \[\dfrac{1}{x_1}+\dfrac{1}{x_2}=\dfrac{x_1+x_2}{x_1x_2}=-\dfrac{4}{3}\]

For the second one: $2x^{2} - 4x - 3$: We have: \[\begin{cases}  x_3+x_4=\tfrac{4}{2}\\ x_3x_4=-\tfrac{3}{2} \end{cases}\] So we have: \[\dfrac{1}{x_3}+\dfrac{1}{x_4}=\dfrac{x_3+x_4}{x_3x_4}=-\dfrac{4}{3}\]

For the third one: $3x^{2} - 4x - 3$: We have: \[\begin{cases}  x_5+x_6=\tfrac{4}{3}\\ x_5x_6=-\tfrac{3}{3} \end{cases}\] So we have: \[\dfrac{1}{x_5}+\dfrac{1}{x_6}=\dfrac{x_5+x_6}{x_5x_6}=-\dfrac{4}{3}\]

......

Then we should check the last one. For the 2025th. one: $2025x^{2} - 4x - 3$: We have: \[\begin{cases}  x_{4049}+x_{4050}=\tfrac{4}{2025}\\ x_{4049}x_{4050}=-\tfrac{3}{2025} \end{cases}\] So we have: \[\dfrac{1}{x_{4049}}+\dfrac{1}{x_{4050}}=\dfrac{x_{4049}+x_{4050}}{x_{4049}x_{4050}}=-\dfrac{4}{3}\]\begin{align*} \therefore H.M.&=\dfrac{1}{\dfrac{1}{4050}\sum_{i=1}^{4050}\dfrac{1}{x_i}}\\ &=\dfrac{4050}{2025\times\left(-\dfrac{4}{3}\right)}\\ &=-\dfrac{3}{2} \end{align*} Therefore, the final answer is $\color{red}\boxed{\color{black}-\dfrac{3}{2}}\color{black}$.

~funkCCP

## Solution 5 (Vietas Formulas)

For a general quadratic polynomial $ax^2 + bx + c = 0$ with roots $p$ and $q$, the sum of the reciprocals is: Using Vieta's formulas ($p+q = -\frac{b}{a}$ and $pq = \frac{c}{a}$): This result demonstrates that the sum of the reciprocals depends only on the coefficients $b$ and $c$, and is independent of the leading coefficient $a$. Since the overall polynomial is a product of quadratics, and all these quadratics share the same $b$ and $c$ coefficients, the sum of the reciprocals for the roots of every individual quadratic is the same. We use the coefficients from one of the quadratics, which is $ax^2 - 4x - 3 = 0$. Thus, $b=-4$ and $c=-3$.

\[\sum (\text{reciprocals}) = -\frac{b}{c} = -\frac{(-4)}{(-3)} = -\frac{4}{3}\]

We substitute the calculated sum of the reciprocals into the formula for the harmonic mean of 2 numbers:

\[\text{HM} = \frac{2}{-\frac{4}{3}} = 2 \times \left(-\frac{3}{4}\right) = -\frac{6}{4} = -\frac{3}{2}\]

The harmonic mean of the roots of any single quadratic is $-\frac{3}{2}$. Since the sum of the reciprocals is the same for all quadratics, the harmonic mean of all the roots of the overall polynomial is also $\boxed{\textbf{(B) }\dfrac{-3}{2}}$.

~Voidling

~small type fix by i_am_not_suk_at_math (saharshdevaraju 13:39, 8 November 2025 (EST)saharshdevaraju)

## Note

It is important to note that the question asks for the sum of all _real_ roots. We must therefore be careful to make sure that the $4050$ roots of the polynomial are all real, and also that they are distinct, as otherwise e.g. double roots would be counted twice, when the problem requires us to only count each root once (i.e. regardless of multiplicity). Accordingly, we compute that each quadratic factor $\left(kx^2-4x-3\right)$ (for $1 \leq k \leq 2025$) has discriminant $(-4)^2-4 \cdot k \cdot (-3) = 16+12k$, which is clearly positive as $k \geq 1$. This means the $2$ roots of each quadratic factor are indeed real and distinct (i.e. none of these quadratics has a double root), so it only remains to show that these roots are also distinct from those of all the _other_ quadratic factors. Hence, if we assume that $a$ is a common root of $2$ different quadratic factors simultaneously, say $\left(px^2-4x-3\right)$ and $\left(qx^2-4x-3\right)$ with $1 \leq p,q \leq 2025$ and $p \neq q$, then we must have $pa^2-4a-3=qa^2-4a-3=0$, which implies $pa^2 = qa^2$. This equation factorises as $(p-q)a^2 = 0$, and because $p \neq q$, i.e. $p-q \neq 0$, it further reduces to simply $a^2 = 0$, and hence $a = 0$. But then it follows that $pa^2-4a-3 = p \cdot 0^2 - 4 \cdot 0 - 3 = -3 \neq 0$, yielding a contradiction, so $a$ cannot in fact have been a common root of $2$ different quadratic factors, and thus we finally deduce that all $4050$ roots are distinct, as required. ~ Shadowleafy

## Solution 6

Let the polynomial be $f(x),$ and denote the $4050$ roots to be $x_1,x_2,...,x_{4050}.$ Hence, \[HM = \dfrac{4050}{\frac{1}{x_1}+\frac{1}{x_2}+...\frac{1}{x_{4050}}}.\] We can multiply the numerator and denominator of this fraction by $x_1x_2...x_{4050}$ to create symmetric sums, which yields \[HM = \dfrac{4050(x_1x_2...x_{4050})}{x_2x_3...x_{4050}+x_1x_3...x_{4050}+...+x_1x_2...x_{4049}}.\]

By Vieta's Formulas, since $f(x)$ is of even degree, the product of its roots, $x_1x_2...x_{4050},$ is just the constant term of $f(x),$ call it $c_0.$ Likewise, the denominator of our harmonic mean, $x_2x_3...x_{4050}+x_1x_3...x_{4050}+...+x_1x_2...x_{4049},$ is the negated coefficient of $x$ in the standard form of $f(x).$ Let the coefficient of $x$ in the standard form of $f(x)$ be $c_1.$ Note that we do not have to worry about dividing by the coefficient of $x^{4050}$ when using Vieta's Formulas, as they will eventually cancel out in our harmonic mean calculations.

So, \[HM = \dfrac{4050c_0}{-c_1}.\]

The constant term in $f(x)$ is just $c_0=(-3)^{2025}.$ For the coefficient of the $x$ term in $f(x),$ there are $\dbinom{2025}{2024}=2025$ ways to choose $2024$ of the trinomials to include a $-3,$ and the one trinomial not chosen will include a $-4x.$ Hence, $c_1=2025\cdot (-3)^{2024}\cdot (-4).$

Finally, \[HM=\dfrac{4050\cdot(-3)^{2025}}{-2025\cdot (-3)^{2024}\cdot (-4)}=\dfrac{2\cdot(-3)}{-(-4)}=\boxed{\text{(B) }-\dfrac{3}{2}}.\]

~Tacos_are_yummy_1

## Solution 7 (Cheese 🧀)

We can try replacing the $2025$ in the problem with smaller numbers like $1$ and $2$. For $1$, we have the quadratic $x^2-4x-3$. Using the quadratic formula, we have the roots are $2+\sqrt{7}$ and $2-\sqrt{7}$ The harmonic mean of these two is \[\frac{2}{\frac{1}{2+\sqrt{7}} + \frac{1}{2-\sqrt{7}}}=\frac{2}{\frac{\sqrt{7}-2}{3}+\frac{2+\sqrt{7}}{-3}}=\frac{2}{\frac{-4}{3}}=-\frac{3}{2}\].

We notice that this is one of the answer choices. Also, given that the random choice of $2025$, and that the rest of the answer choices are also simple fractions, we can safely guess that the answer is $\boxed{\textbf{(B)}~-\frac{3}{2}}$

~andliu766

## Solution 8 (Symmetry of Unweighted Means)

Note that all the roots are real since for each quadratic, \[\Delta=b^2-4ac=(-4)^2-4k(-3)=16+12k>0\] for $k\ge 1$. We will use the fundamental theorem of symmetric polynomials. By Vieta's formulas, we have for each quadratic $ax^2+bx+c=kx^2-4x-3$: \[\frac{1}{r}+\frac{1}{s}=\frac{r+s}{rs}=\frac{-b/a}{c/a}=-\frac{b}{c}=-\frac{4}{3}\] Thus, $\mathrm{HM}(r,s)=\frac{2}{\frac{1}{r}+\frac{1}{s}}=\frac{2}{-\frac{4}{3}}=-\frac{3}{2}$. Since the unweighted harmonic mean is symmetric in its arguments, we can group terms to get \[\mathrm{HM}(r_{1},r_{2},r_{3},\dots,r_{4050})=\mathrm{HM}\bigg(\mathrm{HM}(r_{1},r_{2}),\mathrm{HM}(r_{3},r_{4}),\dots,\mathrm{HM(r_{4049},r_{4050})}\bigg)=\boxed{\textbf{(B)}~-\frac{3}{2}}\]

Note: For an unweighted symmetric mean $M$, we have for $d|n$, $\mathrm{M}\{ x_{k} \}_{k=1}^{n}=\mathrm{M}\{ \mathrm{M}\{ x_{ds+k} \}_{k=1}^{d} \}_{s=0}^{n/d-1}$ and $\mathrm{M}\{ \bar{x} \}_{k}=\bar{x}$ for constant mean $\bar{x}$. You can also check this individually for HM: \[\mathrm{HM}(x_{1},\dots,x_{n})=n(x_{1}^{-1}+\cdots+x_{n}^{-1})^{-1}=\frac{n}{d}\left[ \underbrace{ d\left(x_{1}^{-1}+\cdots+x_{d}^{-1}\right)+\cdots+d\left(x_{(n-1)d+1}^{-1}+\cdots+x_{n}^{-1}\right) }_{ \frac{n}{d}\text{ terms} } \right]\] or by checking arithmetic mean and using $\mathrm{HM}\{ x_{k} \}_{k}=\frac{1}{\mathrm{AM}\left\{ \frac{1}{x_{k}} \right\}_{k}}$.

~imosilver

## Solution 9 (Easy-ish to understand)

Note: I will try my best to make this solution look less intimidating to read as the other ones. This is my third time writing a solution, so I'm not very used to the $\LaTeX$.

The harmonic mean that the question is asking is \[\frac{1}{\frac{r_1+r_2+...r_{4049}+r_{4050}}{4050}}\] where $r_i$ is between $1$ and $4050$ and is the reciprocal of all $4050$ roots of the polynomial. All we need to find is the sum of the reciprocals of the roots and we can substitute that into this formula.

First of all, notice that there are $2025$ quadratic polynomials. They each hold $2$ out of the $4050$ roots, and the sum of the reciprocals of their roots are $\frac{1}{a} + \frac{1}{b} = \frac{a+b}{ab}.$

Using Vieta's we get $\frac{a+b}{ab}=-\frac{4}{3}$ on the every quadratic because only the coefficient for $x^2$ changes. Also, $a+b$ and $ab$ have the denominator of $a$, so when they are divided, the quotient won't change. Therefore, the sums of the reciprocals of the quadratics sum to $2025 \cdot \frac{-4}{3}$.

Now we can substitute: \[\frac{1}{\frac{2025 \cdot \frac{-4}{3}}{4050}}.\] This gets us

Or...you could just solve the last part yourself easier than my solution!

~slamgirls

## Solution 10 (reciprocal roots)

We know that if for polynomial $ax^2 + bx + c$ is $r_1$ and $r_2$, then the polynomial with roots $\frac{1}{r_1}$ and $\frac{1}{r_2}$ (reciprocal roots) will be $cx^2 + bx + a$ where the coefficients are flipped (works for any degree polynomial, not just quadratic). Thus, using vieta's formula, the sum of the reciprocal roots for polynomial $kx^2 - 4x - 3$ will be the sum of the roots for polynomial $-3x^2 - 4x + k$ which is $- \frac{-4}{-3}=- \frac{4}{3}$.

There are $2025$ polynomials like this, so the sum of roots would be $2025\cdot (- \frac{4}{3})$. Finding the harmonic mean, we get:

\[\frac{1}{\frac{1}{4050} \cdot \frac{-4\cdot 2025}{3}} = \frac{1}{\frac{-2}{3}}\]

Or $\boxed{\textbf{(B) }-\frac{3}{2}}$

~tebby

## See Also

**[2025 AMC 10A](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A "2025 AMC 10A")** (**[Problems](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems "2025 AMC 10A Problems")** • **[Answer Key](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Answer_Key "2025 AMC 10A Answer Key")** • [Resources](https://artofproblemsolving.com/community/c13))
Preceded by

**[Problem 17](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_17 "2025 AMC 10A Problems/Problem 17")**Followed by

**[Problem 19](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_19 "2025 AMC 10A Problems/Problem 19")**
[1](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_1 "2025 AMC 10A Problems/Problem 1")**•**[2](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_2 "2025 AMC 10A Problems/Problem 2")**•**[3](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_3 "2025 AMC 10A Problems/Problem 3")**•**[4](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_4 "2025 AMC 10A Problems/Problem 4")**•**[5](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_5 "2025 AMC 10A Problems/Problem 5")**•**[6](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_6 "2025 AMC 10A Problems/Problem 6")**•**[7](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_7 "2025 AMC 10A Problems/Problem 7")**•**[8](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_8 "2025 AMC 10A Problems/Problem 8")**•**[9](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_9 "2025 AMC 10A Problems/Problem 9")**•**[10](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_10 "2025 AMC 10A Problems/Problem 10")**•**[11](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_11 "2025 AMC 10A Problems/Problem 11")**•**[12](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_12 "2025 AMC 10A Problems/Problem 12")**•**[13](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_13 "2025 AMC 10A Problems/Problem 13")**•**[14](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_14 "2025 AMC 10A Problems/Problem 14")**•**[15](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_15 "2025 AMC 10A Problems/Problem 15")**•**[16](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_16 "2025 AMC 10A Problems/Problem 16")**•**[17](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_17 "2025 AMC 10A Problems/Problem 17")**•**[18](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_18 "2025 AMC 10A Problems/Problem 18")**•**[19](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_19 "2025 AMC 10A Problems/Problem 19")**•**[20](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_20 "2025 AMC 10A Problems/Problem 20")**•**[21](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_21 "2025 AMC 10A Problems/Problem 21")**•**[22](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_22 "2025 AMC 10A Problems/Problem 22")**•**[23](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_23 "2025 AMC 10A Problems/Problem 23")**•**[24](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_24 "2025 AMC 10A Problems/Problem 24")**•**[25](https://artofproblemsolving.com/wiki/index.php?title=2025_AMC_10A_Problems/Problem_25 "2025 AMC 10A Problems/Problem 25")
**[All AMC 10 Problems and Solutions](https://artofproblemsolving.com/wiki/index.php?title=AMC_10_Problems_and_Solutions "AMC 10 Problems and Solutions")**

[](https://artofproblemsolving.com/wiki/index.php?title=File:AMC_Logo.png)
