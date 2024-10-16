# Задание №2

Найти решение задачи линейного программирования симплекс – методом (для "а, с" на max, для "в" на max и min)

## (a)

$$
\begin{aligned}
&F = 2x_1 + x_2 \rightarrow \max(\min)\\
&\begin{cases}
-x_1+x_2\leq2\\
4x_1 - x_2\leq8
\end{cases}
x_1 \geq 0, \quad x_2 \geq 0 \\
\end{aligned}
$$

Записываем в канонической форме:

$$
\begin{aligned}
&\begin{cases}
-x_1+x_2+x_3=2\\
4x_1 - x_2+x_4=8
\end{cases}
x_i \geq 0, \quad i=1..4\\
\end{aligned}
$$

$$
\begin{aligned}
&A_1 = \begin{pmatrix} -1 \\ 4 \end{pmatrix} \quad
A_2 = \begin{pmatrix} 1 \\ -1 \end{pmatrix} \quad
A_3 = \begin{pmatrix} 1 \\ 0 \end{pmatrix} \quad
A_4 = \begin{pmatrix} 0 \\ 1 \end{pmatrix} \quad\\
&\text{Начальный базис:} (A_3, A_4)
\end{aligned}
$$

Полагая, что свободные члены равны 0, получим первый опорный план:

$$
\begin{aligned}
&X_0 = \begin{pmatrix} 0 \\ 0 \\ 2 \\ 8 \end{pmatrix}\\
\end{aligned}
$$

Построим симплекс таблицу:

$$
\begin{tabular}{|c|l|l|l|l|l|}
\hline
Базис & $B$ & $x_1$ & $x_2$ & $x_3$ & $x_4$ \\ \hline
$x_3$ & 2 & -1 & 1 & 1 & 0 \\ \hline
$x_4$ & 8 & 4 & -1 & 0 & 1 \\ \hline
\multicolumn{1}{|l|}{$F(X_0)$} & 0 & -2 & -1 & 0 & 0 \\ \hline
\end{tabular}
$$

**Итерация 0:**  
Текущий опорный план неоптимален, так как в индексной строке находятся отрицательные коэффициенты.  
В качестве ведущего выберем столбец, соответствующий переменной $x_1$, так как это наибольший коэффициент по модулю.  
В качестве ведущей строки выберем строку, в которой отношение свободного члена к коэффициенту при ведущем столбце минимально.  
В данном случае это строка $x_4$.  
Построим новую симплекс таблицу:

$$
\begin{tabular}{|c|l|l|l|l|l|}
\hline
Базис & $B$ & $x_1$ & $x_2$ & $x_3$ & $x_4$ \\ \hline
$x_3$ & 4 & 0 & $\frac{3}{4}$ & 1 & $\frac{1}{4}$ \\ \hline
$x_1$ & 2 & 1 & -$\frac{1}{4}$ & 0 & $\frac{1}{4}$ \\ \hline
\multicolumn{1}{|l|}{$F(X_1)$} & 4 & 0 & $-\frac{3}{2}$ & 0 & $\frac{1}{2}$ \\ \hline
\end{tabular}
$$

**Итерация 1:**  
Текущий опорный план неоптимален, так как в индексной строке находятся отрицательные коэффициенты.  
В качестве ведущего выберем столбец, соответствующий переменной $x_2$, так как это наибольший коэффициент по модулю.  
В качестве ведущей строки выберем строку, в которой отношение свободного члена к коэффициенту при ведущем столбце минимально.  
В данном случае это строка $x_3$.  
Построим новую симплекс таблицу:

$$
\begin{tabular}{|c|l|l|l|l|l|}
\hline
Базис & $B$ & $x_1$ & $x_2$ & $x_3$ & $x_4$ \\ \hline
$x_2$ & $\frac{16}{3}$ & 0 & 1 & $\frac{4}{3}$ & $\frac{1}{3}$ \\ \hline
$x_1$ & $\frac{10}{3}$ & 1 & 0 & $\frac{1}{3}$ & $\frac{1}{3}$ \\ \hline
\multicolumn{1}{|l|}{$F(X_2)$} & 12 & 0 & 0 & 2 & 1 \\ \hline
\end{tabular}
$$

$$
\begin{aligned}
&\begin{cases}
x_1=\frac{10}{3}\\
x_2=\frac{16}{3}
\end{cases}
F(x_1, x_2)=2\cdot\frac{10}{3}+\frac{16}{3}=12 - \max\\
\end{aligned}
$$

## (b)

$$
\begin{aligned}
&F = 2x_1 + 7x_2 \rightarrow \max(\min)\\
&\begin{cases}
2x_1+x_2\geq6\\
3x_1-x_2\leq9
\end{cases}
x_1\geq0,\quad x_2\geq0
\end{aligned}
$$

Записываем в канонической форме:

$$
\begin{aligned}
&\begin{cases}
2x_1+x_2-x_3=6\\
3x_1 - x_2+x_4=9
\end{cases}
x_i \geq 0, \quad i=1..4
\end{aligned}
$$

$$
\begin{aligned}
&A_1 = \begin{pmatrix} 2 \\ 3 \end{pmatrix} \quad
A_2 = \begin{pmatrix} 1 \\ -1 \end{pmatrix} \quad
A_3 = \begin{pmatrix} -1 \\ 0 \end{pmatrix} \quad
A_4 = \begin{pmatrix} 0 \\ 1 \end{pmatrix} \quad\\
&\text{Начальный базис:} (A_3, A_4)
\end{aligned}
$$

## (c)

$$
\begin{aligned}
&F = -2x_1+5x_2 \rightarrow \max(\min)\\
&\begin{cases}
2x_1+x_2 \geq 4 \\
x_1 - 4x_2 \geq 8
\end{cases}
x_1 \geq 0, \quad x_2 \geq 0
\end{aligned}
$$

Записываем в канонической форме:

$$
\begin{aligned}
&\begin{cases}
2x_1+x_2-x_3=4\\
x_1 - 4x_2-x_4=8
\end{cases}
x_i \geq 0, \quad i=1..4
\end{aligned}
$$

$$
\begin{aligned}
&A_1 = \begin{pmatrix} 2 \\ 1 \end{pmatrix} \quad
A_2 = \begin{pmatrix} 1 \\ -4 \end{pmatrix} \quad
A_3 = \begin{pmatrix} -1 \\ 0 \end{pmatrix} \quad
A_4 = \begin{pmatrix} 0 \\ -1 \end{pmatrix} \quad\\
&\text{Начальный базис:} (A_3, A_4)
\end{aligned}
$$
