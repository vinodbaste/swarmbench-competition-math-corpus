## Problem

Consider the paths of length $16$ that follow the lines from the lower left corner to the upper right corner on an $8\times 8$ grid. Find the number of such paths that change direction exactly four times, as in the examples shown below.

[asy] size(10cm); usepackage("tikz");label("\begin{tikzpicture}[scale=.5]\draw(0,0)grid(8,8);\draw[line width=2,red](0,0)--(2,0)--(2,3)--(5,3)--(5,8)--(8,8);\end{tikzpicture}",origin); label("\begin{tikzpicture}[scale=.5]\draw(0,0)grid(8,8);\draw[line width=2,red](0,0)--(0,3)--(3,3)--(3,5)--(8,5)--(8,8);\end{tikzpicture}",E); [/asy]

## Solution 1

We divide the path into eight “$R$” movements and eight “$U$” movements. Five sections of alternating $RURUR$ or $URURU$ are necessary in order to make four “turns" because each transition from $R$ to $U$ or from $U$ to $R$ is one turn. Without loss of generality, we use the first case and multiply by $2$ (because we can convert each path in the first case to one in the second case by turning $R$'s to $U$'s and $U$'s to $R$'s).

For $U$, let $a$ be the length of the first block of $U$'s and $b$ be the second block of $U$'s. There are eight $U$'s in total, so we have to have $a+b=8$. We have seven ordered pairs of such positive integers $(a,b)$, specifically $(1,7),(2,6),\ldots,(6,2),(7,1)$.

For $R$, we subtract $1$ from each block of $R$'s (because each block of $R$'s must have length at least $1$, and to use stars and bars we have to have minimum length $0$). From here, we use stars and bars to get ${7 \choose 5}=21$.

Thus our answer is $7\cdot21\cdot2=\boxed{294}$.

~eevee9406

## Solution 2

Draw a few examples of the path. However, notice one thing in common - if the path starts going up, there will be 3 "segments" where the path goes up, and two horizontal "segments." Similarly, if the path starts going horizontally, we will have three horizontal segments and two vertical segments. Those two cases are symmetric, so we only need to consider one. If our path starts going up, by stars and bars, we can have $\binom{7}{2}$ ways to split the 8 up's into 3 lengths, and have $\binom{7}{1}$ to split the 8-horizontals into 2 lengths. We multiply them together, and multiply by 2 for symmetry, giving us $2*\binom{7}{2}*\binom{7}{1}=294.$

~nathan27 (original by alexanderruan)

## Solution 3

Notice that the $RURUR$ case and the $URURU$ case is symmetrical. WLOG, let's consider the RURUR case.

Now notice that there is a one-to-one correspondence between this problem and the number of ways to distribute 8 balls into 3 boxes and also 8 other balls into 2 other boxes, such that each box has a nonzero amount of balls.

There are ${8+2-3 \choose 2}$ ways for the first part, and ${8+1-2 \choose 1}$ ways for the second part, by stars and bars.

The answer is $2\cdot {7 \choose 2} \cdot {7 \choose 1} = \boxed{294}$.

~northstar47

Feel free to edit this solution

## Solution 4

Starting at the origin, you can either first go up or to the right. If you go up first, you will end on the side opposite to it (the right side) and if you go right first, you will end up on the top. It can then be observed that if you choose the turning points in the middle $7 \times 7$ grid, that will automatically determine your start and ending points. For example, in the diagram if you choose the point $(3,2)$ and $(5,3)$, you must first move three up or two right, determining your first point, and move 5 up or 3 right, determining your final point. Knowing this is helpful because if we first move anywhere horizontally, we have $7$ points on each column to choose from and starting from left to right, we have $6,5,4,3,2,1$ points on that row to choose from. This gives us $7(6)+7(5)+7(4)+7(3)+7(2)+7(1)$ which simplifies to $7\cdot21$. The vertical case is symmetrical so we have $7\cdot21\cdot2 = \boxed{294}$

