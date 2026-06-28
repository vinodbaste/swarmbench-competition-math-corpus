## Problem

There is a collection of $25$ indistinguishable white chips and $25$ indistinguishable black chips. Find the number of ways to place some of these chips in the $25$ unit cells of a $5\times5$ grid such that:

*   each cell contains at most one chip
*   all chips in the same row and all chips in the same column have the same colour
*   any additional chip placed on the grid would violate one or more of the previous two conditions.

## Solution 1

The problem says "some", so not all cells must be occupied. We start by doing casework on the column on the left. There can be 5,4,3,2, or 1 black chip. The same goes for white chips, so we will multiply by 2 at the end. There is $1$ way to select $5$ cells with black chips. Because of the 2nd condition, there can be no white, and the grid must be all black- $1$ way . There are $5$ ways to select 4 cells with black chips. We now consider the row that does not contain a black chip. The first cell must be blank, and the remaining $4$ cells have $2^4-1$ different ways, since each cell can be white or blank($-1$ comes from all blank). This gives us $75$ ways. Notice that for 3,2 or 1 black chips on the left there is a pattern. Once the first blank row is chosen, the rest of the blank rows must be ordered similarly. For example, with 2 black chips on the left, there will be 3 blank rows. There are 15 ways for the first row to be chosen, and the following 2 rows must have the same order. Thus, The number of ways for 3,2,and 1 black chips is $10*15$, $10*15$, $5*15$. Adding these up, we have $1+75+150+150+75 = 451$. Multiplying this by 2, we get $\boxed{902}$. ~wikimonster

## Solution 2

Note that the answer is equivalent to the number of ways to choose rows and columns that the white chips occupy, as once those are chosen, there is only one way to place the chips, and every way to place the chips corresponds to a set of rows and columns occupied by the white pieces.

If the white pieces occupy none of the rows, then because they don't appear on the board, they will not occupy any of the columns. Similar logic can be applied to show that if white pieces occupy all of the rows, they will also occupy all of the columns.

The number of sets of rows and columns that white can occupy are $2^{5} - 2 = 30$ each, accounting for the empty and full set. So, including the board with 25 white pieces and the board with 25 black pieces, the answer is $30^{2}+2 = \boxed{902}$

## Solution 3

Case 1: All chips on the grid have the same color.

In this case, all cells are occupied with chips with the same color. Therefore, the number of configurations in this case is 2.

Case 2: Both black and white chips are on the grid.

Observation 1: Each colored chips must occupy at least one column and one row.

This is because, for each given color, there must be at least one chip. Therefore, all chips placed in the cells that are in the same row or the same column with this given chip must have the same color with this chip.

Observation 2: Each colored chips occupy at most 4 rows and 4 columns.

This directly follows from Observation 1.

Observation 3: For each color, if all chips in this color occupy columns with $x$-coordinates $\left\{ x_1, \cdots, x_m \right\}$ and rows with $y$-coordinates $\left\{ y_1, \cdots, y_n \right\}$, then every cell $\left( x, y \right)$ with $x \in \left\{ x_1, \cdots , x_m \right\}$ and $y \in \left\{ y_1, \cdots , y_n \right\}$ is occupied by a chip with the same color.

This is because, if there is any cell in this region occupied by a chip with a different color, it violates Condition 2. If there is any cell in this region that is empty, then it violates Condition 3.

Observation 4: For each color, if all chips in this color occupy columns with $x$-coordinates $\left\{ x_1, \cdots, x_m \right\}$ and rows with $y$-coordinates $\left\{ y_1, \cdots, y_n \right\}$, then every cell $\left( x, y \right)$ with $x \notin \left\{ x_1, \cdots , x_m \right\}$ and $y \in \left\{ y_1, \cdots , y_n \right\}$, or $x \in \left\{ x_1, \cdots , x_m \right\}$ and $y \notin \left\{ y_1, \cdots , y_n \right\}$ is empty.

