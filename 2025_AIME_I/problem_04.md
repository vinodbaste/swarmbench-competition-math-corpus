## Problem

Find the number of ordered pairs $(x,y)$, where both $x$ and $y$ are integers between $-100$ and $100$ inclusive, such that $12x^2-xy-6y^2=0$.

## Solution 1

We begin by factoring, $12x^2-xy-6y^2=(3x+2y)(4x-3y)=0.$ Since the RHS is $0$ we have two options,

$\underline{\text{Case 1:}}\text{ } 3x+2y = 0$

In this case we have, $y=\frac{-3x}{2}.$ Using the bounding on $y$ we have, \[-100\le\frac{-3x}{2}\le 100.\]\[\frac{200}{3}\ge x \ge \frac{-200}{3}.\] In addition in order for $y$ to be integer $2 | x,$ so we substitute $x=2k.$\[\frac{200}{3}\ge 2k \ge \frac{-200}{3}.\]\[\frac{100}{3}\ge k \ge \frac{-100}{3}.\] From this we have solutions starting from $-33$ to $33$ which is $67$ solutions.

$\underline{\text{Case 2: }}\text{ } 4x-3y = 0$

On the other hand, we have, $y=\frac{4x}{3}.$ From bounds we have, \[-100\le\frac{4x}{3}\le 100.\]\[-75 \le x \le 75.\] In this case, for $y$ to be integer $3 | x,$ so we substitute $x=3t.$\[-75 \le 3t \le 75.\]\[-25 \le t \le 25.\] This gives us $51$ solutions.

Finally we overcount one case which is the intersection of the $2$ lines (which are $y=\frac{-3x}{2}$ and $y=\frac{4x}{3}$) or the point $(0,0).$ Therefore our answer is $67+51-1=\boxed{117}$

~[mathkiddus](https://artofproblemsolving.com/wiki/index.php?title=User:Mathkiddus "User:Mathkiddus")

## Solution 2

First, notice that $(0,0)$ is a solution.

Divide the equation by $y^2$, getting $12(\frac{x}{y})^2-\frac{x}{y}-6 = 0$. (We can ignore the $y=0$ case for now.) Let $a = \frac{x}{y}$. We now have $12a^2-a-6=0$. Factoring, we get $(4a-3)(3a+2) = 0$. Therefore, the graph is satisfied when $4a=3$ or $3a=-2$. Substituting $\frac{x}{y} = a$ back into the equations, we get $4x=3y$ or $3x=-2y$.

Remember that both $x$ and $y$ are bounded by $-100$ and $100$, inclusive. For $4x=3y$, the solutions are $(-75,-100), (-72,-96), (-69, -92), \dots, (72,96), (75,100)$. Remember to not count the $x=y=0$ case for now. There are $25$ positive solutions and $25$ negative solutions for a total of $50$.

For $3x-2y$, we do something similar. The solutions are $(-66,99), (-64,96), \dots, (64, -96), (66, -99)$. There are $33$ solutions when $x$ is positive and $33$ solutions when $x$ is negative, for a total of $66$.

Now we can count the edge case of $(0,0)$. The answer is therefore $50+66+1 = \boxed{117}$.

P.S. This technique of dividing by y^2 and then substituting a variable for $\frac{x}{y}$ is called de-homogeneization. ~lprado

## Solution 3

You can use the quadratic formula for this equation: $12x^2 - xy - 6y^2 = 0$; Although this solution may seem to be misleading, it works! What we are doing is considering the quadratic with respect to $1$, where $12x^2$ is the coefficient of $1^2$, $-xy$ is the coefficient of $1$, and $-6y^2$ is the constant term.

You get: \[\frac{-b \pm \sqrt{b^2-4ac}}{2a}\]

\[\frac{xy \pm \sqrt{x^2 y^2 + (12\cdot6\cdot4\cdot x^2 \cdot y^2)}}{24x^2}\]

\[= \frac{xy \pm\sqrt{289x^2 y^2}}{24x^2}\]

\[= \frac{18xy}{24x^2}\text{, and }\frac{-16xy}{24x^2}\]

Rather than putting this equation as zero, the numerators and denominators must be equal [EDIT: We set each value equal to one because the quadratic is taken with respect to the root $1$]. These two equations simplify to:

\[3y = 4x;\]\[-2y = 3x;\]

As $x$ and $y$ are between $-100$ and $100$, for the first equation, $x$ can be from $[-75,75]$, but $x$ must be a multiple of $3$, so there are:

$((75+75)/3) + 1 = 51$ solutions for this case.

For \[-2y = 3x:\]

$x$ can be between $[-66, 66]$, but $x$ has to be a multiple of $2$.

Therefore, there are $(66+66)/2 + 1 = 67$ solutions for this case.

However, the one overlap would be $x = 0$, because y would be $0$ in both solutions.

Therefore, the answer is $51+67-1 = \boxed{117}.$

-U-King3.14Root -LaTeX corrected by Andrew2019 -clarified by golden_star_123
