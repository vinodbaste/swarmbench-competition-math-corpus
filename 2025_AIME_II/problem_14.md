## Problem

Let ${\triangle ABC}$ be a right triangle with $\angle A = 90^\circ$ and $BC = 38.$ There exist points $K$ and $L$ inside the triangle such\[AK = AL = BK = CL = KL = 14.\]The area of the quadrilateral $BKLC$ can be expressed as $n\sqrt3$ for some positive integer $n.$ Find $n.$

## Solution 1

From the given condition, we get $\angle{LAK}=60^{\circ}$ and $\triangle{LCA}, \triangle{BAK}$ are isosceles. Denote $\angle{BAK}=\alpha, \angle{CAL}=30^{\circ}-\alpha$. From the isosceles condition, we have $\angle{BKA}=180^{\circ}-2\alpha, \angle{CLA}=120^{\circ}+2\alpha$.

Since $\angle{CAB}$ is right, then $AB^2+AC^2=BC^2$, we can use the Law of Cosines to express $AC^2$ and $AB^2$, and sum the equations to get $AC^2+AB^2=2\cdot 14^2(2-\cos \angle{BKA}-\angle {CLA})=2\cdot 14^2(2+\cos(2\alpha)+\cos(60^{\circ}-2\alpha))=38^2$.

This simplifies to $\cos(2\alpha)+\cos(60^{\circ}-2\alpha)=\frac{165}{98}$, and expanding the expression using the angle subtraction formula, we get $\sqrt{3}\sin(2\alpha+60^{\circ})=\frac{165}{98}, \sin(2\alpha+60^{\circ})=\frac{55\sqrt{3}}{98}$.

Connecting $CK$, we notice that $\angle{CLK}=360^{\circ}-\angle{CLA}-\angle{ALK}=180^{\circ}-2\alpha=\angle{AKB}$, and since $CL=LK=AK=KB$, we have $\triangle{CLK}\cong \triangle{AKB}$ by SAS Congruence. Moreover, since $K$ lies on the perpendicular bisector of $AB$, the distance from $K$ to $AC$ is half of the length of $AB$, which means $[ACK]=\frac{[ABC]}{2}$, so we get $[ACK]=[ACL]+[ALK]+[CLK]=[ACL]+[ALK]+[ABK]=[ABC]-[BKLC]$, which means that $[BKLC]=[AKC]=\frac{[ABC]}{2}$. Thus, we find $[AKC]=[ALK]+\frac{14^2\cdot\sin(\angle{CLA})}{2}+\frac{14^2\cdot\sin(\angle{BKA})}{2}=[ALK]+\frac{14^2}{2}(\sin(60^{\circ}-2\alpha)+\sin 2\alpha)=98(\sin(60^{\circ}+2\alpha))+[ALK]=55\sqrt{3}+\frac{\sqrt{3}}{4}14^2=104\sqrt{3}$. Our answer is $\boxed{104}$.

~ Bluesoul

~ Edited by Christian

## Solution 2

[asy] import math; import geometry; import olympiad; point A,C,B,L,K,D,F,G,O; A=(0,0); C=(16sqrt(3),0); B=(0,26); L=(8sqrt(3),2); K=(3sqrt(3),13); D=(16sqrt(3),26); F=(13sqrt(3),13); G=(8sqrt(3),24); O=(8sqrt(3),13); draw(A--B--D--C--A--L--C--F--L--K--A--D); draw(K--B--G--D--F--G--K--F); draw(B--O--L); draw(C--O--G); label("A",A,SW); label("B",B,NW); label("C",C,SE); label("A'",D,NE); label("K",K,W); label("L",L,NW); label("L'",G,SE); label("K'",F,E); label("O",O,NNW); [/asy] Let $O$ be the midpoint of $BC$. Take the diagram and rotate it $180^{\circ}$ around $O$ to get the diagram shown. Notice that we have $\angle ABC+\angle ACB=90^{\circ}$. Because $\triangle AKL$ is equilateral, then $\angle KAL=60^{\circ}$, so $\angle BAK+\angle CAL=30^{\circ}$. Because of isosceles triangles $\triangle BAK$ and $\triangle CAL$, we get that $\angle ABK+\angle ACL=30^{\circ}$ too, implying that $\angle KBC+\angle LCB=60^{\circ}$. But by our rotation, we have $\angle LCO=\angle L'BO$, so this implies that $\angle KBL'=60^{\circ}$, or that $\triangle KBL'$ is equilateral (specifically, the presence of a $60^{\circ}$ angle in between two sides of length $14$ allows us to conclude that $\triangle KBL'$ is congruent to an equilateral triangle by SAS). We can similarly derive that $\angle KBO=\angle K'CO$ implies $\angle LCK'=60^{\circ}$ so that $\triangle LK'C$ is also equilateral. At this point, notice that quadrilateral $KL'K'L$ is a rhombus because all its sides have length $14$. The area of our desired region is now $[BKLC]=\frac{1}{2}[BL'K'CLK]$. We can easily find the areas of $\triangle KBL'$ and $\triangle LK'C$ to be $\frac{\sqrt{3}}{4}\cdot 14^2=49\sqrt{3}$ each. Now it remains to find the area of rhombus $KL'K'L$. [asy] import math; import geometry; import olympiad; point A,K,O,L,M; A=(-7sqrt(3),0); K=(0,7); O=(55sqrt(3)/14,23/14); L=(0,-7); M=(0,0);  draw(A--K--O--L--A--O--M--A); draw(K--L); label("A",A,W); label("K",K,N); label("O",O,E); label("L",L,S); label("M",M,SE); [/asy] Focus on the quadrilateral $AKOL$. Restate the configuration in another way - we have equilateral triangle $\triangle AKL$ with side length 14, and a point $O$ such that $AO=19$ (the median to the hypotenuse of a right triangle is equal to half the length of the hypotenuse) and $\angle KOL=90^{\circ}$. We are trying to find the area of $\triangle KOL$. Let $M$ be the midpoint of $KL$. We see that $AM=7\sqrt{3}$ ($\overline{AM}$ is a median of equilateral $\triangle AKL$ with side length $14$), and since $M$ is the circumcenter of right $\triangle KOL$, it follows that $MO=7$. Let $\angle KMO=\theta$. From the Law of Cosines in $\triangle AMO$, we can see that \[(7\sqrt{3})^2+7^2-2(7\sqrt{3})(7)\cos (\angle AMO)=361,\] so after simplification we get that $\cos (\theta +90^{\circ})=-\frac{55\sqrt{3}}{98}$. Applying the cosine angle sum identity simplifies this to $\sin \theta =\frac{55\sqrt{3}}{98}$. Then, the Pythagorean Identity $\cos^2\theta +\sin^2\theta =1$ gives us $\cos \theta =\frac{23}{98}$ ($\theta$ is clearly acute, so $\sin \theta$ and $\cos \theta$ are both positive). Applying the Law of Cosines in $\triangle KMO$, we get \[49+49-2\cdot 7\cdot 7\cdot \cos \theta =98-98\cdot \frac{23}{98}=98-23=75=KO^2,\] which tells us $KO=5\sqrt{3}$. The Pythagorean Theorem in $\triangle KOL$ gives that $OL=\sqrt{KL^2-KO^2}={11}$, so the area of $\triangle KOL$ is $\frac{KO\cdot KL}{2}=\frac{55\sqrt{3}}{2}$. The rhombus $KL'K'L$ consists of four of these triangles, so its area is $4\cdot \frac{55\sqrt{3}}{2}=110\sqrt{3}$.

