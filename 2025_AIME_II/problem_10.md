## Problem

Sixteen chairs are arranged in a row. Eight people each select a chair in which to sit so that no person sits next to two other people. Let $N$ be the number of subsets of $16$ chairs that could be selected. Find the remainder when $N$ is divided by $1000$.

## Solution 1 (Recursion)

Notice that we can treat each chair as an empty space. If a person selects a chair, we fill in the corresponding space with a '$1$': otherwise, we fill in the corresponding space with a '$0$'. Since no person can sit to two other people (and two other people means having a person to your left and your right), that means that we can't have three people sitting in a row). So now the problem boils down to the following: we have a string of $0$'s and $1$'s of length $16$, $8$ of which will be $1$ and $8$ of which will be $0$. This string cannot have three consecutive $1$'s in a row. We need to find the number of ways to construct this string.

Let's try recursion. The motivation for recursion is that $16$ and $8$ are relatively big numbers (the upper bound is $16$ choose $8$ which is over $12000$!) Also, many problems involving strings and counting with restrictions like 'three in a row' can usually be solved by breaking it up into smaller problems.

Define $S(n,k)$ to be the number of ways to create a string of length $n$ with $k$$1$'s and $n-k$$0$'s such that we can't have three consecutive $1$'s. We need to find $S(16,8)$.

