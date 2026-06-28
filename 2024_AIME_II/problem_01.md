## Problem

Among the 900 residents of Aimeville, there are 195 who own a diamond ring, 367 who own a set of golf clubs, and 562 who own a garden spade. In addition, each of the 900 residents owns a bag of candy hearts. There are 437 residents who own exactly two of these things, and 234 residents who own exactly three of these things. Find the number of residents of Aimeville who own all four of these things.

## Solution 1

Let $w,x,y,z$ denote the number of residents who own $1,2,3$ and $4$ of these items, respectively. We know $w+x+y+z=900$, since there are $900$ residents in total. This simplifies to

$w+z=229$, since we know $x=437$ and $y=234$.

Now, we set an equation of the total number of items. We know there are $195$ rings, $367$ clubs, $562$ spades, and $900$ candy hearts. Adding these up, there are $2024$ (wow! the year!) items in total. Thus, $w+2x+3y+4z=2024$ since we are not adding the number of items each group of people contributes, and this must be equal to the total number of items.

Plugging in $x$ and $y$ once more, we get $w+4z=448$. Solving $w+z=229$ and $w+4z=448$, we get $z=\boxed{073}$

-Westwoodmonster

## Solution 2

We know that there are $195$ diamond rings, $367$ golf clubs, and $562$ garden spades, so we can calculate that there are $195+367+562=1124$ items, with the exclusion of candy hearts which is irrelevant to the question. There are $437$ people who owns $2$ items, which means $1$ item since candy hearts are irrelevant, and there are $234$ people who own $2$ items plus a bag of candy hearts, which means that the 234 people collectively own $234*2=468$ items. We can see that there are $1124-437-468=219$ items left, and since the question is asking us for the people who own $4$ items, which means $3$ items due to the irrelevance of candy hearts, we simply divide $219$ by $3$ and get $219/3=\boxed{073}$.

~Callisto531

## Solution 3

Let $a$ be the number of people who have exactly one of these things and let $b$ be the number of people who have exactlty four of these objects. We have $a + 437 + 234 + d = 900,$ so $a + d = 229.$

Including those who have more than one object, we have \[195 + 367 + 562 + 900 = a + 2\cdot 437 + 3\cdot 234 + 4d.\] This is because we count those who own exactly $2$ objects twice, those who own $3$ thrice, and those who own $4$ four times. Solving gives $a + 4d = 448.$

Solving the system $a + 4d = 448, a + d = 229$ gives $3d = 219,$ so $d = \boxed{\textbf{(073)}}.$

-Benedict T (countmath1)
