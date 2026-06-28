## Problem

Let $ABCD$ be a tetrahedron such that $AB=CD= \sqrt{41}$, $AC=BD= \sqrt{80}$, and $BC=AD= \sqrt{89}$. There exists a point $I$ inside the tetrahedron such that the distances from $I$ to each of the faces of the tetrahedron are all equal. This distance can be written in the form $\frac{m \sqrt n}{p}$, where $m$, $n$, and $p$ are positive integers, $m$ and $p$ are relatively prime, and $n$ is not divisible by the square of any prime. Find $m+n+p$.

## Solution 1

Notice that , , and , let , , , and . Then the plane has a normal

Hence, the distance from to plane , or the height of the tetrahedron, is

Each side of the tetrahedron has the same area due to congruency by "S-S-S", and we call it . Then by the volume formula for pyramids,

Hence, , and so the answer is .

Solution by Quantum-Phantom

## Solution 2

[asy] import three;  currentprojection = orthographic(1,1,1);  triple O = (0,0,0); triple A = (0,2,0); triple B = (0,0,1); triple C = (3,0,0); triple D = (3,2,1); triple E = (3,2,0); triple F = (0,2,1); triple G = (3,0,1);  draw(A--B--C--cycle, red); draw(A--B--D--cycle, red); draw(A--C--D--cycle, red); draw(B--C--D--cycle, red);  draw(E--A--O--C--cycle); draw(D--F--B--G--cycle); draw(O--B); draw(A--F); draw(E--D); draw(C--G);  label("$O$", O, SW); label("$A$", A, NW); label("$B$", B, W); label("$C$", C, S); label("$D$", D, NE); label("$E$", E, SE); label("$F$", F, NW); label("$G$", G, NE); [/asy]

Inscribe tetrahedron $ABCD$ in an rectangular prism as shown above.

By the Pythagorean theorem, we note

\[OA^2 + OB^2 = AB^2 = 41,\]\[OA^2 + OC^2 = AC^2 = 80, \text{and}\]\[OB^2 + OC^2 = BC^2 = 89.\]

Solving yields $OA = 4, OB = 5,$ and $OC = 8.$

Since each face of the tetrahedron is congruent, we know the point we seek is the center of the circumsphere of $ABCD.$ We know all rectangular prisms can be inscribed in a circumsphere, therefore the circumsphere of the rectangular prism is also the circumsphere of $ABCD.$

We know that the distance from all $4$ faces must be the same, so we only need to find the distance from the center to plane $ABC$.

Let $O = (0,0,0), A = (4,0,0), B = (0,5,0),$ and $C = (0,0,8).$ We obtain that the plane of $ABC$ can be marked as $\frac{x}{4} + \frac{y}{5} + \frac{z}{8} = 1,$ or $10x + 8y + 5z - 40 = 0,$ and the center of the prism is $(2,\frac{5}{2},4).$

Using the Point-to-Plane distance formula, our distance is

\[d = \frac{|10\cdot 2 + 8\cdot \frac{5}{2} + 5\cdot 4 - 40|}{\sqrt{10^2 + 8^2 + 5^2}} = \frac{20}{\sqrt{189}} = \frac{20\sqrt{21}}{63}.\]

Our answer is $20 + 21 + 63 = \boxed{104}.$

