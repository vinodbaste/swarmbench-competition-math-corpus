## Problem

Let , , and be points in the coordinate plane. Let be the family of segments of unit length lying in the first quadrant with on the -axis and on the -axis. There is a unique point on , distinct from and , that does not belong to any segment from other than . Then , where and are relatively prime positive integers. Find .

## Solution 1 (completely no calculus required)

Begin by finding the equation of the line $\overline{AB}$: $y= -\sqrt{3}x+\frac{\sqrt{3}}{2}$ Now, consider the general equation of all lines that belong to $\mathcal{F}$. Let $P$ be located at $(a,0)$ and $Q$ be located at $(0,b)$. With these assumptions, we may arrive at the equation $ay +bx =ab$. However, a critical condition that must be satisfied by our parameters is that $a^2+b^2=1$, since the length of $\overline{PQ}=1$.

Here's the golden trick that resolves the problem: we wish to find some point $C$ along $\overline{AB}$ such that $\overline{PQ}$ passes through $C$ if and only if $a=\frac{1}{2}$. It's not hard to convince oneself of this, since the property $a^2+b^2=1$ implies that if $a=\frac{1}{2}$, then $\overline{PQ}=\overline{AB}$.

We should now try to relate the point $C$ to some value of $a$. This is accomplished by finding the intersection of two lines: \[     a\left(-\sqrt{3}x +\frac{\sqrt{3}}{2}\right) + x\sqrt{1-a^2} = a\sqrt{1-a^2} \]

Where we have also used the fact that $b=\sqrt{1-a^2}$, which follows nicely from $a^2+b^2 =1$. \[     a\left(-\sqrt{3}x +\frac{\sqrt{3}}{2}\right)   = (a-x)\sqrt{1-a^2} \]

Square both sides and go through some algebraic manipulations to arrive at \[     -a^4 +2xa^3+\left(-4x^2+3x+\frac{1}{4}\right)a^2-2xa+x^2=0 \]

Note how $a=\frac{1}{2}$ is a solution to this polynomial, and it is logically so. If we found the set of intersections consisting of line segment $\overline{AB}$ with an identical copy of itself, every single point on the line (all $x$ values) should satisfy the equation. Thus, we can perform polynomial division to eliminate the extraneous solution $a=\frac{1}{2}$. \[     -a^3 + \left(2x-\frac{1}{2}\right)a^2+(-4x^2+4x)a-2x^2=0 \]

Remember our original goal. It was to find an $x$ value such that $a=\frac{1}{2}$ is the only valid solution. Therefore, we can actually plug in $a=\frac{1}{2}$ back into the equation to look for values of $x$ such that the relation is satisfied, then eliminate undesirable answers. \[     16x^2-10x+1=0 \] This is easily factored, allowing us to determine that $x=\frac{1}{8},\frac{1}{2}$. The latter root is not our answer, since on line $\overline{AB}$, $y\left(\frac{1}{2}\right)=0$, the horizontal line segment running from $(0,0)$ to $(1,0)$ covers that point. From this, we see that $x=\frac{1}{8}$ is the only possible candidate.

Going back to line $\overline{AB}, y= -\sqrt{3}x+\frac{\sqrt{3}}{2}$, plugging in $x=\frac{1}{8}$ yields $y=\frac{3\sqrt{3}}{8}$. The distance from the origin is then given by $\sqrt{\frac{1}{8^2}+\left(\frac{3\sqrt{3}}{8}\right)^2} =\sqrt{\frac{7}{16}}$. That number squared is $\frac{7}{16}$, so the answer is $\boxed{023}$.

~Installhelp_hex

Why this works: Assume the quartic equation has exactly two real roots. Then for $a=\frac{1}{2}$ to be the only solution, it must be a doubled root. Thus, even after dividing the quartic by $a-\frac{1}{2}$, $a=\frac{1}{2}$ is still a root. ~inaccessibles

Other explanation: Clearly $a=\frac{1}{2}$ works because then PQ = AB. Thus, we can factor out $a-\frac{1}{2}$.

From the 3rd degree polynomial, it must either have 3 real roots, or 1 real root and 2 non real roots, because it has real coefficients.

