## Problem

Let $x,y$ and $z$ be positive real numbers that satisfy the following system of equations: \[\log_2\left({x \over yz}\right) = {1 \over 2}\]\[\log_2\left({y \over xz}\right) = {1 \over 3}\]\[\log_2\left({z \over xy}\right) = {1 \over 4}\] Then the value of $\left|\log_2(x^4y^3z^2)\right|$ is $\tfrac{m}{n}$ where $m$ and $n$ are relatively prime positive integers. Find $m+n$.

## Solution 1

First, let’s realize the rule that $\log{a}{b}=\log{a}+\log{b}$. If we add two equations at a time, and use this rule, we get:

$\log_2{\frac{1}{z^2}} = \frac{1}{2}+\frac{1}{3}= \frac{5}{6}$

$\log_2{\frac{1}{x^2}} = \frac{1}{3}+\frac{1}{4}= \frac{7}{12}$

$\log_2{\frac{1}{y^2}} = \frac{1}{2}+\frac{1}{4}= \frac{3}{4}$

Now we look into the rule $\log{\frac{b}{c}}=\log{b}-\log{c}$

We can convert the equations above and setting them variables to:

$a = \log_2{x^2}=\log_2{1}-\frac{7}{12}$

$b = \log_2{y^2}=\log_2{1}-\frac{3}{4}$

$c = \log_2{z^2}=\log_2{1}-\frac{5}{6}$

Then, using the first rule $a^2bc = 4(\log_2{1})-\frac{11}{4}$ Make sure you see why there is $a^2$! We are trying to get the absolute value equation.

We are still missing one $y$ in our $\log_2{x^4y^2z^2}$

How do we get this? We introduce yet another rule(I know, rules are annoying, but useful and easy to memorize once you derive them yourself), $\log{b^n}=n\log{b}$

Using this in our equation b = $\log_2{y^2}=\log_2{1}-\frac{3}{4}$, we get:

$2\log_2{y} = \log_2{1}-\frac{3}{4}$

Which gives:

$\log_2{y}=\frac{\log_2{1}}{2}-\frac{3}{8}$

Now, using the first rule again, we combine this with $\log_2{x^4y^2z^2}$ to get our desired equation! We yield:

$\log_2{x^4y^3z^2}$ = $\frac{9\log_2{1}}{2}-\frac{25}{8}$

Then, we feel sad because we don’t know what $\log_2{1}$ is. But then we realize, 2 to the power of 0 is 1! So we can just cancel out everything before the $-\frac{25}{8}$.

Therefore, $\log_2{x^4y^3z^2}$ is $-\frac{25}{8}$. After absolute value, it is just $\frac{25}{8}$. Summing $m$ and $n$, we obtain $\boxed{033}$

~MathKatana

## Solution 2

Denote $\log_2(x) = a$, $\log_2(y) = b$, and $\log_2(z) = c$.

Then, we have: $a-b-c = \frac{1}{2}$$-a+b-c = \frac{1}{3}$$-a-b+c = \frac{1}{4}$

Now, we can solve to get $a = \frac{-7}{24}, b = \frac{-3}{8}, c = \frac{-5}{12}$. Plugging these values in, we obtain $|4a + 3b + 2c|  = \frac{25}{8} \implies \boxed{033}$. ~akliu

## Solution 3

$\log_2(y/xz) + \log_2(z/xy) = \log_2(1/x^2) = -2\log_2(x) = \frac{7}{12}$

$\log_2(x/yz) + \log_2(z/xy) = \log_2(1/y^2) = -2\log_2(y) = \frac{3}{4}$

$\log_2(x/yz) + \log_2(y/xz) = \log_2(1/z^2) = -2\log_2(z) = \frac{5}{6}$

$\log_2(x) = -\frac{7}{24}$

$\log_2(y) = -\frac{3}{8}$

$\log_2(z) = -\frac{5}{12}$

$4\log_2(x) + 3\log_2(y) + 2\log_2(z) = -25/8$

$25 + 8 = \boxed{033}$

~Callisto531

## Solution 4