- [spectraldragon8](https://artofproblemsolving.com/wiki/index.php/User:Spectraldragon8)

## Solution 3(Formula Abuse)

We use the formula for the volume of iscoceles tetrahedron. $V = \sqrt{(a^2 + b^2 - c^2)(b^2 + c^2 - a^2)(a^2 + c^2 - b^2)/72}$

Note that all faces have equal area due to equal side lengths. By Law of Cosines, we find \[\cos{\angle ACB} = \frac{80 + 89 - 41}{2\sqrt{80\cdot 89}}= \frac{16}{\sqrt{445}}.\].

From this, we find \[\sin{\angle ACB} = \sqrt{1-\cos^2{\angle ACB}} = \sqrt{1 - \frac{256}{445}} = \sqrt{\frac{189}{445}}\] and can find the area of $\triangle ABC$ as \[A = \frac{1}{2} \sqrt{89\cdot 80}\cdot \sin{\angle ACB} = 6\sqrt{21}.\]

Let $R$ be the distance we want to find. By taking the sum of (equal) volumes \[[ABCI] + [ABDI] + [ACDI] + [BCDI] = V,\] We have \[V = \frac{4AR}{3}.\] Plugging in and simplifying, we get $R = \frac{20\sqrt{21}}{63}$ for an answer of $20 + 21 + 63 = \boxed{104}$

~AtharvNaphade

## Solution 4

Let $AH$ be perpendicular to $BCD$ that meets this plane at point $H$. Let $AP$, $AQ$, and $AR$ be heights to lines $BC$, $CD$, and $BD$ with feet $P$, $Q$, and $R$, respectively.

We notice that all faces are congruent. Following from Heron's formula, the area of each face, denoted as $A$, is $A = 6 \sqrt{21}$.

Hence, by using this area, we can compute $AP$, $AQ$ and $AR$. We have $AP = \frac{2 A}{BC} = \frac{2A}{\sqrt{89}}$, $AQ = \frac{2 A}{CD} = \frac{2A}{\sqrt{41}}$, and $AR = \frac{2 A}{BC} = \frac{2A}{\sqrt{80}}$.

Because $AH \perp BCD$, we have $AH \perp BC$. Recall that $AP \perp BC$. Hence, $BC \perp APH$. Hence, $BC \perp HP$.

Analogously, $CD \perp HQ$ and $BD \perp HR$.

We introduce a function $\epsilon \left( l \right)$ for $\triangle BCD$ that is equal to 1 (resp. -1) if point $H$ and the opposite vertex of side $l$ are on the same side (resp. opposite sides) of side $l$.

The area of $\triangle BCD$ is

Denote $B = 2A$. The above equation can be organized as

This can be further reorganized as

Taking squares on both sides and reorganizing terms, we get

Taking squares on both sides and reorganizing terms, we get

\[ - \epsilon_{BC} 2 B \sqrt{B^2 - 89 AH^2} = - 2 B^2 + 189 AH^2 . \]

Taking squares on both sides, we finally get

Now, we plug this solution to Equation (1). We can see that $\epsilon_{BC} = -1$, $\epsilon_{CD} = \epsilon_{BD} = 1$. This indicates that $H$ is out of $\triangle BCD$. To be specific, $H$ and $D$ are on opposite sides of $BC$, $H$ and $C$ are on the same side of $BD$, and $H$ and $B$ are on the same side of $CD$.

Now, we compute the volume of the tetrahedron $ABCD$, denoted as $V$. We have $V = \frac{1}{3} A \cdot AH = \frac{40 A^2}{3 \cdot 189}$.

Denote by $r$ the inradius of the inscribed sphere in $ABCD$. Denote by $I$ the incenter. Thus, the volume of $ABCD$ can be alternatively calculated as

From our two methods to compute the volume of $ABCD$ and equating them, we get

Therefore, the answer is $20 + 21 + 63 = \boxed{\textbf{(104) }}$.

~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Solution 5(A quicker method to compute the height from $A$ to plane $BCD$)

We put the solid to a 3-d coordinate system. Let $B = \left( 0, 0, 0 \right)$, $D = \left( \sqrt{80}, 0, 0 \right)$. We put $C$ on the $x-o-y$ plane. Now, we compute the coordinates of $C$.

Applying the law of cosines on $\triangle BCD$, we get $\cos \angle CBD = \frac{4}{\sqrt{41 \cdot 5}}$. Thus, $\sin \angle CBD = \frac{3 \sqrt{21}}{\sqrt{41 \cdot 5}}$. Thus, $C = \left( \frac{4}{\sqrt{5}} , \frac{3 \sqrt{21}}{\sqrt{5}} , 0 \right)$.

Denote $A = \left( x, y , z \right)$ with $z > 0$.

Because $AB = \sqrt{89}$, we have $x^2 + y^2 + z^2 = 89$

Because $AD = \sqrt{41}$, we have

\[\left( x - \sqrt{80} \right)^2 + y^2 + z^2 = 41 \hspace{1cm} (2)\]

Because $AC = \sqrt{80}$, we have

\[\left( x - \frac{4}{\sqrt{5}} \right)^2 + \left( y - \frac{3 \sqrt{21}}{\sqrt{5}} \right)^2  + z^2 = 80 \hspace{1cm} (3)\]

Now, we compute $x$, $y$ and $z$.

Taking $(1)-(2)$, we get \[2 \sqrt{80} x = 128 .\]

Thus, $x = \frac{16}{\sqrt{5}}$.

Taking $(1) - (3)$, we get \[2 \cdot \frac{4}{\sqrt{5}} x + 2 \cdot \frac{3 \sqrt{21}}{\sqrt{5}} y = 50 .\]

Thus, $y = \frac{61}{3 \sqrt{5 \cdot 21}}$.

Plugging $x$ and $y$ into Equation (1), we get $z = \frac{80 \sqrt{21}}{63}$.

~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com) ~numerophile (formatting edits)

