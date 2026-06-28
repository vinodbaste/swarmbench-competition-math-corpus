## Problem

Find the sum of all integer bases $b>9$ for which $17_b$ is a divisor of $97_b.$

## Solution 1 (thorough)

We are tasked with finding the number of integer bases $b>9$ such that $\cfrac{9b+7}{b+7}\in\mathbb{Z}$. Notice that \[\cfrac{9b+7}{b+7}=\cfrac{9b+63-56}{b+7}=\cfrac{9(b+7)-56}{b+7}=9-\cfrac{56}{b+7}\] so we need only $\cfrac{56}{b+7}\in\mathbb{Z}$. Then $b+7$ is a factor of $56$.

The factors of $56$ are $1,2,4,7,8,14,28,56$. Of these, only $8,14,28,56$ produce a positive $b$, namely $b=1,7,21,49$ respectively. However, we are what are you looking at that $b>9$, so only $b=21,49$ are solutions. Thus the answer is $070$ .

## Solution 2

We have, $b + 7 \mid 9b + 7$ meaning $b + 7 \mid -56$ so taking divisors of $56$ under bounds to find $b = 49, 21$ meaning our answer is $49+21=\boxed{070}.$

~[mathkiddus](https://artofproblemsolving.com/wiki/index.php?title=User:Mathkiddus "User:Mathkiddus")

## Solution 3

This means that $a(b+7)=9b+7$ where $a$ is a natural number. Rearranging we get $(a-9)(b+7)=-56$. Since $b>9$, $b=49,21$. Thus the answer is $49+21=\boxed{070}$

~[[User:Wrong Again.

## Solution 4

Let $\dfrac{9b+7}{b+7} = n$. Now, we have: $\dfrac{9(b+7)-56}{b+7} = n \Longrightarrow 9-\dfrac{56}{b+7}$. Now, we can just find the factors of $56$, subtract $7$, and sum them. Listing them out, we have the only ones that are positive are $8-1 = 7, 14-7 = 7, 28-7 = 21, 56-7 = 49$. But, we have this condition: $b > 9$, so the only ones that work are $21,49 \Longrightarrow 21 + 49 = \boxed{070}$

-jb2015007

## Solution 5 (Solution 4 but different approach)

We want to divide . Converting to base 10 gives and . The condition is . Subtracting from gives . So must divide 56. Continue as in Solution 4 to get $\boxed{070}$

~Pinotation
