def levenshtein_dp(s1: str, s2: str) -> int:
    row_len = len(s1)
    column_len = len(s2)

    memo = [[99999] * column_len for _ in range(row_len)]
    memo[0][0] = 0 if s1[0] == s2[0] else 1
    # 初始化第一行
    for column_index in range(1, column_len):
        # 这行判断是关键，之前一直卡在这里
        if s1[0] == s2[column_index]:
            memo[0][column_index] = column_index
        else:
            memo[0][column_index] = memo[0][column_index - 1] + 1

    # 初始化第一列
    for row_index in range(1, row_len):
        if s2[0] == s1[row_index]:
            memo[row_index][0] = row_index
        else:
            memo[row_index][0] = memo[row_index - 1][0] + 1

    for row_index in range(1, row_len):
        for column_index in range(1, column_len):
            # 分几种情况，如果从[row_index-1,column_index - 1] 转化过来，那就需要判断 当前值是否相等，相等就不需要+1
            #  如果从[row_index,column_index - 1] 和 [row_index-1,column_index] 基础上转化过来，就需要+1，不管是否相等
            if s1[row_index] == s2[column_index]:
                current_step = memo[row_index - 1][column_index - 1]
            else:
                current_step = memo[row_index - 1][column_index - 1] + 1

            memo[row_index][column_index] = min(current_step,
                                                memo[row_index][column_index - 1] + 1,
                                                memo[row_index - 1][column_index - 1] + 1)
    return memo[row_len - 1][column_len - 1]


def common_substring_dp(s1: str, s2: str):
    row_len = len(s1)
    column_len = len(s2)

    memo = [[0] * column_len for _ in range(row_len)]
    memo[0][0] = 1 if s1[0] == s2[0] else 0
    # 初始化第一行
    for column_index in range(1, column_len):
        if s1[0] == s2[column_index]:
            memo[0][column_index] = 1
        else:
            memo[0][column_index] = memo[0][column_index - 1]

    # 初始化第一列
    for row_index in range(1, row_len):
        if s2[0] == s1[row_index]:
            memo[row_index][0] = 1
        else:
            memo[row_index][0] = memo[row_index - 1][0]

    for row_index in range(1, row_len):
        for column_index in range(1, column_len):
            if s1[row_index] == s2[column_index]:
                current_step = memo[row_index - 1][column_index - 1] + 1
            else:
                current_step = memo[row_index - 1][column_index - 1]

            memo[row_index][column_index] = max(current_step, memo[row_index - 1][column_index],
                                                memo[row_index][column_index - 1])

    return memo[row_len - 1][column_len - 1]


if __name__ == "__main__":
    s = "mitcmu"
    t = "mtacnu"

    print(levenshtein_dp(s, t))
    print(common_substring_dp(s, t))

    s = "kitten"
    t = "sitting"

    print(levenshtein_dp(s, t))
    print(common_substring_dp(s, t))

    s = "flaw"
    t = "lawn"

    print(levenshtein_dp(s, t))
    print(common_substring_dp(s, t))