## Solution 6 (Different Perspective)

Consider the following construction of the tetrahedron. Place $AB$ on the floor. Construct an isosceles vertical triangle with $AB$ as its base and $M$ as the top vertex. Place $CD$ on the top vertex parallel to the ground with midpoint $M.$ Observe that $CD$ can rotate about its midpoint. At a certain angle, we observe that the lengths satisfy those given in the problem. If we project $AB$ onto the plane of $CD$, let the minor angle $\theta$ be this discrepancy.

By Median formula or Stewart's theorem, $AM = \frac{1}{2}\sqrt{2AC^2 + 2AD^2 - CD^2} = \frac{3\sqrt{33}}{2}.$ Consequently the area of $\triangle AMB$ is $\frac{\sqrt{41}}{2} \left (\sqrt{(\frac{3\sqrt{33}}{2})^2 - (\frac{\sqrt{41}}{2})^2} \right ) = 4\sqrt{41}.$ Note the altitude $8$ is also the distance between the parallel planes containing $AB$ and $CD.$

By Distance Formula,

\begin{align*} (\frac{\sqrt{41}}{2} - \frac{1}{2}CD \cos{\theta})^2 + (\frac{1}{2}CD \sin{\theta}^2) + (8)^2 &= AC^2 = 80 \\ (\frac{\sqrt{41}}{2} + \frac{1}{2}CD \cos{\theta})^2 + (\frac{1}{2}CD \sin{\theta}^2) + (8)^2 &= AD^2 = 89 \\ \implies CD \cos{\theta} \sqrt{41} &= 9 \\ \sin{\theta} &= \sqrt{1 - (\frac{9}{41})^2} = \frac{40}{41}. \end{align*}

Then the volume of the tetrahedron is given by $\frac{1}{3} [AMB] \cdot CD \sin{\theta} = \frac{160}{3}.$

The volume of the tetrahedron can also be segmented into four smaller tetrahedrons from $I$ w.r.t each of the faces. If $r$ is the inradius, i.e the distance to the faces, then $\frac{1}{3} r([ABC] + [ABD] + [ACD] + [BCD])$ must the volume. Each face has the same area by SSS congruence, and by Heron's it is $\frac{1}{4}\sqrt{(a + b + c)(a + b - c)(c + (a-b))(c -(a - b))} = 6\sqrt{21}.$

Therefore the answer is, $\dfrac{3 \frac{160}{3}}{24 \sqrt{21}} = \frac{20\sqrt{21}}{63} \implies \boxed{104}.$

~Aaryabhatta1

## Solution 7 (simplest way to calculate [ABCD])

After finding that $ABCD$ can be inscribed in a $4\times5\times8$ box, note that $[ABCD]=\mathbf{box}-(\frac{1}{2})(\frac{4}{3})(4)(5)(8)=\frac{160}{3}$, where the third term describes the area of 4 congruent right tetrahedrons whose right angle is at the apex and whose apex lengths are 4, 5, and 8. Then proceed as in Solution 3.

~clarkculus

## Solution 8 (fast)

Observe that $ABCD$ can be inscribed in a $4\times5\times8$ box, which gives the coordinates of the points: we have $A=(8,0,0)$, $B=(8,5,4)$, $C=(0,0,4)$ and $D=(0,5,0)$. Recall the formula $V=\frac{1}{3}RS$, where $V$ is the volume of the tetrahedron, $S$ is the surface area, and $R$ is the insphere radius. Using the fact that the faces of $ABCD$ have equal area and that $V=\frac{1}{3}[ACD] \times h$, where $h$ is the distance from plane $ACD$ to $B$, we can rearrange to get $R=\frac{h}{4}$. We compute that the the equation of plane $ACD$ is $5x+8y+10z-40=0$, and applying point-to-plane gives $h=\frac{\vert 5(8)+8(5)+10(4)-40 \vert}{\sqrt{5^2+8^2+10^2}}=\frac{80}{\sqrt{189}} \implies R=\frac{20\sqrt{21}}{63} \implies \boxed{104}$.

~bomberdoodles

## Solution 9 (Analytical Geometry)

