# Задание №7 - Задача коммивояжера

## Условие

Придумать задачу коммивояжера размерности $10 \times 10$. Значения в матрице расстояний должны быть любыми целыми числами от 1 до 100.  
Решить задачу методом ветвей и границ. Полный перебор не использовать.  
После выполнения задания добавить в отчёт граф решения, добавить решение задачи с помощью программных средств.

## Постановка задачи

Дано $n = 10$ городов. $D = |d_{ij}|, i, j = \overline{1, n}, i \neq j$ - матрица расстояний от городов $i$ до городов $j$. Коммивояжер должен выехать из своего города, посетить все города по одному разу и вернуться в исходный. Необходимо найти замкнутый маршрут по всем городам такой, чтобы суммарное расстояние было минимальным.

$$
D = \begin{pmatrix}
    0 & 71 & 9 & 65 & 94 & 68 & 76 & 30 & 39 & 4 \\
    43 & 0 & 82 & 50 & 31 & 59 & 17 & 15 & 61 & 21 \\
    79 & 48 & 0 & 65 & 70 & 68 & 6 & 73 & 67 & 29 \\
    50 & 90 & 6 & 0 & 2 & 45 & 67 & 9 & 47 & 76 \\
    36 & 76 & 20 & 87 & 0 & 5 & 72 & 30 & 17 & 26 \\
    17 & 6 & 33 & 89 & 23 & 0 & 67 & 20 & 85 & 81 \\
    97 & 8 & 97 & 54 & 58 & 60 & 0 & 47 & 18 & 72 \\
    28 & 83 & 21 & 34 & 65 & 14 & 98 & 0 & 43 & 70 \\
    67 & 42 & 83 & 8 & 10 & 53 & 52 & 63 & 0 & 28 \\
    39 & 28 & 79 & 98 & 59 & 29 & 7 & 53 & 12 & 0 \\
\end{pmatrix}
$$

$$
x_{ij} = \begin{cases}
1, & \text{если коммивояжер едет из i в j}, \\
0, & \text{иначе}.
\end{cases}
$$

Математическая модель задачи коммивояжера:

$$
F = \sum\limits_{i=1}^{n} \sum\limits_{j=1}^{n} c_{ij} \cdot x_{ij} \to \min
$$

$$
\begin{cases}
    \sum\limits_{j=1}^{n} x_{ij} = 1, i = \overline{1, n} \text{-- выезжает из каждого города ровно один раз} \\
    \sum\limits_{i=1}^{n} x_{ij} = 1, j = \overline{1, n} \text{-- въезжает в каждый город ровно один раз}    \\
    \text{Маршрут замкнут, петли отсутствуют}
\end{cases}
$$

## Метод ветвей и границ

Возьмем в качестве произвольного маршрута:  
$X_0 = (1,2);(2,3);(3,4);(4,5);(5,6);(6,7);(7,8);(8,9);(9,10);(10,1)$  
Тогда $F(X_0) = 71 + 82 + 65 + 2 + 5 + 67 + 47 + 43 + 28 + 39 = 449$

Для определения нижней границы множества воспользуемся **операцией редукции** или приведения матрицы по строкам, для чего необходимо в каждой строке матрицы $D$ найти минимальный элемент.  
$d_i = \min\limits_{j=1}^{n} d_{ij}$

$$
\begin{tabular}{|l|l|l|l|l|l|l|l|l|l|l|>{\columncolor[HTML]{98FB98}}l|}
\hline
    \textbf{i j} & \textbf{1} & \textbf{2} & \textbf{3} & \textbf{4} & \textbf{5} & \textbf{6} & \textbf{7} & \textbf{8} & \textbf{9} & \textbf{10} & \textbf{$d_i$} \\ \hline
    \textbf{1} & M & 71 & 9 & 65 & 94 & 68 & 76 & 30 & 39 & 4 & 4 \\ \hline
    \textbf{2} & 43 & M & 82 & 50 & 31 & 59 & 17 & 15 & 61 & 21 & 15 \\ \hline
    \textbf{3} & 79 & 48 & M & 65 & 70 & 68 & 6 & 73 & 67 & 29 & 6 \\ \hline
    \textbf{4} & 50 & 90 & 6 & M & 2 & 45 & 67 & 9 & 47 & 76 & 2 \\ \hline
    \textbf{5} & 36 & 76 & 20 & 87 & M & 5 & 72 & 30 & 17 & 26 & 5 \\ \hline
    \textbf{6} & 17 & 6 & 33 & 89 & 23 & M & 67 & 20 & 85 & 81 & 6 \\ \hline
    \textbf{7} & 97 & 8 & 97 & 54 & 58 & 60 & M & 47 & 18 & 72 & 8 \\ \hline
    \textbf{8} & 28 & 83 & 21 & 34 & 65 & 14 & 98 & M & 43 & 70 & 14 \\ \hline
    \textbf{9} & 67 & 42 & 83 & 8 & 10 & 53 & 52 & 63 & M & 28 & 8 \\ \hline
    \textbf{10} & 39 & 28 & 79 & 98 & 59 & 29 & 7 & 53 & 12 & M & 7 \\ \hline
\end{tabular}
$$

Затем вычитаем $d_i$ из элементов рассматриваемой строки. В связи с этим во вновь полученной матрице в каждой строке будет как минимум один ноль.

$$
\begin{tabular}{|l|l|l|l|l|l|l|l|l|l|l|}
\hline
    \textbf{i j} & \textbf{1} & \textbf{2} & \textbf{3} & \textbf{4} & \textbf{5} & \textbf{6} & \textbf{7} & \textbf{8} & \textbf{9} & \textbf{10} \\ \hline
    \textbf{1} & M & 67 & 5 & 61 & 90 & 64 & 72 & 26 & 35 & 0 \\ \hline
    \textbf{2} & 28 & M & 67 & 35 & 16 & 44 & 2 & 0 & 46 & 6 \\ \hline
    \textbf{3} & 73 & 42 & M & 59 & 64 & 62 & 0 & 67 & 61 & 23 \\ \hline
    \textbf{4} & 48 & 88 & 4 & M & 0 & 43 & 65 & 7 & 45 & 74 \\ \hline
    \textbf{5} & 31 & 71 & 15 & 82 & M & 0 & 67 & 25 & 12 & 21 \\ \hline
    \textbf{6} & 11 & 0 & 27 & 83 & 17 & M & 61 & 14 & 79 & 75 \\ \hline
    \textbf{7} & 89 & 0 & 89 & 46 & 50 & 52 & M & 39 & 10 & 64 \\ \hline
    \textbf{8} & 14 & 69 & 7 & 20 & 51 & 0 & 84 & M & 29 & 56 \\ \hline
    \textbf{9} & 59 & 34 & 75 & 0 & 2 & 45 & 44 & 55 & M & 20 \\ \hline
    \textbf{10} & 32 & 21 & 72 & 91 & 52 & 22 & 0 & 46 & 5 & M \\ \hline
