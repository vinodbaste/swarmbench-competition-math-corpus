## Problem 22

Three real numbers are chosen independently and uniformly at random between $0$ and $1$. What is the probability that the greatest of these three numbers is greater than $2$ times each of the other two numbers? (In other words, if the chosen numbers are $a \geq b \geq c$, then $a > 2b$.)

$\textbf{(A)}~\frac{1}{12}\qquad\textbf{(B)}~\frac19\qquad\textbf{(C)}~\frac18\qquad\textbf{(D)}~\frac16\qquad\textbf{(E)}~\frac14$

## Problem 22 (Chinese exams)

Three real numbers are chosen independently and uniformly at random between $0$ and $1$. What is the probability that the greatest of these three numbers is greater than the sum of the other two numbers?

(The answer to this version of the problem is $\frac{1}{2}$, which is not one of the answer choices above.)

## Solution 1 (3D geometry)

Let the three numbers be $X$, $Y$, and $Z$, and consider each possible triple $(X,Y,Z)$ as the (Cartesian) coordinates of a point in 3-dimensional space. Then, as each number is chosen independently and uniformly from the interval $[0,1]$, the total space of possible points $(X,Y,Z)$ is the unit cube $0 \leq X,Y,Z \leq 1$. Using the idea of [geometric probability](https://artofproblemsolving.com/wiki/index.php?title=Geometric_probability "Geometric probability"), it follows that the required probability equals the volume of the region consisting of all points $(X,Y,Z)$ that satisfy the required condition, divided by the volume of the total space, i.e. the unit cube (which is simply $1^3 = 1$). Accordingly, it only remains to determine the region of possible points $(X,Y,Z)$ and then compute its volume.

For simplicity, we may assume that e.g. $X$ is the maximum - clearly, by symmetry, the corresponding regions where $Y$ is the maximum and where $Z$ is the maximum have the same volume, and these regions overlap only where at least two of $X,Y,Z$ are both the maximum. In such cases, those two variables must be equal (e.g. $X$ and $Y$ will both be the maximum precisely if $X = Y \geq Z$), and so each of these overlaps is either a region within a plane (as e.g. the equation $X = Y$ defines a plane), or a straight line (in the special case where $X = Y = Z$). It follows that the overlaps between the $3$ regions all have zero volume, so since each region has the same volume (as explained above), the answer will simply be $3$ times the volume of one of these regions, say the one where $X$ is the maximum and the required condition is satisfied.

Within that region, we therefore have $0 \leq X,Y,Z \leq 1$, $X \geq Y$ and $X \geq Z$ for $X$ to be the maximum, and $X > 2Y$ and $X > 2Z$ for the required condition, but this combination of inequalities reduces to simply $0 \leq 2Y,2Z < X \leq 1$, since we automatically have $2Y \geq Y$ and $2Z \geq Z$ as $Y,Z \geq 0$. This means the boundaries of the region are the lines $X = 2Y$, $X = 2Z$, $X = 0$, $Y = 0$, and $X = 1$, so now by drawing the unit cube as well as those boundaries, we deduce that this region is a square-based pyramid: the base has vertices $\left(1,0,0\right)$, $\left(1,0,\frac{1}{2}\right)$, $\left(1,\frac{1}{2},\frac{1}{2}\right)$, and $\left(1,\frac{1}{2},0\right)$, while the apex of the pyramid is at $(0,0,0)$. The square base thus clearly has side length $\frac{1}{2}$, and hence area $\left(\frac{1}{2}\right)^2 = \frac{1}{4}$; moreover, as the base lies in the plane $X = 1$, the perpendicular height of this pyramid is the same as the perpendicular distance from the apex $(0,0,0)$ to that plane, which is obviously $1-0 = 1$.

It follows that the volume of this pyramid, i.e. of the region where $X$ is the maximum and the required condition is satisfied, is $\frac{1}{3} \cdot \frac{1}{4} \cdot 1 = \frac{1}{12}$ (using the standard formula for the volume of a pyramid). Finally, as explained above, this means the required probability is $3 \cdot \frac{1}{12} = \boxed{\textbf{(E)}~\frac14}$.

## Solution 2 (calculus)

Consider three independent uniform random variables $X, Y, Z$ on $[0, 1]$. The goal is to find the probability that the maximum value is greater than twice each of the other two values. Equivalently, if we order them as $a \geq b \geq c$, this is the probability that $a > 2b$ (which implies $a > 2c$ since $b \geq c$). Therefore, if we assume that $X$ is the maximum (but make no assumption about the order of $Y$ and $Z$), the required condition reduces (almost surely) to $X > 2Y$ and $X > 2Z$. Conversely, if $X > 2Y$ and $X > 2Z$, then we will necessarily have $X > 2Y \geq Y$ and $X > 2Z \geq Z$ since $Y,Z \geq 0$, and so $X$ will indeed be the maximum.

Accordingly, the probability that $X$ is the maximum and the required condition is satisfied is simply $P(X > 2Y \cap X > 2Z)$, and then the answer will be $3$ times this probability, to account for the $3$ total cases (the maximum can be $X$, $Y$, or $Z$, and clearly all of these cases are symmetric). Since $X,Y,Z$ are chosen uniformly at random from the interval $[0,1]$, the marginal distribution of each one is simply the uniform distribution on this interval. As they are also chosen independently, we deduce that their joint distribution is uniform over $[0,1] \times [0,1] \times [0,1]$, i.e. the unit cube, and hence the joint probability density is $\frac{1}{\text{volume of the unit cube}} = \frac{1}{1^3} = 1$.

For the bounds of integration, we can first choose $X \in [0,1]$, and then we require $Y,Z \in [0,1]$, $X > 2Y$, and $X > 2Z$; as $X \leq 1$, the latter two conditions will also automatically give $Y,Z < \frac{X}{2} \leq \frac{1}{2} < 1$, so it is both necessary and sufficient that $0 \leq Y,Z < \frac{X}{2}$. Thus we can now compute \begin{align*} P(X > 2Y \cap X > 2Z) &= \int_{0}^{1} \int_{0}^{\frac{x}{2}} \int_{0}^{\frac{x}{2}} 1 \, \mathop{}\!\mathrm{d}z \, \mathop{}\!\mathrm{d}y \, \mathop{}\!\mathrm{d}x \\ &= \int_{0}^{1} \left(\frac{x}{2}\right)^2 \, \mathop{}\!\mathrm{d}x \\ &= \int_{0}^{1} \frac{x^2}{4} \, \mathop{}\!\mathrm{d}x \\ &= \frac{1}{4}\left[\frac{1}{3}x^3\right]_{0}^{1} \\ &= \frac{1}{4} \cdot \frac{1}{3} \left(1^3-0^3\right) \\ &= \frac{1}{12}, \end{align*} and so, as explained above, the total probability is $3 \cdot \frac{1}{12} = \boxed{\textbf{(E)}~\frac{1}{4}}$.

### Solution 2.1 (alternative, fixing the entire order)

Alternatively, instead of just fixing the maximum as $X$, we can fix the entire order of the $3$ variables as e.g. $X > Y > Z$. It then follows that the required condition reduces (almost surely) to $X > 2Y > 2Z$, while conversely, if $X > 2Y > 2Z$, it will indeed necessarily follow that the order is $X > Y > Z$, as $Y \geq 0$ again gives $X > 2Y \geq Y$ and $2Y > 2Z$ gives $Y > Z$.

Hence, similarly to above, the probability that the required condition is satisfied is $P(X > 2Y > 2Z)$, and then as $X > Y > Z$ is just $1$ of the total $3! = 3 \cdot 2 \cdot 1 = 6$ possible orders (with all of them clearly being symmetric), the answer will be $6$ times this probability. The joint probability density is still $1$ as shown above, but now for the bounds of integration, we first choose $Y$, where we must have $1 \geq X > 2Y$, and thus $0 < Y < \frac{1}{2}$. We can now choose $X$, again satisfying $X > 2Y$ and of course $0 \leq X \leq 1$, i.e. $2Y < X \leq 1$ (since we then automatically have $X > 2Y \geq 2 \cdot 0 = 0$). Lastly, we need to choose $Z$ such that $Y > Z$ and $0 \leq Z \leq 1$ (as then $X > 2Y$ will automatically also give $X > 2Z$), i.e. $0 \leq Z < Y$ (since $Y \leq 1$ will then automatically give $Z \leq 1$).

Accordingly, we obtain \begin{align*} P(X > 2Y > 2Z) &= \int_{0}^{\frac{1}{2}} \int_{2y}^{1} \int_{0}^{y} 1 \, \mathop{}\!\mathrm{d}z \, \mathop{}\!\mathrm{d}x \, \mathop{}\!\mathrm{d}y \\ &= \int_{0}^{\frac{1}{2}}y(1-2y) \, \mathop{}\!\mathrm{d}y \\ &= \int_{0}^{\frac{1}{2}}\left(y-2y^2\right) \, \mathop{}\!\mathrm{d}y \\ &= \left[\frac{1}{2}y^2-\frac{2}{3}y^3\right]_{0}^{\frac{1}{2}} \\ &= \left(\frac{1}{2} \cdot \left(\frac{1}{2}\right)^2 - \frac{2}{3} \cdot \left(\frac{1}{2}\right)^3\right) - (0-0) \\ &= \frac{1}{24}, \end{align*} and so, as explained above (and just as obtained in Solution 2), the required probability is $6 \cdot \frac{1}{24} = \boxed{\textbf{(E)}~\frac{1}{4}}$.

~funkCCP

## See Also

*   [AMC 12](https://artofproblemsolving.com/wiki/index.php?title=AMC_12 "AMC 12")
*   [AMC 12 Problems and Solutions](https://artofproblemsolving.com/wiki/index.php?title=AMC_12_Problems_and_Solutions "AMC 12 Problems and Solutions")
*   [Mathematics competitions](https://artofproblemsolving.com/wiki/index.php?title=Mathematics_competitions "Mathematics competitions")
*   [Mathematics competition resources](https://artofproblemsolving.com/wiki/index.php?title=Mathematics_competition_resources "Mathematics competition resources")

[](https://artofproblemsolving.com/wiki/index.php?title=File:AMC_Logo.png)