~KEVIN_LIU

## Solution 5

As in Solution 1, there are two cases: $RURUR$ or $URURU$. We will work with the first case and multiply by $2$ at the end. We use stars and bars; we can treat the $R$s as the stars and the $U$s as the bars. However, we must also use stars and bars on the $U$s to see how many different patterns of bars we can create for the reds. We must have $1$ bar in $8$ blacks, so we use stars and bars on the equation \[x + y = 8\]. However, each divider must have at least one black in it, so we do the change of variable $x' = x-1$ and $y' = x-1$. Our equation becomes \[x' + y' = 6\]. By stars and bars, this equation has $\binom{6 + 2 - 1}{1} = 7$ valid solutions. Now, we use stars and bars on the reds. We must distribute two bars amongst the reds, so we apply stars and bars to \[x + y + z = 8\]. Since each group must have one red, we again do a change of variables with $x' = x-1$, $y' = y-1$, and $z' = z-1$. We are now working on the equation \[x' + y' + z' = 5\]. By stars and bars, this has $\binom{5 + 3 - 1}{2} = 21$ solutions. The number of valid paths in this case is the number of ways to create the bars times the number of valid arrangements of the stars given fixed bars, which equals $21 \cdot 7 = 147$. We must multiply by two to account for both cases, so our final answer is $147 \cdot 2 = \boxed{294}$.

~ [cxsmi](https://artofproblemsolving.com/wiki/index.php/User:Cxsmi)

## Solution 6

We note that we either start with $R$ or $U$ and that these cases are symmetric, so we will simply consider the $R$ case and multiply by $2$ at the end. We make the key observation that making a path is the same as choosing two vertical lines and one horizontal line to mark our path; this gives us a unique path. Because we change directions exactly 4 times, we must travel at least 1 unit before turning, and we also must end by traveling at least one unit, so we cannot choose vertical lines that are on the edge of our grid. Similarly, we cannot do that for the horizontal line. Our final answer is simply choosing 2 vertical lines from 7 total, and choosing one horizontal line from 7 total, all multiplied by two. $2 \cdot \binom{7}{2} \cdot \binom{7}{1} = \boxed{294}.$

~those who know

## Solution 7

[](https://artofproblemsolving.com/wiki/index.php?title=File:2024-AIME-I-P6-S7.jpeg)

Our path must either go right, up, right, up, and right (RURUR) or up, right, up, right, and up (URURU). We will consider the RURUR case and multiply by 2 since they're symmetrical.

Label the $x$-axis from 0 to 8, starting at the origin and ending at the edge. For the first move (right), we can stop at point 1, 2, 3, 4, 5, 6, or 7.

Let's consider the choices for the first and third rightward moves. If we stop at point 7 on the first rightward move, when we get to the third move, we will have 0 choices for choosing a point to go right until; no matter what we do, if we stop at point 7 on the first move, the path will never have more than three turns (see diagram). If we stop at point 6, we will have 1 choice for the third move (we can stop going right until one point before the right edge of the grid for the third move and our path will have 4 turns). If we stop at point 5, we can stop going right until one or two points before the right edge of the grid for the third move. As we continue to move down points, the number of choices for the third rightward move increases by 1. This pattern continues until we stop at point 1 on the first move and have 6 choices for the third move. So, for the first and third moves, we have a total of \[0 + 1 + 2 + 3 + 4 + 5 + 6 = \frac{6 \cdot 7}{2} = 21\] choices.

For the second move (upward), we always have 7 choices to stop at (the top, one point before the top, two points before the top... 1 point from the bottom), and the fourth move will always have 1 choice, which is the move that reaches the final point.

Finally, we multiply by 2 to account for the URURU case, which gives us a total of $21 \cdot 7 \cdot 2 = \boxed{294}$ paths.

~[grogg007](https://artofproblemsolving.com/wiki/index.php/User:grogg007)