\end{tabular}
$$

Такую же операцию редукции проводим по столбцам, для чего в каждом столбце находим минимальный элемент:  
$d_j = \min\limits_{i=1}^{n} d_{ij}$

$$
\begin{tabular}{|l|l|l|l|l|l|l|l|l|l|l|}
\hline
    \textbf{i j} & \textbf{1} & \textbf{2} & \textbf{3} & \textbf{4} & \textbf{5} & \textbf{6} & \textbf{7} & \textbf{8} & \textbf{9} & \textbf{10} \\ \hline
    \textbf{1} & M & 67 & 5 & 61 & 90 & 64 & 72 & 26 & 35 & 0 \\ \hline
    \textbf{2} & 28 & M & 67 & 35 & 16 & 44 & 2 & 0 & 46 & 6 \\ \hline
    \textbf{3} & 73 & 42 & M & 59 & 64 & 62 & 0 & 67 & 61 & 23 \\ \hline
    \textbf{4} & 48 & 88 & 4 & M & 0 & 43 & 65 & 7 & 45 & 74 \\ \hline
    \textbf{5} & 31 & 71 & 15 & 82 & M & 0 & 67 & 25 & 12 & 21 \\ \hline
    \textbf{6} & 11 & 0 & 27 & 83 & 17 & M & 61 & 14 & 79 & 75 \\ \hline
    \textbf{7} & 89 & 0 & 89 & 46 & 50 & 52 & M & 39 & 10 & 64 \\ \hline
    \textbf{8} & 14 & 69 & 7 & 20 & 51 & 0 & 84 & M & 29 & 56 \\ \hline
    \textbf{9} & 59 & 34 & 75 & 0 & 2 & 45 & 44 & 55 & M & 20 \\ \hline
    \textbf{10} & 32 & 21 & 72 & 91 & 52 & 22 & 0 & 46 & 5 & M \\ \hline
    \rowcolor[HTML]{E0FFFF}
    \textbf{$d_j$} & 11 & 0 & 4 & 0 & 0 & 0 & 0 & 0 & 5 & 0 \\ \hline
\end{tabular}
$$

После вычитания минимальных элементов получаем полностью редуцированную матрицу, где величины $d_i$ и $d_j$ называются **константами приведения**.

$$
\begin{tabular}{|l|l|l|l|l|l|l|l|l|l|l|}
\hline
    \textbf{i j} & \textbf{1} & \textbf{2} & \textbf{3} & \textbf{4} & \textbf{5} & \textbf{6} & \textbf{7} & \textbf{8} & \textbf{9} & \textbf{10} \\ \hline
    \textbf{1} & M & 67 & 1 & 61 & 90 & 64 & 72 & 26 & 30 & 0 \\ \hline
    \textbf{2} & 17 & M & 63 & 35 & 16 & 44 & 2 & 0 & 41 & 6 \\ \hline
    \textbf{3} & 62 & 42 & M & 59 & 64 & 62 & 0 & 67 & 56 & 23 \\ \hline
    \textbf{4} & 37 & 88 & 0 & M & 0 & 43 & 65 & 7 & 40 & 74 \\ \hline
    \textbf{5} & 20 & 71 & 11 & 82 & M & 0 & 67 & 25 & 7 & 21 \\ \hline
    \textbf{6} & 0 & 0 & 23 & 83 & 17 & M & 61 & 14 & 74 & 75 \\ \hline
    \textbf{7} & 78 & 0 & 85 & 46 & 50 & 52 & M & 39 & 5 & 64 \\ \hline
    \textbf{8} & 3 & 69 & 3 & 20 & 51 & 0 & 84 & M & 24 & 56 \\ \hline
    \textbf{9} & 48 & 34 & 71 & 0 & 2 & 45 & 44 & 55 & M & 20 \\ \hline
    \textbf{10} & 21 & 21 & 68 & 91 & 52 & 22 & 0 & 46 & 0 & M \\ \hline
\end{tabular}
$$

Сумма констант приведения определяет нижнюю границу $H$:  
$H = \sum\limits_{i=1}^{n} d_i + \sum\limits_{j=1}^{n} d_j = 4+15+6+2+5+6+8+14+8+7+11+0+4+0+0+0+0+0+5+0 = 95$

Элементы матрицы $d_{ij}$ соответствуют расстоянию от пункта $i$ до пункта $j$.  
Поскольку в матрице $n$ городов, то $D$ является матрицей $n \times n$ с неотрицательными элементами $d_{ij} \geq 0$  
Каждый допустимый маршрут представляет собой цикл, по которому коммивояжер посещает город только один раз и возвращается в исходный город.  
Длина маршрута определяется выражением:  
$F(M_k) = \sum d_{ij}$  
Причем каждая строка и столбец входят в маршрут только один раз с элементом $d_{ij}$

### Шаг 1

**Определяем ребро ветвления** и разобьем все множество маршрутов относительно этого ребра на два подмножества $(i,j)$ и $(i^*,j^*)$.  
С этой целью для всех клеток матрицы с нулевыми элементами заменяем поочередно нули на M(бесконечность) и определяем для них сумму образовавшихся констант приведения, они приведены в скобках.

$$
\begin{aligned}
&d(1,10) = 1 + 6 = 7 \quad
&d(2,8) = 2 + 7 = 9 \\
&d(3,7) = 23 + 0 = 23 \quad
&d(4,3) = 0 + 1 = 1 \\
&d(4,5) = 0 + 2 = 2 \quad
&d(5,6) = 7 + 0 = 7 \\
&d(6,1) = 0 + 3 = 3 \quad
&d(6,2) = 0 + 0 = 0 \\
&d(7,2) = 5 + 0 = 5 \quad
&d(8,6) = 3 + 0 = 3 \\
&d(9,4) = 2 + 20 = 22 \quad
&d(10,7) = 0 + 0 = 0 \\
&d(10,9) = 0 + 5 = 5
\end{aligned}
$$