So now we're going to take our recursive step, which usually involves splitting the string into two smaller strings. Suppose we split the string into two strings of length $n-b$ and $b$. Also suppose that in the string of length $b$ there are $i$$1$'s (which means that in the string of length $n-b$, there are $k-i$$1$'s. Now consider the first two digits in the string of length $b$: we do casework on them.

$\textbf{Case 1: 00}$

In this case, we can imagine the string as _ _ _ _ ... _ _ | 0 0 _ _ ... _ _ where the vertical line | shows the split. To the left of the split, we can choose the string without constraints in $S(n-b, k-i)$ ways since there are $n-b$ spaces and $k-i$$1$'s to place there. To the right of the $0$, there are $b-2$ spaces and we still have to place $i$$1's$, so this can be done in $S(b-2,i)$ ways. Now choosing the left string and the right string are independent, so the number of ways in this case is \[S(n-b, k-i)S(b-2, i)\].

$\textbf{Case 2: 01}$

Now the split string looks something like _ _ _ _ ... _ _ | 0 1 _ _ ... _ _ . The number of ways to choose the string to the left remains unchanged: $S(n-b, k-i)$ ways. Similarly, it would seem that the number of ways to choose the remainder of the string on the right is $S(b-2, i-1)$ (just as in the previous case but we've used up one of the $i$$1$'s already). However we're overcounting, since if the remainder of the string on the right starts with 1 1 0 _ _ ... it makes a valid string by itself, but together with the 0 1 at the start, it makes 0 1 1 1 0, which is not allowed. Therefore we subtract the number of ways that we start with 0 1 1 1 0: there are $b-5$ spaces left and $i-3$$1$'s left to allocate, so we subtract $S(b-5, i-3)$. So the total in this case is \[S(n-b,k-i) \cdot (S(b-2, i-1)-S(b-5, i-3))\]

$\textbf{Case 3: 10}$

Now the split string looks something like _ _ _ _ ... _ _ | 1 0 _ _ ... _ _ . Now the number of ways to fill in the empty slots to the right is unconstrained as it's following a $0$: there are $b-2$ spaces and $i-1$$1$'s to allocate, so this gives $S(b-2, i-1)$ ways. Now for the left, we overcount just like in the previous case: filling $k-i$$1$'s in $n-b$ slots can be done in $S(n-b, k-i)$ ways. However any way ending with 0 1 1 violates the three $1$'s in a row rule since in the center we have 0 1 1 1 0. The number of violations is the number of ways to fill in the empty slots to the left of _ _ _ ... _ _ 0 1 1 |, which can be done in $S(n-b-3, k-i-2)$ ways since we've already allocated $2$$1$'s and used up $3$ spaces. Therefore the total in this case is:

\[S(b-2, i-1) \cdot (S(n-b, k-i)-S(n-b-3, k-i-2))\]

$\textbf{Case 4: 11}$

In this case, we have something like _ _ _ _ ... _ _ | 1 1 _ _ ... _ _ . Since we can't have three $1$'s in a row, we can automatically fill $0$'s in: _ _ _ _ ... _ 0 | 1 1 0 _ ... _ _ . Now the number of ways to fill in the spaces on the left is $S(n-b-1, k-i)$ and the number of ways to fill in the spaces on the right is $S(b-3, i-2)$. So the number of ways for this case is

\[S(n-b-1,k-i)S(b-3,i-2)\]

Now that we've finished casework, note that $i$ can be anything: at minimum $i$ can be zero, meaning that the string on the right has $0$$1$'s, and at maximum $i$ can be $b$: the string is filled with $1$'s. To encapsulate all of the cases of $i$, we sum over the values of $i$:

\[S(n,k) = \sum_{i = 0}^{b} S(n-b, k-i)S(b-2, i) + S(n-b,k-i) \cdot (S(b-2, i-1)-S(b-5, i-3))\]\[+ S(b-2, i-1) \cdot (S(n-b, k-i)-S(n-b-3, k-i-2)) + S(n-b-1,k-i)S(b-3,i-2)\]

This is our recurrence relationship. But where do we make the split? The above formula works for any $b$, but if we make the split too close to the end, we could end up having to make lots of computations: if we split the string into $15$ and $1$, we'll have to compute $S(15,8)$, $S(14,8)$, etc. which could end up being a lot of work. We want to choose the best $b$ to minimize the number of computations to save time. If we split the string unequally, one side will be larger and that side will require more computations. Therefore, we split the string in half so we just need to compute values of $n$ less than $8$.

So suppose $b = 8$ and plug in $n=16$, $k=8$. Then the above recurrence relation becomes

\[S(16,8) = \sum_{i = 0}^{8} S(8, 8-i)S(6, i) + S(8,8-i) \cdot (S(6, i-1)-S(3, i-3))\]\[+ S(6, i-1) \cdot (S(8, 8-i)-S(5, 6-i)) + S(7,8-i)S(5,i-2)\]

Before we start with computations, let's state our base cases for recursion. Note that if $n<0$ and $k = 0$, $S(n,k) = 1$. Otherwise if $n<0$ or $k<0$ or $k>n$, $S(n,k) = 0$. Also, $S(x,0) = 1$, $S(x,1) = x$, $S(x,2) = \binom{x}{2}$, $S(x,3) = \binom{x}{3}-x+2$ (the last one subtracting $x-2$ for the number of three $1$'s in a row possible). Finally, for other cases of $S(n,k)$ we don't want to use the earlier large recursive formula since we'll have to break those into many small components. Instead, we modify the formula so that $b=2$. This should be fine as $n$ has already been broken down to at most $8$, so these computations shouldn't balloon. Using $b=2$, we get $S(n,k) = S(n-2,k) + 2S(n-2,k-1) - S(n-5,k-3)+S(n-3,k-2)$.

Let's start the computation through the earlier cases.

$\textbf{Case 1}$

\[\sum_{i = 0}^{8} S(8,8-i)S(6,i) = \sum_{i = 2}^{4} S(8,8-i)S(6,i)\]

This is because for $i = 5$, $S(6,5) = 0$ since the best we can do without three in a row is 1 1 0 1 1 0, which is four $1$'s, and it's impossible to achieve $5$$1$'s without three back to back. Also if $i=5$ makes $S(6,i)$$0$, then $i \geq 5$ makes $S(6,i)$$0$. Similarly we can't fit $7$$1$'s in $8$ slots without three back-to-back, so $i$ can't be $0$ or $1$. So $i$ must go from $2$ to $4$. In future cases, I'll skip the explanation of why we tighten our bounds on $i$ since the reasoning is the same as here.

\[\implies \sum_{i = 0}^{8} S(8,8-i)S(6,i) = S(8,6)S(6,2) + S(8,5)S(6,3) + S(8,4)S(6,4)\]

