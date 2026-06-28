## Problem

Pentagon $ABCDE$ is inscribed in a circle, and $\angle BEC = \angle CED = 30^\circ$. Let line $AC$ and line $BD$ intersect at point $F$, and suppose that $AB = 9$ and $AD = 24$. What is $BF$?

$\textbf{(A) } \frac{57}{11} \qquad\textbf{(B) } \frac{59}{11} \qquad\textbf{(C) } \frac{60}{11} \qquad\textbf{(D) } \frac{61}{11} \qquad\textbf{(E) } \frac{63}{11}$

## Diagram

[asy] /* Made by MRENTHUSIASM */ size(200); real r = 7*sqrt(3); pair O, A, B, C, D, E, F; O = origin; B = r*dir(30); C = r*dir(-30); D = r*dir(-90); E = r*dir(180); A = intersectionpoints(Circle(O,r),Circle(B,9))[0]; F = intersectionpoint(A--C,B--D);  draw(Circle(O,r)^^A--B--C--D--E--cycle^^D--B--E--C--A--cycle); dot("$B$",B,1.5*B/r,linewidth(4)); dot("$C$",C,1.5*C/r,linewidth(4)); dot("$D$",D,1.5*D/r,linewidth(4)); dot("$E$",E,1.5*E/r,linewidth(4)); dot("$A$",A,1.5*A/r,linewidth(4)); dot("$F$",F,1.5*F/r,linewidth(4)); label("$30^{\circ}$",E,6*(1,0),fontsize(8)); label("$30^{\circ}$",E,7*dir(-32),fontsize(8)); label("$9$",0.92*midpoint(A--B)); label("$24$",1.8*midpoint(A--D)); [/asy] ~MRENTHUSIASM

## Solution 1

We will scale down the diagram by a factor of $3$ so that $AB = 3$ and $AD = 8.$ Since $\angle BEC = 30^{\circ},$ it follows that $\angle BAC = \angle BDC = 30^{\circ}$ as they all subtend the same arc. Similarly, since $\angle CED = 30^{\circ},$ it follows that $\angle CAD = \angle CBD = 30^{\circ}$ as well.

We obtain the following diagram: [asy] /* Made by MRENTHUSIASM */ size(200); real r = 7*sqrt(3); pair O, A, B, C, D, E, F; O = origin; B = r*dir(30); C = r*dir(-30); D = r*dir(-90); E = r*dir(180); A = intersectionpoints(Circle(O,r),Circle(B,9))[0]; F = intersectionpoint(A--C,B--D);  draw(Circle(O,r)^^B--C--D--E--A^^B--E--C--F); draw(A--D--B--cycle^^A--F,red); dot("$B$",B,1.5*B/r,linewidth(4)); dot("$C$",C,1.5*C/r,linewidth(4)); dot("$D$",D,1.5*D/r,linewidth(4)); dot("$E$",E,1.5*E/r,linewidth(4)); dot("$A$",A,1.5*A/r,linewidth(4)); dot("$F$",F,1.5*F/r,linewidth(4)); label("$30^{\circ}$",E,6*(1,0),fontsize(8)); label("$30^{\circ}$",E,7*dir(-32),fontsize(8)); label("$30^{\circ}$",A,9*dir(-56),red+fontsize(8)); label("$30^{\circ}$",A,9*dir(-84),red+fontsize(8)); label("$3$",1.1*midpoint(A--B),red); label("$8$",0.4*midpoint(A--D),red); [/asy] Note that $\triangle ABD$ has $\angle BAD = 60^{\circ}.$ Applying Law of Cosines, we get \begin{align*} BD^2 &= AB^2+AD^2-2AB\cdot AD \cdot\cos{60^{\circ}} \\ &= 9 + 64 - 2 \cdot 3 \cdot 8 \cdot \frac{1}{2} \\ &= 49, \end{align*} from which $BD = 7.$

From here, we wish to find $BF.$ As $AF$ is the angle bisector of $\angle BAD,$ we apply the Angle Bisector Theorem: \begin{align*} \frac{AB}{BF} &= \frac{AD}{DF} \\ \frac{3}{BF} &= \frac{8}{7-BF}. \end{align*} Solving for $BF,$ we get $BF = \frac{21}{11}.$ Remember to scale the figure back up by a factor of $3,$ so our answer is $\frac{21}{11}\cdot 3 = \boxed{\textbf{(E) } \frac{63}{11}}.$

~lprado ~MRENTHUSIASM

## Solution 2 Law of (Co)Sine

From cyclic quadrilateral $CDAE$, we have $\angle CAD = \angle CED = 30^\circ.$ Since $ABDE$ is also cyclic, we have $\angle BAD = \angle BED = 60^\circ$, so, \[\angle BAC= \angle BAD - \angle CAD = 60^\circ - 30^\circ = 30^\circ.\] Using Law of Cosines on $\triangle ABD$, we get \[BD^2=9^2+24^2-2(9)(24)\cos(60^\circ).\] Solving, we get $BD=21$. Next, let $\overline{BF}=x$, and $\angle AFB = \theta$, which means $\overline{FD}=21-x$ and $\angle AFD = 180-\theta$. Using Law of Sines on $\triangle AFB$, we have \[\frac{9}{\sin \theta}=\frac{x}{\sin 30}.\] Solving for $\sin \theta$, we get $\sin \theta = \frac{9}{2x}$. Now we apply the Law of Sines to $\triangle AFD.$ We have \[\frac{24}{\sin(180-\theta)} = \frac{21-x}{\sin 30}.\] Since $\sin(180-\theta) = \sin(\theta),$ and $\sin \theta = \frac{9}{2x}$, we have \[\frac{16x}{3} = 42-2x.\] Solving for $x$ gives $\boxed{x=\frac{63}{11}}$ or $\boxed{\textbf{(E) } \frac{63}{11}}$.