So it must have atleast 1 real root. If this root wasn't $\frac{1}{2}$ this would mean their is another line PQ that satisfies the equation. Thus, their must be another root at $a=\frac{1}{2}$ and plugging in, we can solve for $x$. ~Bigbrain_2009

## Solution 2

$y=-(\tan \theta) x+\sin \theta=-\sqrt{3}x+\frac{\sqrt{3}}{2}, x=\frac{\sqrt{3}-2\sin \theta}{2\sqrt{3}-2\tan \theta}$

Now, we want to find $\lim_{\theta\to\frac{\pi}{3}}\frac{\sqrt{3}-2\sin \theta}{2\sqrt{3}-2\tan \theta}$. By L'Hôpital's rule, we get $x=\lim_{\theta\to\frac{\pi}{3}}\frac{\sqrt{3}-2\sin \theta}{2\sqrt{3}-2\tan \theta}=\lim_{\theta\to\frac{\pi}{3}}\cos^3{\theta}=\frac{1}{8}$. This means that $y=\frac{3\sqrt{3}}{8}\implies OC^2=\frac{7}{16}$, so we get $\boxed{023}$.

~Bluesoul

## Solution 3

The equation of line $AB$ is \[ y = \frac{\sqrt{3}}{2}  - \sqrt{3} x.  \hspace{1cm} (1) \]

The position of line $PQ$ can be characterized by $\angle QPO$, denoted as $\theta$. Thus, the equation of line $PQ$ is

\[ y = \sin \theta - \tan \theta \cdot x . \hspace{1cm} (2) \]

Solving (1) and (2), the $x$-coordinate of the intersecting point of lines $AB$ and $PQ$ satisfies the following equation:

\[ \frac{\frac{\sqrt{3}}{2} - \sqrt{3} x}{\sin \theta} + \frac{x}{\cos \theta} = 1 . \hspace{1cm} (1) \]

We denote the L.H.S. as $f \left( \theta; x \right)$.

We observe that $f \left( 60^\circ ; x \right) = 1$ for all $x$. Therefore, the point $C$ that this problem asks us to find can be equivalently stated in the following way:

We interpret Equation (1) as a parameterized equation that $x$ is a tuning parameter and $\theta$ is a variable that shall be solved and expressed in terms of $x$. In Equation (1), there exists a unique $x \in \left( 0, 1 \right)$, denoted as $x_C$ ($x$-coordinate of point $C$), such that the only solution is $\theta = 60^\circ$. For all other $x \in \left( 0, 1 \right) \backslash \{ x_C \}$, there are more than one solutions with one solution $\theta = 60^\circ$ and at least another solution.

Given that function $f \left( \theta ; x \right)$ is differentiable, the above condition is equivalent to the first-order-condition \[ \frac{\partial f \left( \theta ; x_C \right) }{\partial \theta} \bigg|_{\theta = 60^\circ} = 0 . \]

Calculating derivatives in this equation, we get \[ - \left( \frac{\sqrt{3}}{2} - \sqrt{3} x_C \right) \frac{\cos 60^\circ}{\sin^2 60^\circ} + x_C \frac{\sin 60^\circ}{\cos^2 60^\circ} = 0. \]

By solving this equation, we get \[ x_C = \frac{1}{8} . \]

Plugging this into Equation (1), we get the $y$-coordinate of point $C$: \[ y_C = \frac{3 \sqrt{3}}{8} . \]

Therefore,

Therefore, the answer is $7 + 16 = \boxed{\textbf{(23) }}$.

~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Solution 4 (coordinate bash)

Let $s$ be a segment in $\mathcal{F}$ with x-intercept $a$ and y-intercept $b$. We can write $s$ as Let the unique point in the first quadrant $(x, y)$ lie on $s$ and no other segment in $\mathcal{F}$. We can find $x$ by solving \[b(1 - \frac{x}{a}) = (b + db)(1 - \frac{x}{a + da})\] and taking the limit as $da, db \to 0$. Since $s$ has length $1$, $a^2 + b^2 = 1^2$ by the Pythagorean theorem. Solving this for $db$, we get After we substitute $db = -\frac{a}{b}da$, the equation for $x$ becomes \[b(1 - \frac{x}{a}) = (b -\frac{a}{b} da)(1 - \frac{x}{a + da}).\]

