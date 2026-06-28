## Problem

Let $a$, $b$, and $c$ be the roots of the polynomial $x^3 + kx + 1$. What is the sum\[a^3b^2 + a^2b^3 + b^3c^2 + b^2c^3 + c^3a^2 + c^2a^3?\]$\textbf{(A)}~-k\qquad\textbf{(B)}~-k+1\qquad\textbf{(C)}~1\qquad\textbf{(D)}~k-1\qquad\textbf{(E)}~k$

## Solution 1

We begin by factoring:

From Vieta's Formulas, we know that $a+b+c = 0$, $ab+bc+ca = k$, and $abc = -1$. Therefore, the answer equals $(a^2b^2+b^2c^2+c^2a^2)(0) - (-1)(k) = \boxed{k}.$

~lprado

## Solution 2

Notice that this is $\sum_{\text{cyc}} a^2b^2(a+b)$. By Vieta's (just like in solution 1), we have $a+b+c=0$, so $a+b=-c$, $abc=-1$, and $ab+bc+ac=k$, so this is equivalent to $\sum_{\text{cyc}} -a^2b^2c = \sum_{\text{cyc}} -(abc)(ab) = \sum_{\text{cyc}} ab = k$ by Vieta's. ~ScoutViolet

## Solution 3 (BS)

Let’s just pick a nice and convenient a, b, c. Observe that $2\cdot2^{-\frac13}-2^\frac23=0$, so we can just have $(a,b,c)=(2^{-\frac13}, 2^{-\frac13},-2^\frac23$). So expanding $(x-a)(x-b)(x-c)$ we get $x^3-3\cdot2^{-\frac23}+1$. Evaluating $a^3b^2 + a^2b^3 + b^3c^2 + b^2c^3 + c^3a^2 + c^2a^3$, or $2a^5+2a^2c^3+2a^3c^2$, we get $-3\cdot2^{-\frac23}=k$, so the answer is $\boxed{\textit{E}}$. (i did this on the actual test)

~benjamintontungtungtungsahur

who is going to think of this on the test bro 😭😭 and change ur username dawg 🥀🥀

this solution is acc so fire leave him alone

yo lowk it's acc so fire that the entire tung tung tung sahor family agreed (they told me) and EVERYONE is going to think of this on the test (because, y'know, I totally didn't factor then use Vieta in a few secs *cough *cough) and his username is tuff idk what the first guy was on abt

## Solution 4 (Vieta's)

First, note that $a+b+c=0$, $\sum_{cyc} ab = k$, $abc=-1$. We can factor the original expression into:

\[\sum_{cyc} a^2b^2(a+b) = \sum_{cyc} \left(-\frac{1}{c}\right)^2(-c) = -\frac{\sum_{cyc} ab}{abc} = \boxed{\text{(E) } k.}\]

~ABC09090927

## Solution 5 (Newton's Sums) (If you suck at factoring like me)

Note that $a^3b^2+a^2b^3+b^3c^2+b^2c^3+c^3a^2+c^2a^3 = (a^3+b^3+c^3)(a^2+b^2+c^2)-(a^5+b^5+c^5)$

By Newton's sums, we have: \[(a^3 + b^3 + c^3) + k(a+b+c) + 3 = 0\]\[(a^5 + b^5 + c^5) + k(a^3+b^3+c^3) + 1(a^2+b^2+c^2) = 0\]

Note that $a^2+b^2+c^2 = (a+b+c)^2 - 2(ab+bc+ca)$

From Vieta's formulas, we have $a+b+c = 0$ and $ab + bc + ca = k$

Solving, we get: \[(a^3 + b^3 + c^3) = -3\]\[(a^2 + b^2 + c^2) = -2k\]\[(a^5 + b^5 + c^5) - 3k - 2k = 0 \to (a^5 + b^5 + c^5) = 5k\]

Therefore, $a^3b^2+a^2b^3+b^3c^2+b^2c^3+c^3a^2+c^2a^3 = (-3)(-2k)-5k = \boxed{\textbf{(E) }k}$

~ku220

## Solution 6

Like in solution 1, we begin by factoring:

From Vieta's Formulas, we know that $a+b+c = 0$, $ab+bc+ca = k$, and $abc = -1$.

square $a+b+c = 0$ to get $a^2 + b^2 + c^2 = 0$, then isolating one variable each time yields:

Isolating a + b + c = 0, you get

This simplifies to:

Therefore, the answer equals = $\boxed{k}.$

~BOTNATE

## Solution 7 (Vieta + Factorization)

We can easily factor the expression into \[a^2b^2(a+b)+b^2c^2(b+c)+a^2c^2(a+c)\]

By Vieta, we get $a+b+c=0$, so we can rewrite the expression into $a^2b^2(-c)+b^2c^2(-a)+a^2c^2(-b)$ which is just $-abc(ab+bc+ac)$. By Vieta we also get $abc=-1$ and $ab+bc+ac=k$. Therefore the expression is just $-(-1)k=$$\boxed{k}.$

~backtosq-1

## Solution 8 (no Vieta + not quite factoring)

Let the expression we are asked to evaluate equal $y$.

We have that $x^3+kx+1=(x-a)(x-b)(x-c)$. Expanding the right hand side yields $x^3-x^2(a+b+c)+x(ac+bc+ab)-abc$. Equating coefficients, $a+b+c=0$, $ac+bc+ab=k$, and $abc=-1$.

We may find the first equation helpful for cancelling things out, so let us fiddle around with it, trying to piece out as much of $y$ as possible: we discover that $(a+b+c)(ab)^2=a^3b^2+a^2b^3+c(ab)^2=0$, which shares terms with $y$. Likewise, $(a+b+c)(bc)^2=b^3c^2+b^2c^3+a(bc)^2=0$ and $(a+b+c)(ac)^2=a^3c^2+a^2c^3+b(ac)^2=0$.

Adding the three equations gives $y+a(bc)^2+b(ac)^2+c(ab)^2=0.$ Observe that $a(bc)^2+b(ac)^2+c(ab)^2=(abc)(ac+bc+ab)=-1(k)$. Thus $y-k=0$; $y=\boxed{k}$.

~iluminate

## See Also

*   [AMC 12](https://artofproblemsolving.com/wiki/index.php?title=AMC_12 "AMC 12")
*   [AMC 12 Problems and Solutions](https://artofproblemsolving.com/wiki/index.php?title=AMC_12_Problems_and_Solutions "AMC 12 Problems and Solutions")
*   [Mathematics competitions](https://artofproblemsolving.com/wiki/index.php?title=Mathematics_competitions "Mathematics competitions")
*   [Mathematics competition resources](https://artofproblemsolving.com/wiki/index.php?title=Mathematics_competition_resources "Mathematics competition resources")

[](https://artofproblemsolving.com/wiki/index.php?title=File:AMC_Logo.png)