Applying the modified recurrence relation for $b=2$, $S(8,6) = S(6,6) + 2S(6,5)-S(3,3)+S(5,4) = 0+0-0+S(5,4)$$= S(3,4)+2S(3,3)-S(0,1)+S(2,2) = 0+0-0+1 = 1$. Let's remember these for future computations: $S(8,6) = S(5,4) = 1$.

$S(8,5) = S(6,5)+2S(6,4)-S(3,2)+S(5,3) = 0+2S(6,4)-3+7$. $S(6,4) = S(4,4) + 2S(4,3)-S(1,1)+S(3,2) = 0+2 \cdot 2 - 1 + 3 = 6 \implies S(8,5) = 2 \cdot 6 + 4 = 16$. We'll remember $S(6,4) = 6$, $S(8,5) = 16$.

Lastly $S(8,4) = S(6,4) + 2S(6,3)-S(3,1)+S(5,2) = 6+2 \cdot 16 - 3 + 10 = 45$

Therefore \[\sum_{i = 0}^{8} S(8,8-i)S(6,i) = S(8,6)S(6,2) + S(8,5)S(6,3) + S(8,4)S(6,4)\]\[= 1 \cdot 15 + 16 \cdot 16 + 45 \cdot 6 = 541\]

$\textbf{Cases 2 and 3}$

Rewrite \[\sum_{i = 0}^{8} S(8,8-i) \cdot (S(6, i-1)-S(3, i-3)) + S(6, i-1) \cdot (S(8, 8-i)-S(5, 6-i))\]\[= \sum_{i = 0}^{8} 2S(8,8-i)S(6,i-1) - S(8,8-i)S(3,i-3) - S(6,i-1)S(5,6-i)\]\[= 2 \sum_{i=2}^{5} S(8,8-i)S(6,i-1) - \sum_{i=3}^{5} S(8,8-i)S(3,i-3) - \sum_{i=2}^{5} S(6,i-1)S(5,6-i)\]

$\textbf{Case 2 and 3 a.}$

\[\sum_{i=2}^{5} S(8,8-i)S(6,i-1) = S(8,6)S(6,1) + S(8,5)S(6,2) + S(8,4)S(6,3) + S(8,3)S(6,4)\]\[= 1 \cdot 6 + 16 \cdot 15 + 45 \cdot 16 + 50 \cdot 6 = 1266\]

$\textbf{Case 2 and 3 b.}$

\[\sum_{i=3}^{5} S(8,8-i)S(3,i-3) = S(8,5)S(3,0) + S(8,4)S(3,1)+S(8,3)S(3,2)\]\[= 16 \cdot 1 + 45 \cdot 3 + 50 \cdot 3 = 301\]

$\textbf{Case 2 and 3 c.}$

\[\sum_{i=2}^{5} S(6,i-1)S(5,6-i) = S(6,1)S(5,4) + S(6,2)S(5,3) + S(6,3)S(5,2) + S(6,4)S(5,1)\]\[= 6 \cdot 1 + 15 \cdot 7 + 16 \cdot 10 + 6 \cdot 5 = 301\]

Putting it all together, in this case we have

\[\sum_{i = 0}^{8} S(8,8-i)S(6,i-1) = 2 \cdot 1266 - 301 - 301 = 2 \cdot 965 = 1930\]

$\textbf{Case 4}$

Finally, \[\sum_{i=0}^{8} S(7,8-i)S(5,i-2) = \sum_{i=3}^{6} S(7,8-i)S(5,i-2)\]\[= S(7,5)S(5,1)+S(7,4)S(5,2)+S(7,3)S(5,3)+S(7,2)S(5,4)\]

Now $S(7,5) = S(5,5)+2S(5,4)-S(2,2)+S(4,3) = 0+2-1+2 = 3$ and $S(7,4) = S(5,4)+2S(5,3)-S(2,1)+S(4,2) = 1+2 \cdot 7 - 2 + 6 = 19$.

Therefore, \[\sum_{i=0}^{8} S(7,8-i)S(5,i-2) = 3 \cdot 5 + 19 \cdot 10 + 30 \cdot 7 + 21 \cdot 1 = 436\]