$$
\begin{tabular}{|l|l|l|l|l|l|l|l|l|l|l|>{\columncolor[HTML]{98FB98}}l|}
\hline
    \textbf{i j} & \textbf{1} & \textbf{2} & \textbf{3} & \textbf{4} & \textbf{5} & \textbf{6} & \textbf{7} & \textbf{8} & \textbf{9} & \textbf{10} & \textbf{$d_i$} \\ \hline
    \textbf{1} & M & 67 & 1 & 61 & 90 & 64 & 72 & 26 & 30 & 0(7) & 1 \\ \hline
    \textbf{2} & 17 & M & 63 & 35 & 16 & 44 & 2 & 0(9) & 41 & 6 & 2 \\ \hline
    \textbf{3} & 62 & 42 & M & 59 & 64 & 62 & 0(23) & 67 & 56 & 23 & 23 \\ \hline
    \textbf{4} & 37 & 88 & 0(1) & M & 0(2) & 43 & 65 & 7 & 40 & 74 & 0 \\ \hline
    \textbf{5} & 20 & 71 & 11 & 82 & M & 0(7) & 67 & 25 & 7 & 21 & 7 \\ \hline
    \textbf{6} & 0(3) & 0(0) & 23 & 83 & 17 & M & 61 & 14 & 74 & 75 & 0 \\ \hline
    \textbf{7} & 78 & 0(5) & 85 & 46 & 50 & 52 & M & 39 & 5 & 64 & 5 \\ \hline
    \textbf{8} & 3 & 69 & 3 & 20 & 51 & 0(3) & 84 & M & 24 & 56 & 3 \\ \hline
    \textbf{9} & 48 & 34 & 71 & 0(22) & 2 & 45 & 44 & 55 & M & 20 & 2 \\ \hline
    \textbf{10} & 21 & 21 & 68 & 91 & 52 & 22 & 0(0) & 46 & 0(5) & M & 0 \\ \hline
    \rowcolor[HTML]{E0FFFF}
    \textbf{$d_j$} & 3 & 0 & 1 & 20 & 2 & 0 & 0 & 7 & 5 & 6 & \cellcolor[HTML]{FFFFFF} 0 \\ \hline
\end{tabular}
$$

Наибольшая сумма констант приведения равна $(23 + 0) = 23$ для ребра $(3,7)$, следовательно, множество разбивается на два подмножества $(3,7)$ и $(3^*,7^*)$.

**Исключение ребра** $(3,7)$ проводим путем замены элемента $d_{37} = 0$ на $M$, после чего осуществляем очередное приведение матрицы расстояний для образовавшегося подмножества $(3^*,7^*)$, в результате получим редуцированную матрицу.

$$
\begin{tabular}{|l|l|l|l|l|l|l|l|l|l|l|>{\columncolor[HTML]{98FB98}}l|}
\hline
    \textbf{i j} & \textbf{1} & \textbf{2} & \textbf{3} & \textbf{4} & \textbf{5} & \textbf{6} & \textbf{7} & \textbf{8} & \textbf{9} & \textbf{10} & \textbf{$d_i$} \\ \hline
    \textbf{1} & M & 67 & 1 & 61 & 90 & 64 & 72 & 26 & 30 & 0 & 0 \\ \hline
    \textbf{2} & 17 & M & 63 & 35 & 16 & 44 & 2 & 0 & 41 & 6 & 0 \\ \hline
    \textbf{3} & 62 & 42 & M & 59 & 64 & 62 & M & 67 & 56 & 23 & 23 \\ \hline
    \textbf{4} & 37 & 88 & 0 & M & 0 & 43 & 65 & 7 & 40 & 74 & 0 \\ \hline
    \textbf{5} & 20 & 71 & 11 & 82 & M & 0 & 67 & 25 & 7 & 21 & 0 \\ \hline
    \textbf{6} & 0 & 0 & 23 & 83 & 17 & M & 61 & 14 & 74 & 75 & 0 \\ \hline
    \textbf{7} & 78 & 0 & 85 & 46 & 50 & 52 & M & 39 & 5 & 64 & 0 \\ \hline
    \textbf{8} & 3 & 69 & 3 & 20 & 51 & 0 & 84 & M & 24 & 56 & 0 \\ \hline
    \textbf{9} & 48 & 34 & 71 & 0 & 2 & 45 & 44 & 55 & M & 20 & 0 \\ \hline
    \textbf{10} & 21 & 21 & 68 & 91 & 52 & 22 & 0 & 46 & 0 & M & 0 \\ \hline
    \rowcolor[HTML]{E0FFFF}
    \textbf{$d_j$} & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & \cellcolor[HTML]{FFFFFF} 23 \\ \hline
\end{tabular}
$$

Нижняя граница гамильтоновых циклов этого подмножества:  
$H(3^*,7^*) = 95 + 23 = 118$

**Включение ребра** $(3,7)$ проводится путем исключения всех элементов 3-ой строки и 7-го столбца, в которой элемент $d_{73}$ заменяем на $M$, для исключения образования негамильтонова цикла.  
В результате получим другую сокращенную матрицу $(9 \times 9)$, которая подлежит операции приведения.  
После операции приведения сокращенная матрица будет иметь вид:

$$
\begin{tabular}{|l|l|l|l|l|l|l|l|l|l|>{\columncolor[HTML]{98FB98}}l|}
\hline
    \textbf{i j} & \textbf{1} & \textbf{2} & \textbf{3} & \textbf{4} & \textbf{5} & \textbf{6} & \textbf{8} & \textbf{9} & \textbf{10} & \textbf{$d_i$} \\ \hline
    \textbf{1} & M & 67 & 1 & 61 & 90 & 64 & 26 & 30 & 0 & 0 \\ \hline
    \textbf{2} & 17 & M & 63 & 35 & 16 & 44 & 0 & 41 & 6 & 0 \\ \hline
    \textbf{4} & 37 & 88 & 0 & M & 0 & 43 & 7 & 40 & 74 & 0 \\ \hline
    \textbf{5} & 20 & 71 & 11 & 82 & M & 0 & 25 & 7 & 21 & 0 \\ \hline
    \textbf{6} & 0 & 0 & 23 & 83 & 17 & M & 14 & 74 & 75 & 0 \\ \hline
    \textbf{7} & 78 & 0 & M & 46 & 50 & 52 & 39 & 5 & 64 & 0 \\ \hline
    \textbf{8} & 3 & 69 & 3 & 20 & 51 & 0 & M & 24 & 56 & 0 \\ \hline
    \textbf{9} & 48 & 34 & 71 & 0 & 2 & 45 & 55 & M & 20 & 0 \\ \hline
    \textbf{10} & 21 & 21 & 68 & 91 & 52 & 22 & 46 & 0 & M & 0 \\ \hline
    \rowcolor[HTML]{E0FFFF}
    \textbf{$d_j$} & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & \cellcolor[HTML]{FFFFFF} 0 \\ \hline
\end{tabular}
$$

Сумма констант приведения сокращенной матрицы:  
$\sum d_i + \sum d_j = 0 + 0 = 0$  
Нижняя граница подмножества $(3,7)$ равна:  
$H(3,7) = 95 + 0 = 95 \leq 118$  
Поскольку нижняя граница этого подмножества $(3,7)$ меньше, чем подмножества $(3^*,7^*)$, то ребро $(3,7)$ включаем в маршрут с новой границей $H = 95$.

### Шаг 2

**Определяем ребро ветвления.**