Finally, the area of hexagon $BL'K'CLK$ is $49\sqrt{3}+110\sqrt{3}+49\sqrt{3}=208\sqrt{3}$, and since this consists of quadrilaterals $BKLC$ and $CK'L'B$, which must be congruent by rotation, the area of $BKLC$ is $104\sqrt{3}$. Therefore, the answer is $\boxed{104}$.

~ethanzhang1001

~ Edited by Christian

## Solution 3 (coordinates and bashy algebra)

By drawing out the triangle, I set $A$ to be $(0, 0)$ in the coordinate plane. I set $C$ to be $(x, 0)$ and B to be $(0, y)$. I set $K$ to be $(a, b)$ and $L$ to be $(c, d)$. Then, since all of these distances are $14$, I used coordinate geometry to set up the following equations: $a^{2} + b^{2} = 196$; $a^{2} + (b - y)^{2} = 196$; $(a - c)^{2} + (b - d)^{2} = 196$; $c^{2} + d^{2} = 196$; $(c - x)^{2} + d^{2} = 196$. Notice by merging the first two equations, the only possible way for it to work is if $b - y = -b$ which means $y = 2b$. Next, since the triangle is right, and we know one leg is $2b$ as $y = 2b$, the other leg, $x$, is $\sqrt{38^{2} - (2b)^{2}}$. We now have:

$a^{2} + b^{2} = 196  \hspace{1 cm} \textbf{(1)}$

$(a - c)^{2} + (b - d)^{2} = 196 \hspace{1 cm} \textbf{(2)}$

$c^{2} + d^{2} = 196  \hspace{1 cm} \textbf{(3)}$

$(c - \sqrt{38^{2} - (2b)^{2}})^{2} + d^{2} = 196  \hspace{1 cm} \textbf{(4)}$

