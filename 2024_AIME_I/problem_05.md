## Problem

Rectangles $ABCD$ and $EFGH$ are drawn such that $D,E,C,F$ are collinear. Also, $A,D,H,G$ all lie on a circle. If $BC=16$,$AB=107$,$FG=17$, and $EF=184$, what is the length of $CE$?

[asy] import graph; unitsize(0.1cm);  pair A = (0,0);pair B = (70,0);pair C = (70,16);pair D = (0,16);pair E = (3,16);pair F = (90,16);pair G = (90,33);pair H = (3,33); dot(A^^B^^C^^D^^E^^F^^G^^H); label("$A$", A, S);label("$B$", B, S);label("$C$", C, N);label("$D$", D, N);label("$E$", E, S);label("$F$", F, S);label("$G$", G, N);label("$H$", H, N); draw(E--D--A--B--C--E--H--G--F--C); [/asy]

## Solution 1

We use simple geometry to solve this problem.

[asy] import graph; unitsize(0.1cm);  pair A = (0,0);pair B = (107,0);pair C = (107,16);pair D = (0,16);pair E = (3,16);pair F = (187,16);pair G = (187,33);pair H = (3,33); label("$A$", A, SW);label("$B$", B, SE);label("$C$", C, N);label("$D$", D, NW);label("$E$", E, S);label("$F$", F, SE);label("$G$", G, NE);label("$H$", H, NW); draw(E--D--A--B--C--E--H--G--F--C); /*Diagram by Technodoggo*/ [/asy]

We are given that $A$, $D$, $H$, and $G$ are concyclic; call the circle that they all pass through circle $\omega$ with center $O$. We know that, given any chord on a circle, the perpendicular bisector to the chord passes through the center; thus, given two chords, taking the intersection of their perpendicular bisectors gives the center. We therefore consider chords $HG$ and $AD$ and take the midpoints of $HG$ and $AD$ to be $P$ and $Q$, respectively.

[asy] import graph; unitsize(0.1cm);  pair A = (0,0);pair B = (107,0);pair C = (107,16);pair D = (0,16);pair E = (3,16);pair F = (187,16);pair G = (187,33);pair H = (3,33); label("$A$", A, SW);label("$B$", B, SE);label("$C$", C, N);label("$D$", D, NW);label("$E$", E, S);label("$F$", F, SE);label("$G$", G, NE);label("$H$", H, NW); draw(E--D--A--B--C--E--H--G--F--C);  pair P = (95, 33);pair Q = (0, 8); dot(A);dot(B);dot(C);dot(D);dot(E);dot(F);dot(G);dot(H);dot(P);dot(Q); label("$P$", P, N);label("$Q$", Q, W);  draw(Q--(107,8));draw(P--(95,0)); pair O = (95,8); dot(O);label("$O$", O, NW); /*Diagram by Technodoggo*/ [/asy]

We could draw the circumcircle, but actually it does not matter for our solution; all that matters is that $OA=OH=r$, where $r$ is the circumradius.

By the Pythagorean Theorem, $OQ^2+QA^2=OA^2$. Also, $OP^2+PH^2=OH^2$. We know that $OQ=DE+HP$, and $HP=\dfrac{184}2=92$; $QA=\dfrac{16}2=8$; $OP=DQ+HE=8+17=25$; and finally, $PH=92$. Let $DE=x$. We now know that $OA^2=(x+92)^2+8^2$ and $OH^2=25^2+92^2$. Recall that $OA=OH$; thus, $OA^2=OH^2$. We solve for $x$:

The question asks for $CE$, which is $CD-x=107-3=\boxed{104}$.

~Technodoggo

## Solution 2

