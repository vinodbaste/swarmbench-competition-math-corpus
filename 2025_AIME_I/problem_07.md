## Problem

The twelve letters $A$,$B$,$C$,$D$,$E$,$F$,$G$,$H$,$I$,$J$,$K$, and $L$ are randomly grouped into six pairs of letters. The two letters in each pair are placed next to each other in alphabetical order to form six two-letter words, and then those six words are listed alphabetically. For example, a possible result is $AB$, $CJ$, $DG$, $EK$, $FL$, $HI$. The probability that the last word listed contains $G$ is $\frac mn$, where $m$ and $n$ are relatively prime positive integers. Find $m+n$.

## Solution 1

Note that order does not matter here. This is because any permutation of the $6$ pairs will automatically get ordered in alphabetical order. The same is true for within each of the pairs. In other words, $AB$$CH$$DI$$EJ$$FK$$GL$ should be counted equally as $HC$$AB$$DI$$EJ$$FK$$GL$.

We construct two cases: $G$ is the first letter of the last word and $G$ is the second letter of the last word.

Our first case is when $G$ is the first letter of the last word. Then the second letter of the last word must be one of $H, I, J, K, L$. Call that set of $5$ letters $\Omega$. There are $5$ ways to choose the second letter from $\Omega$. The other $4$ letters of $\Omega$ must be used in the other $5$ words.

For the other 5 words, each of their first letters must be before $G$ in the alphabet. Otherwise, the word with $G$ will not be the last. There are $6$ letters before $G$: $A,B,C,D,E,F$. Call that set of $6$ letters $\Sigma$. Exactly one of the words must have two letters from $\Sigma$. The other 4 will have their first letter from $\Sigma$ and the second letter from $\Omega$. There are $4!$ ways to determine the possible pairings of letters from $\Sigma$ and $\Omega$, respectively.

Therefore, this case has $5 \cdot {6\choose{2}} \cdot 4! = 5 \cdot 15 \cdot 24 = 1800$ orderings.

The second case is when $G$ is the second letter of the last word. You can see that the first letter of that word must be $F$. Otherwise, that word cannot be the last word. The other $5$ words must start with $A$, $B$, $C$, $D$, and $E$. The second letter of each of those words will come from $\Omega$. There will be $5!$ ways to distribute the elements of $\Omega$ to one of $A, B, C, D, E$. There are therefore $5! = 120$ orderings in the case.

In total, there are $1800+120 = 1920$ orderings. However, we want the probability. The number of ways to put the $12$ letters into pairs is $11 \cdot 9 \cdot 7 \cdot 5 \cdot 3 \cdot 1$. This is true because we can say this: Start with $A$. It has $11$ options for who it will partner with. There are now $10$ letters left. Pick one of those letters. It has $9$ options for who it will partner with. There are now $8$ letters left. Continue until there are only $2$ letters left, and there is only $1$ option for that last word. Therefore, there will be $11 \cdot 9 \cdot 7 \cdot 5 \cdot 3 \cdot 1$ options.

The probability is therefore $\frac{1920}{11 \cdot 9 \cdot 7 \cdot 5 \cdot 3 \cdot 1} = \frac{128}{693}$. The requested answer is $128 + 693 = \boxed{821}$.

~lprado

Minor latex edits by [T3CHN0B14D3](https://artofproblemsolving.com/wiki/index.php?title=User:T3chn0b14d3&action=edit&redlink=1 "User:T3chn0b14d3 (page does not exist)")

## Solution 2: Same but quicker

Splitting up into $2$ cases: $G$ is the first letter or the second letter of the last word.

Case $1:$$G$ in first letter

Notice that $A$ must take the first letter of first word, one of the letters $B$ - $F$ needs to be the second letter of a word and the rest being the first letter of a word. The combinations will be $1 + 2 + 3 + 4 + 9 = 19.$ After the first $7$ letters has been decided then the last $5$ will just fill by $5!.$ This case will have $19 \cdot 5!$ outcomes.

Case $2:$$G$ in last letter

Notice that $A$ - $G$ has been arranged by $A? B? C? D? E? FG,$ where the $?$ is undecided. We have another $5!$ to fill out the possible outcomes.

In total, there are $16 \cdot 5!.$ The total case will be $11 \cdot 9 \cdot 7 \cdot 5 \cdot 3 \cdot 1$ (Consider A must be in the first letter of first word, then you have $11$ choices, then you must take the next letter in alphabetical order as mandatory, then you have a free choice of $9$ and so on).

Answer: \[= \frac{16 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1}{ 11 \cdot 9 \cdot 7 \cdot 5 \cdot 3 \cdot 1}\]\[= \frac{16 \cdot 4 \cdot 2}{11 \cdot 9 \cdot 7}\]\[= \frac{128}{ 693}\] Therefore it gives us the answer of ${128 + 693 = \boxed{821}.}$

~Mitsuihisashi14 ~Latex by [mathkiddus](https://artofproblemsolving.com/wiki/index.php?title=User:Mathkiddus "User:Mathkiddus")

## Alternative Step in Solutions 1 and 2: Total Arrangements

The total number of possible arrangements can also be calculated using combinations. We wish to find the total number of ways to form $6$ pairs of letters from the given $12$. There are $12!$ ways to do so. However, the $2$ letters in each pair can only be arranged in $1$ way, not $2!$ ways, because they must be in alphabetical order. Thus, we must divide by $2!$ for each of the $6$ pairs, giving $\frac{12!}{2!2!2!2!2!2!}$ or $\frac{12!}{2^6}$ arrangements.

We must also take into account the number of ways to arrange the $6$ pairs relative to each other. In the problem, only $1$ possible arrangement can arise from $6!$ different cases because the pairs of letters must be in alphabetical order. Therefore, we must divide by $6!$ to give the total number of possible arrangements as $\frac{12!}{2^6\cdot6!}=\frac{2^{10}\cdot3^5\cdot5^2\cdot7\cdot11}{2^6\cdot2^4\cdot3^2\cdot5}=3^3\cdot5\cdot7\cdot11=10,395$.

~Christian

## Alternative view 2

Similar to what he said above, we can do $\frac{\binom{12}{2} * \binom{10}{2} * \binom{8}{2} * \binom{6}{2} * \binom{4}{2} * \binom{2}{2}}{6!}$

This makes 6 pairs and we divide by 6! because there is only one configuration which will be in alphabetical order

~Aarav22
