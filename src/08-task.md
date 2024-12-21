# Задание 8 - Задача о назначениях

## Условие

Придумать задачу о назначениях размерности $10 \times 10$. Диапазон значений элементов матрицы от 1 до 9.  
Решить задачу, используя венгерский алгоритм.  
В отчёт добавить решение задачи с помощью программных средств.

## Постановка задачи

$n = 10$ ресурсов и объектов. Матрица стоимостей $C$ размерности $n \times n$:

$$
C = \begin{pmatrix}
    6 & 4 & 5 & 2 & 6 & 4 & 4 & 7 & 4 & 2 \\
    1 & 7 & 6 & 2 & 9 & 8 & 6 & 2 & 4 & 6 \\
    1 & 9 & 2 & 5 & 3 & 3 & 7 & 7 & 5 & 2 \\
    9 & 5 & 4 & 2 & 5 & 2 & 3 & 6 & 7 & 6 \\
    5 & 8 & 4 & 6 & 6 & 3 & 8 & 4 & 9 & 3 \\
    6 & 5 & 1 & 3 & 2 & 8 & 2 & 7 & 5 & 2 \\
    8 & 4 & 9 & 2 & 6 & 3 & 4 & 7 & 3 & 3 \\
    8 & 4 & 4 & 9 & 6 & 5 & 8 & 3 & 7 & 2 \\
    7 & 4 & 7 & 7 & 8 & 8 & 2 & 6 & 7 & 7 \\
    3 & 7 & 6 & 7 & 5 & 5 & 1 & 3 & 8 & 9 \\
\end{pmatrix}
$$

$$
x_{ij} = \begin{cases}
    1, & \text{если назначается i-ый ресурс j-ому объекту}, \\
    0, & \text{иначе}.
\end{cases}
$$

Математическая модель задачи о назначениях:

$F = \sum\limits_{i=1}^{n} \sum\limits_{j=1}^{n} c_{ij} x_{ij} \to \min$

$$
\begin{cases}
    \sum\limits_{j=1}^{n} x_{ij} = 1, i = \overline{1, n} \text{-- для каждого объекта назначен ровно один ресурс} \\
    \sum\limits_{i=1}^{n} x_{ij} = 1, j = \overline{1, n} \text{-- для каждого ресурса назначен ровно один объект}
\end{cases}
$$

## Венгерский алгоритм

$$
\begin{tabular}{|l|l|l|l|l|l|l|l|l|l|l|}
\hline
    \diagbox{Ресурс}{Объект} & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 \\ \hline
    1 & 6 & 4 & 5 & 2 & 6 & 4 & 4 & 7 & 4 & 2 \\ \hline
    2 & 1 & 7 & 6 & 2 & 9 & 8 & 6 & 2 & 4 & 6 \\ \hline
    3 & 1 & 9 & 2 & 5 & 3 & 3 & 7 & 7 & 5 & 2 \\ \hline
    4 & 9 & 5 & 4 & 2 & 5 & 2 & 3 & 6 & 7 & 6 \\ \hline
    5 & 5 & 8 & 4 & 6 & 6 & 3 & 8 & 4 & 9 & 3 \\ \hline
    6 & 6 & 5 & 1 & 3 & 2 & 8 & 2 & 7 & 5 & 2 \\ \hline
    7 & 8 & 4 & 9 & 2 & 6 & 3 & 4 & 7 & 3 & 3 \\ \hline
    8 & 8 & 4 & 4 & 9 & 6 & 5 & 8 & 3 & 7 & 2 \\ \hline
    9 & 7 & 4 & 7 & 7 & 8 & 8 & 2 & 6 & 7 & 7 \\ \hline
    10 & 3 & 7 & 6 & 7 & 5 & 5 & 1 & 3 & 8 & 9 \\ \hline
\end{tabular}
$$

### Шаг 1

Проводим редукцию матрицы по строкам: вычитаем из каждой строки её минимальный элемент.  
В связи с этим во вновь полученной матрице в каждой строке будет как минимум один ноль.

