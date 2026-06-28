## Problem

Find the largest possible real part of\[(75+117i)z+\frac{96+144i}{z}\]where $z$ is a complex number with $|z|=4$. Here $i = \sqrt{-1}$.

## Solution 1

Let $z=4e^{i\theta}$. Then the expression becomes \[(300+468i)e^{i\theta}+(24+36i)e^{-i\theta}\] The real part of this comes out to be $(300\cos \theta - 468 \sin \theta)+(24\cos \theta + 36 \sin \theta) = (324\cos \theta - 432 \sin \theta)$. Using Cauchy-Schwarz to maximize this, \[(324\cos \theta - 432 \sin \theta)^2 \leq (\cos ^2 \theta+\sin ^2 \theta)(324^2+432^2) = (1)(324^2+432^2) = 540^2\] This value is attainable. Thus, the maximum is $\boxed{540}$.

## Solution 2a (Cauchy-Schwarz and vector algebra)

Simplify rectangular form as in Solution 1 until we get $\text{Re}(w)=81a-108b = 27(3a-4b)$.

By Cauchy-Schwarz, to maximize $\text{Re}(w)$, the vector $z=[a,b]$ ( $|z| =4$) is $\frac{4}{|[3,-4]|}[3,-4]$.

We don't need to bash the arithmetic next, because the unit vector $u$ that maximizes $v \cdot u$ is $u=v/|v|$, so $v \cdot u= v\cdot v = |v|^2/|v| = |v|$, which here is just $\sqrt{3^2+(-4)^2} =5$.

Combining what remains, we get answer $= 27 |z| |v|  = 27(4)(5)=\boxed{540}$.

~oinava

## Solution 2b (Simple Analytic Geometry)

Simplify rectangular form as in Solution 1 until we get $\text{Re}(w)=81x-108y = 27(3x-4y)$.

We also know $|z|=4$ or $x^2+y^2=16$.

By AM-GM or Cauchy-Schwarz, b = 4a/3, so

You can also prove this like so: We want to find the line $81x-108y=k$ tangent to circle $x^2+y^2=16$, which is perpendicular to the line connecting tangent point to circle's center $(0,0)$.

Using the formula for (perpendicular) distance from a point to a line: $\frac{|ax+by+c|}{\sqrt{a^2+b^2}}=r$ we can substitute and get $\frac{|81(0)-108(0)-k|}{\sqrt{81^2+108^2}}=4$\begin{align*} \frac{k}{27\sqrt{3^2+4^2}}&=4 \\\frac{k}{135}&=4 \\k&=\boxed{540} \end{align*}

~BH2019MV0

## Solution 2c (Dot product)

