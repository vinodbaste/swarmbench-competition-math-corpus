## Problem

What value of $x$ satisfies \[\frac{\log_2x \cdot \log_3x}{\log_2x+\log_3x}=2?\]

$\textbf{(A) } 25 \qquad\textbf{(B) } 32 \qquad\textbf{(C) } 36 \qquad\textbf{(D) } 42 \qquad\textbf{(E) } 48$

## Solution 1

We have so $\boxed{\textbf{(C) }36}$

~kafuu_chino

## Solution 2 (Change of Base)

~sourodeepdeb

## Solution 3 (Using Variables)

Let $a=\log_2x$ and $b=\log_3x$. This gives us the equation \[\frac{ab}{a+b}=2.\]

Then, from our definitions of $a$ and $b$, $2^a=x$ and $3^b=x$, so $2^a=3^b.$ Taking the logarithm base $3$ of both sides of this equation gives us $\log_3 2^a=b$, hence $a \log_3 2=b.$ Now, we substitute $a \log_3 2$ for $b$ in the equation, which gives \[\frac{a \cdot a \log_3 2}{a+a \log_3 2}=2.\]Notice that we can factor out an $a$ in the numerator and denominator, if $a \neq 0,$ and doing so yields \[\frac{a \log_3 2}{1+\log_3 2}=2.\] We know that $1= \log_3 3,$ so putting that in gives us \[\frac{a \log_3 2}{\log_3 3+\log_3 2}=2 \implies \frac{a \log_3 2}{\log_3 6}=2.\]So, $a=2 \cdot  \frac{\log_3 6}{\log_3 2}$, which, using the change of base formula, is equivalent to $2 \cdot \log_2 6,$ thus, \[a=2 \cdot \log_2 6= \log _2 6^2= \log _2 36.\] Finally, using our original definition of $a,$ we have \[a = \log_2 x=\log_2 36,\] so $x=\boxed{\textbf{(C) }36}.$

~hdanger

## Solution 4 (Educated Guess)

Prime factorize all the options to get

A) $5^2$

B) $2^5$

C) $2^2 3^2$

D) $2\cdot 3\cdot 7$

E) $2^4 3$

Since the LHS of the equation

\[\frac{\log_2x\cdot\log_3x}{\log_2x+\log_3x}=2\]

is symmetric in 2 and 3 we can guess that the answer has equal powers of 2 and 3 to get $\boxed{\textbf{(C) }36}.$. (Note: you can verify this quickly by changing all the logs base 3 to logs base 2 or vice versa) ~GoldemGem4848