$$
\begin{tabular}{|l|l|l|l|l|l|l|l|l|l|>{\columncolor[HTML]{98FB98}}l|}
\hline
    4 & 2 & 3 & 0 & 4 & 2 & 2 & 5 & 2 & 0 & 2 \\ \hline
    0 & 6 & 5 & 1 & 8 & 7 & 5 & 1 & 3 & 5 & 1 \\ \hline
    0 & 8 & 1 & 4 & 2 & 2 & 6 & 6 & 4 & 1 & 1 \\ \hline
    7 & 3 & 2 & 0 & 3 & 0 & 1 & 4 & 5 & 4 & 2 \\ \hline
    2 & 5 & 1 & 3 & 3 & 0 & 5 & 1 & 6 & 0 & 3 \\ \hline
    5 & 4 & 0 & 2 & 1 & 7 & 1 & 6 & 4 & 1 & 1 \\ \hline
    6 & 2 & 7 & 0 & 4 & 1 & 2 & 5 & 1 & 1 & 2 \\ \hline
    6 & 2 & 2 & 7 & 4 & 3 & 6 & 1 & 5 & 0 & 2 \\ \hline
    5 & 2 & 5 & 5 & 6 & 6 & 0 & 4 & 5 & 5 & 2 \\ \hline
    2 & 6 & 5 & 6 & 4 & 4 & 0 & 2 & 7 & 8 & 1 \\ \hline
\end{tabular}
$$

Затем такую же операцию редукции проводим по столбцам, для чего в каждом столбце находим минимальный элемент.

$$
\begin{tabular}{|l|l|l|l|l|l|l|l|l|l|}
\hline
    4 & 0 & 3 & 0 & 3 & 2 & 2 & 4 & 1 & 0 \\ \hline
    0 & 4 & 5 & 1 & 7 & 7 & 5 & 0 & 2 & 5 \\ \hline
    0 & 6 & 1 & 4 & 1 & 2 & 6 & 5 & 3 & 1 \\ \hline
    7 & 1 & 2 & 0 & 2 & 0 & 1 & 3 & 4 & 4 \\ \hline
    2 & 3 & 1 & 3 & 2 & 0 & 5 & 0 & 5 & 0 \\ \hline
    5 & 2 & 0 & 2 & 0 & 7 & 1 & 5 & 3 & 1 \\ \hline
    6 & 0 & 7 & 0 & 3 & 1 & 2 & 4 & 0 & 1 \\ \hline
    6 & 0 & 2 & 7 & 3 & 3 & 6 & 0 & 4 & 0 \\ \hline
    5 & 0 & 5 & 5 & 5 & 6 & 0 & 3 & 4 & 5 \\ \hline
    2 & 4 & 5 & 6 & 3 & 4 & 0 & 1 & 6 & 8 \\ \hline
    \rowcolor[HTML]{E0FFFF}
    0 & 2 & 0 & 0 & 1 & 0 & 0 & 1 & 1 & 0 \\ \hline
\end{tabular}
$$

После вычитания минимальных элементов получаем полностью редуцированную матрицу.  
Проводим поиск допустимого решения, для которого все назначения имеют нулевую стоимость.

$$
\begin{tabular}{|l|l|l|l|l|l|l|l|l|l|}
\hline
    4 & \cancel0 & 3 & \cancel0 & 3 & 2 & 2 & 4 & 1 & \cellcolor[HTML]{98FB98}0 \\ \hline
    \cancel0 & 4 & 5 & 1 & 7 & 7 & 5 & \cellcolor[HTML]{98FB98}0 & 2 & 5 \\ \hline
    \cellcolor[HTML]{98FB98}0 & 6 & 1 & 4 & 1 & 2 & 6 & 5 & 3 & 1 \\ \hline
    7 & 1 & 2 & \cancel0 & 2 & \cellcolor[HTML]{98FB98}0 & 1 & 3 & 4 & 4 \\ \hline
    2 & 3 & 1 & 3 & 2 & \cancel0 & 5 & \cancel0 & 5 & \cancel0 \\ \hline
    5 & 2 & 0 & 2 & 0 & 7 & 1 & 5 & 3 & 1 \\ \hline
    6 & 0 & 7 & 0 & 3 & 1 & 2 & 4 & 0 & 1 \\ \hline
    6 & 0 & 2 & 7 & 3 & 3 & 6 & \cancel0 & 4 & \cancel0 \\ \hline
    5 & 0 & 5 & 5 & 5 & 6 & 0 & 3 & 4 & 5 \\ \hline
    2 & 4 & 5 & 6 & 3 & 4 & 0 & 1 & 6 & 8 \\ \hline
\end{tabular}
$$

