_The following problem is from the [2025 USAMO #4](https://artofproblemsolving.com/wiki/index.php/2025\_USAMO\_Problems/Problem\_4) and [2025 USAJMO #5](https://artofproblemsolving.com/wiki/index.php?title=2025\_USAJMO\_Problems/Problem\_5 "2025 USAJMO Problems/Problem 5"), so those problems redirect to this page._
## Problem

Let $H$ be the orthocenter of acute triangle $ABC$, let $F$ be the foot of the altitude from $C$ to $AB$, and let $P$ be the reflection of $H$ across $BC$. Suppose that the circumcircle of triangle $FAP$ intersects line $BC$ at two distinct points $X$ and $Y$. Prove that $C$ is the midpoint of $XY$.

## Solution 1

Let AP intersects BC at D. Extend FC to the point E on the circumcircle $\omega$ of $FAP$. Since $H$ is the orthocenter of $\Delta ABC$, we know that $HD = DP$ or $HP = 2HD$, and $AH \cdot HD = CH \cdot HF$. Next we use the power of H in $\omega$: $AH \cdot HP = CH \cdot HE$. These relations imply that $HE = 2HF$.

Hence $C, D$ are midpoints of $HE, HP$ respectively. By midline theorem, $CD // EP$. Since $AD \perp CD$, we have $AD \perp EP$. This implies that $\angle APE = 90^{\circ}$. Consequently, $AE$ is the diameter of $\omega$. Let $G$ be the midpoint of $AE$ which is also the center of $\omega$. $G,C$ are midpoints of $AE, EH$ respectively. By the midline theorem again, we have $GC//AH$, consequently, $GC \perp BC$. This implies that $GC$ is the perpendicular bisector of the chord $XY$ hence $C$ is the midpoint of $XY$. ~ Dr. Shi davincimath.com

## Solution 2

Denote $O_1$ as the center of $(ABC)$, $O_2$ as the center of $FAP$, $K$ as the midpoint of $AF$, $M$ as the midpoint of $AC$, and $N$ as the midpoint of $AP$. It suffices to show that $\angle{O_2CB}=90$.

Claim: $O_1MO_2C$ is cyclic.

Proof: Since $AK=FK$ and $AM=MC$, KM is a midline of $\triangle{AFC}$ and $KM\parallel FC$. $KO_2\parallel FC$ as well since $\angle{AKO_2}=\angle{AFC}=90$, so $M$ lies on $KO_2$. Next, note that $P$ lies on $(ABC)$, so the perpendicular bisector of $AP$ through $N$ passes through $O_1$. In other words, $N, O_1$, and $O_2$ are collinear. Since $NO_2$ and $BC$ are both perpendicular to $AP$, it follows that they are parallel. Since $KO_2\parallel FC$ and $NO_2\parallel BC$, then $\angle KO_2N=\angle{FCB}$. Finally, we have that \[\angle{MO_2O_1}=\angle{KO_2N}=\angle{FCB}=90-B=\angle{MCO_1},\] and thus $O_1MO_2C$ is cyclic. It follows that $\angle O_1O_2C=\angle{O_1MC}=90$, so $\angle{O_2CB}=180-\angle{O_1MC}=90$, as desired.

-mop

## Solution 3

Connect $HP$ and have $HP$ intersect $XY$ at $W$. Also extend $FC$ past point $C$ and have it intersect with the circle at point $D$.

Since $P$ is the reflection of $H$ over $BC$, we know that $HP\perp XY$. Since $H$ is the orthocenter, we can draw the altitude and tell that $A$, $H$, and $P$ are collinear. We know $m\angle{AFH} = m\angle{CWH}=90^{\circ}$ and $m\angle{FHA} = m\angle{WHC}$, so $\triangle{AHF} \sim \triangle{CHW}$ by AA, so $m\angle{FAH} = m\angle{WCH}$.

$m\angle{FAP} = \frac{1}{2}m\overarc{FP} = \frac{1}{2}(m\overarc{FX} + m\overarc{XP})$ and $m\angle{FCX} = \frac{1}{2}(m\overarc{FX} + m\overarc{DY})$. From this, we can tell that $m\overarc{XP} = m\overarc{DY}$. Therefore, $m\overarc{XD} = m\overarc{PY}$ and $XD = PY$.

If we connect $HY$, we can tell that that $PY = HY$ due to $P$ being the reflection of $H$ and $WY$ being perpendicular to $HP$, so $XD = HY$. In addition, $m\angle{HYW} = m\angle{PYW} = \frac{1}{2} m\overarc{XP} = \frac{1}{2} m\overarc{DY} = m\angle{YXD}$. Also, $m\angle{HCY} = m\angle{XCD}$ because they are vertical angles.

So, $\triangle{HCY} \cong \triangle{XCD}$ because of SAA. From this we can conclude that $XC = CY$, so $C$ is the midpoint of $XY$.

## Solution 4

Let $D$ be the foot of the altitude from $A$ to $BC.$ By Power of a Point, we have \[BF\cdot BA = BX \cdot BY = (BC-CX)(BC+CY) = BC^2 + BC(CY-CX) - CX\cdot CY\] and \[DB\cdot DC = DX\cdot DY = (CX-CD)(CD+CY) = CX\cdot CY - CD(CY-CX) - CD^2.\] Adding, we get \[BF \cdot BA + DB\cdot DC = BC^2-DC^2 + (BC-CD)(CY-CX).\] It is well known that the reflection of $H$ over $AB,$ which we denote by $P,$ lies on $(ABC).$ Then, let $\angle{BAP} = \angle{BCP} = \angle{BCH} = \theta.$ We have \[BF\cdot BA + DB\cdot DC = (BC\sin\theta)\cdot BA + DB\cdot DC = BC\cdot (BA \sin\theta) + DB\cdot DC = DB\cdot (BC+DC) = (BC-DC)(BC+DC) = BC^2-DC^2.\] Thus, $(BC-CD)(CY-CX)=0,$ and since $BC\neq CD$ we have $CY=CX.$ Hence, $C$ is the midpoint of $XY.$ ~TThB0501

## Solution 5

Let Q be the antipode of B. Claim — AHQC is a parallelogram, and AP CQ is an isosceles trapezoid.

Proof. As AH ⊥ BC ⊥ CQ and CF ⊥ AB ⊥ AQ. Let M be the midpoint of QC.

Claim — Point M is the circumcenter of triangle AFP.

Proof. It’s clear that MA = MP from the isosceles trapezoid.

As for MA = MF, let N denote the midpoint of AF; then MN is a midline of the parallelogram, so MN ⊥ AF. Since CM ⊥ BC and M is the center of (AF P), it follows CX = CY .

## Solution 6

Quick angle chasing gives $\angle FAP = \angle BCF = \angle BCP = \alpha$. Let $O$ be the circumcenter of $\triangle AFP$.

Thus $\angle FOP= 2 \angle FAP = 2\alpha$ (because O and A lie on the same side of segment $AF$).

As $\angle FOP = \angle FCP = 2 \alpha$, the quadrilateral FOCP is cyclic.

Observe that $2\angle FPO = 180-2\alpha$, so $\angle FPO = 90^{\circ} - \alpha$.

From the properties of cyclic quadrilaterals, $\angle FCO = \angle FPO$

Thus $\angle BCO = \angle BCF + \angle FCO = \alpha + (90^{\circ} - \alpha) =90^{\circ}$. Therefore $OC$ is perpendicular to chord $XY$, $XC=CY$.

[](https://artofproblemsolving.com/wiki/index.php?title=File:Usamo_2025_problem4.png)

## Solution 7

Let the line perpendicular to $BC$ and going through $C$ be line $l$. Let the midpoint of $AF$ be $M$, and let the line perpendicular to $AF$ and going through $M$ be line $n$. Let $O$ be the intersection of $l$ and $n$, and let $D$ be the intersections of $n$ and $AH$.

Because $AH\parallel l$ and $CF\parallel n$, $CODH$ is a parallelogram. From this, we get $OC=DH$. Looking at triangle $\triangle{FAP}$, because $n\parallel HF$, and $M$ is the midpoint of $AF$, it is clear that $D$ is the midpoint of $AH$.

Let the intersection of $HP$ and $BC$ be $Z$. $PZ=ZH$ because $P$ is a reflection of $H$ across $BC$. $AP=AH+HP=2DH+2PZ$

Substituting the equation from earlier, we get $AP=2OC+2PZ$

Draw a line perpendicular to $OC$ starting from $O$. Let the intersection of that line and $AP$ be $E$. Because $BC$ is perpendicular to $OC$ which is perpendicular to $OE$, $BC\parallel OE$. By the same logic, $AP\parallel OC$. This means $OCZE$ is a parallelogram (specifically a rectangle). Therefore $EZ=OC$. $EP=EZ+PZ$ and by substituting, we get $EP=OC+PZ$, and because $AP=2OC+2PZ$, that means $2EP=AP$, so $E$ is a midpoint of $AP$. This means $OE$ is the perpendicular bisector of $AP$, and because $AP$ is a chord of the circumcircle of $\triangle{FAP}$, $OE$ goes through the center of the circle. By the same logic, $n$ also goes through the center of the circle, since it is the perpendicular bisector of $AF$. This means the center of the circle is $O$, because it is the only point on both $OE$ and $n$. Because $O$ is on line $OC$ and line $OC$ is perpendicular to line $BC$, line $OC$ must perpendicularly bisect the chord of circle $O$ containing $C$ that lies on line $BC$ (basically $OC$ must perpendicularly bisect $XY$). This means $C$ is the midpoint of $XY$.

-Nolan Lin

[](https://artofproblemsolving.com/wiki/index.php?title=File:USAMO4diagram.png)

## Solution 8 (fast, similar to Solution 7)

Construct the point $O$ such that $OC\perp BC$ and $OC=AH/2$.

Claim 1: $O$ passes through the perpendicular bisector of $AP$. Let $N$ be the foot of the altitude from $O$ to $AP$ and $D$ be the foot of the altitude from $A$ to $BC$. Indeed, we have $2NP=2(ND+DP)=2(\frac{AH}{2}+DP)=AH+HP=AP$.

Claim 2: $O$ passes through the perpendicular bisector of $AF$. Let the perpendicular bisector of $AF$ intersect $AH$ at $K$ and the line passing through $C$ perpendicular to $BC$ at $O'$. Clearly, $O'CHK$ is a parallelogram, so $O'C=HK=\frac{AH}{2}$. Thus, $O'=O$.

Hence, $O$ is the unique circumcenter of $\triangle AFP$ and has the property that $OC\perp BC$. Combined, this means that $OX=OY$, as desired.

~Mathkiddie

## Solution 9

We proceed with complex numbers. Let the circumcenter be the origin and circumradius = $1$.

$B=b, C=\frac{1}{b}, A = a, F = \frac{1}{2}(a+b+\frac{1}{b}-ab^2), P = -\frac{1}{a}$

We claim that the circumradius of $\triangle AFP$ is $O=\frac{\frac{1}{b}-b}{2}$

It is easy to check the distances are the same (divide the two relative vectors, check that the inverse conjugates are equal).

Now, $O-C$ is real, and $\overline{BC}$ is a vertical line, meaning that $\overline{OX}=\overline{OY}$. Thus, we are done.

Note that the hard part of the solution was finding the center. Without it, one would have to shift the coordinate system such that $C$ is the origin and show that the circumcenter is purely real using the circumcenter formula.

~MATHLOVERSSD

## Solution 10 (zero iq)

Unlike my previous solution, this is a no iq complex bash.

We proceed with complex numbers. Let the circumcenter be the origin and circumradius = $1$.

$B=b, C=\frac{1}{b}, A = a, F = \frac{1}{2}(a+b+\frac{1}{b}-ab^2), P = -\frac{1}{a}$

Now shift the coordinate system by $C$.

$C=0, A=a-\frac{1}{b}, F = \frac{a+b-\frac{1}{b}-ab^2}{2}, P=-\frac{1}{a}-\frac{1}{b}$

We aim to prove that the circumcenter of $\triangle AFP$ is purely real. That is, in the circumcenter formula, we can take the conjugate and it won't change the location. Note that the denominator in the circumcenter formula is simply negated by conjugation. Therefore, we aim to prove:

$\det(\begin{bmatrix} A+\bar{A}& A\bar{A} & 1\\ F+\bar{F}& F\bar{F} & 1\\ P+\bar{P}&P\bar{P}&1 \end{bmatrix})=0$

Now we begin the long journey of simplification

$\det(\begin{bmatrix} a+\frac{1}{a}-b-\frac{1}{b}& 2-ab-\frac{1}{ab} & 1\\ 2(a+\frac{1}{a}-ab^2-\frac{1}{ab^2})& 4+ab^3+\frac{1}{ab^3}-2ab-\frac{2}{ab}+\frac{b}{a}+\frac{a}{b}-2b^2-\frac{2}{b^2}& 4\\ -a-\frac{1}{a}-b-\frac{1}{b}&2+\frac{a}{b}+\frac{b}{a}&1 \end{bmatrix})$

$\det(\begin{bmatrix} a+\frac{1}{a}-b-\frac{1}{b}& 2-ab-\frac{1}{ab} & 1\\ 2(a+\frac{1}{a}-ab^2-\frac{1}{ab^2})& 4+ab^3+\frac{1}{ab^3}-2ab-\frac{2}{ab}+\frac{b}{a}+\frac{a}{b}-2b^2-\frac{2}{b^2}& 4\\ -2a-\frac{2}{a}&ab+\frac{1}{ab}+\frac{a}{b}+\frac{b}{a}&0 \end{bmatrix})$

$\det(\begin{bmatrix} a+\frac{1}{a}-b-\frac{1}{b}& 2-ab-\frac{1}{ab} & 1\\ 2(-a-\frac{1}{a}-ab^2-\frac{1}{ab^2}+2b+\frac{2}{b})& -4+ab^3+\frac{1}{ab^3}+2ab+\frac{2}{ab}+\frac{b}{a}+\frac{a}{b}-2b^2-\frac{2}{b^2}& 0\\ -2a-\frac{2}{a}&ab+\frac{1}{ab}+\frac{a}{b}+\frac{b}{a}&0 \end{bmatrix})$

$\det(\begin{bmatrix} -a-\frac{1}{a}-ab^2-\frac{1}{ab^2}+2b+\frac{2}{b}& -4+ab^3+\frac{1}{ab^3}+2ab+\frac{2}{ab}+\frac{b}{a}+\frac{a}{b}-2b^2-\frac{2}{b^2}&\\ -a-\frac{1}{a}&ab+\frac{1}{ab}+\frac{a}{b}+\frac{b}{a} \end{bmatrix})$

$\det(\begin{bmatrix} -ab^2-\frac{1}{ab^2}+2b+\frac{2}{b}& -4+ab^3+\frac{1}{ab^3}+ab+\frac{1}{ab}-2b^2-\frac{2}{b^2}&\\ -a-\frac{1}{a}&ab+\frac{1}{ab}+\frac{a}{b}+\frac{b}{a} \end{bmatrix})$

$2$nd column becomes $2$nd column plus $b$ times the first column:

$\det(\begin{bmatrix} -ab^2-\frac{1}{ab^2}+2b+\frac{2}{b}& -2+\frac{1}{ab^3}+ab-\frac{2}{b^2}&\\ -a-\frac{1}{a}&\frac{1}{ab}+\frac{a}{b} \end{bmatrix})$

$2$nd column becomes $2$nd column plus $\frac{1}{b}$ times the first column:

$\det(\begin{bmatrix} -ab^2-\frac{1}{ab^2}+2b+\frac{2}{b}& 0&\\ -a-\frac{1}{a}&0 \end{bmatrix})$

The determinant is obviously $0$, so we have proven the problem (clearly this brainless strategy was a lot more tedious than guessing the circumcenter. However, if one really manages to guess the circumcenter, a synthetic solution would finish it off a lot cleaner than the complex proof).

~MATHLOVERSSD

## See Also

**[2025 USAMO](https://artofproblemsolving.com/wiki/index.php?title=2025_USAMO "2025 USAMO")** (**[Problems](https://artofproblemsolving.com/wiki/index.php?title=2025_USAMO_Problems "2025 USAMO Problems")** • [Resources](http://www.artofproblemsolving.com/Forum/resources.php?c=182&cid=27&year=2025))
Preceded by

**[Problem 3](https://artofproblemsolving.com/wiki/index.php?title=2025_USAMO_Problems/Problem_3 "2025 USAMO Problems/Problem 3")**Followed by

**[Problem 5](https://artofproblemsolving.com/wiki/index.php?title=2025_USAMO_Problems/Problem_5 "2025 USAMO Problems/Problem 5")**
[1](https://artofproblemsolving.com/wiki/index.php?title=2025_USAMO_Problems/Problem_1 "2025 USAMO Problems/Problem 1")**•**[2](https://artofproblemsolving.com/wiki/index.php?title=2025_USAMO_Problems/Problem_2 "2025 USAMO Problems/Problem 2")**•**[3](https://artofproblemsolving.com/wiki/index.php?title=2025_USAMO_Problems/Problem_3 "2025 USAMO Problems/Problem 3")**•**[4](https://artofproblemsolving.com/wiki/index.php/2025_USAMO_Problems/Problem_4)**•**[5](https://artofproblemsolving.com/wiki/index.php?title=2025_USAMO_Problems/Problem_5 "2025 USAMO Problems/Problem 5")**•**[6](https://artofproblemsolving.com/wiki/index.php?title=2025_USAMO_Problems/Problem_6 "2025 USAMO Problems/Problem 6")
**[All USAMO Problems and Solutions](https://artofproblemsolving.com/wiki/index.php?title=USAMO_Problems_and_Solutions "USAMO Problems and Solutions")**

**[2025 USAJMO](https://artofproblemsolving.com/wiki/index.php?title=2025_USAJMO "2025 USAJMO")** (**[Problems](https://artofproblemsolving.com/wiki/index.php?title=2025_USAJMO_Problems "2025 USAJMO Problems")** • [Resources](http://www.artofproblemsolving.com/Forum/resources.php?c=182&cid=176&year=2025))
Preceded by

**[Problem 4](https://artofproblemsolving.com/wiki/index.php?title=2025_USAJMO_Problems/Problem_4 "2025 USAJMO Problems/Problem 4")**Followed by

**[Problem 6](https://artofproblemsolving.com/wiki/index.php?title=2025_USAJMO_Problems/Problem_6 "2025 USAJMO Problems/Problem 6")**
[1](https://artofproblemsolving.com/wiki/index.php?title=2025_USAJMO_Problems/Problem_1 "2025 USAJMO Problems/Problem 1")**•**[2](https://artofproblemsolving.com/wiki/index.php?title=2025_USAJMO_Problems/Problem_2 "2025 USAJMO Problems/Problem 2")**•**[3](https://artofproblemsolving.com/wiki/index.php?title=2025_USAJMO_Problems/Problem_3 "2025 USAJMO Problems/Problem 3")**•**[4](https://artofproblemsolving.com/wiki/index.php?title=2025_USAJMO_Problems/Problem_4 "2025 USAJMO Problems/Problem 4")**•**[5](https://artofproblemsolving.com/wiki/index.php?title=2025_USAJMO_Problems/Problem_5 "2025 USAJMO Problems/Problem 5")**•**[6](https://artofproblemsolving.com/wiki/index.php?title=2025_USAJMO_Problems/Problem_6 "2025 USAJMO Problems/Problem 6")
**[All USAJMO Problems and Solutions](https://artofproblemsolving.com/wiki/index.php?title=USAJMO_Problems_and_Solutions "USAJMO Problems and Solutions")**

[](https://artofproblemsolving.com/wiki/index.php?title=File:AMC_Logo.png)
