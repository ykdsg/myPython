# 0-1背包进一步考虑最大价值
def check_weight(items: list, item_values: list, max_weight: int) -> int:
    item_count = len(items)
    memo = [[-1] * (max_weight + 1) for i in range(item_count)]
    memo[0][0] = 0
    memo[0][items[0]] = item_values[0]

    for i in range(1, item_count):
        # 不把第i个物品放入的时候，相当于直接继承上一层的数据
        for j in range(max_weight + 1):
            if memo[i - 1][j] != 0 and memo[i - 1][j] > memo[i][j]:
                memo[i][j] = memo[i - 1][j]

        # 将第i个物品放入的时候，可能存在的情况，这里需要+1，因为rang 不包括最后一位
        # 这里处理了下，因为最终不可以超过max_weight ，只考察 max_weight - items[i] 之前的数据才有意义
        for j in range(max_weight - items[i] + 1):
            if memo[i - 1][j] != 0:
                new_value = memo[i - 1][j] + item_values[i]
                if memo[i][j + items[i]] < new_value:
                    memo[i][j + items[i]] = new_value
    max_value = 0
    for i in range(0, max_weight + 1):
        if memo[item_count - 1][i] > max_value:
            max_value = memo[item_count - 1][i]

    return max_value


if __name__ == '__main__':
    # [weight, ...]
    items_info = [2, 2, 4, 6, 3]
    items_values = [9, 2, 4, 6, 3]
    capacity = 9
    print(check_weight(items_info, items_values, capacity))