Спускаясь по строкам, для 5-ой строки уже не можем найти подходящий нулевой элемент.  
Поскольку расположение нулевых элементов в матрице не позволяет образовать систему из 10-х независимых нулей (в матрице их только 4), то решение недопустимое.  
Проводим модификацию матрицы. Вычеркиваем строки и столбцы с возможно большим количеством нулевых элементов чтобы количество вычеркиваний было минимальным.

Столбец 2, строку 5, столбец 4, строку 2, строку 6, столбец 7, строку 8, столбец 1, строку 1, столбец 6, строку 7.

$$
\begin{tabular}{|>{\columncolor[HTML]{98FB98}}l|>{\columncolor[HTML]{98FB98}}l|l|>{\columncolor[HTML]{98FB98}}l|l|>{\columncolor[HTML]{98FB98}}l|>{\columncolor[HTML]{98FB98}}l|l|l|l|}
\hline
    \rowcolor[HTML]{E0FFFF}
    \cellcolor[HTML]{BDFDCC}4 & \cellcolor[HTML]{BDFDCC}0 & 3 & \cellcolor[HTML]{BDFDCC}0 & 3 & \cellcolor[HTML]{BDFDCC}2 & \cellcolor[HTML]{BDFDCC}2 & 4 & 1 & 0 \\ \hline
    \rowcolor[HTML]{E0FFFF}
    \cellcolor[HTML]{BDFDCC}0 & \cellcolor[HTML]{BDFDCC}4 & 5 & \cellcolor[HTML]{BDFDCC}1 & 7 & \cellcolor[HTML]{BDFDCC}7 & \cellcolor[HTML]{BDFDCC}5 & 0 & 2 & 5 \\ \hline
    0 & 6 & 1 & 4 & 1 & 2 & 6 & 5 & 3 & 1 \\ \hline
    7 & 1 & 2 & 0 & 2 & 0 & 1 & 3 & 4 & 4 \\ \hline
    \rowcolor[HTML]{E0FFFF}
    \cellcolor[HTML]{BDFDCC}2 & \cellcolor[HTML]{BDFDCC}3 & 1 & \cellcolor[HTML]{BDFDCC}3 & 2 & \cellcolor[HTML]{BDFDCC}0 & \cellcolor[HTML]{BDFDCC}5 & 0 & 5 & 0 \\ \hline
    \rowcolor[HTML]{E0FFFF}
    \cellcolor[HTML]{BDFDCC}5 & \cellcolor[HTML]{BDFDCC}2 & 0 & \cellcolor[HTML]{BDFDCC}2 & 0 & \cellcolor[HTML]{BDFDCC}7 & \cellcolor[HTML]{BDFDCC}1 & 5 & 3 & 1 \\ \hline
    \rowcolor[HTML]{E0FFFF}
    \cellcolor[HTML]{BDFDCC}6 & \cellcolor[HTML]{BDFDCC}0 & 7 & \cellcolor[HTML]{BDFDCC}0 & 3 & \cellcolor[HTML]{BDFDCC}1 & \cellcolor[HTML]{BDFDCC}2 & 4 & 0 & 1 \\ \hline
    \rowcolor[HTML]{E0FFFF}
    \cellcolor[HTML]{BDFDCC}6 & \cellcolor[HTML]{BDFDCC}0 & 2 & \cellcolor[HTML]{BDFDCC}7 & 3 & \cellcolor[HTML]{BDFDCC}3 & \cellcolor[HTML]{BDFDCC}6 & 0 & 4 & 0 \\ \hline
    5 & 0 & 5 & 5 & 5 & 6 & 0 & 3 & 4 & 5 \\ \hline
    2 & 4 & 5 & 6 & 3 & 4 & 0 & 1 & 6 & 8 \\ \hline
\end{tabular}
$$

Минимальный элемент сокращенной матрицы - 1. Вычитаем его из всех её элементов.