$$
\begin{aligned}
&d(1,10) = 1 + 6 = 7 \quad
&d(2,8) = 6 + 7 = 13 \\
&d(4,3) = 0 + 1 = 1 \quad
&d(4,5) = 0 + 2 = 2 \\
&d(5,6) = 7 + 0 = 7 \quad
&d(6,1) = 0 + 3 = 3 \\
&d(6,2) = 0 + 0 = 0 \quad
&d(7,2) = 5 + 0 = 5 \\
&d(8,6) = 3 + 0 = 3 \quad
&d(9,4) = 2 + 20 = 22 \\
&d(10,9) = 21 + 5 = 26
\end{aligned}
$$

$\max: d(10, 9) = 26$

$$
\begin{tabular}{|l|l|l|l|l|l|l|l|l|l|>{\columncolor[HTML]{98FB98}}l|}
\hline
    \textbf{i j} & \textbf{1} & \textbf{2} & \textbf{3} & \textbf{4} & \textbf{5} & \textbf{6} & \textbf{8} & \textbf{9} & \textbf{10} & \textbf{$d_i$} \\ \hline
    \textbf{1} & M & 67 & 1 & 61 & 90 & 64 & 26 & 30 & 0(7) & 1 \\ \hline
    \textbf{2} & 17 & M & 63 & 35 & 16 & 44 & 0(13) & 41 & 6 & 6 \\ \hline
    \textbf{4} & 37 & 88 & 0(1) & M & 0(2) & 43 & 7 & 40 & 74 & 0 \\ \hline
    \textbf{5} & 20 & 71 & 11 & 82 & M & 0(7) & 25 & 7 & 21 & 7 \\ \hline
    \textbf{6} & 0(3) & 0(0) & 23 & 83 & 17 & M & 14 & 74 & 75 & 0 \\ \hline
    \textbf{7} & 78 & 0(5) & M & 46 & 50 & 52 & 39 & 5 & 64 & 5 \\ \hline
    \textbf{8} & 3 & 69 & 3 & 20 & 51 & 0(3) & M & 24 & 56 & 3 \\ \hline
    \textbf{9} & 48 & 34 & 71 & 0(22) & 2 & 45 & 55 & M & 20 & 2 \\ \hline
    \textbf{10} & 21 & 21 & 68 & 91 & 52 & 22 & 46 & 0(26) & M & 21 \\ \hline
    \rowcolor[HTML]{E0FFFF}
    \textbf{$d_j$} & 3 & 0 & 1 & 20 & 2 & 0 & 7 & 5 & 6 & \cellcolor[HTML]{FFFFFF} 0 \\ \hline
\end{tabular}
$$

**Исключение ребра** $(10,9): d_{109}=M$.

$$
\begin{tabular}{|l|l|l|l|l|l|l|l|l|l|>{\columncolor[HTML]{98FB98}}l|}
\hline
    \textbf{i j} & \textbf{1} & \textbf{2} & \textbf{3} & \textbf{4} & \textbf{5} & \textbf{6} & \textbf{8} & \textbf{9} & \textbf{10} & \textbf{$d_i$} \\ \hline
    \textbf{1} & M & 67 & 1 & 61 & 90 & 64 & 26 & 30 & 0 & 0 \\ \hline
    \textbf{2} & 17 & M & 63 & 35 & 16 & 44 & 0 & 41 & 6 & 0 \\ \hline
    \textbf{4} & 37 & 88 & 0 & M & 0 & 43 & 7 & 40 & 74 & 0 \\ \hline
    \textbf{5} & 20 & 71 & 11 & 82 & M & 0 & 25 & 7 & 21 & 0 \\ \hline
    \textbf{6} & 0 & 0 & 23 & 83 & 17 & M & 14 & 74 & 75 & 0 \\ \hline
    \textbf{7} & 78 & 0 & M & 46 & 50 & 52 & 39 & 5 & 64 & 0 \\ \hline
    \textbf{8} & 3 & 69 & 3 & 20 & 51 & 0 & M & 24 & 56 & 0 \\ \hline
    \textbf{9} & 48 & 34 & 71 & 0 & 2 & 45 & 55 & M & 20 & 0 \\ \hline
    \textbf{10} & 21 & 21 & 68 & 91 & 52 & 22 & 46 & M & M & 21 \\ \hline
    \rowcolor[HTML]{E0FFFF}
    \textbf{$d_j$} & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 5 & 0 & \cellcolor[HTML]{FFFFFF} 26 \\ \hline
\end{tabular}
$$

$H(10^*,9^*) = 95 + 26 = 121$  
**Включение ребра** $(10,9): d_{910}=M$.

$$
\begin{tabular}{|l|l|l|l|l|l|l|l|l|>{\columncolor[HTML]{98FB98}}l|}
\hline
    \textbf{i j} & \textbf{1} & \textbf{2} & \textbf{3} & \textbf{4} & \textbf{5} & \textbf{6} & \textbf{8} & \textbf{10} & \textbf{$d_i$} \\ \hline
    \textbf{1} & M & 67 & 1 & 61 & 90 & 64 & 26 & 0 & 0 \\ \hline
    \textbf{2} & 17 & M & 63 & 35 & 16 & 44 & 0 & 6 & 0 \\ \hline
    \textbf{4} & 37 & 88 & 0 & M & 0 & 43 & 7 & 74 & 0 \\ \hline
    \textbf{5} & 20 & 71 & 11 & 82 & M & 0 & 25 & 21 & 0 \\ \hline
    \textbf{6} & 0 & 0 & 23 & 83 & 17 & M & 14 & 75 & 0 \\ \hline
    \textbf{7} & 78 & 0 & M & 46 & 50 & 52 & 39 & 64 & 0 \\ \hline
    \textbf{8} & 3 & 69 & 3 & 20 & 51 & 0 & M & 56 & 0 \\ \hline
    \textbf{9} & 48 & 34 & 71 & 0 & 2 & 45 & 55 & M & 0 \\ \hline
    \rowcolor[HTML]{E0FFFF}
    \textbf{$d_j$} & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & \cellcolor[HTML]{FFFFFF} 0 \\ \hline
\end{tabular}
$$

$\sum d_i + \sum d_j = 0 + 0 = 0$  
$H(10,9) = 95 + 0 = 95 \leq 121$  
Ребро $(10,9)$ включаем в маршрут с новой границей $H=95$.

### Шаг 3

**Определяем ребро ветвления.**

$$
\begin{aligned}
&d(1,10) = 1 + 6 = 7 \quad
&d(2,8) = 6 + 7 = 13 \\
&d(4,3) = 0 + 1 = 1 \quad
&d(4,5) = 0 + 2 = 2 \\
&d(5,6) = 11 + 0 = 11 \quad
&d(6,1) = 0 + 3 = 3 \\
&d(6,2) = 0 + 0 = 0 \quad
&d(7,2) = 39 + 0 = 39 \\
&d(8,6) = 3 + 0 = 3 \quad
&d(9,4) = 2 + 20 = 22
\end{aligned}
$$

