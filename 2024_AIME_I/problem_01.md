## Problem

Every morning Aya goes for a $9$-kilometer-long walk and stops at a coffee shop afterwards. When she walks at a constant speed of $s$ kilometers per hour, the walk takes her 4 hours, including $t$ minutes spent in the coffee shop. When she walks $s+2$ kilometers per hour, the walk takes her 2 hours and 24 minutes, including $t$ minutes spent in the coffee shop. Suppose Aya walks at $s+\frac{1}{2}$ kilometers per hour. Find the number of minutes the walk takes her, including the $t$ minutes spent in the coffee shop.

## Solution 1

$\frac{9}{s} + t = 4$ in hours and $\frac{9}{s+2} + t = 2.4$ in hours.

Subtracting the second equation from the first, we get,

$\frac{9}{s} - \frac{9}{s+2} = 1.6$

Multiplying by $(s)(s+2)$, we get

$9s+18-9s=18=1.6s^{2} + 3.2s$

Multiplying by 5/2 on both sides, we get

$0 = 4s^{2} + 8s - 45$

Factoring gives us

$(2s-5)(2s+9) = 0$, of which the solution we want is $s=2.5$.

Substituting this back to the first equation, we can find that $t = 0.4$ hours.

Lastly, $s + \frac{1}{2} = 3$ kilometers per hour, so

$\frac{9}{3} + 0.4 = 3.4$ hours, or $\framebox{204}$ minutes

-Failure.net

## Solution 2

The amount of hours spent while walking on the first travel is $\frac{240-t}{60}$. Thus, we have the equation $(240-t)(s) = 540$, and by the same logic, the second equation yields $(144-t)(s+2) = 540$. We have $240s-st = 540$, and $288+144s-2t-st = 540$. We subtract the two equations to get $96s+2t-288 = 0$, so we have $48s+t = 144$, so $t = 144-48s$, and now we have $(96+48s)(s) = 540$. The numerator of $s$ must evenly divide 540, however, $s$ must be less than 3. We can guess that $s = 2.5$. Now, $2.5+0.5 = 3$. Taking $\frac{9}{3} = 3$, we find that it will take three hours for the 9 kilometers to be traveled. The t minutes spent at the coffee shop can be written as $144-48(2.5)$, so t = 24. $180 + 24 =  \framebox{204}$. -sepehr2010