$$
\begin{tabular}{|>{\columncolor[HTML]{98FB98}}l|>{\columncolor[HTML]{98FB98}}l|l|>{\columncolor[HTML]{98FB98}}l|l|>{\columncolor[HTML]{98FB98}}l|>{\columncolor[HTML]{98FB98}}l|l|l|l|}
\hline
    \rowcolor[HTML]{E0FFFF}
    \cellcolor[HTML]{BDFDCC}4 & \cellcolor[HTML]{BDFDCC}0 & 3 & \cellcolor[HTML]{BDFDCC}0 & 3 & \cellcolor[HTML]{BDFDCC}2 & \cellcolor[HTML]{BDFDCC}2 & 4 & 1 & 0 \\ \hline
    \rowcolor[HTML]{E0FFFF}
    \cellcolor[HTML]{BDFDCC}0 & \cellcolor[HTML]{BDFDCC}4 & 5 & \cellcolor[HTML]{BDFDCC}1 & 7 & \cellcolor[HTML]{BDFDCC}7 & \cellcolor[HTML]{BDFDCC}5 & 0 & 2 & 5 \\ \hline
    0 & 6 & 0 & 4 & 0 & 2 & 6 & 4 & 2 & 0 \\ \hline
    7 & 1 & 1 & 0 & 1 & 0 & 1 & 2 & 3 & 3 \\ \hline
    \rowcolor[HTML]{E0FFFF}
    \cellcolor[HTML]{BDFDCC}2 & \cellcolor[HTML]{BDFDCC}3 & 1 & \cellcolor[HTML]{BDFDCC}3 & 2 & \cellcolor[HTML]{BDFDCC}0 & \cellcolor[HTML]{BDFDCC}5 & 0 & 5 & 0 \\ \hline
    \rowcolor[HTML]{E0FFFF}
    \cellcolor[HTML]{BDFDCC}5 & \cellcolor[HTML]{BDFDCC}2 & 0 & \cellcolor[HTML]{BDFDCC}2 & 0 & \cellcolor[HTML]{BDFDCC}7 & \cellcolor[HTML]{BDFDCC}1 & 5 & 3 & 1 \\ \hline
    \rowcolor[HTML]{E0FFFF}
    \cellcolor[HTML]{BDFDCC}6 & \cellcolor[HTML]{BDFDCC}0 & 7 & \cellcolor[HTML]{BDFDCC}0 & 3 & \cellcolor[HTML]{BDFDCC}1 & \cellcolor[HTML]{BDFDCC}2 & 4 & 0 & 1 \\ \hline
    \rowcolor[HTML]{E0FFFF}
    \cellcolor[HTML]{BDFDCC}6 & \cellcolor[HTML]{BDFDCC}0 & 2 & \cellcolor[HTML]{BDFDCC}7 & 3 & \cellcolor[HTML]{BDFDCC}3 & \cellcolor[HTML]{BDFDCC}6 & 0 & 4 & 0 \\ \hline
    5 & 0 & 4 & 5 & 4 & 6 & 0 & 2 & 3 & 4 \\ \hline
    2 & 4 & 4 & 6 & 2 & 4 & 0 & 0 & 5 & 7 \\ \hline
\end{tabular}
$$

Затем складываем минимальный элемент с элементами, расположенными на пересечениях вычеркнутых строк и столбцов:

$$
\begin{tabular}{|>{\columncolor[HTML]{98FB98}}l|>{\columncolor[HTML]{98FB98}}l|l|>{\columncolor[HTML]{98FB98}}l|l|>{\columncolor[HTML]{98FB98}}l|>{\columncolor[HTML]{98FB98}}l|l|l|l|}
\hline
    \rowcolor[HTML]{E0FFFF}
    \cellcolor[HTML]{BDFDCC}5 & \cellcolor[HTML]{BDFDCC}1 & 3 & \cellcolor[HTML]{BDFDCC}1 & 3 & \cellcolor[HTML]{BDFDCC}3 & \cellcolor[HTML]{BDFDCC}3 & 4 & 1 & 0 \\ \hline
    \rowcolor[HTML]{E0FFFF}
    \cellcolor[HTML]{BDFDCC}1 & \cellcolor[HTML]{BDFDCC}5 & 5 & \cellcolor[HTML]{BDFDCC}2 & 7 & \cellcolor[HTML]{BDFDCC}8 & \cellcolor[HTML]{BDFDCC}6 & 0 & 2 & 5 \\ \hline
    0 & 6 & 0 & 4 & 0 & 2 & 6 & 4 & 2 & 0 \\ \hline
    7 & 1 & 1 & 0 & 1 & 0 & 1 & 2 & 3 & 3 \\ \hline
    \rowcolor[HTML]{E0FFFF}
    \cellcolor[HTML]{BDFDCC}3 & \cellcolor[HTML]{BDFDCC}4 & 1 & \cellcolor[HTML]{BDFDCC}4 & 2 & \cellcolor[HTML]{BDFDCC}1 & \cellcolor[HTML]{BDFDCC}6 & 0 & 5 & 0 \\ \hline
    \rowcolor[HTML]{E0FFFF}
    \cellcolor[HTML]{BDFDCC}6 & \cellcolor[HTML]{BDFDCC}3 & 0 & \cellcolor[HTML]{BDFDCC}3 & 0 & \cellcolor[HTML]{BDFDCC}8 & \cellcolor[HTML]{BDFDCC}2 & 5 & 3 & 1 \\ \hline
    \rowcolor[HTML]{E0FFFF}
    \cellcolor[HTML]{BDFDCC}7 & \cellcolor[HTML]{BDFDCC}1 & 7 & \cellcolor[HTML]{BDFDCC}1 & 3 & \cellcolor[HTML]{BDFDCC}2 & \cellcolor[HTML]{BDFDCC}3 & 4 & 0 & 1 \\ \hline
    \rowcolor[HTML]{E0FFFF}
    \cellcolor[HTML]{BDFDCC}7 & \cellcolor[HTML]{BDFDCC}1 & 2 & \cellcolor[HTML]{BDFDCC}8 & 3 & \cellcolor[HTML]{BDFDCC}4 & \cellcolor[HTML]{BDFDCC}7 & 0 & 4 & 0 \\ \hline
    5 & 0 & 4 & 5 & 4 & 6 & 0 & 2 & 3 & 4 \\ \hline
    2 & 4 & 4 & 6 & 2 & 4 & 0 & 0 & 5 & 7 \\ \hline
