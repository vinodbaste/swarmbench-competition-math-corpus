## Problem

Let $N$ be the greatest four-digit positive integer with the property that whenever one of its digits is changed to $1$, the resulting number is divisible by $7$. Let $Q$ and $R$ be the quotient and remainder, respectively, when $N$ is divided by $1000$. Find $Q+R$.

## Solution 1

We note that by changing a digit to $1$ for the number $\overline{abcd}$, we are subtracting the number by either $1000(a-1)$, $100(b-1)$, $10(c-1)$, or $d-1$. Thus, $1000a + 100b + 10c + d \equiv 1000(a-1) \equiv 100(b-1) \equiv 10(c-1) \equiv d-1 \pmod{7}$. We can casework on $a$ backwards, finding the maximum value.

(Note that computing $1000 \equiv 6 \pmod{7}, 100 \equiv 2 \pmod{7}, 10 \equiv 3 \pmod{7}$ greatly simplifies computation).

Applying casework on $a$, we can eventually obtain a working value of $\overline{abcd} = 5694 \implies \boxed{699}$. ~akliu

## Solution 2

Let our four digit number be $abcd$. Replacing digits with $1$, we get the following equations:

$1000+100b+10c+d \equiv 0 \pmod{7}$

$1000a+100+10c+d \equiv 0 \pmod{7}$

$1000a+100b+10+d \equiv 0 \pmod{7}$

$1000a+100b+10c+1 \equiv 0 \pmod{7}$

Reducing, we get

$6+2b+3c+d \equiv 0 \pmod{7}$$(1)$

$6a+2+3c+d \equiv 0 \pmod{7}$$(2)$

$6a+2b+3+d \equiv 0 \pmod{7}$$(3)$

$6a+2b+3c+1 \equiv 0 \pmod{7}$$(4)$

Subtracting $(2)-(1), (3)-(2), (4)-(3), (4)-(1)$, we get:

$3a-b \equiv 2 \pmod{7}$

$2b-3c \equiv 6 \pmod{7}$

$3c-d \equiv 2 \pmod{7}$

$6a-d \equiv 5 \pmod{7}$

For the largest four-digit number, we test values for $a$ starting with $9$. When $a = 9$, $b = 4$, $c = 3$, and $d = 7$. However, when switching the digits with $1$, we quickly notice this doesn't work.

Once we get to $a = 5$, we get $b=6$, $c=9$, and $d=4$. Summing $694$ with $5$, we get $\boxed{699}$ -westwoodmonster

## Solution 3

Let our four digit number be $\overline{abcd}$. Replacing digits with $1$, we get the following equations:

$1000+100b+10c+d \equiv 0 \pmod{7}$

$1000a+100+10c+d \equiv 0 \pmod{7}$

$1000a+100b+10+d \equiv 0 \pmod{7}$

$1000a+100b+10c+1 \equiv 0 \pmod{7}$

Add the equations together, we get:

$3000a+300b+30c+3d+1111 \equiv 0 \pmod{7}$

And since the remainder of 1111 divided by 7 is 5, we get:

$3\overline{abcd} \equiv 2 \pmod{7}$

Which gives us:

$\overline{abcd} \equiv 3 \pmod{7}$

And since we know that changing each digit into $1$ will make $\overline{abcd}$ divisible by $7$, we get that $d-1$, $10c-10$, $100b-100$, and $1000a-1000$ all have a remainder of $3$ when divided by $7$. Thus, we get $a=5$, $b=6$, $c=9$, and $d=4$. Thus, we get $5694$ as $\overline{abcd}$, and the answer is $694+5=\boxed{699}$.

~Callisto531

## Solution 4

Let our four digit number be $abcd$. Replacing digits with 1, we get the following equations:

$1000+100b+10c+d \equiv 0 \pmod{7}$

$1000a+100+10c+d \equiv 0 \pmod{7}$

$1000a+100b+10+d \equiv 0 \pmod{7}$

$1000a+100b+10c+1 \equiv 0 \pmod{7}$

Then, we let x, y, z, t be the smallest whole number satisfying the following equations:

$1000a \equiv x \pmod{7}$

$100b \equiv y \pmod{7}$

$10a \equiv z \pmod{7}$

$d \equiv t \pmod{7}$

Since 1000, 100, 10, and 1 have a remainder of 6, 2, 3, and 1 when divided by 7, we can get the equations of:

(1): $6+y+z+t \equiv 0 \pmod{7}$

(2): $x+2+z+t \equiv 0 \pmod{7}$

(3): $x+y+3+t \equiv 0 \pmod{7}$

(4): $x+y+z+1 \equiv 0 \pmod{7}$

Add (1), (2), (3) together, we get:

$2x+2y+2z+3t+11 \equiv 0 \pmod{7}$

We can transform this equation to:

$2(x+y+z+1)+3t+9 \equiv 0 \pmod{7}$

Since, according to (4), $x+y+z+1$ has a remainder of 0 when divided by 7, we get:

$3t+9 \equiv 0 \pmod{7}$

And because t is 0 to 6 due to it being a remainder when divided by 7, we use casework and determine that t is 4.

Using the same methods of simplification, we get that x=2, y=5, and z=6, which means that 1000a, 100b, 10c, and d has a remainder of 2, 5, 6, and 4, respectively. Since a, b, c, and d is the largest possible number between 0 to 9, we use casework to determine the answer is a=5, b=6, c=9, and d=4, which gives us an answer of $5+694=\boxed{699}$

~Callisto531 and his dad