Suppose $DE=x$. Extend $AD$ and $GH$ until they meet at $P$. From the [Power of a Point Theorem](https://artofproblemsolving.com/wiki/index.php?title=Power_of_a_Point_Theorem "Power of a Point Theorem"), we have $(PH)(PG)=(PD)(PA)$. Substituting in these values, we get $(x)(x+184)=(17)(33)=561$. We can use guess and check to find that $x=3$, so $EC=\boxed{104}$. [asy] import graph; unitsize(0.1cm);  pair A = (0,0);pair B = (107,0);pair C = (107,16);pair D = (0,16);pair E = (3,16);pair F = (187,16);pair G = (187,33);pair H = (3,33);pair P = (0,33); label("$A$", A, SW);label("$B$", B, SE);label("$C$", C, N);label("$D$", D, W);label("$E$", E, S);label("$F$", F, SE);label("$G$", G, NE);label("$H$", H, N);label("$P$", P, NW); draw(E--D--A--B--C--E--H--G--F--C); draw(D--P--H, dashed);  /*graph originally by Technodoggo, revised by alexanderruan*/ [/asy]

~alexanderruan

~diagram by Technodoggo

rabbit47 - quadratic actually factors as (x+187)(x-3)=0, from which x=3

## Solution 3

We find that \[\angle GAB = 90-\angle DAG = 90 - (180 - \angle GHD) = \angle DHE.\]

Let $x = DE$ and $T = FG \cap AB$. By similar triangles $\triangle DHE \sim \triangle GAT$ we have $\frac{DE}{EH} = \frac{GT}{AT}$. Substituting lengths we have $\frac{x}{17} = \frac{16 + 17}{184 + x}.$ Solving, we find $x = 3$ and thus $CE = 107 - 3 = \boxed{104}.$ ~AtharvNaphade ~coolruler ~eevee9406

## Solution 4

One liner: $107-\sqrt{92^2+25^2-8^2}+92=\boxed{104}$

~Bluesoul

### Explanation

Let $OP$ intersect $DF$ at $T$ (using the same diagram as Solution 2).

The formula calculates the distance from $O$ to $H$ (or $G$), $\sqrt{92^2+25^2}$, then shifts it to $OD$ and the finds the distance from $O$ to $Q$, $\sqrt{92^2+25^2-8^2}$. $107$ minus that gives $CT$, and when added to $92$, half of $FE=TE$, gives $CT+TE=CE$

## Solution 5

Let $\angle{DHE} = \theta.$ This means that $DE = 17\tan{\theta}.$ Since quadrilateral $ADHG$ is cyclic, $\angle{DAG} = 180 - \angle{DHG} = 90 - \theta.$

Let $X = AG \cap DF.$ Then, $\Delta DXA \sim \Delta FXG,$ with side ratio $16:17.$ Also, since $\angle{DAG} = 90 - \theta, \angle{DXA} = \angle{FXG} = \theta.$ Using the similar triangles, we have $\tan{\theta} = \frac{16}{DX} = \frac{17}{FX}$ and $DX + FX = DE + EF = 17\tan{\theta} + 184.$

Since we want $CE = CD - DE = 107 - 17\tan{\theta},$ we only need to solve for $\tan{\theta}$ in this system of equations. Solving yields $\tan{\theta} = \frac{3}{17},$ so $CE = \boxed{104.}$

~PureSwag

## Solution 6

Using a ruler (also acting as a straight edge), draw the figure to scale with one unit = 1mm. With a compass, draw circles until you get one such that $A,D,H,G$ are on the edge of the drawn circle. From here, measuring with your ruler should give $CE = \boxed{104.}$

Note: 1 mm is probably the best unit to use here just for convenience (drawing all required parts of the figure fits into a normal-sized scrap paper 8.5 x 11); also all lines can be drawn with a standard 12-inch ruler

~kipper

## Solution 7(Ptolemy's Theorem)

Since ADHG is cyclic, AH*DG=AD*HG+DH*AG,let DE be x, we represent the equation in terms of x,and you get $x=3, 107-3= \boxed{104.}$

Ps: extremely time consuming, do not use on the test