\end{tabular}
$$

### Шаг 2

Проводим редукцию матрицы по строкам: вычитаем из каждой строки её минимальный элемент.  
В связи с этим во вновь полученной матрице в каждой строке будет как минимум один ноль.  
Затем такую же операцию редукции проводим по столбцам, для чего в каждом столбце находим минимальный элемент.  
После вычитания минимальных элементов получаем полностью редуцированную матрицу.  
Проводим поиск допустимого решения, для которого все назначения имеют нулевую стоимость.

$$
\begin{tabular}{|l|l|l|l|l|l|l|l|l|l|}
\hline
    5 & 1 & 3 & 1 & 3 & 3 & 3 & 4 & 1 & \cellcolor[HTML]{98FB98}0 \\ \hline
    1 & 5 & 5 & 2 & 7 & 8 & 6 & \cellcolor[HTML]{98FB98}0 & 2 & 5 \\ \hline
    \cancel0 & 6 & \cancel0 & 4 & \cellcolor[HTML]{98FB98}0 & 2 & 6 & 4 & 2 & \cancel0 \\ \hline
    7 & 1 & 1 & \cancel0 & 1 & \cellcolor[HTML]{98FB98}0 & 1 & 2 & 3 & 3 \\ \hline
    3 & 4 & 1 & 4 & 2 & 1 & 6 & \cancel0 & 5 & \cancel0 \\ \hline
    6 & 3 & 0 & 3 & \cancel0 & 8 & 2 & 5 & 3 & 1 \\ \hline
    7 & 1 & 7 & 1 & 3 & 2 & 3 & 4 & 0 & 1 \\ \hline
    7 & 1 & 2 & 8 & 3 & 4 & 7 & \cancel0 & 4 & \cancel0 \\ \hline
    5 & 0 & 4 & 5 & 4 & 6 & 0 & 2 & 3 & 4 \\ \hline
    2 & 4 & 4 & 6 & 2 & 4 & 0 & \cancel0 & 5 & 7 \\ \hline
\end{tabular}
$$

Спускаясь по строкам, для 5-ой строки уже не можем найти подходящий нулевой элемент.  
Поскольку расположение нулевых элементов в матрице не позволяет образовать систему из 10-х независимых нулей (в матрице их только 4), то решение недопустимое.  
Проводим модификацию матрицы. Вычеркиваем строки и столбцы с возможно большим количеством нулевых элементов чтобы количество вычеркиваний было минимальным.

Строку 3, столбец 8, столбец 10, строку 4, строку 6, столбец 7, строку 7, столбец 2.

