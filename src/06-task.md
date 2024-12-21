# Задание 6 - метод отсечения Гомори

## Условие

Задачу из первого задания пункта "a" на $\max$ решить методом Гомори.

## Постановка задачи

$$
\begin{aligned}
&F = 2x_1 + x_2 \rightarrow \max\\
&\begin{cases}
-x_1+x_2\leq2\\
4x_1 - x_2\leq8
\end{cases}
x_1 \geq 0, \quad x_2 \geq 0
\end{aligned}
$$

## Графическое[^3] решение

![](tmp/images/1-a.jpg){ width=50% }

$$
\begin{aligned}
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
&F(x_1, x_2)=2\cdot\frac{10}{3}+\frac{16}{3}=12 - \max
\end{aligned}
$$

## Симплекс-метод

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

## Метод отсечения Гомори

### Графическое[^3] решение

![](tmp/images/6.jpg){ width=50% }

[^3]: _График построен с помощью [www.geogebra.org](www.geogebra.org)_

Решение:

$$
\begin{cases}
x_1 = \frac{10}{3}\\
x_2 = \frac{16}{3}
\end{cases}
\quad
\Rightarrow
\quad
F(x_1, x_2) = F\left(\frac{10}{3}, \frac{16}{3}\right) = 2 \cdot \frac{10}{3} + \frac{16}{3} = 12
$$

Целочисленное решение:

$$
\begin{cases}
x_1 = 3\\
x_2 = 5
\end{cases}
\quad
\Rightarrow
\quad
F(x_1, x_2) = F(3, 5) = 2 \cdot 3 + 5 = 11
$$

#### Вывод

Максимум функции $F(x_1, x_2) = 2x_1 + x_2$ равен 12 и достигается при $x_1 = \frac{10}{3}$ и $x_2 = \frac{16}{3}$, а с учётом целочисленных ограничений достигается в точке $(3, 5)$, где $F(3, 5) = 11$.

### Симплекс-метод

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

Конечная симплекс-таблица:

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

Найдено оптимальное нецелочисленное решение: $x_1 = \frac{10}{3}$ и $x_2 = \frac{16}{3}$, где $F(x_1, x_2) = 12$.  
В полученном оптимальном плане присутствуют дробные числа.  
Среди свободных переменных находим ту, у которой дробная часть максимальна:

$$
\begin{aligned}
&\frac{10}{3} = 3 + \frac{1}{3}\\
&\frac{16}{3} = 5 + \frac{1}{3}
\end{aligned}
$$

Дробные части равны, поэтому выбираем любую из них. Пусть это будет $x_2$.  
Введём новое ограничение:  
$\frac{1}{3} - 0 \cdot x_1 - 0 \cdot x_2 - \frac{1}{3}x_3 - \frac{1}{3}x_4 \leq 0$  
Преобразуем полученное неравенство в уравнение:  
$\frac{1}{3} - \frac{1}{3}x_3 - \frac{1}{3}x_4 + x_5 = 0$  
Коэффициенты которого введём дополнительной строкой в оптимальную симплексную таблицу.  
Поскольку двойственный симплекс-метод используется для поиска минимума целевой функции, делаем преобразование $F = -F$.

$$
\begin{tabular}{|c|c|c|c|c|c|c|}
    \hline
        Базис & $x_1$ & $x_2$ & $x_3$ & $x_4$ & $x_5$ & $b_i$ \\
    \hline
        $x_2$ & 0 & 1 & $\frac{4}{3}$ & $\frac{1}{3}$ & 0 & $\frac{16}{3}$ \\ \hline
        $x_1$ & 1 & 0 & $\frac{1}{3}$ & $\frac{1}{3}$ & 0 & $\frac{10}{3}$ \\ \hline
        $x_5$ & 0 & 0 & $-\frac{1}{3}$ & $-\frac{1}{3}$ & 1 & $-\frac{1}{3}$ \\ \hline
        $F$ & 0 & 0 & -2 & -1 & 0 & -12 \\ \hline
\end{tabular}
$$

Так как среди свободных членов есть отрицательные значения, то решение недопустимое, и нужно перейти к допустимому.  
Для этого находим среди свободных членов наиболее отрицательный. Он будет задавать разрешающую строку.  
В этой строке так же находим наиболее отрицательный элемент. Он будет задавать разрешающий столбец.

Разрешающая строка: $x_5$  
$\theta = \frac{F}{x_5}$, минимальное значение соответствует разрешающему столбцу. $\Rightarrow$ разрешающий столбец: $x_4$

$$
\begin{tabular}{|c|c|c|c|>{\columncolor[HTML]{98FB98}}c|c|c|}
    \hline
        Базис & $x_1$ & $x_2$ & $x_3$ & $x_4$ & $x_5$ & $b_i$ \\
    \hline
        $x_2$ & 0 & 1 & $\frac{4}{3}$ & $\frac{1}{3}$ & 0 & $\frac{16}{3}$ \\ \hline
        $x_1$ & 1 & 0 & $\frac{1}{3}$ & $\frac{1}{3}$ & 0 & $\frac{10}{3}$ \\ \hline
        \rowcolor[HTML]{E0FFFF}
        $x_5$ & 0 & 0 & $-\frac{1}{3}$ & \cellcolor[HTML]{BDFDCC} $-\frac{1}{3}$ & 1 & $-\frac{1}{3}$ \\ \hline
        $F$ & 0 & 0 & -2 & -1 & 0 & -12 \\ \hline
        $\theta$ & ~ & ~ & $6$ & $3$ & ~ & ~ \\ \hline
\end{tabular}
$$

Пересчитываем симплекс-таблицу:

$$
\begin{tabular}{|c|c|c|c|c|c|c|}
    \hline
        Базис & $x_1$ & $x_2$ & $x_3$ & $x_4$ & $x_5$ & $b_i$ \\
    \hline
        $x_2$ & 0 & 1 & 1 & 0 & 1 & 5 \\ \hline
        $x_1$ & 1 & 0 & 0 & 0 & 1 & 3 \\ \hline
        $x_4$ & 0 & 0 & 1 & 1 & -3 & 1 \\ \hline
        $F$ & 0 & 0 & -1 & 0 & -3 & -11 \\ \hline
\end{tabular}
$$

Решение получилось целочисленным.

#### Вывод

Оптимальной целочисленный план:

$$
\begin{cases}
x_1 = 3\\
x_2 = 5
\end{cases}
\quad
\Rightarrow
\quad
F(x_1, x_2) = F(3, 5) = 2 \cdot 3 + 5 = 11
$$