~evanhliu2009

## Solution 3 (Ptolemy’s + Similarity)

We have $ABCDE$ cyclic, so $\angle BAC=\angle CAD=\angle BEC=30^\circ$. Hence cyclic quadrilateral $ABCD$ has $\angle BAD=60^\circ$. Law of Cosines on triangle $BAD$ gives $\overline{BD}^2=9^2+24^2-2\cdot9\cdot24\cos60^\circ$. Hence $\overline{BD}=21$. Since triangle $BCD$ is a 120-30-30 triangle, we can use law of sines or just memorize ratios to get $\overline{BC}=\overline{CD}=7\sqrt3$. Now Ptolemy’s on $ABCD$ yields $7\sqrt3(9+24)=21\overline{AC}$. Hence $\overline{AC}=11\sqrt3$. Now notice that $\angle BCF=\angle ACB$, and $\angle CBF=\angle CAB=30^\circ$. Hence triangles $CBF$ and $CAB$ are similar, and $\frac{\overline{BF}}{\overline{BC}}=\frac{\overline{AB}}{\overline{AC}}$, so $\frac{\overline{BF}}{7\sqrt3}=\frac9{11\sqrt3}$ and $\overline{BF}=\frac{63}{11}$, or $\boxed{\textbf{(E) } \frac{63}{11}}$.

~benjamintontungtungtungsahur (look guys im famous)

## Solution 4 (Area & Angle Bisector Length)

As shown in previous solutions, the angles subtending the same arcs give us $\angle BAC = \angle BEC = 30^\circ$ and $\angle CAD = \angle CED = 30^\circ.$ This tells us that \[\angle BAD = \angle BAC + \angle CAD = 60^\circ,\] and line $AF$ acts as the interior angle bisector of $\angle BAD.$

We can find the length of the angle bisector $AF$ by splitting the area of $\triangle ABD$ into the sum of the areas of $\triangle ABF$ and $\triangle AFD$: \[\text{Area}(\triangle ABD) = \text{Area}(\triangle ABF) + \text{Area}(\triangle AFD).\]

Using the sine formula for area ($\text{Area} = \frac{1}{2}ab\sin C$), we have: \[\frac{1}{2}(AB \cdot AD) \sin 60^\circ = \frac{1}{2}(AB \cdot AF) \sin 30^\circ + \frac{1}{2}(AD \cdot AF) \sin 30^\circ.\]

Substituting the known values $AB = 9$ and $AD = 24$: \[\frac{1}{2}(9 \cdot 24) \frac{\sqrt{3}}{2} = \frac{1}{2}(9 \cdot AF) \frac{1}{2} + \frac{1}{2}(24 \cdot AF) \frac{1}{2}.\]

Multiplying the entire equation by $4$ to clear the denominators yields: \begin{align*} 216\sqrt{3} &= 9(AF) + 24(AF) \\ 216\sqrt{3} &= 33(AF) \\ AF &= \frac{216\sqrt{3}}{33} = \frac{72\sqrt{3}}{11}. \end{align*}

Now, we apply the Law of Cosines on $\triangle ABF$ to solve directly for $BF$: \[BF^2 = AB^2 + AF^2 - 2(AB \cdot AF)\cos 30^\circ.\]

Substituting $AB = 9,$$AF = \frac{72\sqrt{3}}{11},$ and $\cos 30^\circ = \frac{\sqrt{3}}{2}$: \begin{align*} BF^2 &= 9^2 + \left(\frac{72\sqrt{3}}{11}\right)^2 - 2 \cdot 9 \cdot \frac{72\sqrt{3}}{11} \cdot \frac{\sqrt{3}}{2} \\ BF^2 &= 81 + \frac{15552}{121} - \frac{1944}{11}. \end{align*}

Finding a common denominator of $121$: \begin{align*} BF^2 &= \frac{81 \cdot 121 + 15552 - 1944 \cdot 11}{121} \\ BF^2 &= \frac{9801 + 15552 - 21384}{121} \\ BF^2 &= \frac{3969}{121}. \end{align*}

Taking the square root of both sides ($\sqrt{3969} = 63$ and $\sqrt{121} = 11$), we find: \[BF = \frac{63}{11}.\]

Thus, the answer is $\boxed{\textbf{(E) } \frac{63}{11}}.$

~ARJUNKHOKHAR

## See Also

*   [AMC 12](https://artofproblemsolving.com/wiki/index.php?title=AMC_12 "AMC 12")
*   [AMC 12 Problems and Solutions](https://artofproblemsolving.com/wiki/index.php?title=AMC_12_Problems_and_Solutions "AMC 12 Problems and Solutions")
*   [Mathematics competitions](https://artofproblemsolving.com/wiki/index.php?title=Mathematics_competitions "Mathematics competitions")
*   [Mathematics competition resources](https://artofproblemsolving.com/wiki/index.php?title=Mathematics_competition_resources "Mathematics competition resources")

[](https://artofproblemsolving.com/wiki/index.php?title=File:AMC_Logo.png)
