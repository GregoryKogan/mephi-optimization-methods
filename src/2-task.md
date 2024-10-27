# Задание №2

Найти решение задачи линейного программирования симплекс-методом (для "a, c" на $\max$, для "b" на $\max$ и $\min$).

## Пункт (a)

$$
\begin{aligned}
&F = 2x_1 + x_2 \rightarrow \max\\
&\begin{cases}
-x_1+x_2\leq2\\
4x_1 - x_2\leq8
\end{cases}
x_1 \geq 0, \quad x_2 \geq 0 \\
\end{aligned}
$$

$$
\begin{cases}
    F = 2x_1 + x_2 \rightarrow \max\\
    -x_1+x_2\leq2\\
    4x_1 - x_2\leq8\\
    x_1 \geq 0, \quad x_2 \geq 0
\end{cases}
\quad
\rightarrow
\quad
\begin{cases}
    F - 2x_1 - x_2 = 0\\
    -x_1+x_2 + x_3 = 2\\
    4x_1 - x_2 + x_4 = 8\\
    x_i \geq 0, \quad i \in \overline{1, 4}
\end{cases}
$$

$$
\begin{tabular}{|c|>{\columncolor[HTML]{98FB98}}c|c|c|c|c|c|}
    \hline
        Базис & $x_1$ & $x_2$ & $x_3$ & $x_4$ & $b_i$ & $\frac{b_i}{\text{р.с.}} \geq 0$ \\
    \hline
        $x_3$ & -1 & 1 & 1 & 0 & 2 & -2 \\ \hline
        \rowcolor[HTML]{E0FFFF}
        $x_4$ & \cellcolor[HTML]{BDFDCC} 4 & -1 & 0 & 1 & 8 & 2 \\ \hline
        $F$ & -2 & -1 & 0 & 0 & 0 & ~ \\ \hline
\end{tabular}
$$

В последней строке есть элементы меньше нуля. Занулим элементы выше и ниже стоящие от разрешающего элемента.

$$
\begin{tabular}{|c|c|>{\columncolor[HTML]{98FB98}}c|c|c|c|c|}
    \hline
        Базис & $x_1$ & $x_2$ & $x_3$ & $x_4$ & $b_i$ & $\frac{b_i}{\text{р.с.}} \geq 0$ \\
    \hline
        \rowcolor[HTML]{E0FFFF}
        $x_3$ & 0 & \cellcolor[HTML]{BDFDCC} $\frac{3}{4}$ & 1 & $\frac{1}{4}$ & 4 & $\frac{16}{3}$ \\ \hline
        $x_1$ & 4 & -1 & 0 & 1 & 8 & -8 \\ \hline
        $F$ & 0 & $-\frac{3}{2}$ & 0 & $\frac{1}{2}$ & 4 & ~ \\ \hline
\end{tabular}
$$

В последней строке есть элементы меньше нуля. Занулим элементы выше и ниже стоящие от разрешающего элемента.

$$
\begin{tabular}{|c|c|c|c|c|c|}
    \hline
        Базис & $x_1$ & $x_2$ & $x_3$ & $x_4$ & $b_i$ \\
    \hline
        $x_2$ & 0 & 3 & 4 & 1 & 16 \\ \hline
        $x_1$ & 4 & 0 & $\frac{4}{3}$ & $\frac{4}{3}$ & $\frac{40}{3}$ \\ \hline
        $2F$ & 0 & 0 & 4 & 2 & 2 \\ \hline
\end{tabular}
\quad
\rightarrow
\quad
\begin{tabular}{|c|c|c|c|c|c|c|}
    \hline
        Базис & $x_1$ & $x_2$ & $x_3$ & $x_4$ & $b_i$ & $\frac{b_i}{\text{р.с.}} \geq 0$ \\
    \hline
        $x_2$ & 0 & 1 & $\frac{4}{3}$ & $\frac{1}{3}$ & $\frac{16}{3}$ & $\frac{16}{3}$ \\ \hline
        $x_1$ & 1 & 0 & $\frac{1}{3}$ & $\frac{1}{3}$ & $\frac{10}{3}$ & $\frac{10}{3}$ \\ \hline
        $F$ & 0 & 0 & 2 & 1 & 12 & ~ \\ \hline