Like in Solution 1, we have $A = (0,0,0)$, $B = (4,5,0)$, $C = (0,5,8)$, $D = (4,0,8)$. If we let the inradius be $r$, then the volume of the tetrahedron is equal to $\frac{1}{3}[ABC]r + \frac{1}{3}[BCD]r + \frac{1}{3}[ABD]r + \frac{1}{3}[ACD]r = V$ by the formula $V = \frac{1}{3}Ah$. Also note that $[ABC] = [BCD] = [ABD] = [ACD]$ because they all have the same side lengths. So, if we let $[ABC] = A$, then $\frac{4}{3}Ar = V$, so $r = \frac{3V}{4A}$. Now, all we need to do is to find V and A. We note that the area of the triangle $[ABC] = |\frac{\overrightarrow{AB}\times\overrightarrow{AC}}{2}|$. Also, if we let the normal vector from $\Delta ABC$ to be $\bold{n}$, the height $h$ from $D$ to $\Delta ABC$ is $\overrightarrow{AD} \cdot \hat{\bold{n}} = \frac{\overrightarrow{AD} \cdot \bold{n}}{\bold{|n|}}$. Therefore, the volume of the tetrahedron is equal to $\frac{1}{3}[ABC]h = \frac{1}{3}|\frac{\overrightarrow{AB}\times\overrightarrow{AC}}{2}|\frac{\overrightarrow{AD} \cdot \bold{n}}{\bold{|n|}} = \frac{1}{6}|\overrightarrow{AB}\times\overrightarrow{AC}|\frac{\overrightarrow{AD} \cdot \bold{n}}{\bold{|n|}}$. Now, we notice that $\overrightarrow{AB}\times\overrightarrow{AC}$ is a normal vector of the $\Delta ABC$ because the cross product of two vectors is always perpendicular to both of the vectors, and both of the vectors lie in the plane of $\Delta ABC$. This means that we can let $\bold{n} = \overrightarrow{AB}\times\overrightarrow{AC}$. So, the volume of the tetrahedron is $V = \frac{1}{6}|\overrightarrow{AB}\times\overrightarrow{AC}|\frac{\overrightarrow{AD} \cdot (\bold{\overrightarrow {AB}\times\overrightarrow{AC}})}{\bold{|\overrightarrow{AB}\times\overrightarrow{AC}|}} = \frac{1}{6}\overrightarrow{AD} \cdot (\bold{\overrightarrow{AB}\times\overrightarrow{AC}})$. The expression $\overrightarrow{AD} \cdot (\bold{\overrightarrow{AB}\times\overrightarrow{AC}})$ is more commonly known as a box product and can be used to find the volume of any parallelepiped. We know that $\overrightarrow{AB} = (4,5,0)$, $\overrightarrow{AC} = (0,5,8)$, and $\overrightarrow{AD} = (4,0,8)$. Now, $\overrightarrow{AB} \times \overrightarrow{AC} = (8*5-5*0, 0*0-8*4, 4*5-5*0) = (40, -32, 20)$. So, $\overrightarrow{AD} \cdot (\bold{\overrightarrow{AB}\times\overrightarrow{AC}}) = (4,0,8) \cdot (40,-32,20) = 4*40 + 0*-32 + 8*20 = 320$. So, $V = \frac{1}{6}\overrightarrow{AD} \cdot (\bold{\overrightarrow{AB}\times\overrightarrow{AC}}) = \frac{320}{6} = \frac{160}{3}$. Now $[ABC]$ is just equal to $\frac{1}{2}|\overrightarrow{AB} \times \overrightarrow{AC}|$ as it is half the parallelogram. So, we have $A = \frac{1}{2}|\overrightarrow{AB} \times \overrightarrow{AC}| = \frac{1}{2}|(40,-32,20)| = \frac{1}{2}\sqrt{3024}$. So, $r = \frac{3V}{4A} = \frac{160}{2\sqrt{3024}}$. This expression can be simplified to $\frac{20\sqrt{21}}{63}$. So, our answer is $20 + 63 + 21 = \boxed{104}$.

- Rutvik Arora (plz sub to [https://www.youtube.com/@themathguy6302](https://www.youtube.com/@themathguy6302))

## Solution 10 (simplest)

Obviously, $ABCD$ is a [disphenoid](https://artofproblemsolving.com/wiki/index.php?title=Disphenoid "Disphenoid"), and it follows that its circumscribing rectangular prism with nonadjacent vertices $A$, $B$, $C$, and $D$ has a length, width, and height of $4$, $5$, and $8$. Thus, \[[ABCD]=4\cdot 5\cdot 8\left(1-4\cdot\frac 16\right)=\frac{160}{3}.\] Since the distances from $I$ to the faces of $ABCD$ are all equal, let this common value be $x$ and WLOG it follows that

through Heron's formula, so the desired value is $\boxed{104}$.

-pieMax2713