$$
\begin{tabular}{|l|>{\columncolor[HTML]{98FB98}}l|l|l|l|l|>{\columncolor[HTML]{98FB98}}l|>{\columncolor[HTML]{98FB98}}l|l|>{\columncolor[HTML]{98FB98}}l|}
\hline
    5 & 1 & 3 & 1 & 3 & 3 & 3 & 4 & 1 & 0 \\ \hline
    1 & 5 & 5 & 2 & 7 & 8 & 6 & 0 & 2 & 5 \\ \hline
    \rowcolor[HTML]{E0FFFF}
    0 & \cellcolor[HTML]{BDFDCC}6 & 0 & 4 & 0 & 2 & \cellcolor[HTML]{BDFDCC}6 & \cellcolor[HTML]{BDFDCC}4 & 2 & \cellcolor[HTML]{BDFDCC}0 \\ \hline
    \rowcolor[HTML]{E0FFFF}
    7 & \cellcolor[HTML]{BDFDCC}1 & 1 & 0 & 1 & 0 & \cellcolor[HTML]{BDFDCC}1 & \cellcolor[HTML]{BDFDCC}2 & 3 & \cellcolor[HTML]{BDFDCC}3 \\ \hline
    3 & 4 & 1 & 4 & 2 & 1 & 6 & 0 & 5 & 0 \\ \hline
    \rowcolor[HTML]{E0FFFF}
    6 & \cellcolor[HTML]{BDFDCC}3 & 0 & 3 & 0 & 8 & \cellcolor[HTML]{BDFDCC}2 & \cellcolor[HTML]{BDFDCC}5 & 3 & \cellcolor[HTML]{BDFDCC}1 \\ \hline
    \rowcolor[HTML]{E0FFFF}
    7 & \cellcolor[HTML]{BDFDCC}1 & 7 & 1 & 3 & 2 & \cellcolor[HTML]{BDFDCC}3 & \cellcolor[HTML]{BDFDCC}4 & 0 & \cellcolor[HTML]{BDFDCC}1 \\ \hline
    7 & 1 & 2 & 8 & 3 & 4 & 7 & 0 & 4 & 0 \\ \hline
    5 & 0 & 4 & 5 & 4 & 6 & 0 & 2 & 3 & 4 \\ \hline
    2 & 4 & 4 & 6 & 2 & 4 & 0 & 0 & 5 & 7 \\ \hline
\end{tabular}
$$

Минимальный элемент сокращенной матрицы - 1. Вычитаем его из всех её элементов и прибавляем к элементам, расположенным на пересечениях вычеркнутых строк и столбцов:

$$
\begin{tabular}{|l|l|l|l|l|l|l|l|l|l|}
\hline
    4 & 1 & 2 & 0 & 2 & 2 & 3 & 4 & 0 & 0 \\ \hline
    0 & 5 & 4 & 1 & 6 & 7 & 6 & 0 & 1 & 5 \\ \hline
    0 & 7 & 0 & 4 & 0 & 2 & 7 & 5 & 2 & 1 \\ \hline
    7 & 2 & 1 & 0 & 1 & 0 & 2 & 3 & 3 & 4 \\ \hline
    2 & 4 & 0 & 3 & 1 & 0 & 6 & 0 & 4 & 0 \\ \hline
    6 & 4 & 0 & 3 & 0 & 8 & 3 & 6 & 3 & 2 \\ \hline
    7 & 2 & 7 & 1 & 3 & 2 & 4 & 5 & 0 & 2 \\ \hline
    6 & 1 & 1 & 7 & 2 & 3 & 7 & 0 & 3 & 0 \\ \hline
    4 & 0 & 3 & 4 & 3 & 5 & 0 & 2 & 2 & 4 \\ \hline
    1 & 4 & 3 & 5 & 1 & 3 & 0 & 0 & 4 & 7 \\ \hline
\end{tabular}
$$

### Шаг 3

Проводим редукцию матрицы по строкам: вычитаем из каждой строки её минимальный элемент.  
В связи с этим во вновь полученной матрице в каждой строке будет как минимум один ноль.  
Затем такую же операцию редукции проводим по столбцам, для чего в каждом столбце находим минимальный элемент.  
После вычитания минимальных элементов получаем полностью редуцированную матрицу.  
Проводим поиск допустимого решения, для которого все назначения имеют нулевую стоимость.