Let $z = a + bi.$ Simplify until we get to maximizing $81a - 108b$ given $a^2 +b^2 = 16.$ We can write $81a - 108b$ as the [Dot Product](https://artofproblemsolving.com/wiki/index.php/Vector?srsltid=AfmBOoqdT29SM62x_yUNcVA7yUtSecmXlpmyOtury4Rl4Y_Bo-6fLXh4) of two vectors: \[81a - 108b = \langle 81 , -108 \rangle \cdot \langle a, b \rangle.\] From this, we have the line $b = -\frac{108}{81}a =  -\frac{4}{3}a$ and the circle $a^2 + b^2 = 16.$ We need to find their intersection $(a,b)$ such that $a$ and $b$ are maximized. The line intersects the circle at two points, but to maximize $81a - 108b$ we want $b$ to be negative and $a$ to be positive. So the point that works has coordinates $a = 2.4$ and $b = -3.2$. We get $81\cdot 2.4 + 108 \cdot 3.2 = \boxed{540}.$

~[grogg007](https://artofproblemsolving.com/wiki/index.php/User:grogg007)

[](https://artofproblemsolving.com/wiki/index.php?title=File:2024-AIMEI-P7-S12.png)

## Solution 3

Follow Solution 1 to get $81a-108b$. We can let $a=4\cos\theta$ and $b=4\sin\theta$ as $|z|=4$, and thus we have $324\cos\theta-432\sin\theta$. Furthermore, we can ignore the negative sign in front of the second term as we are dealing with sine and cosine, so we finally wish to maximize $324\cos\theta+432\sin\theta$ for obviously positive $\cos\theta$ and $\sin\theta$.

Using the previous fact, we can use the [Cauchy-Schwarz Inequality](https://artofproblemsolving.com/wiki/index.php?title=Cauchy-Schwarz_Inequality "Cauchy-Schwarz Inequality") to calculate the maximum. By the inequality, we have:

$(324^2+432^2)(\cos^2\theta+\sin^2\theta)\ge(324\cos\theta+432\sin\theta)^2$

$540^2\cdot1\ge(324\cos\theta+432\sin\theta)^2$

$\boxed{540}\ge324\cos\theta+432\sin\theta$

~eevee9406

## Solution 4 (Simple Quadratic Discriminant)

Similar to the solutions above, we find that $Re((75+117i)z+\frac{96+144i}{z})=81a-108b=27(3a-4b)$, where $z=a+bi$. To maximize this expression, we must maximize $3a-4b$. Let this value be $x$. Solving for $a$ yields $a=\frac{x+4b}{3}$. From the given information we also know that $a^2+b^2=16$. Substituting $a$ in terms of $x$ and $b$ gives us $\frac{x^2+8bx+16b^2}{9}+b^2=16$. Combining fractions, multiplying, and rearranging, gives $25b^2+8xb+(x^2-144)=0$. This is useful because we want the maximum value of $x$ such that this quadratic has real roots which is easy to find using the discriminant. For the roots to be real, $(8x)^2-4(25)(x^2-144) \ge 0$. Now all that is left to do is to solve this inequality. Simplifying this expression, we get $-36x^2+14400 \ge 0$ which means $x^2 \le 400$ and $x \le 20$. Therefore the maximum value of $x$ is $20$ and $27 \cdot 20 = \boxed{540}$

~vsinghminhas

## Solution 5 ("Completing the Triangle")

First, recognize the relationship between the reciprocal of a complex number $z$ with its conjugate $\overline{z}$, namely:

\[\frac{1}{z} \cdot \frac{\overline{z}}{\overline{z}} = \frac{\overline{z}}{|z|^2} = \frac{\overline{z}}{16}\]

Then, let $z = 4(\cos\theta + i\sin\theta)$ and $\overline{z} = 4(\cos\theta - i\sin\theta)$.

\begin{align*} Re \left ((75+117i)z+\frac{96+144i}{z} \right) &= Re\left ( (75+117i)z + (6+9i)\overline{z}    \right ) \\                                                &= 4 \cdot Re\left ( (75+117i)(\cos\theta + i\sin\theta) + (6+9i)(\cos\theta - i\sin\theta)    \right ) \\                                                &= 4 \cdot (75\cos\theta - 117\sin\theta + 6\cos\theta + 9\sin\theta) \\                                                &= 4 \cdot (81\cos\theta - 108\sin\theta) \\                                                &= 4\cdot 27 \cdot (3\cos\theta - 4\sin\theta) \end{align*}

Now, recognizing the 3 and 4 coefficients hinting at a 3-4-5 right triangle, we "complete the triangle" by rewriting our desired answer in terms of an angle of that triangle $\phi$ where $\cos\phi = \frac{3}{5}$ and $\sin\phi = \frac{4}{5}$

\begin{align*} 4\cdot 27 \cdot(3\cos\theta - 4\sin\theta) &= 4\cdot 27 \cdot 5 \cdot (\frac{3}{5}\cos\theta - \frac{4}{5}\sin\theta) \\                                                &= 540 \cdot (\cos\phi\cos\theta - \sin\phi\sin\theta) \\                                                &= 540 \cos(\theta + \phi) \end{align*}

Since the simple trig ratio is bounded above by 1, our answer is $\boxed{540}$

~ Cocoa @ [https://www.corgillogical.com/](https://www.corgillogical.com/) (yes i am a corgi that does math)

## Solution 6 (Cauchy-Schwarz Inequality ) (Fastest)

Follow as solution 1 would to obtain $81a + 108\sqrt{16-a^2}.$

By the Cauchy-Schwarz Inequality, we have

\[(a^2 + (\sqrt{16-a^2})^2)(81^2 + 108^2) \geq (81a + 108\sqrt{16-a^2})^2,\]

so

\[4^2 \cdot 9^2 \cdot 15^2 \geq (81a + 108\sqrt{16-a^2})^2\]

and we obtain that $81a + 108\sqrt{16-a^2} \leq 4 \cdot 9 \cdot 15 = \boxed{540}.$

- [spectraldragon8](https://artofproblemsolving.com/wiki/index.php/User:Spectraldragon8)

## Solution 7 (Geometry)

Follow solution 2 to get that we want to find the line $81a-108b=k$ tangent to circle $a^2+b^2=16$. The line turns into $a=\frac{k}{81}+\frac{4b}{3}$ Connect the center of the circle to the tangency point and the y-intercept of the line. Let the tangency point be $A$, the y-intercept be $C$, and the center be $B$. Drop the perpendicular from $A$ to $BC$ and call it $D$. Let $AD=3x$, $DC=4x$. Then, $BD=\sqrt{AB^2-AD^2}=\sqrt{16-9x^2}$. By similar triangles, get that $\frac{BD}{AD}=\frac{AD}{DC}$, so $\frac{\sqrt{16-9x^2}}{3x}=\frac{3x}{4x}$. Solve this to get that $x=\frac{16}{15}$, so $BC=\frac{20}{3}$ and $\frac{k}{81}=\frac{20}{3}$, so $k=\boxed{540}$ ~ryanbear

## Solution 8 (Euler's Formula and Trig Optimization)

Because $|z|=4$, we can let $z=4e^{i\theta}$. Then, substituting $i=e^{\frac{i\pi}{2}}$, we get that the complex number is

We know that the $\text{Re}(e^{i\alpha})=\cos(\alpha)$ from Euler's formula, so applying this and then applying trig identities yields

We can see that the right-hand side looks an awful lot like the sum of angles formula for cosine, but 3 and 4 don't satisfy the pythagorean identity. To make them do so, we can divide everything by $\sqrt{3^2+4^2}=5$ and set $\cos{(\alpha)}::=\frac{3}{5}$ and $\sin{(\alpha)}::=\frac{4}{5}$. Now we have that \[\dfrac{1}{540}\text{Re}(w)=\cos{(\theta+\alpha)}\] Obviously the maximum value of the right hand side is 1, so the maximum value of the real part is $\boxed{540}$.

~Mooshiros

## Solution 9 (Calc semi-bash)

Let $c$ denote value of the above expression such that $\mathsf{Re} (c)$ is maximized. We write $z=4e^{i\theta}$ and multiply the second term in the expression by $\overline{z} = 4e^{-i\theta},$ turning the expression into \[4e^{i\theta}(75+117i) + \frac{(96 + 144i)\cdot 4e^{-i\theta}}{4e^{i\theta}\cdot 4e^{-i\theta}} = 300e^{i\theta} + 468ie^{i\theta} + (24+ 36i)e^{-i\theta}.\] Now, we write $e^{i\theta} = \cos\theta + i\sin\theta$. Since $\cos$ is even and $\sin$ is odd, \begin{align*} &300(\cos\theta + i\sin\theta) +468i + (24+36i)(\cos\theta -i\sin\theta) \\ \iff & \mathsf{Re}(c) = 324\cos\theta -468\sin\theta \end{align*} We want to maximize this expression, so we take its derivative and set it equal to $0$ (and quickly check the second derivative for inflection points): \begin{align*}     &\mathsf{Re}(c) = 108\left(3\cos\theta - 4\sin\theta\right)\\     \frac{d}{d\theta} &\mathsf{Re}(c) = -324\sin\theta -468\cos\theta = 0, \end{align*} so $\tan\theta = -\dfrac{468}{324} = -\dfrac{4}{3},$ which is reminiscent of a $3-4-5$ right triangle in the fourth quadrant (side lengths of $3, -4, 5$). Since $\tan\theta = -\frac{4}{3},$ we quickly see that $\sin\theta = -\dfrac{4}{5}$ and $\cos\theta = \dfrac{3}{5}.$ Therefore, \begin{align*}  \mathsf{Re}(c) &= 108\left(3\cos\theta - 4\sin\theta \right) =  108\left(\frac{9}{5} + \frac{16}{5} \right)  = 108\cdot 5 = \boxed{\textbf{(540)}} \end{align*}

-Benedict T (countmath1)

## Solution 10 (Lagrange multipliers)

With $z = a + bi$ such that $a^2 + b^2 = 16,$ we have \begin{align*} (75 +117i)(a + bi) + \frac{48}{a + bi}  (2 + 3i) &= 75a + 75bi + 117ai - 117b + \frac{48}{a + bi}(2 + 3i) \\ &= 75a - 117b + (117a + 75b)i + 48 (2 + 3i) \cdot \frac{a - bi}{16} \\ &= 75a - 117b + (117a + 75b)i + 3 (2 + 3i)(a - bi) \end{align*} where we use $z^{-1} = \frac{\bar z}{|z|^2}.$ With $3 (2 + 3i)(a - bi) = 3 [2a - 2bi + 3ai + 3b] = 6a +9b +9ai-6bi,$ the expression becomes $81a-108b+ (126a + 69b)i$ and we would like to maximize $81a - 108b = 9(9a - 12b) = 27(3a - 4b)$ with $a^2 + b^2 = 16.$ With $f(a, b) = 3a - 4b$ and $g(a, b) = a^2 + b^2 = 16,$ we have \begin{align*} 3 = 2\lambda a, \quad -4 = 2\lambda b \implies -\frac{3}{4} = \frac ab \implies -3b = 4a \implies b = -\frac 43 a\end{align*} so \[a^2 + \frac{16}{9}a^2 = \frac{25}{9}a^2 = 16 \implies \frac{5}{3}a = 4 \implies a = \frac {12}5, b = -\frac{16}{5}\] and we have $3a - 4b = \frac{36}{5} + \frac{64}{5} = 20,$ so the maximum is $27 \cdot 20 = \boxed{540}.$ -centslordm

## Solution 11 (basically Lagrange but easier-ish)

Proceeding as with Solution 10, we aim to maximize $27(3a-4b)$ under the constraint $a^2+b^2-16=0$. It is a well-known result of Lagrange multipliers that a linear function is maximized under a circle when the values of the variables are proportional to their coefficients; that is, in our case, $a=3x$ and $b=-4x$. (Technically $a=27\cdot3x$ and $b=27(-4)x$, but it's easier to use $a=3x$ and $b=-4x$.)

Then, $(3x)^2+(-4x)^2=25x^2=16$, so $x=\dfrac45$ and we have $a=\dfrac{12}5$ and $b=-\dfrac{16}5$. This yields

\[27\left(3\left(\dfrac{12}5\right)-4\left(-\dfrac{16}5\right)\right)=27\left(\dfrac{36}5+\dfrac{64}5\right)=27\cdot\dfrac{100}5=\boxed{540}~.\]

QED. $\Box$

~Technodoggo

## Solution 12 (Wave function)

Note that we can scale down the expression by a factor of $3$, namely, we compute the maximum possible real part of ${25+39i}z+{32+48i\over z}$ for $|z|=4$ and multiply this result by 3. Write $z=4(\cos t+i\sin t)$ we have

The real part of $(100+156i)(\cos t+i\sin t)+(8+12i)(\cos t-i\sin t)$ is then \[108\cos t-144\sin t=36(3\cos t-4\sin t)\]

The function $3\cos t-4\sin t$ oscillates with amplitude $5$, so the maximum value of the scaled-down expression is $36\cdot 5=180$. Hence, our requested answer is $180\cdot 3=\boxed{540}$.

## Solution 13 (Conjugate)(simplest)

Suppose $z = 4e^{i\theta}$

*   $\overline{z_1z_2} = \overline{z_1} \cdot \overline{z_2}$,

*   The real parts of conjugates are equal,

*   $\mathrm{Re}(z) \leq |z|$.

The idea comes from the geometric meaning of this problem. The only difficulty is that the rotation directions are opposite. To make the rotations same, using conjugate is a good idea without changing the real part. Finally we can get a rotating parallelogram as shown in the following graph. Just find the length of the diagonal.

[asy] unitsize(25); draw((-1, 0) -- (5, 0), Arrows(TeXHead)); draw((0, -3) -- (0, 5), Arrows(TeXHead)); draw((0, 0) -- (3, 3), EndArrow); draw((0, 0) -- (1, 2), EndArrow); draw((0, 0) -- (1, -2), dashed, EndArrow); draw((3, 3) -- (4, 1) -- (1, -2), dashed); draw((0, 0) -- (4, 1), red, EndArrow); draw(arc((0, 0), (3, 3), rotate(-20) * (3, 3), CW), blue, EndArrow(TeXHead)); draw(arc((0, 0), (1, 2), rotate(20) * (1, 2), CCW), blue, EndArrow(TeXHead)); draw(arc((0, 0), (1, -2), rotate(-20) * (1, -2), CW), blue, EndArrow(TeXHead)); draw(arc((0, 0), (4, 1), rotate(-20) * (4, 1), CW), blue, EndArrow(TeXHead)); label(scale(0.8) * "Diagram not on scale", (7, 3)); label(scale(0.9) * "$z_1$", (3, 3), N); label(scale(0.9) * "$z_2$", (1, 2), N); label(scale(0.9) * "$\overline{z_2}$", (1, -2), S); label(scale(0.9) * "$z_1 + \overline{z_2}$", (4, 1), E); [/asy]

~[reda_mandymath](https://artofproblemsolving.com/wiki/index.php/User:Reda_mandymath)

## Solution 14 (Dot Product Maximality, The Hadamard Vector)

Let $z=4e^{i \theta}$. We have

\[(75+117i)(4e^{i \theta}) + (96+144i)(\frac{1}{4}e^{-i\theta})\]\[(300+468i)(\cos(\theta) + i\sin(\theta)) + (24+36i)(\cos(\theta) - i\sin(\theta))\]\[(300\cos(\theta)-468\sin(\theta))+i(468\cos(\theta)+300\sin(\theta))+(24\cos(\theta)+36\sin(\theta)) +i(36\cos(\theta)-24\sin(\theta))\]\[(324\cos(\theta)-432\sin(\theta))+i(504\cos(\theta)+276\sin(\theta))\]

From here, we need to maximize

\[324\cos(\theta) - 432\sin(\theta)\].

Recall for two vectors $\textbf{a} = (a_1,a_2)$ and $\textbf{b} = (b_1,b_2)$, the **dot product property** states $\textbf{ab} = (a_1, a_2) \cdot (b_1,b_2) = a_1b_1 + a_2b_2$.

Rewriting $324\cos(\theta) - 432\sin(\theta)$ as a dot product, we have $(324, -432) \cdot (\cos(\theta), \sin(\theta))$, so one vector yields $\textbf{u} = (324, -432)$ and $\textbf{v} = (\cos(\theta), \sin(\theta))$. To find the maximum $| \textbf{uv} |$, we require the maximalization of the product to form a vector of maximal magnitude. Consider the Hadamard product, the resulting vector formed via the dot product. Then, this vector is maximal when both vectors face the same direction. The largest possible vector direction for $\textbf{v}$ always yields a magnitude 1. For the maximality of $\textbf{u}$, consider $|\textbf{u}|  = \sqrt{324^2 + 432^2}$. Divide both by 108 and multiply at the end, obtaining $108 \cdot \sqrt{3^2 + 4^2} = 108 \cdot 5 = 540$. So, the max value of $| \textbf{uv} |$ is $540 \cdot 1 = \boxed{540}$.

~Pinotation