$\max: d(7,2) = 39$

$$
\begin{tabular}{|l|l|l|l|l|l|l|l|l|>{\columncolor[HTML]{98FB98}}l|}
\hline
    \textbf{i j} & \textbf{1} & \textbf{2} & \textbf{3} & \textbf{4} & \textbf{5} & \textbf{6} & \textbf{8} & \textbf{10} & \textbf{$d_i$} \\ \hline
    \textbf{1} & M & 67 & 1 & 61 & 90 & 64 & 26 & 0(7) & 1 \\ \hline
    \textbf{2} & 17 & M & 63 & 35 & 16 & 44 & 0(13) & 6 & 6 \\ \hline
    \textbf{4} & 37 & 88 & 0(1) & M & 0(2) & 43 & 7 & 74 & 0 \\ \hline
    \textbf{5} & 20 & 71 & 11 & 82 & M & 0(11) & 25 & 21 & 11 \\ \hline
    \textbf{6} & 0(3) & 0(0) & 23 & 83 & 17 & M & 14 & 75 & 0 \\ \hline
    \textbf{7} & 78 & 0(39) & M & 46 & 50 & 52 & 39 & 64 & 39 \\ \hline
    \textbf{8} & 3 & 69 & 3 & 20 & 51 & 0(3) & M & 56 & 3 \\ \hline
    \textbf{9} & 48 & 34 & 71 & 0(22) & 2 & 45 & 55 & M & 2 \\ \hline
    \rowcolor[HTML]{E0FFFF}
    \textbf{$d_j$} & 3 & 0 & 1 & 20 & 2 & 0 & 7 & 6 & \cellcolor[HTML]{FFFFFF} 0 \\ \hline
\end{tabular}
$$

**Исключение ребра** $(7,2): d_{72}=M$.

$$
\begin{tabular}{|l|l|l|l|l|l|l|l|l|>{\columncolor[HTML]{98FB98}}l|}
\hline
    \textbf{i j} & \textbf{1} & \textbf{2} & \textbf{3} & \textbf{4} & \textbf{5} & \textbf{6} & \textbf{8} & \textbf{10} & \textbf{$d_i$} \\ \hline
    \textbf{1} & M & 67 & 1 & 61 & 90 & 64 & 26 & 0 & 0 \\ \hline
    \textbf{2} & 17 & M & 63 & 35 & 16 & 44 & 0 & 6 & 0 \\ \hline
    \textbf{4} & 37 & 88 & 0 & M & 0 & 43 & 7 & 74 & 0 \\ \hline
    \textbf{5} & 20 & 71 & 11 & 82 & M & 0 & 25 & 21 & 0 \\ \hline
    \textbf{6} & 0 & 0 & 23 & 83 & 17 & M & 14 & 75 & 0 \\ \hline
    \textbf{7} & 78 & M & M & 46 & 50 & 52 & 39 & 64 & 39 \\ \hline
    \textbf{8} & 3 & 69 & 3 & 20 & 51 & 0 & M & 56 & 0 \\ \hline
    \textbf{9} & 48 & 34 & 71 & 0 & 2 & 45 & 55 & M & 0 \\ \hline
    \rowcolor[HTML]{E0FFFF}
    \textbf{$d_j$} & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & \cellcolor[HTML]{FFFFFF} 39 \\ \hline
\end{tabular}
$$

$H(7^*,2^*) = 95 + 39 = 134$  
**Включение ребра** $(7,2): d_{27}=M$.

$$
\begin{tabular}{|l|l|l|l|l|l|l|l|>{\columncolor[HTML]{98FB98}}l|}
\hline
    \textbf{i j} & \textbf{1} & \textbf{3} & \textbf{4} & \textbf{5} & \textbf{6} & \textbf{8} & \textbf{10} & \textbf{$d_i$} \\ \hline
    \textbf{1} & M & 1 & 61 & 90 & 64 & 26 & 0 & 0 \\ \hline
    \textbf{2} & 17 & 63 & 35 & 16 & 44 & 0 & 6 & 0 \\ \hline
    \textbf{4} & 37 & 0 & M & 0 & 43 & 7 & 74 & 0 \\ \hline
    \textbf{5} & 20 & 11 & 82 & M & 0 & 25 & 21 & 0 \\ \hline
    \textbf{6} & 0 & 23 & 83 & 17 & M & 14 & 75 & 0 \\ \hline
    \textbf{8} & 3 & 3 & 20 & 51 & 0 & M & 56 & 0 \\ \hline
    \textbf{9} & 48 & 71 & 0 & 2 & 45 & 55 & M & 0 \\ \hline
    \rowcolor[HTML]{E0FFFF}
    \textbf{$d_j$} & 0 & 0 & 0 & 0 & 0 & 0 & 0 & \cellcolor[HTML]{FFFFFF} 0 \\ \hline
\end{tabular}
$$

$\sum d_i + \sum d_j = 0 + 0 = 0$  
$H(7,2) = 95 + 0 = 95 \leq 134$

Запрещаем переходы: $(2,3)$,  
Ребро $(7,2)$ включаем в маршрут с новой границей $H=95$.

### Шаг 4

**Определяем ребро ветвления.**

$$
\begin{aligned}
&d(1,10) = 1 + 6 = 7 \quad
&d(2,8) = 6 + 7 = 13 \\
&d(4,3) = 0 + 1 = 1 \quad
&d(4,5) = 0 + 2 = 2 \\
&d(5,6) = 11 + 0 = 11 \quad
&d(6,1) = 14 + 3 = 17 \\
&d(8,6) = 3 + 0 = 3 \quad
&d(9,4) = 2 + 20 = 22
\end{aligned}
$$

$\max: d(9,4) = 22$

$$
\begin{tabular}{|l|l|l|l|l|l|l|l|>{\columncolor[HTML]{98FB98}}l|}
\hline
    \textbf{i j} & \textbf{1} & \textbf{3} & \textbf{4} & \textbf{5} & \textbf{6} & \textbf{8} & \textbf{10} & \textbf{$d_i$} \\ \hline
    \textbf{1} & M & 1 & 61 & 90 & 64 & 26 & 0(7) & 1 \\ \hline
    \textbf{2} & 17 & M & 35 & 16 & 44 & 0(13) & 6 & 6 \\ \hline
    \textbf{4} & 37 & 0(1) & M & 0(2) & 43 & 7 & 74 & 0 \\ \hline
    \textbf{5} & 20 & 11 & 82 & M & 0(11) & 25 & 21 & 11 \\ \hline
    \textbf{6} & 0(17) & 23 & 83 & 17 & M & 14 & 75 & 14 \\ \hline
    \textbf{8} & 3 & 3 & 20 & 51 & 0(3) & M & 56 & 3 \\ \hline
    \textbf{9} & 48 & 71 & 0(22) & 2 & 45 & 55 & M & 2 \\ \hline
    \rowcolor[HTML]{E0FFFF}
    \textbf{$d_j$} & 3 & 1 & 20 & 2 & 0 & 7 & 6 & \cellcolor[HTML]{FFFFFF} 0 \\ \hline