Adding all three equations, $\log_2(\frac{1}{xyz}) = \frac{1}{2}+\frac{1}{3}+\frac{1}{4} = \frac{13}{12}$. Subtracting this from every equation, we have: \[2\log_2x = -\frac{7}{12},\]\[2\log_2y = -\frac{3}{4},\]\[2\log_2z = -\frac{5}{6}\] Our desired quantity is the absolute value of $4\log_2x+3\log_2y+2\log_2z = 2(\frac{7}{12})+3/2(\frac{3}{4})+\frac{5}{6} = \frac{25}{8}$, so our answer is $25+8 = \boxed{033}$. ~Spoirvfimidf

## Solution 5 (using linear algebra)

You can think of the power of the powers of the expressions inside each logarithm as a vector. The goal is to find some linear combination of those vectors that output the vector $\begin{bmatrix} 4 \\ 3 \\ 2 \end{bmatrix}$. We can write this: \[c_1 \begin{bmatrix} 1 \\ -1 \\ -1 \end{bmatrix} + c_2 \begin{bmatrix} -1 \\ 1 \\ -1 \end{bmatrix} + c_3 \begin{bmatrix} -1 \\ -1 \\ 1 \end{bmatrix} = \begin{bmatrix} 4 \\ 3 \\ 2 \end{bmatrix}\] To solve this, we can use an augmented matrix and reduce it to reduced row-echelon form:

\[\begin{bmatrix} 1 & -1 & -1 & 4 \\ -1 & 1 & - 1 & 3 \\ -1 & -1 & 1 & 2 \end{bmatrix} \xrightarrow{RREF} \begin{bmatrix} 1 & 0 & 0 & -\frac{5}{2} \\ 0 & 1 & 0 & -3 \\ 0 & 0 & 1 & -\frac{7}{2} \end{bmatrix}\]

Notice that in the same way we wrote the initial linear combination, the solution we solved for above also works for the following linear combination:

\[c_1 \log_2{\left(\frac{x}{yz}\right)} + c_2 \log_2{\left( \frac{y}{xz} \right)} + c_3 \log_2{\left(\frac{z}{xy}\right)} = \log_2{\left(x^4y^3z^2\right)}\]

Therefore, using the given information, we have:

\[-\frac{5}{2} \log_2{\left(\frac{x}{yz}\right)} - 3 \log_2{\left( \frac{y}{xz} \right)} - \frac{7}{2} \log_2{\left(\frac{z}{xy}\right)} = -\frac{5}{2} \left(\frac{1}{2}\right) - 3 \left(\frac{1}{3}\right) - \frac{7}{2} \left( \frac{1}{4} \right) = -\frac{17}{8} - \frac{8}{8} = -\frac{25}{8} = \log_2{\left(x^4y^3z^2\right)}\]

Finally, $| \log_2{\left(x^4y^3z^2\right)} | = \frac{25}{8}$ and $25+8=\boxed{033}$

~AudaxGG

## Solution 6 (straightforward)

Using the rule $\log{a}{b}=\log{a}+\log{b}$ and $\log{a^b}=b\log{a}$, we turn the value we want into $|4\log_2{x}+3\log_2{y}+2\log_2{z}|$.

Then, according to the definition of logarithms, which is, $\log_a{b}=c$ implies $a^c=b$, we eliminate the logs for all three equations, move the denominator to the other side, then raise both sides to the same power to rearrange them nicely like this:

\[x^2=2y^2z^2\]\[y^3=2x^3z^3\]\[z^4=2x^4y^4\]

We then raise the first equation to the sixth power, the second one to the fourth, the third one to the third to bring them to a common power:

\[x^{12}=2^6y^{12}z^{12}\]\[y^{12}=2^4x^{12}z^{12}\]\[z^{12}=2^3x^{12}y^{12}\]

Then, we substitute the first equation to the second, first to the third, and second to the third to get:

\[x=2^{-\frac{7}{24}}\]\[y=2^{-\frac{9}{24}}\]\[z=2^{-\frac{10}{24}}\]

Therefore, the value we want is $|-\frac{28}{24}-\frac{27}{24}-\frac{20}{24}|=\frac{75}{24}=\frac{25}{8}$. So the answer is $25+8=\boxed{033}$.

~metrixgo