$$
\begin{tabular}{|l|l|l|l|l|l|l|l|l|l|}
\hline
    4 & 1 & 2 & \cellcolor[HTML]{98FB98}0 & 2 & 2 & 3 & 4 & \cancel0 & \cancel0 \\ \hline
    \cellcolor[HTML]{98FB98}0 & 5 & 4 & 1 & 6 & 7 & 6 & \cancel0 & 1 & 5 \\ \hline
    \cancel0 & 7 & \cellcolor[HTML]{98FB98}0 & 4 & \cancel0 & 2 & 7 & 5 & 2 & 1 \\ \hline
    7 & 2 & 1 & \cancel0 & 1 & \cellcolor[HTML]{98FB98}0 & 2 & 3 & 3 & 4 \\ \hline
    2 & 4 & \cancel0 & 3 & 1 & \cancel0 & 6 & \cellcolor[HTML]{98FB98}0 & 4 & \cancel0 \\ \hline
    6 & 4 & \cancel0 & 3 & \cellcolor[HTML]{98FB98}0 & 8 & 3 & 6 & 3 & 2 \\ \hline
    7 & 2 & 7 & 1 & 3 & 2 & 4 & 5 & \cellcolor[HTML]{98FB98}0 & 2 \\ \hline
    6 & 1 & 1 & 7 & 2 & 3 & 7 & \cancel0 & 3 & \cellcolor[HTML]{98FB98}0 \\ \hline
    4 & \cellcolor[HTML]{98FB98}0 & 3 & 4 & 3 & 5 & \cancel0 & 2 & 2 & 4 \\ \hline
    1 & 4 & 3 & 5 & 1 & 3 & \cellcolor[HTML]{98FB98}0 & \cancel0 & 4 & 7 \\ \hline
\end{tabular}
$$

Количество найденных нулей равно k = 10. Значит, найдено оптимальное решение.  
Построим матрицу оптимального назначения:

$$
X^* = \begin{pmatrix}
    0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
    1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\
    0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \\
    0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0
\end{pmatrix}
$$

При этом функция обращается в минимум:  
$F^* = F_{min} = \sum\limits_{i=1}^{n} \sum\limits_{j=1}^{n} c_{ij} x^*_{ij} = 2 + 1 + 2 + 2 + 4 + 2 + 3 + 2 + 4 + 1 = 23$

## Программное решение

```python
# requires hungarian-algorithm
# https://pypi.org/project/hungarian-algorithm/

from hungarian_algorithm import algorithm

G = {
  "01": {"1": 6, "2": 4, "3": 5, "4": 2, "5": 6, "6": 4, "7": 4, "8": 7, "9": 4, "10": 2},
  "02": {"1": 1, "2": 7, "3": 6, "4": 2, "5": 9, "6": 8, "7": 6, "8": 2, "9": 4, "10": 6},
  "03": {"1": 1, "2": 9, "3": 2, "4": 5, "5": 3, "6": 3, "7": 7, "8": 7, "9": 5, "10": 2},
  "04": {"1": 9, "2": 5, "3": 4, "4": 2, "5": 5, "6": 2, "7": 3, "8": 6, "9": 7, "10": 6},
  "05": {"1": 5, "2": 8, "3": 4, "4": 6, "5": 6, "6": 3, "7": 8, "8": 4, "9": 9, "10": 3},
  "06": {"1": 6, "2": 5, "3": 1, "4": 3, "5": 2, "6": 8, "7": 2, "8": 7, "9": 5, "10": 2},
  "07": {"1": 8, "2": 4, "3": 9, "4": 2, "5": 6, "6": 3, "7": 4, "8": 7, "9": 3, "10": 3},
  "08": {"1": 8, "2": 4, "3": 4, "4": 9, "5": 6, "6": 5, "7": 8, "8": 3, "9": 7, "10": 2},
  "09": {"1": 7, "2": 4, "3": 7, "4": 7, "5": 8, "6": 8, "7": 2, "8": 6, "9": 7, "10": 7},
  "010": {"1": 3, "2": 7, "3": 6, "4": 7, "5": 5, "6": 5, "7": 1, "8": 3, "9": 8, "10": 9},
}

print(
    *algorithm.find_matching(G, matching_type="min", return_type="list"),
    sep='\n'
)
# (('06', '3'), 1)
# (('07', '9'), 3)
# (('04', '6'), 2)
# (('01', '4'), 2)
# (('08', '8'), 3)
# (('05', '10'), 3)
# (('02', '1'), 1)
# (('03', '5'), 3)
# (('09', '2'), 4)
# (('010', '7'), 1)

print(
    algorithm.find_matching(G, matching_type="min", return_type="total")
) # 23
```