\end{tabular}
$$

В последней строке не осталось отрицательных элементов. Оптимальное решение найдено. Максимум функции достигается при $x_1 = \frac{10}{3}$ и $x_2 = \frac{16}{3}$ и равен 12.  
$F(x_1, x_2) = 2 \cdot \frac{10}{3} + \frac{16}{3} = 12 - \max$

## Пункт (b)

$$
\begin{aligned}
&F = 2x_1 + 7x_2 \rightarrow \max(\min)\\
&\begin{cases}
    2x_1+x_2\geq6\\
    3x_1-x_2\leq9
\end{cases}
x_1 \geq 0, \quad x_2 \geq 0 \\
\end{aligned}
$$

### Максимизация

$$
\begin{cases}
    F = 2x_1 + 7x_2 \rightarrow \max\\
    2x_1+x_2\geq6\\
    3x_1-x_2\leq9\\
    x_1 \geq 0, \quad x_2 \geq 0
\end{cases}
\quad
\rightarrow
\quad
\begin{cases}
    F - 2x_1 - 7x_2 = 0\\
    -2x_1-x_2 + x_3 = -6\\
    3x_1-x_2 + x_4 = 9\\
    x_i \geq 0, \quad i \in \overline{1, 4}
\end{cases}
$$

$$
\begin{tabular}{|c|c|c|c|c|c|}
    \hline
        Базис & $x_1$ & $x_2$ & $x_3$ & $x_4$ & $b_i$ \\
    \hline
        $x_3$ & -2 & -1 & 1 & 0 & -6 \\ \hline
        $x_4$ & 3 & -1 & 0 & 1 & 9 \\ \hline
        $F$ & -2 & -7 & 0 & 0 & 0 \\ \hline
\end{tabular}
$$

В последней строке есть элементы меньше нуля. Минимальный из них -7, но все элементы этого столбца отрицательные. Значит, функция не ограничена сверху. Решения для максимума нет.

### Минимизация

Приведем эту задачу к задаче максимизации, умножив целевую функцию на -1.

$$
G = -2x_1 - 7x_2 \rightarrow \max
$$

$$
\begin{cases}
    G = -2x_1 - 7x_2 \rightarrow \max\\
    2x_1+x_2\geq6\\
    3x_1-x_2\leq9\\
    x_1 \geq 0, \quad x_2 \geq 0
\end{cases}
\quad
\rightarrow
\quad
\begin{cases}
    G + 2x_1 + 7x_2 = 0\\
    -2x_1-x_2 + x_3 = -6\\
    3x_1-x_2 + x_4 = 9\\
    x_i \geq 0, \quad i \in \overline{1, 4}
\end{cases}
$$

$$
\begin{tabular}{|c|>{\columncolor[HTML]{98FB98}}c|c|c|c|c|c|}
    \hline
        Базис & $x_1$ & $x_2$ & $x_3$ & $x_4$ & $b_i$ & $\frac{b_i}{\text{р.с.}} \geq 0$ \\
    \hline
        \rowcolor[HTML]{E0FFFF}
        $x_3$ & \cellcolor[HTML]{BDFDCC} -2 & -1 & 1 & 0 & -6 & 3 \\ \hline
        $x_4$ & 3 & -1 & 0 & 1 & 9 & 3 \\ \hline
        $G$ & 2 & 7 & 0 & 0 & 0 & ~ \\ \hline
\end{tabular}
$$

В симплекс-методе начинаем с точки $(0, 0)$, но она не входит в область определения. Поэтому сделаем первый шаг, уменьшающий значение целевой функции, но ведущий в область определения.

