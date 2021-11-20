# 最短编辑距离


def levenshtein_dp(str1: str, str2: str) -> int:
    str1_len, str2_len = len(str1), len(str2)
    memo = [[0] * str2_len for _ in range(str1_len)]

    for i in range(str2_len):
        if str1[0] == str2[i]:
            memo[0][i] = i
        elif i != 0:
            memo[0][i] = memo[0][i - 1] + 1
        else:
            memo[0][i] = 1

    for i in range(str1_len):
        if str2[0] == str1[i]:
            memo[i][0] = i
        elif i != 0:
            memo[i][0] = memo[i - 1][0] + 1
        else:
            memo[i][0] = 1

    for row_index in range(1, str1_len):
        for column_index in range(1, str2_len):
            if str1[row_index] == str2[column_index]:
                current_temp = memo[row_index - 1][column_index - 1]
            else:
                current_temp = memo[row_index - 1][column_index - 1] + 1

            memo[row_index][column_index] = min(memo[row_index - 1][column_index] + 1,
                                                memo[row_index][column_index - 1] + 1, current_temp)

    return memo[-1][-1]


def common_substring_dp(str1: str, str2: str) -> int:
    str1_len, str2_len = len(str1), len(str2)
    memo = [[0] * str2_len for _ in range(str1_len)]
    for str1_index in range(1, str1_len):
        for str2_index in range(1, str2_len):
            current_temp = 0
            # 如果当前字符相等，那么最长距离可能是上一位
            if str1[str1_index] == str2[str2_index]:
                current_temp = 1 + memo[str1_index - 1][str2_index - 1]

            # 最终来看最长的距离是哪个
            memo[str1_index][str2_index] = max(memo[str1_index - 1][str2_index], memo[str1_index][str2_index - 1],
                                               current_temp)

    return memo[-1][-1]


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
