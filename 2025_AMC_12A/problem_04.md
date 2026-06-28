## Problem
Agnes writes the following four statements on a blank piece of paper.

$\bullet$ At least one of these statements is true.

$\bullet$ At least two of these statements are true.

$\bullet$ At least two of these statements are false.

$\bullet$ At least one of these statements is false.

Each statement is either true or false. How many false statements did Agnes write on the paper?

$\textbf{(A) } 0 \qquad\textbf{(B) } 1 \qquad\textbf{(C) } 2 \qquad\textbf{(D) } 3 \qquad\textbf{(E) } 4$

## Solution 1
We first number all the statements:

1) At least one of these statements is true.
2) At least two of these statements are true.
3) At least two of these statements are false.
4) At least one of these statements is false.

We can immediately see that statement 4 must be true, as it would contradict itself if it were false. Similarly, statement 1 must be true, as all the other statements must be false if it were false, which is contradictory because statement 4 is true. Since both 1 and 4 are true, statement 2 has to be true. Therefore, statement 3 is the only false statement, making the answer $\boxed{\text{(B) }1}$.
-Rainjs

## Solution 2
Statements $I,II,$ and $IV$ are true, while statement $III$ is false. Hence, there are $3$ true statements and $\boxed{\text{(B) }1}$ false statement. This result can be checked by examining the statements individually again.

Statements $I$ and $II$ will be true because there are $3\ge2$ true statements. Statement $IV$ is also true because there is $1\ge1$ false statement. Finally, statement $III$ is false because there are $1\ngeq2$ false statements.

~Tacos_are_yummy_1

Note: This solution does not give a path to the solution, but rather only how to check the answer after the answer has been identified.

## Solution 3
Let's say there are $T$ true statements. We know that $T$ can be any integer from $0$ to $4$. Numbering the $4$ given statements in order as $S1$ to $S4,$ we can represent $S1$ as $T \geq 1$, $S2$ as $T \geq 2$, and since there are $(4-T)$ false statements, $S3$ as $4-T \geq 2 \iff T \leq 2$, and $S4$ as $4-T \geq 1 \iff T \leq 3$.

Accordingly, we now consider the possible cases for the value of $T$. If $T=0$, then the true statements are $S3$ and $S4$, i.e. there are $2$ true statements in total. But that means $T = 2 \neq 0$, giving a contradiction.

Similarly, if $T=1$, then the true statements are $S1$, $S3$, and $S4$, i.e. there are $3$ true statements in total. This means $T = 3 \neq 1$, again giving a contradiction.

If $T=2$, then all $4$ statements are true, yielding the contradiction $T = 4 \neq 2$.

Finally, however, if $T=3$, then the true statements are $S1$, $S2$, and $S4$. Hence there are again $3$ true statements in total, but now as $T=3$ in the first place, this is actually consistent and not a contradiction.

For completeness, we also observe that if $T=4$, then the true statements are only $S1$ and $S2$, i.e. $T = 2 \neq 4$, and so this case again leads to a contradiction.

Thus we conclude that the only possible value is $T = 3$, which gives a consistent solution when $S1$, $S2$, and $S4$ are true and $S3$ is false (as noted above). It follows that the number of false statements is $\boxed{\textbf{(B) }1}$, namely precisely $S3$ (and indeed, $T = 3$ gives $4-T = 4-3 = 1$, as expected).

~lprado

## Solution 4
Suppose Statement $I$ is false, then none of the Statements are true, which contradicts the fact that a false Statement $III$ or $IV$ is telling the truth. Therefore, Statement $I$ is true and assume Statement $II$ is false.

Statement $II$ thus implies that only Statement $I$ was the truth, and the rest, false. But then, there are 3 false statements but then Statement $III$ and Statement $IV$ are telling the truth. So Statement $II$ is also true.

