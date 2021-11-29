def levenshtein_dp(str1: str, str2: str):
    str1_len, str2_len = len(str1), len(str2),
    memo = [[0] * str2_len for _ in range(str1_len)]
    memo[0][0] = 0 if str1[0] == str2[0] else 1
    for column_index in range(1, str2_len):
        memo[0][column_index] = memo[0][column_index - 1] if str1[0] == str2[column_index] \
            else memo[0][column_index - 1] + 1

    for row_index in range(1, str1_len):
        memo[row_index][0] = memo[row_index - 1][0] if str2[0] == str1[row_index] else memo[row_index - 1][0] + 1

    for row_index in range(1, str1_len):
        for column_index in range(1, str2_len):
            # 当前字母是否相等
            current_step = 0 if str1[row_index] == str2[column_index] else 1
            # 相当于左边、上边、斜上角的最小值，加上当前步的数值
            memo[row_index][column_index] = min(memo[row_index - 1][column_index], memo[row_index][column_index - 1],
                                                memo[row_index - 1][column_index - 1]) + current_step
    return memo[-1][-1]


if __name__ == "__main__":
    s = "mam"
    t = "mbm"
    print(levenshtein_dp(s, t))

    s = "maa"
    t = "mba"
    print(levenshtein_dp(s, t))

    s = "ama"
    t = "mab"
    print(levenshtein_dp(s, t))
