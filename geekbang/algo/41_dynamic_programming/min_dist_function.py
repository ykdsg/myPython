# 这里使用状态转移方程法
from typing import List


def min_dist(row: int, column: int, memo: List[List[int]], weights: List[List[int]]) -> int:
    if row == 0 and column == 0:
        return weights[0][0]
    if memo[row][column] > 0:
        return memo[row][column]

    # 分别计算左边的值和上一行的值
    min_left = float("inf") if column < 1 else min_dist(row, column - 1, memo, weights)
    min_up = float("inf") if row < 1 else min_dist(row - 1, column, memo, weights)

    memo[row][column] = min(min_left, min_up) + weights[row][column]
    return memo[row][column]


if __name__ == "__main__":
    weights = [[1, 3, 5, 9], [2, 1, 3, 4], [5, 2, 6, 7], [6, 8, 4, 3]]
    row_num, column_num = len(weights), len(weights[0])
    memo = [[-1] * column_num for i in range(row_num)]

    print(min_dist(row_num - 1, column_num - 1, memo, weights))