Expanding equation (4) and simplifying, we end with $38^{2} - 4b^{2} = 2c \cdot \sqrt{38^{2} - 4b^{2}}$. Next, squaring both sides and canceling terms, we have $4 \cdot 19^{2} - 4b^{2} = 4c^{2}$ which tells us that $c^{2} = 19^{2} - b^{2}$. Now, plugging this value in into equation (3) tells us that $d^{2} = 196 - 19^{2} + b^{2}$. We expand equation (2) to get $a^{2} - 2ac + c^{2} + b^{2} - 2bd + d^{2} = 196$. Using equation (1), we can cancel terms and shift things over to get $196 = 2ac + 2bd$ which means $98 = ac + bd$. From equation (1), we have $a^{2} = 196 - b^{2}$. Now, plugging in all of our variables in terms of $b$ to this new equation, we have $98 = \sqrt{(361 - b^{2})(196 - b^{2})} + b\sqrt{b^{2} - 165}$. We now move things over to get $98 - b\sqrt{b^{2} - 165} = \sqrt{(361 - b^{2})(196 - b^{2})}$. Squaring both sides and canceling, we have $98^{2} - 196b\sqrt{b^{2} - 165} = (361)(196) - 392b^{2}$. We can now divide both sides by $196$ to get $49 - b\sqrt{b^{2} - 165} = 361 - 2b^{2}$. Rearranging and simplifying, we now have $2b^{2} - 312 = b\sqrt{b^{2} - 165}$. Squaring both sides and combining like terms, we have $3b^{4} - 1083b^{2} + 312^{2} = 0$. This part will be a bit of a bash. Quadratic Formula tells us that $b^{2} = \frac{1083 \pm \sqrt{1083^{2} - 12 \cdot 312^{2}}}{6}$. The discriminant nicely simplifies to $\sqrt{4761} = 69$(this will be an extremely long bash but it's worth it). In fact, after computing, we end up with $b^{2} = 192, 169$. This leads us to solutions of $b = 8\sqrt{3}, 13$. If we choose $b = 8\sqrt{3}$, then $c^{2} = 361 - b^{2} = 361 - 192 = 169$ which tells us that $c = 13$.(In fact if you choose $b = 13$, then $c = 8\sqrt{3}$ so it's symmetrical and doesn't matter which one you choose). Next, $a^{2} = 196 - b^{2} = 196 - 192 = 4$ which tells us that $a = 2$. Finally, $d^{2} = 196 - c^{2} = 196 - 169 = 27$ which tells us that $d = 3\sqrt{3}$. Therefore, after all the bashing, our solution quadruple is $a = 2, b = 8\sqrt{3}, c = 13, d = 3\sqrt{3}$. Now plugging in all the points and using the Pythagorean Theorem, we get the coordinates of the quadrilateral which are $(0, 16\sqrt{3}), (2, 8\sqrt{3}), (13, 3\sqrt{3})$, and $(26, 0)$. By Shoelace, our area is $104\sqrt{3}$. Thus, the answer is $\boxed{104}$.

~ilikemath247365

## Solution 4 (Trigonometry)

[asy] import math; import geometry; import olympiad; point A,B,C,L,K; A=(0,0); C=(16sqrt(3),0); B=(0,26); L=(8sqrt(3),2); K=(3sqrt(3),13); draw(A--B--C--cycle); draw(A--K--L--cycle); draw(B--K); draw(C--L); draw(B--L); label("A",A,SW); label("B",B,NW); label("C",C,SE); label("K",K,W); label("L",L,NE); markscalefactor=1; draw(anglemark(L,C,A)); draw(anglemark(A,B,K)); [/asy] Immediately we should see that $\triangle{AKL}$ is equilateral, so $\angle{KAL}=60$.

We assume $\angle{LCA}=x$, and it is easily derived that $\angle{KBA}=30-x$. Using trigonometry, we can say that $AC=28\cos{x}$ (imagine extending $\overrightarrow{CL}$ to intersect $\overline{AB}$, forming a right triangle with hypotenuse length $2\cdot14=28$) and $AB=28\cos{(30-x)}$. Pythagoras tells us that $BC^2=AC^2+AB^2$ so now we evaluate as follows:

It is obvious that $\angle{ALC}=180-2x$. We can easily derive $\cos{(150+(30-2x))}$ using angle addition we know, and then the Law of Cosines to find side $AC$.

We easily find $\cos{x}=\frac{4\sqrt{3}}{7}$ and $\sin{x}=\frac{1}{7}$ (draw a perpendicular down from $L$ to $AC$). What we are trying to find is the area of $BKLC$, which can be found by adding the areas of $\triangle{BKL}$ and $\triangle{BLC}$. It is trivial that $\triangle{BKL}$ and $\triangle{ACL}$ are congruent (do some angle chasing in terms of $x$ and use the given side lengths of $14$), so we know that $BL=28\cos{x}$. What we require is

We do similar calculations to obtain that $\sin{(120+x)}=\frac{11}{14}$ and $\cos{(180-2x)}=-\frac{47}{49}$ implies $\sin{(180-2x)}=\frac{8\sqrt{3}}{49}$, so now we plug in everything we know to calculate the area of the quadrilateral:

We see that $n=\boxed{104}$.

~ [lisztepos](https://artofproblemsolving.com/wiki/index.php?title=User:Lisztepos "User:Lisztepos")

~ Edited by [Aoum](https://artofproblemsolving.com/wiki/index.php?title=User:Aoum "User:Aoum")

~ Edited by [Souledgeii](https://artofproblemsolving.com/wiki/index.php?title=User:Souledgeii&action=edit&redlink=1 "User:Souledgeii (page does not exist)")

~ Edited by Christian

## Solution 5 (Circles and Trigonometry)

[](https://artofproblemsolving.com/wiki/index.php?title=File:AIME2025II_P14_Solution5.PNG)

Since $KB=KL=KA=14$ and $LK=LA=LC=14$, we can construct 2 circles of radus 14 with $K$ and $L$ as the center of the two circles. Let the intersection of the 2 circles other than $A$ be point $M$. Connect $BM$, $CM$, $KM$, and $LM$. Connect $AM$, which is the radical axis of the 2 circles.

From the figure, we know that \[[KLCB] = [KLCMB] - [BMC]\]\[[KLCB] = [BKM] + [CLM] + [KLM] - [BMC]\]

Let $\angle{BAM} = \theta$, which means that $\angle{CAM} = \frac{\pi}{2} - \theta$. For easier calculation, we temporarily define the radius of the 2 circles (which is 14) to be $R$. $\angle{BAM}$ is an inscribed angle and $\angle{BKM}$ is a central angle, so $\angle{BKM} = 2\angle{BAM} = 2\theta$. Similar with the other side, $\angle{CLM} = \pi-2\theta$. $KM = KL = LM = R$, so $\triangle{KLM}$ is an equilateral triangle.

Using the Law of Cosines, we get the area of each little triangle, and applying the Law of Sines gives $BM$ and $MC$. \[[BKM] = \frac{1}{2}\cdot R^2\cdot\sin(2\theta)\]\[[CLM] = \frac{1}{2}\cdot R^2\cdot\sin(\pi-2\theta) = \frac{1}{2}\cdot R^2\cdot\sin(2\theta)\]\[[KLM] = \frac{1}{2}\cdot R^{2} \cdot\sin({\frac{\pi}{3}})=\frac{\sqrt3}{4}R^2\]

We can conclude that \[[KLCB] = \frac{1}{2}\cdot R^2\cdot\sin(2\theta)+\frac{1}{2}\cdot R^2\cdot\sin(2\theta)+\frac{\sqrt3}{4}R^2-\frac{1}{2}\cdot R^2\sin(2\theta)\]\[[KLCB] = {14}^2\cdot(\frac{\sin(2\theta)}{2}+\frac{\sqrt3}{4})\]

Now, we just needed to find the value of $\sin(2\theta)$. We analyze the $\triangle{BMC}$. We already know that $\angle{BMC} = {150}^{\circ}$, $BM = 2R\sin(\theta)$, and $CM = 2R\cos(\theta)$. Using the Laws of Cosines (again!) and the given condition of $BC = 38$, we can create a formula on $\theta$.

\[{BC}^2 = {BM}^2+{CM}^2-2\cdot BM\cdot MC\cdot\cos(\angle{BMC})\]\[{BC}^2 = (2R\sin(\theta))^2+(2R\cos(\theta))^2-2\cdot\cos({150}^{\circ})\cdot(2R\cos(\theta))\cdot(2R\cos(\theta)) = {38}^2\]\[4R^2(\sin^2(\theta)+\cos^2(\theta)+\sqrt3\sin(\theta)\cos(\theta)) = {38}^2\]\[4R^2(1+\frac{\sqrt3}{2}\cdot\sin(2\theta)) = {38}^2\]\[4R^2+\frac{4R^2\sqrt3}{2}\cdot\sin(2\theta) = {38}^2\]\[\sin(2\theta) = \frac{2}{\sqrt3}\cdot(\frac{{38}^2}{4\cdot{R}^2}-1)\]\[\sin(2\theta) = \frac{2\cdot165}{\sqrt3\cdot{14}^2} = \frac{165}{98\sqrt3}\]

We put the calculated value of $\sin(2\theta)$ back into $[KLCB]$: \[[KLCB] = {14}^2\cdot(\frac{165}{2\cdot98\sqrt3}+\frac{\sqrt3}{4})\]\[[KLCB] = 55\sqrt3+49\sqrt3 = 104\sqrt3\]

Therefore, $n=\boxed{104}$.

~cassphe

~ Edited by Christian

## Solution 6 (Trig Identities; warning: bashy)

Consider a diagram to the original problem (credit to solution 4):

[asy] import math; import geometry; import olympiad; point A,B,C,L,K; A=(0,0); C=(16sqrt(3),0); B=(0,26); L=(8sqrt(3),2); K=(3sqrt(3),13); draw(A--B--C--cycle); draw(A--K--L--cycle); draw(B--K); draw(C--L); draw(B--L); label("A",A,SW); label("B",B,NW); label("C",C,SE); label("K",K,W); label("L",L,NE); markscalefactor=1; [/asy]

Now, let us simplify the problem further. We know that $K$ and $L$ must lie on the perpendicular bisectors of $AB$ and $AC$, respectively. The real problem here is the equilateral triangle in the middle, inscribed in a rectangle with diagonal length 19.

We create a further simplified problem: given that the inscribed equilateral triangle of a certain rectangle with diagonal length $19$ has side length $14$, find the sides and intersection points on this rectangle. For reference, here is a diagram:

[asy] import math; import geometry; import olympiad; point A,B,C,D,L,K; A=(0,0); D=(13,0); B=(0,8sqrt(3)); C=(13,8sqrt(3)); L=(13,3sqrt(3)); K=(2,8sqrt(3)); draw(A--B--C--D--cycle); draw(A--K--L--cycle); label("A",A,SW); label("B",B,NW); label("C",C,NE); label("K",K,N); label("L",L,E); label("D",D,SE); markscalefactor=1; [/asy]

Note the angles $\angle{LAD}$ and $\angle{BAK}$. Since $\angle{LAD} + \angle{BAK} + 60^{\circ} = 90^{\circ}$, $\angle{LAD} + \angle{BAK} = 30^{\circ}$, and $\angle{BAK} = 30^{\circ} - \angle{LAD}$. Thus, let $\angle{LAD} = \alpha$ and $\angle{BAK} = 30 - \alpha$.

Now, we know that $AB^2 + AD^2 = 19^2$, as the hypotenuse of the larger right triangle is $38$. However, we can also express $AB$ and $AD$ in terms of $\alpha$: $AB = 14(\cos(30^{\circ}-\alpha))$ and $AD = 14(\cos(\alpha))$. Thus, $\cos^2(\alpha) + \cos^2(30^{\circ}-\alpha) = 361/196$. We expand this using the cosine difference identity:

$\cos^2(\alpha) + (\cos(30^{\circ})\cos(\alpha) + \sin(30^{\circ})\sin(\alpha))^2 = \frac{361}{196}$

$\frac{7}{4}\cos^2(\alpha) + \frac{1}{4}\sin^2(\alpha) + \frac{\sqrt3}{2}\sin(\alpha)\cos(\alpha) = \frac{361}{196}$

Using the fact that $\sin^2(\alpha) + \cos^2(\alpha) = 1$, then multiplying the entire equation by $2$,

$3\cos^2(\alpha) + \sqrt3\sin(\alpha)\cos(\alpha) = \frac{156}{49}$

Now, to save some writing, let us denote $\sin(\alpha)$ with $x$, and $\cos(\alpha)$ with $y$.

We have the following equations:

$x^2 + y^2 = 1$

$3y^2 + \sqrt3xy = \frac{156}{49}$

Substituting $x$ for $y$, moving $3y^2$ to the left side, squaring, and dividing by 9, we end up with the quartic:

$\frac{4}{3}y^4 - \frac{361}{147}y^2 + \frac{52^2}{49^2} = 0$

Using the quadratic formula, we end up with this:

$y^2 = \frac{\frac{361}{49} \pm \frac{1}{49}\cdot\sqrt{361^2 - 208^2\cdot3}}{8}$

Now, we could just compute $361^2 - 208^2\cdot3$, but instead, we can do this:

$361^2 - 208^2\cdot3 = (129600 + 720 + 1) - (40000 + 3200 + 64)\cdot3$

$(129600 + 721) - (43200 + 64)\cdot3$

$(129600 + 721) - (129600 + 192) = 529 = 23^2$

Thus, we have two cases:

$1. \cos(\alpha) = \frac{13}{14}$

$2. \cos(\alpha) = \frac{4\sqrt3}{7}$

Both lead to the same side lengths of the rectangle: $8\sqrt3$, and $13$. Referring back to our original rectangle diagram and plugging in our trigonometric values, we get that $CK = 13 - 2 = 11$, and $CL = 8\sqrt3 - 3\sqrt3 = 5\sqrt3$. Thus, the area of the original quadrilateral is $\frac{88\sqrt3 + 55\sqrt3 + 65\sqrt3}{2}$, or $\boxed{104}\sqrt3$.

~Stead

~ Edited by Christian

## Solution 7 (analytic geometry with roots of unity)

[asy] import math; import geometry; import olympiad; point A,B,C,L,K; A=(0,0); C=(16sqrt(3),0); B=(0,26); L=(8sqrt(3),2); K=(3sqrt(3),13); point M,N; M=(8sqrt(3), 0); N=(0,13); draw(A--B--C--cycle); draw(A--K--L--cycle); draw(B--K); draw(C--L); draw(N--K); draw(L--M); label("A",A,SW); label("B",B,NW); label("C",C,SE); label("K",K,ENE); label("L",L,NE); label(“N”,N,W); label(“M”,M,S); point am, ml, an, nk, mc, bn; am=(4sqrt(3), 0); mc=(12sqrt(3),0); ml=(8sqrt(3),1); an=(0,6.5); bn=(0,19.5); nk=(2.5981, 13); label(“a",am,S); label(“a",mc,S); label(“y”,ml,ESE); label(“b”,an,W); label(“b”,bn,W); label(“x”,nk,S); markscalefactor=1; [/asy] This diagram is modified from the solution 4 diagram. Let $M$ be the midpoint of $AC$, and let $N$ be the midpoint of $AB$.

We place the diagram onto the Cartesian coordinate grid. Let $A = (0, 0)$, $M = (a, 0)$, $C = (2a, 0)$, $N = (0, b)$, and $B = (0, 2b)$. We are given $AL = CL$, so $\triangle ACL$ is isosceles. Therefore, $LM$ is the perpendicular bisector of $AC$, so we can let $L = (a, y)$. Similarly, we’re given $AK = BK$, so $\triangle ABK$ is also isosceles, and $NK$ is the perpendicular bisector of $AB$. Therefore, we can let $K = (x, b)$.

We have $AB = 2b$ and $AC = 2a$. We’re given that $\angle BAC = 90^\circ$ and $BC = 38$, so by the Pythagorean theorem, \[(2a)^2 + (2b)^2 = 38^2 \implies 4a^2 + 4b^2 = 1444 \implies a^2 + b^2 = 361.\]

We now place the diagram onto the complex plane. We use the x-axis of the coordinate plane as the complex plane’s real axis, and we use the y-axis of the coordinate plane as the complex plane’s imaginary axis. So, on the complex plane, $A = 0$, $L = a + yi$, and $K = x + bi$. Also, since we are given $AK = KL = AL$, $\triangle AKL$ is equilateral. In addition, since $AL = AK$, $\angle KAL = 60^\circ$, and because we constructed our diagram with $K$ counterclockwise of $L$ (if it were the other way around, we could go through the same steps as this solution, but with variables switched around), $K$ is a $60^\circ$ counterclockwise rotation of $L$ about $A$, and $L$ is a $60^\circ$ clockwise or $300^\circ$ counterclockwise rotation of $K$ about $A$.

Rotation on the complex plane is equivalent to multiplying by a root of unity. Here, $K$ and $L$ are rotated a multiple of $60^\circ$ to each other about $A$. $60^\circ$ is one-sixth of a full circle, so to go from $L$ to $K$ or $K$ to $L$, we multiply by a 6th root of unity. Specifically, to go from $L$ to $K$, we multiply by $\dfrac{1}{2} + \dfrac{\sqrt{3}}{2}i$, and to go from $K$ to $L$, we multiply by $\dfrac{1}{2} - \dfrac{\sqrt{3}}{2}i$.

We multiply the coordinate of $L$ by $\dfrac{1}{2} + \dfrac{\sqrt{3}}{2}i$ on the complex plane to obtain equations for the coordinates of $K$: \[(a + yi)\left(\dfrac{1}{2} + \dfrac{\sqrt{3}}{2}i\right) = \left(\dfrac{a}{2} - \dfrac{\sqrt{3}}{2}y\right) + \left(\dfrac{y}{2} + \dfrac{\sqrt{3}}{2}a\right)i = x + bi.\] Equating real and imaginary parts, we obtain \[x = \dfrac{a}{2} - \dfrac{\sqrt{3}}{2}y \text{ and } b = \dfrac{y}{2} + \dfrac{\sqrt{3}}{2}a.\]

Similarly, we multiply the coordinate of $K$ by $\dfrac{1}{2} - \dfrac{\sqrt{3}}{2}i$ to obtain equations for the coordinates of $L$: \[(x + bi)\left(\dfrac{1}{2} - \dfrac{\sqrt{3}}{2}i\right) = \left(\dfrac{x}{2} + \dfrac{\sqrt{3}}{2}b\right) + \left(\dfrac{b}{2} - \dfrac{\sqrt{3}}{2}x\right) = a + yi.\] Equating real and imaginary parts, we obtain \[a = \dfrac{x}{2} + \dfrac{\sqrt{3}}{2}b \text{ and } y = \dfrac{b}{2} - \dfrac{\sqrt{3}}{2}x.\]

We now look back at the problem to see what it asks for: $[BKLC]$. Looking at the diagram, we see we can express the area of the quadrilateral as the area of the big right triangle $ABC$ minus the two isosceles triangles $ABK$ and $ALC$ minus the equilateral triangle $AKL$: \[[BKLC] = [ABC] - [ABK] - [ACL] - [AKL].\]

We are given that $AK = KL = AL = 14$, so the area of equilateral triangle $AKL$ is $\dfrac{\sqrt{3}}{4} \cdot 14^2 = 49\sqrt{3}$. Also, we can use $AC = 2a$ as the base of $\triangle ABC$ and $AB = 2b$ as the height, so $[ABC] = \dfrac{(2a)(2b)}{2} = 2ab$. Similarly, we use $AC = 2a$ as the base of $\triangle ACL$ and $ML = y$ ($M = (a, 0)$ and $L = (a, y)$, so the distance between the two is equal to $y$) as the height, so $[ACL] = \dfrac{(2a)(y)}{2} = ay$. Finally, we use $AB = 2b$ and $KN = x$ ($N = (0, b)$ and $K = (x, b)$, so the distance between the two is equal to $x$) as the base and height of $\triangle ABK$ respectively, so $[ABK] = \dfrac{(2b)(x)}{2} = bx$. Therefore, \[[BKLC] = [ABC] - [ABK] - [ACL] - [AKL] = 2ab - bx - ay - 49\sqrt{3}.\]

We have already shown that $b = \dfrac{y}{2} + \dfrac{\sqrt{3}}{2}a$. Substituting this into $a^2 + b^2 = 361$, we have \[a^2 + \left(\dfrac{y}{2} + \dfrac{\sqrt{3}}{2}a\right)^2 = 361.\] Expanding this out, we have \[a^2 + \dfrac{y^2}{4} + \dfrac{\sqrt{3}}{2}ay + \dfrac{3}{4}a^2 = 361.\] Multiplying both sides by $4$ and rearranging the left side, we have \[7a^2 + y^2 + 2ay\sqrt{3} = 1444.\] We previously showed that $AC \perp ML$, so $AM \perp ML$ (since $M$ is on $AC$). Therefore, $\triangle AML$ has a right angle at $M$. By the Pythagorean Theorem, $AM^2 + ML^2 = a^2 + y^2 = AL^2 = 196$. Subtracting $a^2 + y^2$ from the left side and $196$ from the right side, we obtain \[6a^2 + 2ay\sqrt{3} = 1248.\] Dividing both sides of the equation by $2\sqrt{3}$ and factoring $a$ out of the left side, we have \[a(a\sqrt{3} + y) = 208\sqrt{3}.\] However, we have $b = \dfrac{y}{2} + \dfrac{\sqrt{3}}{2}a$, so the expression inside the parentheses is simply $2b$! Therefore, \[2ab = 208\sqrt{3}.\]

The algebra’s not over yet. We also showed that $a = \dfrac{x}{2} + \dfrac{\sqrt{3}}{2}b$, so substituting that into $a^2 + b^2 = 361$, we obtain \[b^2 + \left(\dfrac{x}{2} + \dfrac{\sqrt{3}}{2}b\right)^2 = 361.\] Expanding this out, we have \[b^2 + \dfrac{x^2}{4} + \dfrac{\sqrt{3}}{2}bx + \dfrac{3}{4}b^2 = 361.\] Multiplying both sides by $4$ and rearranging the left side, we now have \[7b^2 + x^2 + 2xb\sqrt{3} = 1444.\] Does this equation look familiar? We previously showed that $NK \perp AB$. Therefore, $NK \perp AN$ (since $N$ is on $AB$). So, $\triangle ANK$ has a right angle at $N$. By the Pythagorean Theorem, $AN^2 + KN^2 = b^2 + x^2 = AK^2 = 196$. Subtracting $b^2 + x^2$ from the left side and $196$ from the right side, we have \[6b^2 + 2xb\sqrt{3} = 1248.\] We previously also had the equation $6a^2 + 2ay\sqrt{3} = 1248$, and adding this equation to the above equation and factoring out $2\sqrt{3}$, we have \[6a^2 + 6b^2 + 2\sqrt{3}(bx + ay) = 2496.\] We previously showed $a^2 + b^2 = 361$, so $6a^2 + 6b^2 = 6 \cdot 361 = 2166$. Subtracting $6a^2 + 6b^2$ from the left side and $2166$ from the right side, we obtain $2\sqrt{3}(bx + ay) = 330$. Finally, dividing both sides by $2\sqrt{3}$, we have \[bx + ay = 55\sqrt{3}.\]

We previously arrived at this expression for $[BKLC]$: \[[BKLC] = 2ab - bx - ay - 49\sqrt{3}.\] We now know $2ab = 208\sqrt{3}$ and $bx + ay = 55\sqrt{3}$, so we can simply substitute them in. Therefore, \[[BKLC] = 2ab - bx - ay - 49\sqrt{3} = 208\sqrt{3} - 55\sqrt{3} - 49\sqrt{3} = 104\sqrt{3}.\] Finally, we are given $[BKLC] = n\sqrt{3}$ for some integer $n$. We know $[BKLC] = 104\sqrt{3}$, so $n = \boxed{104}$.

Notice that $[BKLC] = 104\sqrt{3} = \dfrac{208\sqrt{3}}{2} = \dfrac{[ABC]}{2}$. Is this a coincidence?

~V0305

~ Slight edits by Christian, but otherwise explained extremely well!

## Solution 8

[](https://artofproblemsolving.com/wiki/index.php?title=File:2025_AIME_II_14_vvsss.png)

$AK = BK = KL, \angle AKL = 60 ^\circ \implies \angle ABL = 30^\circ$ because an inscribed angle has half the measure of its corresponding central angle.

Similarly, $\angle ACK = 30^\circ.$\[\angle BAK = \angle ABK, \angle LBK + \angle ABK = 30^\circ.\]\[\angle CAL + \angle BAK = 90^\circ - \angle LAK = 30^\circ \implies\]\[\angle CAL = \angle LBK \implies \triangle KLB = \triangle LAC \implies\]$AC = BL.$ Similarly, $AB = CK.$

Denote the area of triangle $X$ as $[X]$ ($\leftarrow$ Wait, what's this? ~ Christian). \[2[ABL] = AB \cdot BL \cdot \sin 30^\circ = \frac{AB \cdot AC}{2} = [ABC].\] Similarly, $[ABL] = [ACK] = \frac {[ABC]}{2}.$\[[BKLC] = [ABC] - [ABL] - [ALC]+ [BLK] = [ABC] - [ABL] = [ABL].\] By applying the Law of Cosines on $\triangle ABL,$ we get $AB^2 + BL^2 - 2 AB \cdot BL \cos 30^\circ = AL^2 \implies  AB^2 + AC^2 - AB \cdot AC \sqrt{3} = AL^2 \implies$$BC^2-2[ABC]\sqrt{3}=AL^2 \implies$\[BC^2 - AL^2 = 4 [BKLC] \sqrt{3} \implies\]\[[BLKC] = \frac {38^2-14^2}{4 \sqrt{3}} = \frac{19^2-7^2}{3} \sqrt{3} = 4 \cdot 26 \sqrt{3} = 104 \sqrt{3}.\]**vladimir.shelomovskii@gmail.com, vvsss**

~ Edited by Christian

## Solution 9

$\triangle KAL$ is clearly equilateral, and $\triangle AKB$ and $\triangle ALC$ are clearly isosceles. Now, we can do a bit of angle chasing. Say $\angle AKB = 2\theta$. Then, since $\triangle AKB$ is isosceles, $\angle ABK = 90^\circ - \theta$. $\angle KAL = 60^\circ$, so $\angle LAC = \theta - 60^\circ$, so $\angle ALC = 300^\circ - 2\theta$, so $\angle KLC = 2\theta$. Since the angles are congruent, $\triangle AKB$ is congruent to $\triangle KLC$ by SAS. As such, we can rotate it around the center of $\triangle KAL$ onto side $\overline{AL}$ to produce $\triangle LAD$. Because all the triangles are congruent, connecting the congruent corners will all produce the same length. From $BC$, we see that this same length is $38$, so $\triangle BCD$ is equilateral with side length $38$. This triangle is comprised of 3 quadrilaterals and $\triangle KAL$ in the center, and it's easy to see that each quadrilateral is congruent to $BKLC$. As such, $[BKLC] = \frac{[BCD]-[KAL]}{3} = \frac{361 \sqrt{3} - 49 \sqrt{3}}{3} = 104 \sqrt{3}$, giving an answer of $\boxed{104}$.

~noob1877

~ Edited by Christian

## Solution 10 (Algebraic bashing with some trig)

[asy] import olympiad; import geometry; size(300); defaultpen(linewidth(0.7)+fontsize(10pt)); pair A = (0,0); pair B = (0,26);  pair C = (16*sqrt(3),0); // approx 27.71 pair K = (sqrt(14^2 - 13^2), 13);  pair L = (8*sqrt(3), sqrt(14^2 - (8*sqrt(3))^2)); draw(A--B--C--cycle); draw(B--K--L--C--cycle); draw(A--K, linewidth(0.5pt)); draw(A--L, linewidth(0.5pt)); draw(K--L, linewidth(0.5pt)); dot(A); dot(B); dot(C); dot(K); dot(L); label("$A$", A, SW); label("$B$", B, NW); label("$C$", C, SE); label("$K$", K, E); label("$L$", L, N); label("$a$", (A+C)/2, S); label("$b$", (A+B)/2, W); label("$14$", (B+K)/2, SW, fontsize(8pt)); label("$14$", (C+L)/2, SW, fontsize(8pt)); label("$14$", (K+L)/2, SW, fontsize(8pt)); label("$38$", (B+C)/2, NE, fontsize(8pt)); draw(rightanglemark(B,A,C, 25)); draw(anglemark(C,A,L, 50)); draw(anglemark(K,A,B, 50)); label("$\alpha$", A, 13.5*dir(degrees(L)/2), fontsize(9pt)); label("$\beta$", A, 8*dir(81.7), fontsize(9pt)); [/asy]
We observe that the desired area can be found by subtracting the areas of the three smaller triangles $\triangle BAK$, $\triangle KAL$, and $\triangle LAC$ from the area of the large triangle $\triangle ABC$. This can be expressed as . Thus, our goal is to compute these four areas.

Since $\triangle KAL$ is equilateral with side length $14$, its area is \[[KAL]=\frac{14^2\sqrt{3}}{4}=49\sqrt{3}.\]

Let $AC=a$ and $AB=b$. Because $\angle CAB$ is a right angle, by the Pythagorean Theorem we have \[a^2+b^2=1444.\]

Let $\angle CAL=\alpha$ and $\angle KAB=\beta$. Then \[\cos\alpha=\frac{a}{28}\] (imagine extending $\overrightarrow{CL}$ to intersect $\overline{AB}$, forming a right triangle with hypotenuse length $2\cdot14=28$), \[\quad \cos\beta=\frac{b}{28}\] similarly. Using Pythagorean identities, \[\sin\alpha=\frac{\sqrt{784-a^2}}{28}, \quad \sin\beta=\frac{\sqrt{784-b^2}}{28}.\]

Since $\angle CAB=90^\circ$ and $\triangle KAL$ is equilateral, we have \[\alpha+\beta=30^\circ.\] Thus, \[\cos(\alpha+\beta)=\cos\alpha\cos\beta-\sin\alpha\sin\beta=\frac{\sqrt{3}}{2}.\]

Substituting, \[\frac{\sqrt{3}}{2}=\frac{ab}{784}-\frac{\sqrt{(784-a^2)(784-b^2)}}{784}.\] Rearranging, \[\frac{ab}{784}-\frac{\sqrt{3}}{2}=\frac{\sqrt{(784-a^2)(784-b^2)}}{784}.\] Clearing denominators, \[ab-392\sqrt{3}=\sqrt{(784-a^2)(784-b^2)}\] Squaring both sides gives \[a^2b^2-784ab\sqrt{3}+392^2\cdot3=(784-a^2)(784-b^2).\] Expanding the RHS, \[a^2b^2-784ab\sqrt{3}+392^2\cdot3=784^2-784a^2-784b^2+a^2b^2.\] Canceling $a^2b^2$ and using $a^2+b^2=1444$, \[-784ab\sqrt{3}+392^2\cdot3=784^2-784(1444).\] Simplifying, \[ab\sqrt{3}=1248 \quad \Rightarrow \quad ab=416\sqrt{3}.\]

The area of the large triangle is \[[ABC]=\frac{ab}{2}=208\sqrt{3}.\]

Now substitute $b=\frac{416\sqrt{3}}{a}$ into $a^2+b^2=1444$: \[a^2+\left(\frac{416\sqrt{3}}{a}\right)^2=1444,\]\[a^4-1444a^2+416^2\cdot3=0.\] Solving for $a^2$, \[a^2=\frac{1444\pm\sqrt{1444^2-12\cdot416^2}}{2}=\frac{1444\pm184}{2},\] so \[a^2=768 \text{ or } 676.\]

From the diagram, $a$ is the longer side, so \[a=16\sqrt{3}, \quad b=26.\]

Points $L$ and $K$ lie on the perpendicular bisectors of $AC$ and $AB$, respectively. Let the heights from $L$ to $AC$ and from $K$ to $AB$ be $h_L$ and $h_K$. Then, \[(8\sqrt{3})^2+h_L^2=14^2, \quad 13^2+h_K^2=14^2,\] which gives \[h_L=2, \quad h_K=3\sqrt{3}.\]

Thus, \[[LAC]=\frac{16\sqrt{3}\cdot2}{2}=16\sqrt{3},\]\[[BAK]=\frac{26\cdot3\sqrt{3}}{2}=39\sqrt{3}.\]

Finally, subtracting areas, \[[ABC]-[BAK]-[KAL]-[LAC]=208\sqrt{3} - 39\sqrt{3} - 49\sqrt{3} - 16\sqrt{3} = 104\sqrt{3}.\]

Therefore, the answer is $\boxed{104}$.

~Voidling

~ Edited by Christian

## Solution 11 (Easier Trig)

The diagram can be found here: [https://docs.google.com/presentation/d/1gJWzTw_nJBmIR8V8ZqY8rkC2hByY-Q-kMjLdP4ICyDQ/edit?usp=sharing](https://docs.google.com/presentation/d/1gJWzTw_nJBmIR8V8ZqY8rkC2hByY-Q-kMjLdP4ICyDQ/edit?usp=sharing) (Credits to the previous solution for some of the diagram)

First, $KAL$ is an equilateral triangle. Letting $\angle LAC = x$, we have $\angle KAB = 90-60-x = 30-x$. Note that since $\Delta CAL$ and $\Delta BAK$ are both isosceles triangles, we have that $AC = 2 \cdot 14\cos(x)$ and $AB = 2 \cdot 14\cos(30-x)$. By the Pythagorean Theorem, we then have \[28^2(\cos^2(x) + \cos^2(30-x)) = 38^2\]\[\implies \cos^2(x) + \cos^2(30-x) = \left(\frac{19}{14}\right)^2\]\[\implies \left(\frac{19}{14}\right)^2  = (\cos(x) + \cos(30-x))^2 - 2\cos(x)\cos(30-x).\] We use the sum to product and product to sum identities on the two parts, respectively: \[\left(\frac{19}{14}\right)^2  = (2\cos(15)\cos(x-15))^2 - 2(\cos(30) + \cos(2x-30)).\] Then, using the fact that $2\cos(15) = 2 \cdot \frac{\sqrt{6} + \sqrt{2}}{4} = \frac{\sqrt{6} + \sqrt{2}}{2}$ and the half angle identity: \[\implies \frac{165}{196} = \frac{\sqrt{3}}{2}\cos(2x-30)\]\[\implies \cos(2x-30) = \frac{55\sqrt{3}}{98}.\]

Next, we note that $\angle BKA = 180 - 2 \cdot (30-x) = 120 + 2x$, so that $\angle BKL = 360 - 60 - (120 + 2x) = 180 - 2x = \angle ALC$. Therefore, by SAS, $\Delta ACL \cong \Delta BLK$. Then $BL = AC = 28\cos(x)$. Similarly, we can find that $KC = AB = 28\cos(30-x)$.

Recall that the area of a quadrilateral equals $\frac{1}{2}$ the product of its diagonals, multiplied by the sine of the angle between them. In this case, we are lucky to have the angle between them be $180 - (30-x) - x = 150$. Therefore, we just need to find $\frac{1}{2} \cdot \sin(150) \cdot BL \cdot CK = 196\cos(x)\cos(30-x)$. Then, using the product to sum identity again, we have that this is just $196\cdot \frac{1}{2}(\cos(30) + \cos(2x-30)) =$\[49\sqrt{3} + 98\cos(2x-30) = 49\sqrt{3} + 55\sqrt{3} = \boxed{104}\sqrt{3}.\]

## Solution 12

Suppose the coordinates of $A(0, 0)$, $B(0, 2b)$, $C(2a, 0)$, $K(d, b)$, $L(a, c)$ because $K$ and $L$ lie on the perpendicular bisector of $AB$ and $AC$ respectively. According to the lengths given, we have

Use shoelace formula,

Here, let $x = a - d$, $y = b - c$, $x^2 + y^2 = 14^2$, the goal is to find $xy$. While using elimination with $(1) - (3)$, we get $a^2 - d^2 = 19^2 - 14^2 \implies (a - d)(a + d) = 165 \implies a + d = \dfrac{165}{x} \implies a = \dfrac{x + \dfrac{165}{x}}{2}$. Similarly, $b = \dfrac{y + \dfrac{165}{y}}{2}$.

We substitute them in equation $(1)$,

Then, \[S_{CBKL} = |49\sqrt{3} + 55\sqrt{3}| = 104\sqrt{3}\]

The answer is $\boxed{104}$.

~[reda_mandymath](https://artofproblemsolving.com/wiki/index.php/User:Reda_mandymath) discussed with James Y
