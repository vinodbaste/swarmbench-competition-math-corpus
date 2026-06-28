## Problem

Suppose $\triangle ABC$ has angles $\angle BAC = 84^\circ, \angle ABC=60^\circ,$ and $\angle ACB = 36^\circ.$ Let $D, E,$ and $F$ be the midpoints of sides $\overline{BC}, \overline{AC},$ and $\overline{AB},$ respectively. The circumcircle of $\triangle DEF$ intersects $\overline{BD}, \overline{AE},$ and $\overline{AF}$ at points $G, H,$ and $J,$ respectively. The points $G, D, E, H, J,$ and $F$ divide the circumcircle of $\triangle DEF$ into six minor arcs, as shown. Find $\widehat{DE}+2\cdot \widehat{HJ} + 3\cdot\widehat{FG},$ where the arcs are measured in degrees. [asy]         import olympiad;         size(6cm);         defaultpen(fontsize(10pt));         pair B = (0, 0), A = (Cos(60), Sin(60)), C = (Cos(60)+Sin(60)/Tan(36), 0), D = midpoint(B--C), E = midpoint(A--C), F = midpoint(A--B);         guide circ = circumcircle(D, E, F);         pair G = intersectionpoint(B--D, circ), J = intersectionpoints(A--F, circ)[0], H = intersectionpoints(A--E, circ)[0];         draw(B--A--C--cycle);         draw(D--E--F--cycle);         draw(circ);  dot(A);dot(B);dot(C);dot(D);dot(E);dot(F);dot(G);dot(H);dot(J);         label("$A$", A, (0, .8));         label("$B$", B, (-.8, -.8));         label("$C$", C, (.8, -.8));         label("$D$", D, (0, -.8));         label("$E$", E, (.8, .2));         label("$F$", F, (-.8, .2));         label("$G$", G, (0, .8));         label("$H$", H, (-.2, -1));         label("$J$", J, (.2, -.8)); [/asy]

## Solution 1

Notice that due to midpoints and properties of medial triangle, $\triangle DEF\sim\triangle FBD\sim\triangle AFE\sim\triangle EDC\sim\triangle ABC$ (and by medial triangle $\triangle DEF \cong \triangle FBD \cong \triangle AFE \cong \triangle EDC.$) . As a result, the angles and arcs are readily available. Due to inscribed angles, \[\widehat{DE}=2\angle DFE=2\angle ACB=2\cdot36=72^\circ\] Similarly, \[\widehat{FG}=2\angle FDB=2\angle ACB=2\cdot36=72^\circ\]

In order to calculate $\widehat{HJ}$, we use the fact that $\angle BAC=\frac{1}{2}(\widehat{FDE}-\widehat{HJ})$. We know that $\angle BAC=84^\circ$, and \[\widehat{FDE}=360-\widehat{FE}=360-2\angle FDE=360-2\angle CAB=360-2\cdot84=192^\circ\]

Substituting,

Thus, $\widehat{DE}+2\cdot\widehat{HJ}+3\cdot\widehat{FG}=72+48+216=\boxed{336}^\circ$.

~ [eevee9406](https://artofproblemsolving.com/wiki/index.php/User:Eevee9406)

~ Edited by [aoum](https://artofproblemsolving.com/wiki/index.php/User:Aoum)

Alternatively,

~ [Pengu14](https://artofproblemsolving.com/community/user/1096232)

## Solution 2

Notice that $\triangle ABC \sim \triangle FHE \sim \triangle DEF$ because $FE \parallel BC$ and $DE \parallel AB,$ so all angles in each triangle will be equal by the Midline Theorem. Therefore, we have $\widehat{DE} = 2 \cdot 36^\circ = 72^\circ.$ Now, quadrilateral $FHED$ is cyclic, so opposite angles add to $180^\circ.$ Since we know from similar triangles that $\angle{FED} = 60^\circ + 36^\circ = 96^\circ,$ we see that $\angle{HFD} = 84^\circ.$ We also know that $\angle{JFE} = 60^\circ + 36^\circ = 96^\circ,$ so that means $\angle{JFH} = 96^\circ - 84^\circ = 12^\circ \implies \widehat{JH} = 24^\circ.$ Finally, $\angle{B} = 60^\circ = \frac{\widehat{JED} - \widehat{FG}}{2}.$\[\widehat{JED} = \widehat{DE} + \widehat{JE} = 72^\circ + 2(\angle{JFE}) = 192^\circ.\] So $\widehat{FG} = 192^\circ - 120^\circ = 72^\circ.$ The answer is $72^\circ + 2\cdot 24^\circ + 3\cdot 72^\circ = \boxed{336^\circ}.$

~[grogg007](https://artofproblemsolving.com/wiki/index.php?title=User:Grogg007 "User:Grogg007")

NOTE: Several of the letters appear to be misused. For example, $\angle{FED}=60^\circ$ not $96^\circ$.

~Christian

NOTE2: It should be $\angle{HED}=60^\circ + 36^\circ = 96^\circ$ and $\angle{HFD} = 180^\circ - \angle{HED} = 84^\circ$. The same for $\angle{JFD}$, not $\angle{JFE}$.

~LANOUZHIHUN

## Solution 3

Triangle $DEF$ is the median triangle of $ABC$. It's known that the circumcircle of $DEF$ is the Nine-Point Circle of $ABC$.

Arc $DE$ is easy to find through inscribed angles theorem, as $72^\circ$.

Through Intercepted Secants Theorem, the measure of angle $JAH$ is precisely half that of the difference of the far arc $FE$ and the near arc $JH$. Thus, $84 = 0.5 \cdot (192-JH)$, or $24 = JH$

Finally, through Alternate Interior it's obvious that angle $FDG$ is $36^\circ$. It follows that arc $FG$ is just $72^\circ$.

\[DE + 2HJ + 3FG:~\text{arcs measured in degrees}~ = 72 + 48 + 216 = \boxed{336}^\circ\]

The purpose of this solution is to bring up the existence of the nine-point circle. Consequently, points $G$, $H$, and $J$ are not random, but are the intersections of the altitudes dropped from $A$, $B$, and $C$ respectively. It may not be used in this problem specifically, but is great information for the long run.

~Pinotation
