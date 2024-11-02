# Задание №1

_Вариант №57_

Найти решение задачи линейного программирования геометрически для "а, в, с" на max и min.  
_Графики построены с помощью [www.geogebra.org](www.geogebra.org)_

## Пункт (a)

$$
\begin{aligned}
&F = 2x_1 + x_2 \rightarrow \max(\min)\\
&\begin{cases}
-x_1+x_2\leq2\\
4x_1 - x_2\leq8
\end{cases}
x_1 \geq 0, \quad x_2 \geq 0 \\
&\nabla F = (2; 1) \\
&\begin{cases}
    -x_1+x_2 = 2\\
    4x_1 - x_2 = 8
\end{cases}
\Leftrightarrow
\begin{cases}
    x_1=\frac{10}{3}\\
    x_2=\frac{16}{3}
\end{cases}\\
&F(x_1, x_2)=2\cdot\frac{10}{3}+\frac{16}{3}=12 - \max\\
&F(0, 0)=2\cdot0+0=0 - \min
\end{aligned}
$$

![](tmp/images/1-a.jpg){ width=50% }

## Пункт (b)

$$
\begin{aligned}
&F = 2x_1 + 7x_2 \rightarrow \max(\min)\\
&\begin{cases}
2x_1+x_2\geq6\\
3x_1-x_2\leq9
\end{cases}
x_1\geq0,\quad x_2\geq0\\
&\nabla F = (2; 7)\\
&\begin{cases}
    2x_1+x_2=6\\
    3x_1-x_2=9
\end{cases}
\Leftrightarrow
\begin{cases}
    x_1=3\\
    x_2=0
\end{cases}\\
&F(x_1, x_2)=2\cdot3+7\cdot0=6 - \max\\
&F \text{ не ограничено сверху} \Rightarrow \text{нет решения для } \max\\
&F(x_1, x_2) = 2\cdot3+7\cdot0=6-\min
\end{aligned}
$$

![](tmp/images/1-b.jpg){ width=50% }

## Пункт (c)

$$
\begin{aligned}
&F = -2x_1+5x_2 \rightarrow \max(\min)\\
&\begin{cases}
2x_1+x_2 \geq 4 \\
x_1 - 4x_2 \geq 8
\end{cases}
x_1 \geq 0, \quad x_2 \geq 0 \\
&\nabla F = (-2; 5) \\
&\begin{cases}
    2x_1+x_2=4\\
    x_1-4x_2=8
\end{cases}
\Leftrightarrow
\begin{cases}
    x_1 &= \frac{8}{3} \\
    x_2 &= -\frac{4}{3}
\end{cases}\\
&x_2 < 0 \Rightarrow \text{другая точка}\\
&\text{По графику видно, что максимум в точке пересечения}\\
&x_1 - 4x_2 = 8 \text{ и оси абсцисс} \Rightarrow (x_3, x_4) = (8, 0)\\
&F(x_3, x_4)=-2\cdot8 + 5\cdot0=-16 - \max \\
&F \text{ не ограничено снизу} \Rightarrow \text{нет решения для } \min
\end{aligned}
$$

![](tmp/images/1-c.jpg){ width=50% }