Finally,

\[S(16,8) = \sum_{i = 0}^{8} S(8, 8-i)S(6, i) + S(8,8-i) \cdot (S(6, i-1)-S(3, i-3))\]\[+ S(6, i-1) \cdot (S(8, 8-i)-S(5, 6-i)) + S(7,8-i)S(5,i-2)\]

\[= \sum_{i = 2}^{4} S(8,8-i)S(6,i) + (2 \sum_{i=2}^{5} S(8,8-i)S(6,i-1) - \sum_{i=3}^{5} S(8,8-i)S(3,i-3) - \sum_{i=2}^{5} S(6,i-1)S(5,6-i)) + \sum_{i=3}^{6} S(7,8-i)S(5,i-2)\]

\[= 541 + 1930 + 436 = 2907\]

Thus the answer is \[\boxed{907}\]

~KingRavi

### Solution 2 and 3 Remark

There is a clarification for solution 2, but really solution 2 and 3 follow the same two main concepts. Casework and stars and bars. Solution 2 directly solves each case while solution 3 includes each case in its summation. ~Bigbrain_2009

## Solution 2 (Casework)

Let's split the problem into a few cases:

Case 1: All $8$ people are sitting isolated (no person sits next to any of them): $^8C_0 \cdot ^9C_1 = 9$

Case 2: $6$ people are isolated, $2$ people sit next to each other (such that each person sits next to either $0$ or $1$ other person): $^7C_1 \cdot ^9C_2 = 7 \cdot 36 = 252$

Case 3: $4$ people are isolated, $2$ people sit next to each other and $2$ other people sit next to each other with the $2$ groups of $2$ people not sitting next to each other (so each person still sits next to either $0$ or $1$ other person): $^6C_2 \cdot ^9C_3 = 1260$

Case 4: $2$ people are isolated, $6$ people are split into $3$ groups of $2$ people, and no $2$ groups sit next to each other: $^5C_3 \cdot ^9C_4 = 10 \cdot 126 = 1260$

Case 5: $4$ groups of $2$, no groups are sitting next to each other: $^4C_4 \cdot ^9C_5 = 126$

We have $N = 9 + 252 + 1260 + 1260 + 126 = 2907$

$2907 \equiv \boxed{907} \pmod{1000}$

~Mitsuihisashi14

### Clarification for the chooses

For each case there are $8$ chairs taken by the people added with the number of chairs it takes to split the groups of people. For example, with $2$ groups of $2$ people sitting next to each other and $4$ groups of $1$ person, an example will be p p c p p c p c p c p c p. This results in there being $16-8-(2+4-1)=3$ chairs available to distribute (subtracting off the number of people and chairs seperating groups). By stars and bars with the bars being the groups of people, there will be $^9C_{number of remaining chairs}$ ways to distribute the remaining chairs. In this case, $^9C_{3}$. Then, you multiply by the number of ways the groups of two people sitting next to each other and groups of one person can be arranged. This would be the total number of groups choose the number of groups of two people. (To clarify the previous two sentences, you start with $8$, $7$, $6$, $5$, or $4$ groups depending on the case, each group being a single or pair, and you are choosing to make $0$, $1$, $2$, $3$, or $4$ of these groups into pairs instead of singles, respectively.) In this case, $2+4=6$ total groups choose $2$ groups of two people. Then, you multiply these two chooses because both arrangements are independent of each other and sum them over all cases!

~Bigbrain_2009

~ Clarification of clarification by Christian

## Solution 3 (Stars-and-bars)

Let $n$ be the number of groups of adjacent people.

Clearly, there will be $8-n$ groups with $2$ people, and there are $\binom{n}{8-n}$ ways to select these groups.

