## Problem

The $9$ members of a baseball team went to an ice-cream parlor after their game. Each player had a single scoop cone of chocolate, vanilla, or strawberry ice cream. At least one player chose each flavor, and the number of players who chose chocolate was greater than the number of players who chose vanilla, which was greater than the number of players who chose strawberry. Let $N$ be the number of different assignments of flavors to players that meet these conditions. Find the remainder when $N$ is divided by $1000.$

## Solution 1

Let $c$ be the number of players who choose chocolate, $v$ be the number of players who choose vanilla, and $s$ be the number of players who choose strawberry ice cream. We are given three pieces of information $c,v,s\ge 1$ and $c+v+s=9$ and $c>v>s$.

By inspection the only solutions for $(c,v,s)$ are $(4,3,2),(5,3,1), (6, 2, 1)$

Now we must choose which player chooses which flavor. For the general case $(c,v,s),$ we begin by choose $c$ of the $9$ players who eat chocolate, then we choose $v$ of the $9-c$ players who eat vanilla, after this the amount of players who eat strawberry is fixed. Therefore the general formula is $\binom{9}{c}\binom{9-c}{v}.$

Therefore our final answer is, \[\binom{9}{4}\binom{9-4}{3} + \binom{9}{5}\binom{9-5}{3} + \binom{9}{6}\binom{9-6}{2} = \binom{9}{4}\binom{5}{3} + \binom{9}{5}\binom{4}{3} + \binom{9}{6}\binom{3}{2} = 2\boxed{016}\]

Alternatively, this can be written in multinomial coefficients as

\[\binom{9}{4,3,2} + \binom{9}{5, 3, 1} + \binom{9}{6, 2, 1}\] 

which gives the same answer

~ [mathkiddus](https://artofproblemsolving.com/wiki/index.php?title=User:Mathkiddus "User:Mathkiddus") ~ sujoybec51 multiple edits to make more clear

## Solution 2

We apply casework on the scoops the team gets.

Case 1: The scoops are $6,2,1$. Then we have $\binom{9}{6}\cdot \binom{3}{2} = 252$.

Case 2: The scoops are $5,3,1$. Then we have $\binom{9}{5}\cdot \binom{4}{3} = 504$.

Case 3: The scoops are $4,3,2$. Then we have $\binom{9}{4}\cdot \binom{5}{3} = 1260$.

Thus the answer is $252+504+1260=2\boxed{016}$.

~ [zhenghua](https://artofproblemsolving.com/wiki/index.php?title=User:Zhenghua "User:Zhenghua")

## Solution 3

Denote the number of people who chose strawberry, vanilla, or chocolate as (S, V, C). Then, as S < V < C, we just need to find values of S, V, and C such that S + V + C = 9. Notice S can only be 1 or 2 as S = 3 will result in V + C = 6 and it just won't work for S < V < C. So using these two values, we get that the possible triples of (S, V, C) are: (1, 3, 5), (2, 3, 4) and (1, 2, 6). Now, let's consider (S, V, C) = (1, 3, 5). If we start with the strawberry people, notice there are ${9\choose 1}$ possibilities. Now, we see there are 8 different people waiting to be assigned to the 3 vanilla people therefore there are ${8\choose 3}$ ways for this to work. We can now go down the list to get: ${9\choose 1}{8\choose 3}{5\choose 5} + {9\choose 2}{7\choose 3}{4\choose 4} + {9\choose 1}{8\choose 2}{6\choose 6}$ which gives a grand total of $2016$ possibilities. The remainder when $N$ is divided by $1000$ is $\boxed{016}$.

~ilikemath247365

## Solution 4

We start by finding the only 3 possible cases, since $C>V>S$. We arrive at

$(6, 2, 1) = {9 \choose 6,2,1} = \frac{9 \cdot 8 \cdot 7 \cdot 6!}{6! \cdot 2! \cdot 1!} = 252$

$(5, 3, 1) = {9 \choose 5,3,1} = \frac{9 \cdot 8 \cdot 7 \cdot 6 \cdot 5!}{5! \cdot 3! \cdot 1!} = 504$

$(4, 3, 2) = {9 \choose 4,3,2} = \frac{9 \cdot 8 \cdot 7 \cdot 6 \cdot 5 \cdot 4!}{4! \cdot 3! \cdot 2!} = 1260$

Summing these up, we get $252+504+1260= 2\boxed{016}$

~shreyan.chethan, cleaned up by cweu001 and dareckolo

## Solution 5

Let $c, v, s$ be chocolate, vanilla, and strawberry respectively. We will also use the notation $(s, v, c)$ to denote the number of chocolate, vanilla, and strawberry respectively. We have this condition, $c>v>s$. Now, we can list out the cases since there wont be a lot. First, we have: \[(1,2,6) \Longrightarrow \binom{9}{1} \cdot \binom{8}{2} = 252\]. Second, we have: \[(1,3,5) \Longrightarrow \binom{9}{1} \cdot \binom{8}{3} = 504\], and last, we have: \[(2,3,4) \Longrightarrow \binom{9}{2} \cdot \binom{7}{3} = 1260\]. Summing them we get $2016$, then, we take $\mod 1000$, to get $\boxed{016}$

-jb2015007
