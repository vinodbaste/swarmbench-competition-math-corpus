## Problem

The product\[\prod^{63}_{k=4} \frac{\log_k (5^{k^2 - 1})}{\log_{k + 1} (5^{k^2 - 4})} = \frac{\log_4 (5^{15})}{\log_5 (5^{12})} \cdot \frac{\log_5 (5^{24})}{\log_6 (5^{21})}\cdot \frac{\log_6 (5^{35})}{\log_7 (5^{32})} \cdots \frac{\log_{63} (5^{3968})}{\log_{64} (5^{3965})}\]is equal to $\tfrac mn,$ where $m$ and $n$ are relatively prime positive integers. Find $m + n.$

## Solution 1

We can rewrite the equation as:

Desired answer: $93 + 13 = \boxed{106}$

(Feel free to correct any $\LaTeX$ and formatting.)

~ Mitsuihisashi14

~ $\LaTeX$ by [Tacos_are_yummy_1](https://artofproblemsolving.com/wiki/index.php/User:Tacos_are_yummy_1)

~ Additional edits by [aoum](https://artofproblemsolving.com/wiki/index.php/User:Aoum)

## Solution 2

We can move the exponents to the front of the logarithms like this: Now we multiply the logs and fractions separately. Let's do it for the logs first: Now fractions: Multiplying these together gets us the original product, which is $\frac{31}{13} \cdot 3 = \frac{93}{13}$. Thus $m+n=\boxed{106}$.

~ Edited by [aoum](https://artofproblemsolving.com/wiki/index.php/User:Aoum)

## Solution 3

Using logarithmic identities and the change of base formula, the product can be rewritten as \[\prod_{k=4}^{63}\frac{k^2-1}{k^2-4}\frac{\log(k+1)}{\log(k)}\]. Then we can separate this into two series. The latter series is a telescoping series, and it can be pretty easily evaluated to be $\frac{\log(64)}{\log(4)}=3$. The former can be factored as $\frac{(k-1)(k+1)}{(k-2)(k+2)}$, and writing out the first terms could tell us that this is a telescoping series as well. Cancelling out the terms would yield $\frac{5}{2}\cdot\frac{62}{65}=\frac{31}{13}$. Multiplying the two will give us $\frac{93}{13}$, which tells us that the answer is $\boxed{106}$.

## Solution 4 (thorough)

The product is equal to $\prod^{63}_{k=4} \frac{(k-1)(k+1)\log_k 5}{(k-2)(k+2)\log_{k + 1} 5}$ from difference of squares and properties of logarithms. We can now expand:

Thus the answer is $93+13=\boxed{106}$.

~ [eevee9406](https://artofproblemsolving.com/wiki/index.php/User:Eevee9406)

~ Edited by [aoum](https://artofproblemsolving.com/wiki/index.php/User:Aoum)
