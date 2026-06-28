## Problem

A list of positive integers has the following properties:

$\bullet$ The sum of the items in the list is $30$.

$\bullet$ The unique mode of the list is $9$.

$\bullet$ The median of the list is a positive integer that does not appear in the list itself.

Find the sum of the squares of all the items in the list.

## Quick note

For those who don't understand why we say the list must have 4 elements.

Suppose there are $2n$ elements in the set. Then, the remaining $2n-2$ elements must sum to 12. So, say instead there were $2n=6$ elements in the set. Then, we need four integers that add to 12. However, the unique mode is 9, which appears twice. Thus, every other number must appear once. The smallest sum of four distinct numbers is $1+2+3+4=10$. To obtain 12, we sub out 4 for 6. However, now we have a problem! The median of the set isn't an integer. Thus, 6 elements cannot work.

Now, say there are $2n = 8$ elements. Like in the previous case, the unique mode is 9, which appears twice. Along with that fact, each number must be distinct. The smallest sum of $8-2=6$ numbers is 21, which is not even close to 12. Thus, we can conclude that as $2n \rightarrow \infty$, the distinct sum $S >> 12$ ($>>$ means much larger). Thus, the case of $2n=8$ doesn't work, and all cases of $2n > 8$ don't work.

So, we have either $2n = 2,4,6$, in which we know $2n \neq 2,6$, and therefore $2n$ must be 4, so there must be 4 elements in the set $\square$.

~Pinotation

## Solution 1

The third condition implies that the list's size must be an even number, as if it were an odd number, the median of the list would surely appear in the list itself.

Therefore, we can casework on what even numbers work.

Say the size is 2. Clearly, this doesn't work as the only list would be $\{9, 9\}$, which doesn't satisfy condition 1.

If the size is 4, then we can have two $9$s, and a remaining sum of $12$. Since the other two values in the list must be distinct, and their sum must equal $30-18=12$, we have that the two numbers are in the form $a$ and $12-a$. Note that we cannot have both values greater than $9$, and we cannot have only one value greater than $9$, because this would make the median $9$, which violates condition 3. Since the median of the list is a positive integer, this means that the greater of $a$ and $12-a$ must be an odd number. The only valid solution to this is $a=5$. Thus, our answer is $5^2+7^2+9^2+9^2 = \boxed{236}$. ~akliu

## Solution 2

If there were an odd number of elements, the median would be in the set. Thus, we start with 4 elements. For 9 to be the mode, there must be 2 9s. For 9 to not be the median, either both numbers are greater than 9, or both numbers are less than 9. Clearly, both numbers must be less. From here, the numbers are clearly $(5,7,9,9)$, and we add their squares to get $\boxed{236}$ -westwoodmonster

## Solution 3

We can tell that the amount of integers in the list is an even number, because the median of the list doesn't appear in the list. The mode or the most frequent number in the list is 9, so there is more than one 9. We start with three 9's, because they will be easy to eliminate the cases. The list should look like \[9,9,9,x\] or \[x,9,9,9\] in which both cases are impossible because the median is 9, which shows up in the list. The next case is 2 9's which looks like: \[x,y,9,9\] or \[9,9,x,y\] Where $x+y=12$ Because both elements of $x$ and $y$ cannot be greater than 9, the set looks like \[x,y,9,9\] and the only number that satisfy this case is 4,8 and 5,7 not 6 and 6 because 9 is the unique mode. it also states the median is an integer, so the pair is 5 and 7 and the set looks like \[5,7,9,9\] and \[5^2+7^2+9^2+9^2=236\]

-Multpi12

## Solution 4 (complete reasoning)

Since the median is not in the list, there must not be an odd number of elements. Suppose the list has two elements. To meet the mode condition, both must equal $9$, but this does not satisfy the other conditions.

Next, suppose the list has six elements. If there were at least three $9$s, then the other elements would sum to at most $30-27=3$. Since the elements are positive integers, this can only be achieved with the set $\{1,1,1,9,9,9\}$, which violates the unique mode condition. Therefore, there must be exactly two $9$s, and the other four elements must be distinct to satisfy the unique mode condition. Two sets of four unique positive integers add to $12$: $\{1,2,3,6\}$ and $\{1,2,4,5\}$. Neither can act as the remaining four elements since both possibilities violate the constraint that the median is an integer.

Next, suppose the list had at least eight elements. For the sake of contradiction, suppose the third-largest element was at least $9$. Then, since every element is a positive integer, the minimum sum would be $1+1+1+1+1+9+9+9>30$. So, to satisfy the unique mode condition, there must be exactly two $9$s, and the other elements must be distinct. But then the minimum sum is $1+2+3+4+5+6+9+9>30$, so the sum constraint can never be satisfied. From these deductions, we conclude that the list has exactly four elements.

Note that no element can appear three times in the list, or else the middle-two-largest elements would be equal, violating the condition that the median is not in the list. Therefore, to satisfy the unique mode condition, the list contains two $9$s and two other distinct integers that add to $30-18=12$. Five sets of two unique positive integers add to $12$: $\{1,11\}$, $\{2,10\}$, $\{3,9\}$, $\{4,8\}$, and $\{5,7\}$. The first four options violate the median condition (either they make the median one of the list elements, or they make the median a non-integer). Thus, the set must be $\{5,7,9,9\}$, and the sum of the squares of these elements is $25+49+81+81=\boxed{236}$.

-ltihoen