In $\overline{AB}$, $a = \frac{1}{2}$ and $b = \frac{\sqrt{3}}{2}$. To find the x-coordinate of $C$, we substitute these into the equation for $x$ and get We take the limit as $da \to 0$ to get \[x = \lim_{da \to 0} \frac{da + 2da^2}{8da} = \lim_{da \to 0} \frac{1 + 2da}{8} = \frac{1}{8}.\] We substitute $x = \frac{1}{8}$ into the equation for $\overline{AB}$ to find the y-coordinate of $C$: \[y = b(1 - \frac{x}{a}) = \frac{\sqrt{3}}{2}(1 - \frac{\frac{1}{8}}{\frac{1}{2}}) = \frac{3\sqrt{3}}{8}.\] The problem asks for \[OC^2 = x^2 + y^2 = (\frac{1}{8})^2 + (\frac{3\sqrt{3}}{8})^2 = \frac{7}{16} = \frac{p}{q},\] so $p + q = 7 + 16 = \boxed{023}$.

## Solution 5 (small perturb)

[asy] pair O=(0,0); pair X=(1,0); pair Y=(0,1); pair A=(0.5,0); pair B=(0,sin(pi/3)); pair A1=(0.6,0); pair B1=(0,0.8); pair A2=(0.575,0.04); pair B2=(0.03,0.816); dot(O); dot(X); dot(Y); dot(A); dot(B); dot(A1); dot(B1); dot(A2); dot(B2); draw(X--O--Y); draw(A--B); draw(A1--B1); draw(A--A2); draw(B1--B2); label("$B$", B, W); label("$A$", A, S); label("$B_1$", B1, SW); label("$A_1$", A1, S); label("$B_2$", B2, E); label("$A_2$", A2, NE); label("$O$", O, SW); pair C=(0.18,0.56); label("$C$", C, E); dot(C); [/asy]

Let's move a little bit from $A$ to $A_1$, then $B$ must move to $B_1$ to keep $A_1B_1 = 1$. $AB$ intersects with $A_1B_1$ at $C$. Pick points $A_2$ and $B_2$ on $CA_1$ and $CB$ such that $CA_2 = CA$, $CB_2 = CB_1$, we have $A_1A_2 = BB_2$. Since $AA_1$ is very small, $\angle CA_1A \approx 60^\circ$, $\angle CBB_1 \approx 30^\circ$, so $AA_2\approx \sqrt{3}A_1A_2$, $B_1B_2 \approx \frac{1}{\sqrt{3}}BB_2$, by similarity, $\frac{CA}{CB} \approx \frac{CA}{CB_2} = \frac{AA_2}{B_1B_2} = \frac{\sqrt{3}A_1A_2}{\frac{1}{\sqrt{3}}BB_2} = 3$. So the coordinates of $C$ is $\left(\frac{1}{8}, \frac{3\sqrt{3}}{8}\right)$.

so $OC^2 = \frac{1}{64} + \frac{27}{64} = \frac{7}{16}$, the answer is $\boxed{023}$.

## Solution 6(trig identities and questionable rigidity)

Let's try to find the general form of a line that is in $\mathcal{F}$ based on what angle it makes with the x-axis, $OP = \cos{\theta}$, and $OQ = \sin{\theta}$ so its slope is $-\tan{\theta}$ and due to us knowing its y-intercept we know that our line has form $y = -\tan{\theta}x + \sin{\theta}.$

Now we can analyze the system of equations made by $y = -\tan{\theta}x + \sin{\theta}$ and $y = -\tan{60^\circ}x + \sin{60^\circ}$, this gives us that $x = \dfrac{\sin{\theta}- \sin{60^\circ}}{\tan{\theta} - \sin{60^\circ}}.$

