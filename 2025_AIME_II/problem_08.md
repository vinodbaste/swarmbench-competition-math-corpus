## Problem

From an unlimited supply of $1$-cent coins, $10$-cent coins, and $25$-cent coins, Silas wants to find a collection of coins that has a total value of $N$ cents, where $N$ is a positive integer. He uses the so-called $\textit{greedy algorithm}$, successively choosing the coin of greatest value that does not cause the value of his collection to exceed $N$. For example, to get $42$ cents, Silas will choose a $25$-cent coin, then a $10$-cent coin, then $7$$1$-cent coins. However, this collection of $9$ coins uses more coins than necessary to get a total of $42$ cents; indeed, choosing $4$$10$-cent coins and $2$$1$-cent coins achieves the same total value with only $6$ coins.

In general, the greedy algorithm succeeds for a given $N$ if no other collection of $1$-cent, $10$-cent, and $25$-cent coins gives a total value of $N$ cents using strictly fewer coins than the collection given by the greedy algorithm. Find the number of values of $N$ between $1$ and $1000$ inclusive for which the greedy algorithm succeeds.

## Solution 1

We begin by noting that all values of $N \leq 25$ work without issue.

Starting from $N = 25$ to $29$, the greedy algorithm will select the $25$-cent coin, and no problem arises.

From $N = 30$ to $34$, the greedy algorithm will select the $25$-cent coin along with $5$$1$-cent coins to reach a total of $30$, while the optimal solution would involve using $3$$10$-cent coins. This issue is resolved from $N = 35$ to $39$, as the greedy algorithm can now select $25 + 10$-cent coins to match the optimal solution.

From $N = 40$ to $44$, a similar problem occurs again. The greedy algorithm selects $25 + 10 + 5 \times 1$-cent coins to reach 40, while the optimal solution would use 4 $10$-cent coins.

The problem occurs again from $N = 55$ to $59$, where $50 + 5 \times 1$ is not as good as using $25 + 3 \times 10$, and it is resolved at $N = 60$. From $N = 65$ to $69$, a similar issue arises, as $25 \times 2 + 10 + 5 \times 1$ is not as optimal as $25 + 4 \times 10$ to approach 65.

We observe that this issue repeats in cycles of $25$ numbers, with $10$ of the $25$ numbers in each cycle not working. The cycle starts at $30$, and the next cycle will start $25$ numbers later, at $55$, then $80$, and so on, continuing until $980$–$1005$ for the last cycle.

The total number of cycles is given by:

\[\frac{955 - 30}{25} + 1 = 38,\]

and each cycle contains $10$ problematic numbers. Therefore, the total number of problematic numbers is:

\[38 \times 10 = 380.\]

The cycle from $980$ to $1005$ has the problematic numbers from $980$ to $984$ and $990$ to $994$, giving another $10$ problematic numbers.

Thus, the total number of unsuccessful numbers from $1$ to $1000$ inclusive is $390$, and the desired count of successful numbers is:

\[1000 - 390 = \boxed{610}.\]

(Feel free to make any edits on grammar, $\LaTeX$ and formatting.)

~ Mitsuihisashi14

~ Edited by [aoum](https://artofproblemsolving.com/wiki/index.php/User:Aoum)

## Proof of the Existence of the Cycle

For completeness, we'll present a proof that the cycle described in the first solution exists.

For a positive integer $n$ in the form $n=30+25m$ where $m$ is a non-negative integer, we claim that in the list of $25$ numbers below, \[\underbrace{n,\ldots,n+4}_{\text{succeeds}},\underbrace{n+5,\ldots, n+9}_{\text{does not succeed}}, \underbrace{n+10,\ldots,n+14}_{\text{does not succeed}}, \underbrace{n+15, \ldots, n+24}_{\text{succeeds}}\] is the situation. We proceed by induction to show that this is true.

The base case of $n=30$ or equivalently $m=0$ is shown in Solution 1. Then, if the claim is true for $m=k$ for some non-negative integer $k$, then consider that for $m=k+1$ (i.e $n$ is increased by $25$), the greedy algorithm will first choose a $25$ cent coin for each of the $25$ numbers in the list, which reduces the problem to finding the numbers that succeeds for $m=k$. Hence, by induction, the claim is true.

~compassmath