This is because, if there is any cell in this region occupied by a chip with a different color, it violates Condition 2.

Observation 5: For each color, if all chips in this color occupy columns with $x$-coordinates $\left\{ x_1, \cdots, x_m \right\}$ and rows with $y$-coordinates $\left\{ y_1, \cdots, y_n \right\}$, then every cell $\left( x, y \right)$ with $x \notin \left\{ x_1, \cdots , x_m \right\}$ and $y \notin \left\{ y_1, \cdots , y_n \right\}$ is occupied by chips with the different color.

This follows from Condition 3.

By using the above observations, the number of feasible configurations in this case is given by

Putting all cases together, the total number of feasible configurations is $2 + 900 =  \boxed{\textbf{(902) }}$.

~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Solution 4 (Notationless Solution 3)

We rely on 3 simple observations: \[~~~~~~~~~\] Observation 1: An intersection of a row and a column must be filled if they are the same color. Proof: If not, we can just fill it with a chip of the color, violating rule #3. \[~~~~~~~~~\] Observation 2: An intersection of a row and column must not be filled if they are of different colors. Proof: If it is filled, it would violate rule #2, as it will be different from one of the colors of the row/column that intersect. \[~~~~~~~`\] Observation 3: Every row and column must have a defined color. Proof: If it didn't, there would be no chips in this row/column. Then, a chip could be placed in any intersection with this row/column in the intersecting row/column's color, violating rule #3. \[~~~~~~~~~~~~~~\] From observations 1 and 2, we could tile the board given the colors of its rows and columns, and it is clear that every tiling must correspond to a selection of colors for the rows and columns. However, observation 3 means we can have all rows be the same color or all columns be the same color but we can have all rows and columns be the same color, as if all rows were white but a column was black, that column can't have any chips, and it doesn't have a defined color, which is not allowed. There are exactly $2^5-2=30$ ways we can color the rows such that they are not all the same color, and $30$ ways for the columns. We must add back $2$ for when all the rows and columns are the same color, so the answer is $30^2+2=\boxed{902}.$

~BS2012

## Solution 5

Observe how each grid is uniquely determined by a choice of "black rows" and "white rows." That is, every intersection of a black row with a black column will be a black cell, and likewise with the white rows and columns, but every intersection of a black row with a white column will remain empty.

However, if we have all the rows or columns be black or white, then the other dimension will become redundant. For example, if all of our rows are black, the ways the columns are colored doesn't matter because the whole grid will have to be filled with only black cells.

Hence, the number of sets of rows and columns that white can occupy are $2^{5} - 2 = 30$ each. But including the board with 25 white pieces and the board with 25 black pieces, the answer is $30^{2}+2 = \boxed{902}$.

~xHypotenuse

## Solution 6

We can denote X as a black pieces, O as a white pieces, and _ as a blank pieces.

We can fill up the left column in any of the 60 ways (2 colors and 30 arrangements as we cannot have the empty column as it will violate the condition, and filling it up all the way only gives us 1 way to fill the grid), WLOG we can fill it out like the following:

X _ _ _ _

_ _ _ _ _

X _ _ _ _

X _ _ _ _

_ _ _ _ _

Now, let's examine the topmost blank row, in which we can fill out in 15 ways in the color that we didn't use when filling out the leftmost column (we cannot fill it out on the very left since that would violate the condition, and we cannot have an empty row as it would violate the condition). WLOG, we can fill it out like the following:

X _ _ _ _

_ _ O _ O

X _ _ _ _

X _ _ _ _

_ _ _ _ _

However, notice that there's only 1 way to fill out all the pieces given the arrangement above. This involves filling any row with an O as how we filled out the topmost row, and strategically filling out the rows with an X's such that they do not share any column with an O:

X X _ X _

_ _ O _ O

X X _ X _

X X _ X _

_ _ O _ O

So, we have a total of $60\times15$ ways to fill out the board, but we also need to add 2 cases if it's completely covered with a white or black piece, giving us $\boxed{902}$.

~aleyang
