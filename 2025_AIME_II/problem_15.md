## Problem

There are exactly three positive real numbers $k$ such that the function \[f(x)=\frac{(x-18)(x-72)(x-98)(x-k)}{x}.\] defined over the positive real numbers achieves its minimum value at exactly two positive real numbers $x$. Find the sum of these three values of $k$.

## Solution 1 ('clunky', trial and error)

Let $n$ be the minimum value of the expression (changes based on the value of $k$, however is a constant). Therefore, we can say that This can be done because $n$ is a constant, and for the equation to be true for all $x$, the right side is also a quartic. The roots must also both be double, or else there is an even smaller value, a contradiction.

We expand as follows, comparing coefficients:

Recall $(\alpha+\beta)^2+2\alpha \beta=\alpha^2+4\alpha \beta +\beta^2$, so we can equate and evaluate as follows:

We now have a quartic with respect to $\sqrt{k}$. Keeping in mind it is much easier to guess the roots of a polynomial with integer coefficients, we set $a=\frac{k}{8}$. Now our equation becomes

We can test for easy roots and find $\sqrt{a}=1$ and $2$. After this, solving the resulting quadratic gets you the remaining roots as $5$ and $-8$. Discard $-8$. Working back through our substitution for $a$, we have generated values of $k$ as $(8, 32, 200)$.

The sum of all $k$ then must be $8+32+200=\boxed{240}$.