We can proceed to simplify our expression further: \[x = \dfrac{\sin{\theta} - \sin{60^\circ}}{\frac{\sin{\theta}}{\cos{\theta}} - \frac{\sin{60^\circ}}{\cos{60^\circ}}}\]\[= \dfrac{\sin{\theta} - \sin{60^\circ}}{\frac{\sin{(\theta - 60^\circ)}}{\cos{\theta}\cos{60^\circ}}}\]\[= \dfrac{2\sin{\dfrac{\theta - 60^\circ}{2}}\cos{\dfrac{\theta + 60^\circ}{2}}}{\dfrac{2\sin{\dfrac{\theta - 60^\circ}{2}}\cos{\dfrac{\theta - 60^\circ}{2}}}{\cos{\theta}\cos{60^\circ}}}\]\[= \dfrac{\sin{\dfrac{\theta - 60^\circ}{2}}}{\sin{\dfrac{\theta - 60^\circ}{2}}} \cdot \dfrac{\cos{\theta}\cos{60^\circ}\cos{\dfrac{\theta + 60^\circ}{2}}}{\cos{\dfrac{\theta - 60^\circ}{2}}}.\]

Seeing that there are only valid solutions when $\theta$ is acute(all that is allowed anyways) and when $\theta \neq 60^\circ$ since one of the expressions in our simplified solution will equal $0/0$. Since there is only one intersection point for every $\theta$ and vice versa in the appropriate domain and range(we can easily prove this by contradiction), we know that the missing element of the range(the points) must correspond with the excluded value. The x-coordinate of which which can be evaluated by taking the limit of our expression as $\theta$ goes to $60^\circ$ which is $\frac{1}{8}$ regardless of the direction we approach $60^\circ$ from. The corresponding $y$ is $\dfrac{3\sqrt{3}}{8}$ and using the distance formula gives us $\boxed{023}$ as our answer.

While this solution may seem long all of these steps come naturally.

~SailS

## Solution 7

