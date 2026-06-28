## Problem

Let be an integer. Call a positive integer if it has exactly two digits when expressed in base and these two digits sum to . For example, is because and . Find the least integer for which there are more than ten integers.

## Solution

We write the base-$b$ two-digit integer as $\left( xy \right)_b$. Thus, this number satisfies \[ \left( x + y \right)^2 = b x + y \] with $x \in \left\{ 1, 2, \cdots , b-1 \right\}$ and $y \in \left\{ 0, 1, \cdots , b - 1 \right\}$.

The above conditions imply $\left( x + y \right)^2 < b^2$. Thus, $x + y \leq b - 1$.

The above equation can be reorganized as \[ \left( x + y \right) \left( x + y - 1 \right) = \left( b - 1 \right) x . \]

Denote $z = x + y$ and $b' = b - 1$. Thus, we have \[ z \left( z - 1 \right) = b' x , \hspace{1cm} (1) \] where $z \in \left\{ 2, 3, \cdots , b' \right\}$ and $x \in \left\{ 1, 2, \cdots , b' \right\}$.

Next, for each $b'$, we solve Equation (1).

We write $b'$ in the prime factorization form as $b' = \Pi_{i=1}^n p_i^{k_i}$. Let $\left(A, \bar A \right)$ be any ordered partition of $\left\{ 1, 2, \cdots , n \right\}$ (we allow one set to be empty). Denote $P_A = \Pi_{i \in A} p_i^{k_i}$ and $P_{\bar A} = \Pi_{i \in \bar A} p_i^{k_i}$.

Because ${\rm gcd} \left( z, z-1 \right) = 1$, there must exist such an ordered partition, such that $P_A | z$ and $P_{\bar A} | z-1$.

Next, we prove that for each ordered partition $\left( A, \bar A \right)$, if a solution of $z$ exists, then it must be unique.

Suppose there are two solutions of $z$ under partition $\left( A, \bar A \right)$: $z_1 = c_1 P_A$, $z_1 - 1 = d_1 P_{\bar A}$, and $z_2 = c_2 P_A$, $z_2 - 1 = d_2 P_{\bar A}$. W.L.O.G., assume $c_1 < c_2$. Hence, we have \[ \left( c_2 - c_1 \right) P_A = \left( d_2 - d_1 \right) P_{\bar A} . \]

Because ${\rm gcd} \left( P_A, P_{\bar A} \right) = 1$ and $c_1 < c_2$, there exists a positive integer $m$, such that $c_2 = c_1 + m P_{\bar A}$ and $d_2 = d_1 + m P_A$. Thus,

However, recall $z_2 \leq b'$. We get a contradiction. Therefore, under each ordered partition for $b'$, the solution of $z$ is unique.

Note that if $b'$ has $n$ distinct prime factors, the number of ordered partitions is $2^n$. Therefore, to find a $b'$ such that the number of solutions of $z$ is more than 10, the smallest $n$ is 4.

With $n = 4$, the smallest number is $2 \cdot 3 \cdot 5 \cdot 7 = 210$. Now, we set $b' = 210$ and check whether the number of solutions of $z$ under this $b'$ is more than 10.

We can easily see that all ordered partitions (except $A = \emptyset$) guarantee feasible solutions of $z$. Therefore, we have found a valid $b'$. Therefore, $b = b' + 1 = \boxed{\textbf{(211) }}$.

~Shen Kislay Kai and Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

### I can't comprehend the end!

Continue until reaching \[ z \left( z - 1 \right) = b' x , \hspace{1cm} (1) \] where $z \in \left\{ 2, 3, \cdots , b' \right\}$ and $x \in \left\{ 1, 2, \cdots , b' \right\}$. Notice that $x$ must divide into $z(z-1)$ as $b'x = z(z-1)$. Then, notice that $\gcd(z,z-1) = 1$, and thus either $x~|~ z$ or $x ~ | ~ z-1$.

Every solution then corresponds to a rough divisor of $b'$. Thus, suppose $b'$ has $n$ positive prime divisors. Then, every divisor can be distributed to $z$ or $z-1$, contributing a total of $2^n$ choices. To obtain more than 10 solutions, one must find $2^n > 10$, in which $n \ge 4$.

The smallest $b'$ occurs with the four smallest prime divisors, those being, 2, 3, 5, 7, giving $b' = 210$, and thus $b = b' + 1 = \boxed{211}$.

~Pinotation