~ [lisztepos](https://artofproblemsolving.com/wiki/index.php/User:Lisztepos)

~ Edited by [aoum](https://artofproblemsolving.com/wiki/index.php/User:Aoum)

Note: I'm not sure what the first author meant by, "or else there is an even more 'minimum' value." The most noticeable reason there are two double roots is that there are two distinct positive solutions per the conditions of the problem

~ fermat_sLastAMC

Further notes (from the author): To clarify why the equation takes the form above, if you do not regard the context of the problem, you could say that $\frac{(x-\alpha)^3(x-\beta)}{x}$ is another form, also having two roots. However when we consider this form, (WLOG assuming $\alpha < \beta$) if we take a value such that $\alpha < x < \beta$, then $x-\beta < 0$, therefore implying that $\frac{(x-\alpha)^3(x-\beta)}{x}<0$ or otherwise resulting $f(x)<n$, which is contradiction as we assumed $n$ is the least value of the function. Similarly, logic proceeds if the third power is on the other binomial.

## Solution 2 (AM-GM)

Consider the function Expanding this, we obtain

Let (where ). By the AM-GM inequality , we have Assuming , the minimum value is .

Let . Then,

when We obtain

Let .

When ,We obtain .

Since , we have which yields or .

With the same method, consider the function When , When , Thus, gives , and the minimum value corresponds to or .

In summary, , , and , with their sum being $8+32+200=\boxed{240}$.

~ Edited by dongjiu0728

Comment: The function $f$ in the solution is different (the denominator $x$ is replaced with $x^2$). So this is another problem. Another issue is that, even if both $y_1$ and $y_2$ assume their minimal value (-18), their product is positive, not necessarily a minimum. Also, there is a problem that the person assumed multiple values of $x$ at the multiplicative of the function and yet assumed it to be a single variable function.

-J.Z.

## Solution 3 (elegant polynomial)

We first do the same thing as Solution 1 did, but in mathematical language.

Lemma: for Polynomial $P(x)$, if $P(x_0) = 0$ and $P'(x_0) = 0$ both hold, then $x_0$ is a multiple root of $P(x)$.

This lemma is obvious since every root of $P(x)$ occurs $\deg P - 1$ times in the derivative polynomial and any single root of $P(x)$ can't be a root of $P'(x)$.

Simply name m as the minimum value of $f(x)$.

Then $f(x) \geq m$ and the equal sign holds if and only of $x=x_1$ or $x=x_2$.

Define $P(x)=(x-18)(x-72)(x-98)(x-k)-mx$. Obviously, $x_1$ and $x_2$ satisfy the two properties in the lemma. So we've got: \[(x-18)(x-72)(x-98)(x-k)-mx = (x-x_1)^2(x-x_2)^2\] Take $x=18, 72, 98, k$, we get: \[(18-x_1)(18-x_2)= \pm\sqrt{-m}\sqrt{18}\] and so on. So we can construct $Q(t)=(t^2-x_1)(t^2-x_2)-\sqrt{-m}t$. As what we have seen, $\pm\sqrt{18}, \pm\sqrt{72}, \pm\sqrt{98}, \pm\sqrt{k}$ are four roots of $Q(t) = 0$. So we've got: \[Q(t)=(t^2-x_1)(t^2-x_2)-\sqrt{-m}t=(t\pm\sqrt{18})(t\pm\sqrt{72})(t\pm\sqrt{98})(t\pm\sqrt{k})\] Comparing the cubic coefficient: \[\pm\sqrt{18}\pm\sqrt{72}\pm\sqrt{98}\pm\sqrt{k}=0\] So \[k=(\pm\sqrt{18}\pm\sqrt{72}\pm\sqrt{98})^2\] Now $8, 32, 200, 512$ are accesible in this form. The final task is to eliminate $512$. In this occasion the four roots are either $\sqrt{18}, \sqrt{72}, \sqrt{98}, -\sqrt{512}$ or $-\sqrt{18}, -\sqrt{72}, -\sqrt{98}, \sqrt{512}$. In either way the constant coefficient of $Q(t)$ is \[x_1x_2 = -\sqrt{18}\sqrt{72}\sqrt{98}\sqrt{512}\] But, $x_1$ and $x_2$ are both positive, so we end up with contradiction.

$8+32+200=\boxed{240}$

~ Edited by ThomasZZW

## Solution 4

What this problem is asking is to choose $k$ for which there exists a real $c$ with the property that \[\frac{(x-18)(x-72)(x-98)(x-k)}{x}=c\] at exactly two positive reals $x$. Specifically, $c$ is the minimum value of the expression for positive reals $x$. This rewrites into $(x-18)(x-72)(x-98)(x-k)-cx=0$ having two roots. Because it is a quartic, then it is either the square of a quadratic or the product of a cubic and a linear. However, for the latter case, note that this essentially contradicts our minimality assumption. Therefore, it needs to be the square of a quadratic. We can write that squared quadratic as $x^2-mx+n$. We would then have the equation \[(x-18)(x-72)(x-98)(x-k)-cx=\left (x^2-mx+n\right )^2.\]

Firstly, compare the coefficients of $x^3$. In the left equation, we can see by vietas that the term is $-(k+188)x^3$, while in the right equation this is $-2mx^3$. We then obtain the relationship $2mx^3=(k+188)x^3\implies k=2m-188$. So it is equivalent to finding the values of $m$ that work. Next, we can start plugging in convenient values for $x$. For $x=18$, we find that $-18c=(324-18m+n)^2$. If we plug in $x=72$, we also get $-72c=(5184-72m+n)^2$. Similarly, $x=98$ gets us $-98c=(9604-98m+n)^2$. Notice how we have three variables in a three-way systems of equations, so it can be solved. Dividing the second equation by the first equation, we get a new equation \[\frac{-72c}{-18c}=\frac{(5184-72m+n)^2}{(324-18m+n)^2},\] which simplifies to \[4=\left (\frac{5184-72m+n}{324-18m+n}\right )^2.\] Taking the square root of both sides and doing a little rearranging, it simplifies into $5184-72m+n=\pm 2(324-18m+n)$. Proceeding similarly, we can divide the third equation by the first equation to get \[\frac{-98c}{-18c}=\frac{(9604-98m+n)^2}{(324-18m+n)^2}\implies \frac{49}{9}=\left (\frac{9604-98m+n}{324-18m+n}\right )^2\implies 3(9604-98m+n)=\pm 7(324-18m+n).\]

At this point, we have now simplified it slightly down into two variables and two equations. We need both equations to be true, although the plus and the minus cases for each equation aren't necessarily both true at the same time. For convenience, let us call the four equations \[5184-72m+n=2(324-18m+n),\]\[5184-72m+n=-2(324-18m+n),\]\[3(9604-98m+n)=7(324-18m+n), \text{ and}\]\[3(9604-98m+n)=-7(324-18m+n)\] as equations 1, 2, 3, and 4, respectively.

To make things simpler, we can simplify each equation down.

In equation 1, we have $5184-72m+n=648-36m+2n$, so $36m+n=4536$.

In equation 2, we have $5184-72m+n=-648+36m-2n$, so $108m-3n=5832\implies 36m-n=1944$.

In equation 3, $28812-294m+3n=2268-126m+7n$, so $168m+4n=26544\implies 42m+n=6636$.

Then in equation 4, $28812-294m+3n=-2268+126m-7n$, so $420m-10n=31080\implies 42m-n=3108$.

Now, recall our earlier condition how both of those equations with the $\pm$ must be true. Then we have four cases of which are true: Equations 1 and 3, 1 and 4, 2 and 3, and 2 and 4.

Case 1: Equations 1 and 3 are true

We then have $36m+n=4536$ and $42m+n=6636$. Subtracting the equations gives $6m=2100\implies m=350$. However, it is obvious that $n$ is negative. But then this would force that one of the roots in the quadratic $x^2-mx+n$ are negative, which contradicts our initial assumption that it occurs in the positive reals $x$. This case doesn't provide any solutions.

Case 2: Equations 1 and 4 are true

It requires $36m+n=4536$ and $42m-n=3108$. Adding the two equations gives $78m=7644\implies m=98$. Then $n$ is positive, so this case does indeed work. Applying the relationship $k=2m-188$ from earlier gives $k=8$ as a possibility.

Case 3: Equations 2 and 3 are true

Then $36m-n=1944$ and $42m+n=6636$. Adding the two equations, $78m=8580\implies m=110$. $n$ is indeed positive, so this case provides $k=2\cdot 110-188=32$.

Case 4: Equations 2 and 4 are true

The two equations are $36m-n=1944$ and $42m-n=3108$. Subtracting the first from the second, we see that $6m=1164\implies m=194$. We find that $n$ is also positive here, so it works. Then it can be easily found that $k=2\cdot 194-188=200$.

Therefore, our possible values of $k$ are $k=8,32,200$, so the answer is $\boxed{240}$.

~ethanzhang1001
