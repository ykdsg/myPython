# 假设我们有一个 n 乘以 n 的矩阵 w[n][n]。矩阵存储的都是正整数。棋子起始位置在左上角,终止位置在右下角。我们将棋子从左上角移动到右下角。
# 每次只能向右或者向下移动一位。从左上角到右下角,会有很多不同的路径可以走。我们把每条路径经过的数字加起来看作路径的长度。
# 那从左上角移动到右下角的最短路径长度是多少呢?

# 这里用了书里面的状态转移表法
from typing import List


def min_dist(weights: List[List[int]]) -> int:
    # 2维数组的行数和列数
    row_num, column_num = len(weights), len(weights[0]),
    memo = [[-1] * column_num for i in range(row_num)]
    memo[0][0] = weights[0][0]

    # 初始化第0列
    for i in range(1, row_num):
        memo[i][0] = memo[i - 1][0] + weights[i][0]

    # 初始化第0行
    for i in range(1, column_num):
        memo[0][i] = memo[0][i - 1] + weights[0][i]

    # 计算其他格子的最小路径值
    for row in range(1, row_num):
        for column in range(1, column_num):
            memo[row][column] = min(memo[row - 1][column], memo[row][column - 1]) + weights[row][column]

    return memo[row_num - 1][column_num - 1]


if __name__ == "__main__":
    weights = [[1, 3, 5, 9], [2, 1, 3, 4], [5, 2, 6, 7], [6, 8, 4, 3]]
    print(min_dist(weights))
