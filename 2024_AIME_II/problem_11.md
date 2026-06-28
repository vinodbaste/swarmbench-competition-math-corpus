## Problem

Find the number of triples of nonnegative integers $(a,b,c)$ satisfying $a + b + c = 300$ and \[a^2b + a^2c + b^2a + b^2c + c^2a + c^2b = 6,000,000.\]

## Solution 1

$ab(a+b)+bc(b+c)+ac(a+c)=300(ab+bc+ac)-3abc=6000000$$\implies 100(ab+bc+ac)-abc=2000000$

Note that $(100-a)(100-b)(100-c)=1000000-10000(a+b+c)+100(ab+bc+ac)-abc=0$. Thus, one of $a, b, c =100$. There are $201$ cases for each but we need to subtract $2$ for $(100,100,100)$. The answer is $\boxed{601}$

~Bluesoul,Shen Kislay Kai, EaglesNRavens

## Solution 2

$a^2(b+c)+b^2(a+c)+c^2(a+b) = 6000000$, thus $a^2(300-a)+b^2(300-b)+c^2(300-c) = 6000000$. Complete the cube to get $-(a-100)^3-(b-100)^3-(c-100)^3 = 9000000-30000(a+b+c)$, which so happens to be 0. Then we have $(a-100)^3+(b-100)^3+(c-100)^3 = 0$. We can use Fermat's last theorem here to note that one of $a, b, c$ has to be 100. We have $200+200+200+1 = 601.$

## Solution 3

We have The first and the fifth equalities follow from the condition that $a+b+c = 300$.

Therefore, \[\left( a - 100 \right) \left( b - 100 \right) \left( c - 100 \right) = 0 .\]

Case 1: Exactly one out of $a - 100$, $b - 100$, $c - 100$ is equal to 0.

Step 1: We choose which term is equal to 0. The number ways is 3.

Step 2: For the other two terms that are not 0, we count the number of feasible solutions.

W.L.O.G, we assume we choose $a - 100 = 0$ in Step 1. In this step, we determine $b$ and $c$.

Recall $a + b + c = 300$. Thus, $b + c = 200$. Because $b$ and $c$ are nonnegative integers and $b - 100 \neq 0$ and $c - 100 \neq 0$, the number of solutions is 200.

Following from the rule of product, the number of solutions in this case is $3 \cdot 200 = 600$.

Case 2: At least two out of $a - 100$, $b - 100$, $c - 100$ are equal to 0.

Because $a + b + c = 300$, we must have $a = b = c = 100$.

Therefore, the number of solutions in this case is 1.

Putting all cases together, the total number of solutions is $600 + 1 = \boxed{\textbf{(601) }}$.

~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Solution 4

We will use Vieta's formulas to solve this problem. We assume $a + b + c = 300$, $ab + bc + ca = m$, and $abc = n$. Thus $a$, $b$, $c$ are the three roots of a cubic polynomial $f(x)$.

We note that $300m = (a + b + c)(ab + bc + ca)=\sum_{cyc} a^2b + 3abc = 6000000 + 3n$, which simplifies to $100m - 2000000 = n$.

Our polynomial $f(x)$ is therefore equal to $x^3 - 300x^2 + mx - (100m - 2000000)$. Note that $f(100) = 0$, and by polynomial division we obtain $f(x) = (x - 100)(x^2 - 200x - (m-20000))$.

We now notice that the solutions to the quadratic equation above are $x = 100 \pm \frac{\sqrt{200^2 - 4(m - 20000)}}{2} = 100 \pm \sqrt{90000 - 4m}$, and that by changing the value of $m$ we can let the roots of the equation be any pair of two integers which sum to $200$. Thus any triple in the form $(100, 100 - x, 100 + x)$ where $x$ is an integer between $0$ and $100$ satisfies the conditions.

Now to count the possible solutions, we note that when $x \ne 0$, the three roots are distinct; thus there are $3! = 6$ ways to order the three roots. As we can choose $x$ from $1$ to $100$, there are $100 \cdot 3! = 600$ triples in this case. When $x = 0$, all three roots are equal to $100$, and there is only one triple in this case.

In total, there are thus $\boxed{601}$ distinct triples.

~GaloisTorrent <Shen Kislay Kai>