\end{tabular}
$$

**Исключение ребра** $(9,4): d_{94}=M$.

$$
\begin{tabular}{|l|l|l|l|l|l|l|l|>{\columncolor[HTML]{98FB98}}l|}
\hline
    \textbf{i j} & \textbf{1} & \textbf{3} & \textbf{4} & \textbf{5} & \textbf{6} & \textbf{8} & \textbf{10} & \textbf{$d_i$} \\ \hline
    \textbf{1} & M & 1 & 61 & 90 & 64 & 26 & 0 & 0 \\ \hline
    \textbf{2} & 17 & M & 35 & 16 & 44 & 0 & 6 & 0 \\ \hline
    \textbf{4} & 37 & 0 & M & 0 & 43 & 7 & 74 & 0 \\ \hline
    \textbf{5} & 20 & 11 & 82 & M & 0 & 25 & 21 & 0 \\ \hline
    \textbf{6} & 0 & 23 & 83 & 17 & M & 14 & 75 & 0 \\ \hline
    \textbf{8} & 3 & 3 & 20 & 51 & 0 & M & 56 & 0 \\ \hline
    \textbf{9} & 48 & 71 & M & 2 & 45 & 55 & M & 2 \\ \hline
    \rowcolor[HTML]{E0FFFF}
    \textbf{$d_j$} & 0 & 0 & 20 & 0 & 0 & 0 & 0 & \cellcolor[HTML]{FFFFFF} 22 \\ \hline
\end{tabular}
$$

$H(9^*,4^*) = 95 + 22 = 117$  
**Включение ребра** $(9,4): d_{49}=M$.

$$
\begin{tabular}{|l|l|l|l|l|l|l|>{\columncolor[HTML]{98FB98}}l|}
\hline
    \textbf{i j} & \textbf{1} & \textbf{3} & \textbf{5} & \textbf{6} & \textbf{8} & \textbf{10} & \textbf{$d_i$} \\ \hline
    \textbf{1} & M & 1 & 90 & 64 & 26 & 0 & 0 \\ \hline
    \textbf{2} & 17 & M & 16 & 44 & 0 & 6 & 0 \\ \hline
    \textbf{4} & 37 & 0 & 0 & 43 & 7 & 74 & 0 \\ \hline
    \textbf{5} & 20 & 11 & M & 0 & 25 & 21 & 0 \\ \hline
    \textbf{6} & 0 & 23 & 17 & M & 14 & 75 & 0 \\ \hline
    \textbf{8} & 3 & 3 & 51 & 0 & M & 56 & 0 \\ \hline
    \rowcolor[HTML]{E0FFFF}
    \textbf{$d_j$} & 0 & 0 & 0 & 0 & 0 & 0 & \cellcolor[HTML]{FFFFFF} 0 \\ \hline
\end{tabular}
$$

$\sum d_i + \sum d_j = 0 + 0 = 0$  
$H(9,4) = 95 + 0 = 95 \leq 117$  
Запрещаем переходы: $(2,3), (4,10)$,  
Ребро $(9,4)$ включаем в маршрут с новой границей $H=95$.

### Шаг 5

**Определяем ребро ветвления.**

$$
\begin{aligned}
&d(1,10) = 1 + 6 = 7 \quad
&d(2,8) = 6 + 7 = 13 \\
&d(4,3) = 0 + 1 = 1 \quad
&d(4,5) = 0 + 16 = 16 \\
&d(5,6) = 11 + 0 = 11 \quad
&d(6,1) = 14 + 3 = 17 \\
&d(8,6) = 3 + 0 = 3
\end{aligned}
$$

$\max: d(6,1) = 17$

$$
\begin{tabular}{|l|l|l|l|l|l|l|>{\columncolor[HTML]{98FB98}}l|}
\hline
    \textbf{i j} & \textbf{1} & \textbf{3} & \textbf{5} & \textbf{6} & \textbf{8} & \textbf{10} & \textbf{$d_i$} \\ \hline
    \textbf{1} & M & 1 & 90 & 64 & 26 & 0(7) & 1 \\ \hline
    \textbf{2} & 17 & M & 16 & 44 & 0(13) & 6 & 6 \\ \hline
    \textbf{4} & 37 & 0(1) & 0(16) & 43 & 7 & M & 0 \\ \hline
    \textbf{5} & 20 & 11 & M & 0(11) & 25 & 21 & 11 \\ \hline
    \textbf{6} & 0(17) & 23 & 17 & M & 14 & 75 & 14 \\ \hline
    \textbf{8} & 3 & 3 & 51 & 0(3) & M & 56 & 3 \\ \hline
    \rowcolor[HTML]{E0FFFF}
    \textbf{$d_j$} & 3 & 1 & 16 & 0 & 7 & 6 & \cellcolor[HTML]{FFFFFF} 0 \\ \hline
\end{tabular}
$$

**Исключение ребра** $(6,1): d_{61}=M$.

$$
\begin{tabular}{|l|l|l|l|l|l|l|>{\columncolor[HTML]{98FB98}}l|}
\hline
    \textbf{i j} & \textbf{1} & \textbf{3} & \textbf{5} & \textbf{6} & \textbf{8} & \textbf{10} & \textbf{$d_i$} \\ \hline
    \textbf{1} & M & 1 & 90 & 64 & 26 & 0 & 0 \\ \hline
    \textbf{2} & 17 & M & 16 & 44 & 0 & 6 & 0 \\ \hline
    \textbf{4} & 37 & 0 & 0 & 43 & 7 & M & 0 \\ \hline
    \textbf{5} & 20 & 11 & M & 0 & 25 & 21 & 0 \\ \hline
    \textbf{6} & M & 23 & 17 & M & 14 & 75 & 14 \\ \hline
    \textbf{8} & 3 & 3 & 51 & 0 & M & 56 & 0 \\ \hline
    \rowcolor[HTML]{E0FFFF}
    \textbf{$d_j$} & 3 & 0 & 0 & 0 & 0 & 0 & \cellcolor[HTML]{FFFFFF} 17 \\ \hline
\end{tabular}
$$

$H(6^*,1^*) = 95 + 17 = 112$  
**Включение ребра** $(6,1): d_{16}=M$.

