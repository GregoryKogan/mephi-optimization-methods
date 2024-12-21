def backpack(capacity, weights, values):
    """Solve the unbounded knapsack problem using dynamic programming."""
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        row_changed = False
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]
            if dp[i][w] != dp[i - 1][w] and not row_changed:
                row_changed = True
                print_dp_table(dp, i, w)

        print_dp_table(dp, i, capacity)

    print(f"Оптимальное значение: {dp[n][capacity]}  ")
    trace_optimal_solution(dp, weights, values, capacity)


def trace_optimal_solution(dp, weights, values, capacity):
    """Backtrack to find which items were chosen in the optimal solution."""
    n = len(weights)
    w = capacity
    selected = []
    i = n
    while i > 0:
        if (
            w >= weights[i - 1]
            and dp[i][w] == dp[i][w - weights[i - 1]] + values[i - 1]
        ):
            selected.append(i)
            w -= weights[i - 1]
        else:
            i -= 1
    print("Выбранные предметы:", selected)


def print_dp_table(dp, i, w):
    """Print current state of the DP table."""
    print(f"Таблица DP после обработки предмета {i} при вместимости {w}:\n")
    print("$$")
    columns = [
        ">{\\columncolor[HTML]{98FB98}}l" if j == w + 1 else "l"
        for j in range(len(dp[0]) + 1)
    ]
    print("\\begin{tabular}{|" + "|".join(columns) + "|}")

    print("\\hline")
    print(
        "\t"
        + "\\diagbox{i}{w} & "
        + " & ".join(str(i) for i in range(len(dp[0])))
        + " \\\\ \\hline"
    )
    for ind, row in enumerate(dp):
        if ind == i:
            print("\\rowcolor[HTML]{E0FFFF}")
        print(f"\t{ind} & ", end="")
        values = [
            (
                "\\cellcolor[HTML]{BDFDCC}" + str(cell)
                if cell == dp[i][w] and i == ind
                else str(cell)
            )
            for cell in row
        ]
        print(" & ".join(values), end="")
        print(" \\\\ \\hline")
    print("\\end{tabular}")
    print("$$")
    print()


if __name__ == "__main__":
    capacity = 20
    weights = [2, 5, 8, 3, 7, 4]
    values = [3, 8, 6, 7, 10, 5]
    backpack(capacity, weights, values)
