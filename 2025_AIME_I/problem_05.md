## Problem

There are $8!= 40320$ eight-digit positive integers that use each of the digits $1, 2, 3, 4, 5, 6, 7, 8$ exactly once. Let $N$ be the number of these integers that are divisible by $22$. Find the difference between $N$ and $2025$.

## Solution 1

Notice that if the 8-digit number is divisible by $22$, it must have an even units digit. Therefore, we can break it up into cases and let the last digit be either $2, 4, 6,$ or $8$. Due to symmetry, upon finding the total count of one of these last digit cases (we look at last digit $2$ here), we may multiply the resulting value by $4$.

Now, we just need to find the number of positions of the remaining numbers such that the units digit is $2$ and the number is divisible by $11$. Denote the odd numbered positions to be $a_1, a_3, a_5, a_7$ and the even numbered positions to be $a_2, a_4, a_6$ (recall $a_8=2$). By the divisibility rule of $11$, we must have: \[(a_1 + a_3 + a_5 + a_7) - (a_2 + a_4 + a_6 + 2)\] which is congruent to $0\hspace{2mm}(\text{mod}\hspace{1mm}11)$. Therefore, after simplifying, we must have: \[a_1 - a_2 + a_3 - a_4 + a_5 - a_6 + a_7\equiv2\hspace{2mm}(\text{mod}\hspace{1mm}11)\] Now consider $a_1+ a_2 +\ldots + a_7=1+2+\ldots+8-2=34\equiv1\hspace{2mm}(\text{mod}\hspace{1mm}11)$. Therefore, \[(a_1 + a_2 + \ldots+ a_7) - 2(a_2 + a_4 + a_6)\equiv2\hspace{2mm}(\text{mod}\hspace{1mm}11)\] which means that \[a_2 + a_4 + a_6\equiv5\hspace{2mm}(\text{mod}\hspace{1mm}11)\] Notice that the minimum of $a_2+a_4+a_6$ is $1 + 3 + 4 = 8$ and the maximum is $6 + 7 + 8 = 21$. The only possible number congruent to $5\hspace{2mm}(\text{mod}\hspace{1mm}11)$ in this range is $16$. All that remains is to count all the possible sums of $16$ using the values $1, 3, 4, 5, 6, 7, 8$. There are a total of four possibilities: \[(1, 7, 8), (3, 5, 8), (3, 6, 7), (4, 5, 7)\] The arrangement of the odd-positioned numbers ($a_1,a_3,a_5,a_7$) does not matter, so there are $4!=24$ arrangements of these numbers. Recall that the $4$ triplets above occupy $a_2,a_4,a_6$; the number of arrangements is $3!=6$. Thus, we have $24\cdot6\cdot4=576$ possible numbers such that the units digit is $2$. Since we claimed symmetry over the rest of the units digits, we must multiply by $4$, resulting in $576\cdot4=2304$ eight-digit positive integers. Thus, the positive difference between $N$ and $2025$ is $2304 - 2025 = \boxed{279}$.

~ilikemath247365

~LaTeX by eevee9406

### Proof of symmetry on last even digit

To see the symmetry in the cases on the last digit $a_8$, you can cycle through the cases bijectively by adding 2 to each digit $\mod 10$.

## Solution 2

1. To be multiple of $11:$ Total of $1,2,3,4,5,6,7,8$ is $36,$ dividing into two groups of $4$ numbers, the difference of sum of two group $x$ and $y$ need to be $0$ or multiple of $11,$ i.e. $x+y=36,$$x-y=0,11,22\dots$ only $x=y=18$ is possible. Number $8$ can only be with $(8,1,4,5),(8,1,2,7),(8,1,3,6),(8,2,3,5).$ One group of $4$ numbers make $4!$ different arrangement, two groups make $4!\cdot{4!},$ the $2$ group makes $2!$ arrangement. The two group of numbers are alternating by digits. Total number of multiple of $11$ is $4\cdot 2!\cdot 4!\cdot 4!.$ 2. To be multiple of $2:$ We noticed in each number group, there are two odd two even. So the final answer is above divided by $2,$$4*2!*4!*4!/2=2304.$$2304-2025=\boxed{279.}$

~Mathzu.club ~Latex by mathkiddus

## Solution 3

\[\begin{array}{|c|c|c|c|c|c|c|c|} \hline w & a & x & b & y & c & z & n \\ \hline \end{array}\] Let $waxbyczn$ be our 8 digit number. For a number to be a multiple of $22$ it must be an even multiple of $11,$ so $n$ must be even and $|(w + x + y + z) - (a + b + c + n)| = 11x$ for $1 \geq x \geq 0.$ Let $n = 8.$ We have three main subcases:

Note that none of the variables can be $8$ since $n$ is $8$. We know that $(a + b + c) + (w + x + y + z) = 28$ and $(a + b + c) + 8 = (w + x + y + z).$ Solving this system, we find $a + b + c = 10$ and $w + x + y + z = 18.$ After some small bashing we find there are $4$ combinations of numbers that will work: the variables $a, b, c$ can be distinct elements of the sets $\{2, 3, 5\}, \{1, 4, 5\}, \{1, 3, 6\}$ or $\{1, 2, 7\}$, and $w, x, y, z$ can be distinct elements of each corresponding set. (So for example, if we chose $a, b, c$ from $\{2, 3, 5\}$ we would choose $w, x, y, z$ from $\{1, 4, 6, 7\},$ the "corresponding" set). There are $4$ different set pairs, $3!$ ways to permute $a, b, c,$ and $4!$ ways to permute $w, x, y, z,$ giving us $4! \cdot 3! \cdot 4$ ways for this subcase.

$19$ is odd, but $a + b + c + w + x + y + z$ is even, so if we set up our system of equations for $(a + b + c)$ and $(w + x + y + z)$ like we did in sub case 1, we would end up with a fraction for the sums.

Same issue as sub case 2, we will end up with a fraction because $3$ is odd.

For every even $n$, there will always be $4! \cdot 3! \cdot 4$ ways for SC1 (pretty easy to confirm this, just do SC1 for $n = 6,4,2$) and $0$ ways for SC2 and SC3 since they will always give fractions for the sums when we try to set up our system. Since $n$ can be $4$ different values, the answer is $4! \cdot 3! \cdot 4 \cdot 4 - 2025 = \boxed{279}.$

~[grogg007](https://artofproblemsolving.com/wiki/index.php?title=User:Grogg007 "User:Grogg007")

## Solution 4

Let the number be $abcdefgh$, based on the rule for divisibility of 11, $(a + c + e + g) - (b+d+f+h)$ must be a multiple of 11. Since the sum of all the 8 digits is 36, and the sum of four digits is at least 10, so we can only have $a+c+e+g = b+d+f+h = 18$. There are 8 ways to sum to 18 using four digits from $1,2,3,4,5,6,7,8$. The digits on even and odd digits can be permuted, so the number of multiples of 11 is $4! \times 4!\times 8 = 4608$, and half of these numbers have even digits on the units digit, so the number of multiple of 22 is $4608/2 = 2304$, the answer to this problem is $2304 - 2025 = \boxed{279}$.

~[Dan Li]
