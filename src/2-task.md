# Задание №2

Найти решение задачи линейного программирования симплекс – методом (для "а, с" на max, для "в" на max и min)

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