[](https://artofproblemsolving.com/wiki/index.php?title=File:2024_AIME_II_12_a.png)

Denote $X(1,0), Y(0,1), P \in OX, Q \in OY, |PQ| = 1,$\[k = const \in (0,1), \alpha = \angle OPQ.\] Then $P = (\cos \alpha, 0), Q = (0, \sin \alpha).$

Let $C \in PQ$ be the point with property $k = \frac {PC}{QC} \implies$$C = \left ( \frac{\cos \alpha}{k+1} , \frac{k \sin \alpha}{k+1} \right ).$

So locus of points $C$ is the ellipse with semiaxes $\frac{1}{k+1}$ and $\frac{k}{k+1}.$

Point $D = C$ is a unique point on $AB$ if the ellipse is tangent to the line $AB.$

In this case in point $C$ we get $\frac{dy}{dx} = \frac{dy}{d \alpha} : \frac{dx}{d \alpha} = - k \cot \alpha.$

The tangent of the line $AB$ is $- \tan \alpha \implies k = \tan^2 \alpha.$

For point $D$ we get $k = \tan^2 \theta.$

\[\tan \angle DOX = \tan \varphi = \frac {D_y}{D_x} = \frac{k \sin \theta}{k+1} : \frac{\cos \theta}{k+1} = k \cdot \tan \theta = \tan^3 \theta.\]

For the line $AB  \tan \theta = \frac {B_y}{A_x} = \sqrt{3} \implies k = 3 \implies$\[D = \left( \frac{\cos \theta}{k+1}, \frac{k \sin \theta}{k+1} \right) = \left( \frac{1}{\sqrt{1+ \tan^2 \theta} \cdot (k+1)}, \frac{k \tan \theta}{\sqrt{1+ \tan^2 \theta} \cdot (k+1)} \right) =\]$\left(\frac{1}{\sqrt{1+ k} \cdot (k+1)}, \frac{k \cdot \sqrt{k}}{\sqrt{1+ k} \cdot (k+1)} \right) = \left(\frac{1}{8}, \frac{3 \sqrt{3}}{8} \right),$ so we get $\boxed{023}$.

**vladimir.shelomovskii@gmail.com, vvsss**

## Solution 8 (intuitive elementary calculus solution)

First, we find the equation of the line $\overline{AB}:$\[ y = -\sqrt{3} x + \dfrac{\sqrt{3}}{2}.  \hspace{1cm} (1) \] Now, say we have some line in $\mathcal{F}$ that spans from point $X$ at $(0,a)$, and because this segment has unit length, ends at point $Y$ located at $(\sqrt{1-a^2},0)$. Note that $\overline{XY}$ has the equation \[ y = -\dfrac{a}{\sqrt{1-a^2}}x + a. \hspace{1cm} (2) \] We notice that as $a$ varies, $\overline{XY}$ will intersect $\overline{AB}$ at all points on $\overline{AB}$ except point $C$. We make the key observation that $C$ is what the intersection point of $\overline{XY}$ and $\overline{AB}$ approaches as $a$ approaches $\dfrac{\sqrt{3}}{2}$.

To find this point, let's find the intersection point of $\overline{XY}$ and $\overline{AB}$ in terms of $a$.

Note that we don't need to find the $y$-coordinate because we know that this point is on line $\overline{AB}$, and once we find the $x$-coordinate, we can simply plug it into the equation of line $\overline{AB}$

Now, we want to find \[ \lim_{a\to\frac{\sqrt{3}}{2}} \dfrac{(a-\dfrac{\sqrt{3}}{2})\cdot\sqrt{1-a^2}}{a - \sqrt{3} \cdot \sqrt{1-a^2}} \] We apply L'Hopital's Rule as this limit is indeterminate. Taking the derivative of the numerator using product rule: Note that we can apply the chain rule to get $\dfrac{d}{da} \left(\sqrt{1-a^2}\right) = \dfrac{-a}{\sqrt{1-a^2}}$ Taking the derivative of the denominator: So, our final expression is \[ \dfrac{\frac{-2a^2 + \frac{a\sqrt{3}}{2} + 1}{\sqrt{1-a^2}}}{\frac{\sqrt{1-a^2} + \sqrt{3}a}{\sqrt{1-a^2}}}  \]\[ = \dfrac{-2a^2 + \frac{a\sqrt{3}}{2} + 1}{\sqrt{1-a^2} + \sqrt{3}a} \]

Now, all that remains is to substitute $a = \dfrac{\sqrt{3}}{2}$ Now, we can plug in $x = \dfrac{1}{8}$ into the equation of $\overline{AB}$: So point C is located at $(\dfrac{1}{8},\dfrac{3\sqrt{3}}{8})$ The question asks for $OC^2$, so we simply apply the Pythagorean Theorem:

~143466534811009我输了游戏56二伯

## Geometry Solution

[asy] pair O=(0,0); pair X=(1,0); pair Y=(0,1); pair A=(0.5,0); pair B=(0,sin(pi/3)); dot(O); dot(X); dot(Y); dot(A); dot(B); draw(X--O--Y); draw(A--B); label("$B$", B, W); pair P=(0.5, sin(pi/3)); dot(P); draw(A--P--B); label("$A$", A, S); label("$O$", O, SW); pair C=(1/8,3*sqrt(3)/8); dot(C); label("$C$", C, SW); draw(C--P); label("$P$", P, NE); [/asy] Let $C$ be a fixed point in the first quadrant. Let $A$ be a point on the positive $x$-axis and $B$ be a point on the positive $y$-axis such that $AB$ passes through $C$ and the length of $AB$ is minimal. Let $P$ be the point such that $OAPB$ is a rectangle. Prove that $PC \perp AB$. (One can solve this through algebra/calculus bash, but I'm trying to find a solution that mainly uses geometry. If you know such a solution, write it here on this wiki page.) ~Furaken

I think there is such a geometry way: Let $DE$ pass through $C$ while point $D$ is on the outside of line segment $OA$ and point $E$ is in between $O$ and $B$. We aim to show $DE$ is longer than $AB$. Now since $PC$ is the altitude of triangle $PAB$ yet just a cevian on the base $DE$ of triangle $PDE$ (thus making the height shorter than $PC$), it suffices to show the area of triangle $PDE$ is bigger than that of triangle $PAB$. To do this, we compare these two triangles (let $DE$ intersect $PA$ at point $F$), and we just want to show $PF*AD > AF*AO$. This is trivial by similarity ratios. ~gougutheorem

Thanks! Now we know that it's possible to solve the AIME problem with only geometry. ~Furaken

Can someone better explain this solution please? How does $PF*AD > AF*AO$ show that $PDE$ is bigger than $PAB$? ~inaccessibles
