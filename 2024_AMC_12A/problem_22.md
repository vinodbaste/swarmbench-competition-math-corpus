_The following problem is from the [2024 AMC 10A #25](https://artofproblemsolving.com/wiki/index.php/2024\_AMC\_12A\_Problems/Problem\_22) and [2024 AMC 12A #22](https://artofproblemsolving.com/wiki/index.php?title=2024\_AMC\_12A\_Problems/Problem\_22 "2024 AMC 12A Problems/Problem 22"), so those problems redirect to this page._
## Problem

The figure below shows a dotted grid $8$ cells wide and $3$ cells tall consisting of $1''\times1''$ squares. Carl places $1$-inch toothpicks along some of the sides of the squares to create a closed loop that does not intersect itself. The numbers in the cells indicate the number of sides of that square that are to be covered by toothpicks, and any number of toothpicks are allowed if no number is written. In how many ways can Carl place the toothpicks? [asy] size(6cm); for (int i=0; i<9; ++i) {   draw((i,0)--(i,3),dotted); } for (int i=0; i<4; ++i){   draw((0,i)--(8,i),dotted); } for (int i=0; i<8; ++i) {   for (int j=0; j<3; ++j) {     if (j==1) {       label("1",(i+0.5,1.5)); }}} [/asy]$\textbf{(A) }130\qquad\textbf{(B) }144\qquad\textbf{(C) }146\qquad\textbf{(D) }162\qquad\textbf{(E) }196$

## Solution 1 (Best Motivated)

Observations:

1. You can not have a vertical line in any place other than the first two columns and the last two columns. If we did, we would have at least one of the middle cells with toothpicks along more than one side, which would violate the conditions of the problem.

2. There are two cases that look completely different. We can have a long horizontal box that spans all eight cells either on top of or below the middle cells, or we have to have a shape that looks like a rectangle, except with a few places "pushed" in.

Thus, using casework, we can split the task of finding those rectangles with squiggly edges into 3 cases.

For case 1, we assume that the green lines shown below are given (always have toothpicks on them). In effect, we will use all eight columns.

[](https://artofproblemsolving.com/wiki/index.php?title=File:Scrasdfasd.png)

[](https://artofproblemsolving.com/wiki/index.php?title=File:Screenshot_2024-11-08_192200.png)

The only toothpicks we can place that will connect to the red lines are to go horizontally inward:

[](https://artofproblemsolving.com/wiki/index.php?title=File:Screenshot_2024-11-08_192516.png)

Now, concentrate on the first row of squares. A toothpick can be placed on either the bottom or top and connected to a continuous squiggle by adding vertical toothpicks:

[](https://artofproblemsolving.com/wiki/index.php?title=File:Screenshot_2024-11-08_193401.png)

How many squiggles are possible?

[](https://artofproblemsolving.com/wiki/index.php?title=File:Screenshot_2024-11-08_194804.png)

We can summarize this by giving a high squiggle position a 1 and a low position a 0, thus we have a 6-digit binary sequence. Thus, we can have $2^6=64$ ways to make this squiggle. (The binary is not absolutely necessary, but it works.)

Case 2: We can also pull in one of the sides, thus we can have a squiggle with 5 binary digits, which only uses the first or last 7 columns:

[](https://artofproblemsolving.com/wiki/index.php?title=File:Screenshot_2024-11-08_195135.png)

[](https://artofproblemsolving.com/wiki/index.php?title=File:Screenshot_2024-11-08_195553.png)

Here, we only have 5 binary digits to work with, so there are $2^5=32$ ways to make this squiggle for each individual subcase. There are two subcases, one with the first 7 columns, and the other with the last 7, so we have a total of $32\cdot 2 = 64$ arrangements in this case.

Case 3: We can use an even smaller section. Using only the middle 6 columns gives us a 4-wide squiggle:

[](https://artofproblemsolving.com/wiki/index.php?title=File:Screenshot_2024-11-08_195945.png)

Thus, there are $2^4=16$ ways to make this squiggle.

These three cases together cover all loops of this form. If we try to bring the square bracket like shapes on each side any closer, there will be some middle cells that do not touch any toothpicks. Adding up all our cases for these types of shapes: $64+32+32+16=144$.

However, there are two more ways to draw a qualifying shape:

[](https://artofproblemsolving.com/wiki/index.php?title=File:Screenshot_2024-11-08_200416.png)

We can draw a rectangle like that in the first row or third row. Thus, we have a total of $144+2=\boxed{\textbf{(C) }146}$ ways.

A note to (potential) editors: This answer was not made to be concise or especially professional. It was made to explicitly explain this problem in a way so that it is easy to understand and follow.

~hermanboxcar5

Notes: Remember these are the ONLY possible cases. It is impossible to cross through the rows of boxes of ones (in a snake like pattern) to connect the loop around the bottom since then the loop would intersect itself.

We are not undercounting by only counting the binary digits on the top. Consider the top squiggle. Each middle square must and can only come in contact with one toothpick, so if the top squiggle doesn't touch a specific middle cell, the bottom squiggle must to ensure that all squares touch one toothpick. ~juwushu

~LeonQS (additional clarity and precision)

## Solution 2 (Cheese)

Notice that for any case where the closed loop does not connect from the top side of the ones and bottom side of the ones, there are two of these cases. A cheese solution can be found from this; noting that B and C are the only two options close to each other, and, being two apart, with people likely to forget this case, $\boxed{\textbf{(C) }146}$ is likely to be the correct answer. Cheese solution done by [juwushu](https://artofproblemsolving.com/wiki/index.php?title=User:Juwushu "User:Juwushu").

## Solution 3 (Observation)

We have $2$ cases where the loop does not go through the middle.

If the loop goes through the middle, we must have a full column on $(0,8),(0,7),(1,8),(1,7).$ Then we have $6,5,5,4$ empty middle squares. For each one we can have one on top or one on bottom, so $2^6+2^5+2^5+2^4=144.$ Notice that for each case of fixed toothpicks, there is only one way to form the loop. Then we just add $2+144=\boxed{\textbf{(C) } 146.}$

~nevergonnagiveup

## See Also

**[2024 AMC 10A](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A "2024 AMC 10A")** (**[Problems](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems "2024 AMC 10A Problems")** • **[Answer Key](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Answer_Key "2024 AMC 10A Answer Key")** • [Resources](https://artofproblemsolving.com/community/c13))
Preceded by

**[2023 AMC 10B Problems](https://artofproblemsolving.com/wiki/index.php?title=2023_AMC_10B_Problems "2023 AMC 10B Problems")**Followed by

**[2024 AMC 10B Problems](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10B_Problems "2024 AMC 10B Problems")**
[1](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_1 "2024 AMC 10A Problems/Problem 1")**•**[2](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_2 "2024 AMC 10A Problems/Problem 2")**•**[3](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_3 "2024 AMC 10A Problems/Problem 3")**•**[4](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_4 "2024 AMC 10A Problems/Problem 4")**•**[5](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_5 "2024 AMC 10A Problems/Problem 5")**•**[6](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_6 "2024 AMC 10A Problems/Problem 6")**•**[7](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_7 "2024 AMC 10A Problems/Problem 7")**•**[8](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_8 "2024 AMC 10A Problems/Problem 8")**•**[9](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_9 "2024 AMC 10A Problems/Problem 9")**•**[10](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_10 "2024 AMC 10A Problems/Problem 10")**•**[11](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_11 "2024 AMC 10A Problems/Problem 11")**•**[12](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_12 "2024 AMC 10A Problems/Problem 12")**•**[13](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_13 "2024 AMC 10A Problems/Problem 13")**•**[14](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_14 "2024 AMC 10A Problems/Problem 14")**•**[15](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_15 "2024 AMC 10A Problems/Problem 15")**•**[16](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_16 "2024 AMC 10A Problems/Problem 16")**•**[17](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_17 "2024 AMC 10A Problems/Problem 17")**•**[18](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_18 "2024 AMC 10A Problems/Problem 18")**•**[19](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_19 "2024 AMC 10A Problems/Problem 19")**•**[20](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_20 "2024 AMC 10A Problems/Problem 20")**•**[21](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_21 "2024 AMC 10A Problems/Problem 21")**•**[22](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_22 "2024 AMC 10A Problems/Problem 22")**•**[23](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_23 "2024 AMC 10A Problems/Problem 23")**•**[24](https://artofproblemsolving.com/wiki/index.php?title=2024_AMC_10A_Problems/Problem_24 "2024 AMC 10A Problems/Problem 24")**•**[25](https://artofproblemsolving.com/wiki/index.php/2024_AMC_12A_Problems/Problem_22)
**[All AMC 10 Problems and Solutions](https://artofproblemsolving.com/wiki/index.php?title=AMC_10_Problems_and_Solutions "AMC 10 Problems and Solutions")**

*   [AMC 10](https://artofproblemsolving.com/wiki/index.php?title=AMC_10 "AMC 10")
*   [AMC 10 Problems and Solutions](https://artofproblemsolving.com/wiki/index.php?title=AMC_10_Problems_and_Solutions "AMC 10 Problems and Solutions")
*   [Mathematics competitions](https://artofproblemsolving.com/wiki/index.php?title=Mathematics_competitions "Mathematics competitions")
*   [Mathematics competition resources](https://artofproblemsolving.com/wiki/index.php?title=Mathematics_competition_resources "Mathematics competition resources")

[](https://artofproblemsolving.com/wiki/index.php?title=File:AMC_Logo.png)