- minor edit made by MEPSPSPSOEODODODO

## Solution 5

Let's define $a=100+x$, $b=100+y$, $c=100+z$. Then we have $x+y+z=0$ and $6000000 = \sum a^2(b+c)$

$= \sum (100+x)^2(200-x) = \sum (10000+200x+x^2)(200-x) = \sum (20000 - 10000 x + x(40000-x^2))$

$= \sum (20000 + 30000 x -x^3) = 6000000 - \sum x^3$, so we get $x^3 + y^3 + z^3 = 0$. Then from $x+y+z = 0$, we can find $0 = x^3+y^3+z^3 = x^3+y^3-(x+y)^3 = 3xyz$, which means that one of $a$, $b$,$c$ must be 0. There are 201 solutions for each of $a=0$, $b=0$ and $c=0$, and subtract the overcounting of 2 for solution $(200, 200, 200)$, the final result is $201 \times 3 - 2 = \boxed{601}$.

~Dan Li

## Solution 6

Since $a + b + c = 300$, $(100 - a) + (100 - b) + (100 - c) = 300 - (a + b + c) = 0$. There is a well known algebraic identity:

If $a + b + c = 0, a^3 + b^3 + c^3 = 3abc$. Hence, as $(100 - a) + (100 - b) + (100 - c) = 0$ as mentioned above, $(100 - a)^3 + (100 - b)^3 + (100 - c)^3 = 3(100 - a)(100 - b)(100 - c)$.

Now expand the LHS of the equation: $(100 - a)^3 + (100 - b)^3 + (100 - c)^3 = 3 * 100^3 - 3 * 100^2 * (a + b + c) + 3 * 100 * (a^2 + b^2 + c^2) - (a^3 + b^3 + c^3)$.

We are given in the problem that \[a^2b + a^2c + b^2a + b^2c + c^2a + c^2b = 6,000,000.\] Notice that $(a + b + c)^3 = a^3 + b^3 + c^3 + 3(a^2b + a^2c + b^2a + b^2c + c^2a + c^2b) + 6abc$. This means that $300^3 = a^3 + b^3 + c^3 + 6abc + 3 * 6 * 10^6$. Simplify to get $a^3 + b^3 + c^3 + 6abc = 9 * 10^6$. This means that $a^3 + b^3 + c^3 = 9 * 10^6 - 6abc$.

We know that $a + b + c = 300$. We also know that $a^2 + b^2 + c^2 = (a + b + c)^2 - 2(ab + bc + ac) = 300^2 - 2(ab + bc + ac)$.

Now the LHS can be written as $3 * 100^3 - 3 * 100^2 * 300 + 3 * 100 * (300^2 - 2(ab + ac + bc)) - (9 * 10^6 - 6abc)$. This simplifies to $12 * 10^6 - 600(ab + bc + ac) + 6abc$.

Now, we evaluate the right side. $(100 - a)(100 - b)(100 - c) = 10^6 - 10^4(a + b + c) + 100(ab + bc + ac) - abc = -2*10^6 - 100(ab + bc + ac) - abc$. Now we set the LHS and RHS equal to each other.

\[12 * 10^6 - 600(ab + ac + bc) + 6abc = -2*10^6 + 100(ab + bc + ac) - abc\]. Notice that the LHS is just $-6$ times the RHS. If the RHS is equal to $-6$ times itself, the only possible value the RHS can take is $0$. The RHS was originally $3(100 - a)(100 - b)(100 - c)$. This must equal $0$. \[3(100 - a)(100 - b)(100 - c) = 0\]. This means one of $a, b,$ or $c$ must be $100$. The remaining two must sum up to $200$ as the three of them together sum to $300$ as indicated by the problem. WLOG Let us assume $a = 100$ and $b + c = 200$. As $b$ and $c$ are nonnegative integers, we employ Stars and Bars to find that there are $\binom{200 + 2 - 1}{2 - 1} = 201$ solutions to the equation. As $a, b,$ or $c$ could in reality be $100$, multiply $201$ by $3$ to get $603$. However, the solution $(a, b, c) = (100, 100, 100)$ is counted thrice in total, but we only want it counted once, so subtract $2$ from $603$ to arrive at the final answer: The number of solutions is $\boxed{601}$.
