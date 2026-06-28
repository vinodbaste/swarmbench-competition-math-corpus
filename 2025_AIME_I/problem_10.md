## Problem

The $27$ cells of a $3 \times 9$ grid are filled in using the numbers $1$ through $9$ so that each row contains $9$ different numbers, and each of the three $3 \times 3$ blocks heavily outlined in the example below contains $9$ different numbers, as in the first three rows of a Sudoku puzzle.

[asy] unitsize(20);  add(grid(9,3));  draw((0,0)--(9,0)--(9,3)--(0,3)--cycle, linewidth(2)); draw((3,0)--(3,3), linewidth(2)); draw((6,0)--(6,3), linewidth(2));  real a = 0.5;  label("5",(a,a)); label("6",(1+a,a)); label("1",(2+a,a)); label("8",(3+a,a)); label("4",(4+a,a)); label("7",(5+a,a)); label("9",(6+a,a)); label("2",(7+a,a)); label("3",(8+a,a));  label("3",(a,1+a)); label("7",(1+a,1+a)); label("9",(2+a,1+a)); label("5",(3+a,1+a)); label("2",(4+a,1+a)); label("1",(5+a,1+a)); label("6",(6+a,1+a)); label("8",(7+a,1+a)); label("4",(8+a,1+a));  label("4",(a,2+a)); label("2",(1+a,2+a)); label("8",(2+a,2+a)); label("9",(3+a,2+a)); label("6",(4+a,2+a)); label("3",(5+a,2+a)); label("1",(6+a,2+a)); label("7",(7+a,2+a)); label("5",(8+a,2+a));  [/asy]

The number of different ways to fill such a grid can be written as $p^a \cdot q^b \cdot r^c \cdot s^d$ where $p$, $q$, $r$, and $s$ are distinct prime numbers and $a$, $b$, $c$, $d$ are positive integers. Find $p \cdot a + q \cdot b + r \cdot c + s \cdot d$.

## Solution 1

We will fill out the grid row by row. Note that there are $9!=2^7\cdot 3^4\cdot 5\cdot 7$ ways to fill out the first row. For the second row, we will consider a little casework. WLOG let the first row be $123 | 456 | 789$ (bars indicate between the $3\times 3$ squares).

Case 1: Every number from the first square goes to the second square. Then there is $1$ way along with $6^3$ orderings giving us $6^3$ cases.

Case 2: Two of the first numbers go in the second square and the last number goes in the third. This results in $3\cdot3\cdot3$ ways to put the numbers along with $6^3$ orderings. Thus there are $27\cdot 6^3$ cases.

Note that we didn't consider $2$ cases but these are symmetric so the number of ways to fill the second row is $56\cdot 6^3$.

There is $1$ way to place the last numbers in with $6^3$ orderings. Thus there are $2^7\cdot 3^4\cdot 5\cdot 7 \cdot 56\cdot 6^3 \cdot 6^3 = 2^{16}\cdot 3^{10}\cdot 5^1\cdot 7^2$ ways to fill out our mini Sudoku puzzle. Thus the answer is $2\cdot 16+3\cdot 10 + 5\cdot 1+7\cdot 2 = \boxed{081}.$