$$
\begin{tabular}{|c|c|c|c|c|c|}
    \hline
        Базис & $x_1$ & $x_2$ & $x_3$ & $x_4$ & $b_i$ \\
    \hline
        $x_1$ & -2 & -1 & 1 & 0 & -6 \\ \hline
        $x_4$ & 0 & $-\frac{5}{2}$ & $\frac{3}{2}$ & 1 & 0 \\ \hline
        $G$ & 0 & 6 & 1 & 0 & -6 \\ \hline
\end{tabular}
\quad
\rightarrow
\quad
\begin{tabular}{|c|c|c|c|c|c|}
    \hline
        Базис & $x_1$ & $x_2$ & $x_3$ & $x_4$ & $b_i$ \\
    \hline
        $x_1$ & 1 & $\frac{1}{2}$ & $-\frac{1}{2}$ & 0 & 3 \\ \hline
        $x_4$ & 0 & $-\frac{5}{2}$ & $\frac{3}{2}$ & 1 & 0 \\ \hline
        $G$ & 0 & 6 & 1 & 0 & -6 \\ \hline
\end{tabular}
$$

Мы сместились в точку $(3, 0)$. Она входит в область определения.  
В последней строке нет отрицательных элементов. Оптимальное решение найдено.  
Максимум функции $G$ достигается при $x_1 = 3$ и $x_2 = 0$ и равен -6.  
Значит, минимум функции $F$ достигается при $x_1 = 3$ и $x_2 = 0$ и равен $F_{\min} = -G_{\max} = 6$.

## Пункт (c)

$$
\begin{aligned}
&F = -2x_1+5x_2 \rightarrow \max\\
&\begin{cases}
    2x_1+x_2 \geq 4 \\
    x_1 - 4x_2 \geq 8
\end{cases}
x_1 \geq 0, \quad x_2 \geq 0 \\
\end{aligned}
$$

$$
\begin{cases}
    F = -2x_1 + 5x_2 \rightarrow \max\\
    2x_1+x_2\geq4\\
    x_1 - 4x_2\geq8\\
    x_1 \geq 0, \quad x_2 \geq 0
\end{cases}
\quad
\rightarrow
\quad
\begin{cases}
    F + 2x_1 - 5x_2 = 0\\
    -2x_1-x_2 + x_3 = -4\\
    -x_1 + 4x_2 + x_4 = -8\\
    x_i \geq 0, \quad i \in \overline{1, 4}
\end{cases}
$$

$$
\begin{tabular}{|c|>{\columncolor[HTML]{98FB98}}c|c|c|c|c|c|}
    \hline
        Базис & $x_1$ & $x_2$ & $x_3$ & $x_4$ & $b_i$ & $\frac{b_i}{\text{р.с.}} \geq 0$ \\
    \hline
        $x_3$ & -2 & -1 & 1 & 0 & -4 & 2 \\ \hline
        \rowcolor[HTML]{E0FFFF}
        $x_4$ & \cellcolor[HTML]{BDFDCC} -1 & 4 & 0 & 1 & -8 & 8 \\ \hline
        $F$ & 2 & -5 & 0 & 0 & 0 & ~ \\ \hline
\end{tabular}
$$

В последней строке есть элементы меньше нуля. Занулим элементы выше и ниже стоящие от разрешающего элемента.

$$
\begin{tabular}{|c|c|c|c|c|c|}
    \hline
        Базис & $x_1$ & $x_2$ & $x_3$ & $x_4$ & $b_i$ \\
    \hline
        $x_3$ & 0 & -9 & 1 & -2 & 12 \\ \hline
        $x_1$ & 1 & -4 & 0 & -1 & 8 \\ \hline
        $F$ & 0 & 3 & 0 & 2 & -16 \\ \hline
\end{tabular}
$$

Оптимальное решение найдено.  
Максимум функции $F$ достигается при $x_1 = 8$ и $x_2 = 0$ и равен -16.  
$F(8, 0) = -2 \cdot 8 + 5 \cdot 0 = -16 - \max$