Now, we use the [stars-and-bars technique](https://artofproblemsolving.com/wiki/index.php?title=Ball-and-urn "Ball-and-urn") to find the number of ways to distribute the $8$ remaining chairs around the $8$ people. Since the $n$ groups are separated, we must choose $n-1$ chairs to place in between beforehand, leaving $8-(n-1)=9-n$ chairs to distribute among $n+1$ spots. Using stars-and-bars, we find that the number of ways to do this is $\binom{9}{9-n}$.

Thus, the total number of arrangements is $\binom{n}{8-n} \binom{9}{9-n}$. Summing this from $n=4$ to $n=8$ yields $\sum_{n=4}^{8} \binom{n}{8-n} \binom{9}{9-n} = 2907 \equiv \boxed{907} \pmod{1000}$.

~[Pengu14](https://artofproblemsolving.com/community/user/1096232)

~ Edited by Christian

## See Also

**[2025 AIME II](https://artofproblemsolving.com/wiki/index.php?title=2025_AIME_II "2025 AIME II")** (**[Problems](https://artofproblemsolving.com/wiki/index.php?title=2025_AIME_II_Problems "2025 AIME II Problems")** • **[Answer Key](https://artofproblemsolving.com/wiki/index.php?title=2025_AIME_II_Answer_Key "2025 AIME II Answer Key")** • [Resources](http://www.artofproblemsolving.com/Forum/resources.php?c=182&cid=45&year=2025))
Preceded by

**[Problem 9](https://artofproblemsolving.com/wiki/index.php?title=2025_AIME_II_Problems/Problem_9 "2025 AIME II Problems/Problem 9")**Followed by

**[Problem 11](https://artofproblemsolving.com/wiki/index.php?title=2025_AIME_II_Problems/Problem_11 "2025 AIME II Problems/Problem 11")**
[1](https://artofproblemsolving.com/wiki/index.php?title=2025_AIME_II_Problems/Problem_1 "2025 AIME II Problems/Problem 1")**•**[2](https://artofproblemsolving.com/wiki/index.php?title=2025_AIME_II_Problems/Problem_2 "2025 AIME II Problems/Problem 2")**•**[3](https://artofproblemsolving.com/wiki/index.php?title=2025_AIME_II_Problems/Problem_3 "2025 AIME II Problems/Problem 3")**•**[4](https://artofproblemsolving.com/wiki/index.php?title=2025_AIME_II_Problems/Problem_4 "2025 AIME II Problems/Problem 4")**•**[5](https://artofproblemsolving.com/wiki/index.php?title=2025_AIME_II_Problems/Problem_5 "2025 AIME II Problems/Problem 5")**•**[6](https://artofproblemsolving.com/wiki/index.php?title=2025_AIME_II_Problems/Problem_6 "2025 AIME II Problems/Problem 6")**•**[7](https://artofproblemsolving.com/wiki/index.php?title=2025_AIME_II_Problems/Problem_7 "2025 AIME II Problems/Problem 7")**•**[8](https://artofproblemsolving.com/wiki/index.php?title=2025_AIME_II_Problems/Problem_8 "2025 AIME II Problems/Problem 8")**•**[9](https://artofproblemsolving.com/wiki/index.php?title=2025_AIME_II_Problems/Problem_9 "2025 AIME II Problems/Problem 9")**•**[10](https://artofproblemsolving.com/wiki/index.php/2025_AIME_II_Problems/Problem_10)**•**[11](https://artofproblemsolving.com/wiki/index.php?title=2025_AIME_II_Problems/Problem_11 "2025 AIME II Problems/Problem 11")**•**[12](https://artofproblemsolving.com/wiki/index.php?title=2025_AIME_II_Problems/Problem_12 "2025 AIME II Problems/Problem 12")**•**[13](https://artofproblemsolving.com/wiki/index.php?title=2025_AIME_II_Problems/Problem_13 "2025 AIME II Problems/Problem 13")**•**[14](https://artofproblemsolving.com/wiki/index.php?title=2025_AIME_II_Problems/Problem_14 "2025 AIME II Problems/Problem 14")**•**[15](https://artofproblemsolving.com/wiki/index.php?title=2025_AIME_II_Problems/Problem_15 "2025 AIME II Problems/Problem 15")
**[All AIME Problems and Solutions](https://artofproblemsolving.com/wiki/index.php?title=AIME_Problems_and_Solutions "AIME Problems and Solutions")**

[](https://artofproblemsolving.com/wiki/index.php?title=File:AMC_Logo.png)