~ [zhenghua](https://artofproblemsolving.com/wiki/index.php?title=User:Zhenghua "User:Zhenghua")

## Solution 2

We will call the sudoku blocks 1-3 from left to right, and rows 1-3 from up to down. Lets start from the entire first block - we have $9!$ options of choosing it as you just arrange the numbers.

Starting from the second block, we need to do some casework. We need to discuss the different possibilities that the first row of the second block contains.

Case 1: The first row of the second block has the exact 3 numbers from the second row of first block.

We have $P^3_3$ choices as you just arrange the numbers for the first row.

Then, considering the second row of the second block, you must take the exact 3 numbers from the third row of first block, and we could arrange then in different order. This will gives another $P^3_3$ choices.

The third row of the second block must contain the 3 numbers of the first row in first block. We will then have another $P^3_3$ of arranging the numbers.

Summing up case 1, we have $P^3_3 \cdot P^3_3 \cdot P^3_3 = 6^3 = 2^3 \cdot 3^3$.

Case 2: The first row of second block contains 2 numbers from the second row of first block and 1 number from the third row of first block.

To satisfy my case 2 statement, we will need $\binom{3}{1}\cdot\binom{3}{2}\cdot P^3_3$.

To look at the second row of the second block, we must first choose the remaining 2 numbers that haven't got picked from the third row of first block, or else the sudoku won't work. This means that we can only pick 1 remaining number from the numbers in first row of first block - because the 6th number is the number in the second row and sudoku doesn't allow repeated numbers in a row. Therefore, the second row has the choice of $\binom{2}{2}\binom{3}{1}P^3_3$.

The third row of the second block gets the remaining 3 numbers that is left from the second block, which is $P^3_3$.

Summing up case 2, we have $\binom{3}{1}\binom{3}{2}P^3_3\binom{2}{2}\binom{3}{1}P^3_3P^3_3= 3^3\cdot2^3\cdot3^3 = 2^3\cdot3^6$.

Notice that case 3 (3 numbers repeating from the third row of first block) and case 4 (2 numbers from block 1 row 3 and 1 number from block 1 row 2) are symmetric to case 1 and 2, respectively. Therefore the second block results with $(1 + 3^3 + 1 + 3^3) \cdot 2^3 \cdot 3^3 = 56 \cdot 2^3 \cdot 3^3 = 7 \cdot 2^6 \cdot 3^3$

Third block: easy

Notice that the 6 numbers of each row has been filled already, the choices of the rest 3 numbers has been done. You only need to arrange them in different orders, which gives $P^3_3P^3_3P^3_3= 2^3 * 3^3$.

In total, our answer is:

$9! \cdot 7 \cdot 2^6 \cdot 3^3 \cdot 2^3 \cdot 3^3$$=2 \cdot 3 \cdot 2^2 \cdot 5 \cdot 2 \cdot 3 \cdot 7 \cdot 2^3 \cdot 3^2 \cdot 7 \cdot 2^9 \cdot 3^6$$=2^{16} \cdot 3^{10} \cdot 5 \cdot 7^2$

Our required answer is therefore $2 \cdot 16 + 3 \cdot 10 + 5 \cdot 1 + 7 \cdot 2 = 32 + 30 + 5 + 14 = \boxed{081}$

~Mitsuihisashi14

Minor latex edits by [T3CHN0B14D3](https://artofproblemsolving.com/wiki/index.php?title=User:T3chn0b14d3&action=edit&redlink=1 "User:T3chn0b14d3 (page does not exist)")

## Solution 3 (Can be very quick but explained well)

First, assume the first row is ordered $1, 2, 3, 4, 5, 6, 7, 8, 9$.

This contributes $9!$ cases.

Next, assume the first box has the remaining numbers, $4, 5, 6, 7, 8, 9$ ordered in some way. This contributes $6! = 720$ cases for the first box.

Third, consider each of the remaining $1$ x $3$ boxes as separate, and they each contribute $3!$ cases.

However, we are undercounting.

The second box may have to be multiplied by 3 if the first box did not define the numbers that go in each $1$ x $3$ box. The third box will always have its rows defined. If the first box is placed such that $4, 5, 6$ are in the same $1$ x $3$ box, and $7, 8, 9$ are in the same $1$ x $3$ box, then the numbers in the second box will be defined and we do not need to multiply by 3. This happens for $2 \cdot 3! \cdot 3! = 72$ cases, or $72 / 720 = 1 / 10$ of the time. Therefore, $9 / 10$ of the time, we need to multiply by another 3. Adding this up, to account for undercounting, we must multiply the total by $1 / 10 + 3(9 / 10) = 28 / 10 = 14 / 5$.

Our final total is $9! \cdot 6! \cdot (3!)^4 \cdot 14 / 5 = (2^7 \cdot 3^4 \cdot 5^1 \cdot 7^1) (2^4 \cdot 3^2 \cdot 5^1) (2^4 \cdot 3^4) \cdot 2 \cdot 7 / 5 = 2^{16} \cdot 3^{10} \cdot 5^1 \cdot 7^2$.

The desired solution is $2\cdot16 + 3\cdot10 + 5\cdot1 + 7\cdot2 = \boxed{081}$

~ILoveMath31415926535

Minor latex edits by Wen_Liang

## Solution 4

Assume the first row of the grid is $123|456|789.$ Note that the numbers in each $3$x$1$ block can be ordered in $3!$ ways amongst themselves and they will still stay in the same row and $3$x$3$ block. There are $6$ unfilled $3$x$1$ blocks, so we'll multiply by $(3!)^6$ at the end. We’ll also have to multiply by $9!$ because we fixed the first row of the grid and there are $9!$ ways to permute the numbers in it.

Let's do casework on where $789$ can be in the second row of the grid.

**Case 1:** All three numbers $789$ are in the second row of the same $3$x$3$ block

$789$ can be the second row of one of two $3$x$3$ blocks (it can't be the second row of the third $3$x$3$ block since the top row of that one already has $789$ in it). WLOG say $789$ is the second row of the first $3$x$3$ block. Then $123$ must be the second row of the second $3$x$3$ block and $456$ must be the second row of the third $3$x$3$ block. Since the second row is completely filled out we are done. So this case gives us 2 ways.

**Case 2:** Two of the numbers of $789$ are in the second row of one $3$x$3$ block, the other left out number is in the second row of the other $3$x$3$ block

We can choose the "left out" number in $\binom{3}{1} = 3$ ways, and it can go in the second row of one of two blocks (remember, it can't be in the third $3$x$3$ block since the top row of that one already has $789$ in it). So we have $3\cdot 2 = 6$ ways. WLOG say the left out number is $9,$ and we put $9$ in the second row of the first $3$x$3$ block, so $7$ and $8$ are in the second row of the second $3$x$3$ block. Now, consider the numbers $456.$ We can choose two of these numbers to join $9$ in the second row of the first $3$x$3$ block in $\binom{3}{2} = 3$ ways. WLOG say we chose $4$ and $5$. Then $6$ must be in the second row of the third $3$x$3$ block. Now we can choose one number out of $1,2,3$ to join $7$ and $8$ in the second row of the second block in $\binom{3}{1} = 3$ ways. WLOG say we chose $1.$ Then $2$ and $3$ must be in the second row of the third $3$x$3$ block with $6.$ Now the second row is completely filled out, so we are done. We have $6 \cdot 3 \cdot 3 = 54$ ways for this case.

The total number of ways is $(54 + 2) \cdot (3!)^6 \cdot 9! = 2^{16} \cdot 3^{10} \cdot 5^1 \cdot 7^2,$ so the answer is $32 + 30 + 5 + 14 = \boxed{81}.$

~[grogg007](https://artofproblemsolving.com/wiki/index.php?title=User:Grogg007 "User:Grogg007")
