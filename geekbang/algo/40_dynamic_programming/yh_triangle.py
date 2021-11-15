# 杨辉三角，求解最短路径，核心是需要找到动态规划转移方程：S[i][j] = min(S[i-1][j],S[i-1][j-1]) + a[i][j]。

from typing import List


# Layer_nums = List[int]


def yh_triangle(nums: List[List[int]]) -> int:
    layer_num: int = len(nums)
    memo = [[0] * layer_num for i in range(layer_num)]
    memo[0][0] = nums[0][0]

    for i in range(1, layer_num):
        for j in range(i + 1):
            if j == 0:
                memo[i][j] = memo[i - 1][j] + nums[i][j]
            elif j == i:
                memo[i][j] = memo[i - 1][j - 1] + nums[i][j]
            else:
                memo[i][j] = min(memo[i - 1][j - 1], memo[i - 1][j]) + nums[i][j]

    return min(memo[layer_num - 1])


if __name__ == '__main__':
    nums = [[3], [2, 6], [5, 4, 2], [6, 0, 3, 2]]
    print(yh_triangle(nums))