Now, if Statement $III$ is true, then both Statement $III$ and Statement $IV$ is false, contradicting the fact that it is true. Statement $III$ is hence false and Statement $IV$ tells the truth since Statement $III$ lied so indeed, there are at least one lie. There are a total of 3 truths and 1 lie, making the answer $\boxed{\text{(B) }1}$. ~hxve

## Solution 5 (Quick)
I tried setting that the statements regarding the true ones (I and II) were true and
regarding the false ones (III and IV) were false, and it clearly doesn't work.
It doesn't work because statement III was true, not false as I set it to be originally.

What if we make that statement (Statement III) true too?
Well, then we have 3 T and 1 F statements, so statement IV is false,
statement III is true, and statements I and II are true too.

So there is $\boxed{\text{(B) }1}$ false statement.

~Aarav22

## Solution 6 (Plug in Answer Choices)
For this question, what I did was to simply test each of the answer choices.

Let's start with $\text{(A)}$ $0$ false statements:

We can check the answer of $0$ false statements against each of the statements.

Statement $\mathrm{I}$: "At least one of these statements is true."

This statement is false, which already invalidates the answer of (A) 0 false statements, as we already have a false statement.

Let's move onto $\text{(B)}$ $1$ false statement:

We can check once again this answer against each of the statements.

Statement $\mathrm{I}$: "At least one of these statements is true."

This statement is true, as when we have $1$ false statement, we have $3$ true statements, and therefore this is true.

Statement $\mathrm{II}$: "At least two of these statements are true."

Once again, this statement is true, as when we have $1$ false statement, we have $3$ true statements, and thus this is also true.

Statement $\mathrm{III}$: "At least two of these statements are false."

This statement is false, as we have one false statement, not $2$ and above.

Statement $\mathrm{IV}$: "At least one of these statements is false."

This statement is true, as we have one false statement.

So, after checking the answer choice of $\boxed{\text{(B)} 1}$ false statement across the $4$ statements, we get three true statements and one false statement, making this statement the correct answer. I will not dive into the other $3$ answer choices, as we have already gotten the answer for this question, and if you were doing this way of solving on the test, you would most likely not test the other $3$ answers either for the sake of saving time.

~EZ123 (Would appreciate it if someone formatted my solution using latex, thanks!)
~Aggrava (major $\LaTeX$ edits)

## Solution 7 (Step by Step, Simple)
Start by going statement by statement and checking if they can be false. If statement 1 were false statement 4 would be true leading to a contradiction so statement 1 is true. If statement 2 were false 4 would be true and one would be true making statement 2 true. If statement 3 was false and we know statement 1 and statement 2 were true and 4 can be true and it works. Therefore, the correct answer is $\boxed{\text{(B) }1}$.

--TFEA(would also appreciate if somebody could please latex my proof).
--Iceboy1221(i wrote it using latex)

## Video Solution by FormulaFocus (Logical, Good Editing, ~0:40)
https://www.youtube.com/shorts/P4P8TfCw_lo

~Ebai

## Video Solution(Quick and Easy)
https://www.youtube.com/watch?v=sRpXHd_t1ZI
~Sigma_Bob

## Video Solution by DDM
https://youtu.be/5eDaXhXykY0

~piggydude

## Video Solution (intuitive)
https://youtu.be/9rzJWhWwG1E?si=tA97LtVnlhZC5QqK - Continuum Math

## Video Solution by Power Solve
https://youtu.be/QBn439idcPo?si=DGqtuDIJ399xE_rh&t=524

## Chinese Video Solution
https://www.bilibili.com/video/BV1t72uBREof/

~metrixgo

## Video Solution by SpreadTheMathLove
https://www.youtube.com/watch?v=dAeyV60Hu5c

## Video Solution (In 1 Min)
https://youtu.be/uv3uIMwIkrg?si=XCbsXL7ikMawCGyM ~ Pi Academy

## Video Solution by Daily Dose of Math
https://youtu.be/gPh9w3X3QSw
~Thesmartgreekmathdude

## Video Solution by Thinking Feet
https://youtu.be/LXFX2ggFeQ8
