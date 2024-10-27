# Задание №3

Для "a" составить и решить геометрически и симплекс-методом задачу двойственную данной.

## Пункт (a)

$$
\begin{aligned}
&F = 2x_1 + x_2 \rightarrow \max\\
&\begin{cases}
-x_1+x_2\leq2\\
4x_1 - x_2\leq8
\end{cases}
x_1 \geq 0, \quad x_2 \geq 0 \\
&F(\frac{10}{3}, \frac{16}{3})=12 - \max\\
\end{aligned}
$$

Составим двойственную задачу:

$$
\begin{cases}
    F' = 2y_1 + 8y_2 \rightarrow \min\\
    -y_1 + 4y_2 \geq 2\\
    y_1 - y_2 \geq 1\\
    y_i \geq 0, \quad i \in \overline{1, 2}
\end{cases}
$$

#### Графическое решение

$$
\begin{aligned}
&\nabla F' = (2; 8)\\
&\begin{cases}
    -y_1 + 4y_2 = 2\\
    y_1 - y_2 = 1
\end{cases}
\Leftrightarrow
\begin{cases}
    y_1 = 2\\
    y_2 = 1
\end{cases}\\
&F'(y_1, y_2) = 2\cdot2+8\cdot1=12 - \min\\
\end{aligned}
$$

_График построен с помощью [www.geogebra.org](www.geogebra.org)_

![](tmp/images/3-a.jpg){ width=50% }

#### Симплекс-метод

$$
\begin{cases}
    F' = 2y_1 + 8y_2 \rightarrow \min\\
    -y_1 + 4y_2 \geq 2\\
    y_1 - y_2 \geq 1\\
    y_1 \geq 0, \quad y_2 \geq 0
\end{cases}
\quad
\rightarrow
\quad
\begin{cases}
    F' - 2y_1 - 8y_2 = 0\\
    y_1 - 4y_2 + y_3 = -2\\
    -y_1 + y_2 + y_4 = -1\\
    y_i \geq 0, \quad i \in \overline{1, 4}
\end{cases}
$$

$$
\begin{tabular}{|c|c|>{\columncolor[HTML]{98FB98}}c|c|c|c|c|}
    \hline
        Базис & $y_1$ & $y_2$ & $y_3$ & $y_4$ & $b_i$ & $\frac{b_i}{\text{р.с.}} \geq 0$ \\
    \hline
        \rowcolor[HTML]{E0FFFF}
        $y_3$ & 1 & \cellcolor[HTML]{BDFDCC} -4 & 1 & 0 & -2 & $\frac{1}{2}$ \\ \hline
        $y_4$ & -1 & 1 & 0 & 1 & -1 & -1 \\ \hline
        $F'$ & -2 & -8 & 0 & 0 & 0 & 0 \\ \hline
\end{tabular}
$$

В последней строке есть элементы больше нуля. Занулим элементы выше и ниже стоящие от разрешающего элемента.

$$
\begin{tabular}{|c|>{\columncolor[HTML]{98FB98}}c|c|c|c|c|c|}
    \hline
        Базис & $y_1$ & $y_2$ & $y_3$ & $y_4$ & $b_i$ & $\frac{b_i}{\text{р.с.}} \geq 0$ \\
    \hline
        $y_2$ & 1 & -4 & 1 & 0 & -2 & -2 \\ \hline
        \rowcolor[HTML]{E0FFFF}
        $y_4$ & \cellcolor[HTML]{BDFDCC} $-\frac{3}{4}$ & 0 & $\frac{1}{4}$ & 1 & $-\frac{3}{2}$ & 2 \\ \hline
        $F'$ & -4 & 0 & -2 & 0 & 4 & ~ \\ \hline
\end{tabular}
$$

В последней строке есть элементы больше нуля. Занулим элементы выше и ниже стоящие от разрешающего элемента.

$$
\begin{tabular}{|c|c|c|c|c|c|}
    \hline
        Базис & $y_1$ & $y_2$ & $y_3$ & $y_4$ & $b_i$ \\
    \hline
        $y_2$ & 0 & 1 & $-\frac{1}{3}$ & $-\frac{1}{3}$ & 1 \\ \hline
        $y_1$ & 1 & 0 & $-\frac{1}{3}$ & $-\frac{4}{3}$ & 2 \\ \hline
        $F'$ & 0 & 0 & $-\frac{10}{3}$ & $-\frac{16}{3}$ & 12 \\ \hline
\end{tabular}
$$

В последней строке нет элементов больше нуля. Оптимальное решение найдено.  
$F'(2, 1)=12 - \min$

#### Симплекс-метод через 3-ю теорему двойственности

$y^{*} = \vec{c} \cdot A^{-1}_B$, где $\vec{c}$ - коэффициенты функции при базисных переменных, $A_B$ - матрица, составленная из векторов, вошедших в оптимальный базис.  
Последняя таблица из симплекс-метода:

$$
\begin{tabular}{|c|c|c|c|c|c|c|}
    \hline
        Базис & $x_1$ & $x_2$ & $x_3$ & $x_4$ & $b_i$ & $\frac{b_i}{\text{р.с.}} \geq 0$ \\
    \hline
        $x_2$ & 0 & 1 & $\frac{4}{3}$ & $\frac{1}{3}$ & $\frac{16}{3}$ & $\frac{16}{3}$ \\ \hline
        $x_1$ & 1 & 0 & $\frac{1}{3}$ & $\frac{1}{3}$ & $\frac{10}{3}$ & $\frac{10}{3}$ \\ \hline
        $F$ & 0 & 0 & 2 & 1 & 12 & ~ \\ \hline
\end{tabular}
$$

Базисные переменные: $x_2$ и $x_1$.  
Коэффициенты функции перед базисными переменными: $c_1 = 8$ и $c_2 = 2$.  
Первая таблица из симплекс-метода:

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

Берём из таблицы векторы, вошедшие в базис: $A_B = \begin{pmatrix} \frac{4}{3} & \frac{1}{3} \\ \frac{1}{3} & \frac{1}{3} \end{pmatrix}$.  
Находим обратную матрицу: $A^{-1}_B =  \begin{pmatrix} \frac{4}{3} & \frac{1}{3} \\ \frac{1}{3} & \frac{1}{3} \end{pmatrix}^{-1} = \begin{pmatrix} 1 & -1 \\ -1 & 4 \end{pmatrix}$.  
По теореме находим $y^{*}$:

$$
y^{*} = \begin{pmatrix}8 & 2\end{pmatrix} \cdot \begin{pmatrix} 1 & -1 \\ -1 & 4 \end{pmatrix} = \begin{pmatrix} 6 & 0 \end{pmatrix}
$$

$F'(6, 0)=2\cdot6+8\cdot0=12 - \min$