$$
\begin{tabular}{|l|l|l|l|l|l|>{\columncolor[HTML]{98FB98}}l|}
\hline
    \textbf{i j} & \textbf{3} & \textbf{5} & \textbf{6} & \textbf{8} & \textbf{10} & \textbf{$d_i$} \\ \hline
    \textbf{1} & 1 & 90 & M & 26 & 0 & 0 \\ \hline
    \textbf{2} & M & 16 & 44 & 0 & 6 & 0 \\ \hline
    \textbf{4} & 0 & 0 & 43 & 7 & M & 0 \\ \hline
    \textbf{5} & 11 & M & 0 & 25 & 21 & 0 \\ \hline
    \textbf{8} & 3 & 51 & 0 & M & 56 & 0 \\ \hline
    \rowcolor[HTML]{E0FFFF}
    \textbf{$d_j$} & 0 & 0 & 0 & 0 & 0 & \cellcolor[HTML]{FFFFFF} 0 \\ \hline
\end{tabular}
$$

$\sum d_i + \sum d_j = 0 + 0 = 0$  
$H(6,1) = 95 + 0 = 95 \leq 112$  
Запрещаем переходы: $(2,3), (4,10)$,  
Ребро $(6,1)$ включаем в маршрут с новой границей $H=95$.

### Шаг 6

**Определяем ребро ветвления.**

$$
\begin{aligned}
&d(1,10) = 1 + 6 = 7 \quad
&d(2,8) = 6 + 7 = 13 \\
&d(4,3) = 0 + 1 = 1 \quad
&d(4,5) = 0 + 16 = 16 \\
&d(5,6) = 11 + 0 = 11 \quad
&d(8,6) = 3 + 0 = 3
\end{aligned}
$$

$\max: d(4,5) = 16$

$$
\begin{tabular}{|l|l|l|l|l|l|>{\columncolor[HTML]{98FB98}}l|}
\hline
    \textbf{i j} & \textbf{3} & \textbf{5} & \textbf{6} & \textbf{8} & \textbf{10} & \textbf{$d_i$} \\ \hline
    \textbf{1} & 1 & 90 & M & 26 & 0(7) & 1 \\ \hline
    \textbf{2} & M & 16 & 44 & 0(13) & 6 & 6 \\ \hline
    \textbf{4} & 0(1) & 0(16) & 43 & 7 & M & 0 \\ \hline
    \textbf{5} & 11 & M & 0(11) & 25 & 21 & 11 \\ \hline
    \textbf{8} & 3 & 51 & 0(3) & M & 56 & 3 \\ \hline
    \rowcolor[HTML]{E0FFFF}
    \textbf{$d_j$} & 1 & 16 & 0 & 7 & 6 & \cellcolor[HTML]{FFFFFF} 0 \\ \hline
\end{tabular}
$$

**Исключение ребра** $(4,5): d_{45}=M$.

$$
\begin{tabular}{|l|l|l|l|l|l|>{\columncolor[HTML]{98FB98}}l|}
\hline
    \textbf{i j} & \textbf{3} & \textbf{5} & \textbf{6} & \textbf{8} & \textbf{10} & \textbf{$d_i$} \\ \hline
    \textbf{1} & 1 & 90 & M & 26 & 0 & 0 \\ \hline
    \textbf{2} & M & 16 & 44 & 0 & 6 & 0 \\ \hline
    \textbf{4} & 0 & M & 43 & 7 & M & 0 \\ \hline
    \textbf{5} & 11 & M & 0 & 25 & 21 & 0 \\ \hline
    \textbf{8} & 3 & 51 & 0 & M & 56 & 0 \\ \hline
    \rowcolor[HTML]{E0FFFF}
    \textbf{$d_j$} & 0 & 16 & 0 & 0 & 0 & \cellcolor[HTML]{FFFFFF} 16 \\ \hline
\end{tabular}
$$

$H(4^*,5^*) = 95 + 16 = 111$  
**Включение ребра** $(4,5): d_{54}=M$.

$$
\begin{tabular}{|l|l|l|l|l|>{\columncolor[HTML]{98FB98}}l|}
\hline
    \textbf{i j} & \textbf{3} & \textbf{6} & \textbf{8} & \textbf{10} & \textbf{$d_i$} \\ \hline
    \textbf{1} & 1 & M & 26 & 0 & 0 \\ \hline
    \textbf{2} & M & 44 & 0 & 6 & 0 \\ \hline
    \textbf{5} & 11 & 0 & 25 & 21 & 0 \\ \hline
    \textbf{8} & 3 & 0 & M & 56 & 0 \\ \hline
    \rowcolor[HTML]{E0FFFF}
    \textbf{$d_j$} & 1 & 0 & 0 & 0 & \cellcolor[HTML]{FFFFFF} 1 \\ \hline
\end{tabular}
$$

$\sum d_i + \sum d_j = 0 + 1 = 1$  
$H(4,5) = 95 + 1 = 96 \leq 111$  
Запрещаем переходы: $(2,3), (5,10), (5,9)$,  
Ребро $(4,5)$ включаем в маршрут с новой границей $H=96$.

### Шаг 7

**Определяем ребро ветвления.**

$$
\begin{aligned}
&d(1,3) = 0 + 2 = 2 \quad
&d(1,10) = 0 + 6 = 6 \\
&d(2,8) = 6 + 25 = 31 \quad
&d(5,6) = 10 + 0 = 10 \\
&d(8,6) = 2 + 0 = 2
\end{aligned}
$$

$\max: d(2,8) = 31$

$$
\begin{tabular}{|l|l|l|l|l|>{\columncolor[HTML]{98FB98}}l|}
\hline
    \textbf{i j} & \textbf{3} & \textbf{6} & \textbf{8} & \textbf{10} & \textbf{$d_i$} \\ \hline
    \textbf{1} & 0(2) & M & 26 & 0(6) & 0 \\ \hline
    \textbf{2} & M & 44 & 0(31) & 6 & 6 \\ \hline
    \textbf{5} & 10 & 0(10) & 25 & M & 10 \\ \hline
    \textbf{8} & 2 & 0(2) & M & 56 & 2 \\ \hline
    \rowcolor[HTML]{E0FFFF}
    \textbf{$d_j$} & 2 & 0 & 25 & 6 & \cellcolor[HTML]{FFFFFF} 0 \\ \hline
\end{tabular}
$$

**Исключение ребра** $(2,8): d_{28}=M$.

$$
\begin{tabular}{|l|l|l|l|l|>{\columncolor[HTML]{98FB98}}l|}
\hline
    \textbf{i j} & \textbf{3} & \textbf{6} & \textbf{8} & \textbf{10} & \textbf{$d_i$} \\ \hline
    \textbf{1} & 0 & M & 26 & 0 & 0 \\ \hline
    \textbf{2} & M & 44 & M & 6 & 6 \\ \hline
    \textbf{5} & 10 & 0 & 25 & M & 0 \\ \hline
    \textbf{8} & 2 & 0 & M & 56 & 0 \\ \hline
    \rowcolor[HTML]{E0FFFF}
    \textbf{$d_j$} & 0 & 0 & 25 & 0 & \cellcolor[HTML]{FFFFFF} 31 \\ \hline
