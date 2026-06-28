## Problem

The orthocenter of a triangle is the concurrent intersection of the three (possibly extended) altitudes. What is the sum of the coordinates of the orthocenter of the triangle whose vertices are $A(2,31), B(8,27),$ and $C(18,27)$?

$\textbf{(A)}~5\qquad\textbf{(B)}~17\qquad\textbf{(C)}~10+4\sqrt{17} +2\sqrt{13}\qquad\textbf{(D)}~\frac{113}{3}\qquad\textbf{(E)}~54$

## Solution 1 (coordinate geometry)

As we are given the coordinates of all $3$ vertices, we can compute the slope (or gradient) of each side, and thus the slope of each altitude since it must be perpendicular to the corresponding side. We can therefore determine the Cartesian equation of each altitude using this slope and a point on it (namely, the vertex opposite to the corresponding side), after which we only need to find the point of intersection of at least $2$ of these lines.

Accordingly, since $BC$ is horizontal (as $B$ and $C$ both have the same $y$-coordinate, namely $27$), we observe that the altitude through $A$ perpendicular to $BC$ will be vertical. As $A$ has $x$-coordinate $2$, the equation of this altitude is therefore precisely $x = 2$. Now, as explained above, we need to determine the equation of $1$ more altitude, so we arbitrarily choose the one through $C$ perpendicular to $AB$. The slope of $AB$ is $\frac{27-31}{8-2} = -\frac{2}{3}$, so because the slopes of perpendicular lines (other than a horizontal and a vertical line) have product $-1$, the slope of this altitude is $\frac{-1}{\left(-\frac{2}{3}\right)} = \frac{3}{2}$. Hence, as this altitude passes through $C$, its equation in point-slope form is $y-27 = \frac{3}{2}(x-18)$, which becomes $y-27 = \frac{3}{2}x-27$, and thus reduces to $y = \frac{3}{2}x$. Consequently, solving this equation simultaneously with $x = 2$ (from above) gives the coordinates of the orthocenter as simply $\left(2,\frac{3}{2} \cdot 2\right) = (2,3)$, and so, finally, the answer is $2+3 = \boxed{\textbf{(A) }5}$.

### Alternative: using the altitude through $B$

While we arbitrarily chose to use the altitudes through $A$ and $C$ in the solution above, we could of course use any $2$ of the $3$ altitudes to find the coordinates of the orthocenter as their point of intersection. It's also a good idea to check our answer from above by verifying that $(2,3)$ indeed lies on the third altitude, namely that through $B$ perpendicular to $AC$. Therefore, we compute the slope of $AC$ as $\frac{27-31}{18-2} = -\frac{1}{4}$, so that of the altitude is $\frac{-1}{\left(-\frac{1}{4}\right)} = 4$ (again using the 'slopes have product $-1$' result referred to above). We deduce that the equation of this altitude in point-slope form is $y-27 = 4(x-8) \iff y-27 = 4x-32 \iff y = 4x-5$, and solving this equation simultaneously with either $x = 2$ or $y = \frac{3}{2}x$ from above indeed gives the solution $x = 2, y = 4 \cdot 2 - 5 = \frac{3}{2} \cdot 2 = 3$. In other words, the coordinates of the orthocenter are precisely $(2,3)$, confirming our answer from above.

~[dg6665](https://artofproblemsolving.com/wiki/index.php?title=User:Dg6665&action=edit&redlink=1 "User:Dg6665 (page does not exist)") (edits for motivation by ~Logibyte)

## Solution 2 (trigonometry)

[asy] size(200); pair A = (2,31); pair B = (8, 27); pair C = (18, 27); pair H1 = (2, 27); pair H2 = (8.5882352941176, 29.3529411764706); pair D = (2,3);  label("$A$", A, NW); label("$B$", (8.5, 27), S); label("$C$", C, SE); label("$H_1$", H1, SW); label("$H_2$", H2, NE); label("$E$", E, S);  draw(A--B--C--cycle); draw(A--E, dashed); draw(H1--B, dashed); draw(H2--E, dashed);  [/asy]

Let $H_1$ be the foot of the altitude from $A$ to $BC$, $H_2$ similarly be the foot of the altitude from $B$ to $AC$, and $E$ be the point of intersection of the lines $AH_1$ and $BH_2$. Then we have $\angle EH_1B = \angle EH_2A = 90^{\circ}$, so since angles in a triangle sum to $180^{\circ}$, we obtain \begin{alignat*}{2}\angle EBH_1 &= 180^{\circ} - \angle EH_1B - \angle BEH_1 \\ &= 180^{\circ} - 90^{\circ} - \angle BEH_1 \qquad &&\text{(from above)} \\ &= 180^{\circ} - \angle EH_2A - \angle BEH_1 \qquad &&\text{(again from above)} \\ &= 180^{\circ} - \angle EH_2A - \angle AEH_2 \qquad &&\text{(as } H_1 \text{ lies on } AE \text{ and } B \text { lies on } H_2E \text{, so } \angle BEH_1 \text{ and } \angle AEH_2 \text{ are the same angle)} \\ &= \angle EAH_2.\end{alignat*} Moreover, $\angle EAH_2$ is also the same angle as $\angle H_1AC$, since (once again) $H_1$ lies on $AE$ and $H_2$ lies on $AC$. As $H_1$ has the same $x$-coordinate as $A$ and the same $y$-coordinate as $C$, its coordinates are precisely $(2,27)$, so we now deduce

\begin{alignat*}{2}\tan{\angle EBH_1} = \tan{\angle EAH_2} &= \tan{\angle H_1AC} \\ &= \frac{CH_1}{AH_1} \qquad &&\text{(as } \angle AH_1C = 90^{\circ} \text{, i.e. triangle } \triangle AH_1C \text{ is right-angled at } H_1 \text{)} \\ &= \frac{18-2}{31-27} \qquad &&\text{(using the coordinates of } H_1 \text{ from above)} \\ &= 4.\end{alignat*}

But again as $\angle EH_1B = 90^{\circ}$, triangle $\triangle EH_1B$ is also right-angled at $H_1$, so, similarly to above,

\begin{align*}&\tan{\angle EBH_1} = \frac{EH_1}{BH_1} \\ &\phantom{\tan{\angle EBH_1} \:} = \frac{EH_1}{8-2} \qquad \text{(again using the coordinates of } H_1 \text{ from above)} \\ &\iff \frac{EH_1}{6} \: = 4 \iff EH_1 = 24.\end{align*}

Hence, as $E$ lies vertically _below_$H_1$, it finally follows that its coordinates are $(2,27-EH_1) = (2,27-24) = (2,3)$, and thus the answer is $2+3 = \boxed{\textbf{(A) }5}$.

~[Bloggish](https://artofproblemsolving.com/wiki/index.php?title=User:Bloggish "User:Bloggish")

## See Also

*   [AMC 12](https://artofproblemsolving.com/wiki/index.php?title=AMC_12 "AMC 12")
*   [AMC 12 Problems and Solutions](https://artofproblemsolving.com/wiki/index.php?title=AMC_12_Problems_and_Solutions "AMC 12 Problems and Solutions")
*   [Mathematics competitions](https://artofproblemsolving.com/wiki/index.php?title=Mathematics_competitions "Mathematics competitions")
*   [Mathematics competition resources](https://artofproblemsolving.com/wiki/index.php?title=Mathematics_competition_resources "Mathematics competition resources")

[](https://artofproblemsolving.com/wiki/index.php?title=File:AMC_Logo.png)