\end{tabular}
$$

$H(2^*,8^*) = 96 + 31 = 127$  
**Включение ребра** $(2,8): d_{82}=M$.

$$
\begin{tabular}{|l|l|l|l|>{\columncolor[HTML]{98FB98}}l|}
\hline
    \textbf{i j} & \textbf{3} & \textbf{6} & \textbf{10} & \textbf{$d_i$} \\ \hline
    \textbf{1} & 0 & M & 0 & 0 \\ \hline
    \textbf{5} & 10 & 0 & M & 0 \\ \hline
    \textbf{8} & 2 & 0 & 56 & 0 \\ \hline
    \rowcolor[HTML]{E0FFFF}
    \textbf{$d_j$} & 0 & 0 & 0 & \cellcolor[HTML]{FFFFFF} 0 \\ \hline
\end{tabular}
$$

$\sum d_i + \sum d_j = 0 + 0 = 0$  
$H(2,8) = 96 + 0 = 96 \leq 127$  
Запрещаем переходы: $(8,3), (5,10), (8,7), (5,9)$,  
Ребро $(2,8)$ включаем в маршрут с новой границей $H=96$.

### Шаг 8

**Определяем ребро ветвления.**

$$
\begin{aligned}
&d(1,3) = 0 + 10 = 10 \quad
&d(1,10) = 0 + 56 = 56 \\
&d(5,6) = 10 + 0 = 10 \quad
&d(8,6) = 56 + 0 = 56
\end{aligned}
$$

$\max: d(1,10) = 56$

$$
\begin{tabular}{|l|l|l|l|>{\columncolor[HTML]{98FB98}}l|}
\hline
    \textbf{i j} & \textbf{3} & \textbf{6} & \textbf{10} & \textbf{$d_i$} \\ \hline
    \textbf{1} & 0(10) & M & 0(56) & 0 \\ \hline
    \textbf{5} & 10 & 0(10) & M & 10 \\ \hline
    \textbf{8} & M & 0(56) & 56 & 56 \\ \hline
    \rowcolor[HTML]{E0FFFF}
    \textbf{$d_j$} & 10 & 0 & 56 & \cellcolor[HTML]{FFFFFF} 0 \\ \hline
\end{tabular}
$$

**Исключение ребра** $(1,10): d_{110}=M$.

$$
\begin{tabular}{|l|l|l|l|>{\columncolor[HTML]{98FB98}}l|}
\hline
    \textbf{i j} & \textbf{3} & \textbf{6} & \textbf{10} & \textbf{$d_i$} \\ \hline
    \textbf{1} & 0 & M & M & 0 \\ \hline
    \textbf{5} & 10 & 0 & M & 0 \\ \hline
    \textbf{8} & M & 0 & 56 & 0 \\ \hline
    \rowcolor[HTML]{E0FFFF}
    \textbf{$d_j$} & 0 & 0 & 56 & \cellcolor[HTML]{FFFFFF} 56 \\ \hline
\end{tabular}
$$

$H(1^*,10^*) = 96 + 56 = 152$  
**Включение ребра** $(1,10): d_{101}=M$.

$$
\begin{tabular}{|l|l|l|>{\columncolor[HTML]{98FB98}}l|}
\hline
    \textbf{i j} & \textbf{3} & \textbf{6} & \textbf{$d_i$} \\ \hline
    \textbf{5} & 10 & 0 & 0 \\ \hline
    \textbf{8} & M & 0 & 0 \\ \hline
    \rowcolor[HTML]{E0FFFF}
    \textbf{$d_j$} & 10 & 0 & \cellcolor[HTML]{FFFFFF} 10 \\ \hline
\end{tabular}
$$

$\sum d_i + \sum d_j = 0 + 10 = 10$  
$H(1,10) = 96 + 10 = 106 \leq 152$  
Ребро $(1,10)$ включаем в маршрут с новой границей $H=106$.  
В соответствии с этой матрицей включаем в гамильтонов маршрут ребра $(5,3)$ и $(8,6)$.  
В результате по дереву ветвлений гамильтонов цикл образуют ребра:  
$(3,7), (7,2), (2,8), (8,6), (6,1), (1,10), (10,9), (9,4), (4,5), (5,3)$  
Длина маршрута равна $F(M_k) = 106$.

## Программное решение

```python
import random


class TSPSolver:
    def __init__(self, matrix):
        self.n = len(matrix)
        self.graph = matrix
        self.best_cost = float('inf')
        self.best_path = []

    def solve(self):
        visited = [False] * self.n
        visited[0] = True
        self._dfs(0, visited, 0, [0])
        return self.best_cost, self.best_path

    def _is_complete(self, path):
        return len(path) == self.n

    def _update_solution(self, node, cost, path):
        total_cost = cost + self.graph[node][0]
        if total_cost < self.best_cost:
            self.best_cost = total_cost
            self.best_path = path + [0]

    def _compute_cost(self, node, next_node, visited, cost):
        if visited[next_node] or self.graph[node][next_node] <= 0:
            return None
        next_cost = cost + self.graph[node][next_node]
        if next_cost >= self.best_cost:
            return None
        return next_cost

    def _dfs(self, curr_node, visited, curr_cost, path):
        if self._is_complete(path):
            self._update_solution(curr_node, curr_cost, path)
            return

        for i in range(self.n):
            next_cost = self._compute_cost(curr_node, i, visited, curr_cost)
            if next_cost is not None:
                visited[i] = True
                self._dfs(i, visited, next_cost, path + [i])
                visited[i] = False


if __name__ == '__main__':
    matrix = [
        [random.randint(1, 99) if i != j else 0 for j in range(10)]
        for i in range(10)
    ]
    list(map(lambda x: print(*x, sep='\t'), matrix))
    cost, path = TSPSolver(matrix).solve()
    print("Cost:", cost)
    print("Path:", " -> ".join(map(str, path)))
```

### Вывод

```plaintext
0	71	9	65	94	68	76	30	39	4
43	0	82	50	31	59	17	15	61	21
79	48	0	65	70	68	6	73	67	29
50	90	6	0	2	45	67	9	47	76
36	76	20	87	0	5	72	30	17	26
17	6	33	89	23	0	67	20	85	81
97	8	97	54	58	60	0	47	18	72
28	83	21	34	65	14	98	0	43	70
67	42	83	8	10	53	52	63	0	28
39	28	79	98	59	29	7	53	12	0
Cost: 106
Path: 0 -> 9 -> 8 -> 3 -> 4 -> 2 -> 6 -> 1 -> 7 -> 5 -> 0
```

$$
$$
