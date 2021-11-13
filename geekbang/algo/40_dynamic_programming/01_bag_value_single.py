# 0-1背包进一步考虑最大价值，使用1维数组解决
def check_weight(items: list, item_values: list, max_weight: int) -> int:
    item_count = len(items)
    memo = [-1] * (max_weight + 1)
    memo[0] = 0
    memo[items[0]] = item_values[0]

    for i in range(1, item_count):

        # 这里处理了下，因为最终不可以超过max_weight ，只考察 max_weight - items[i] 之前的数据才有意义
        # 这里跟之前的一样，需要从大到小处理
        for j in range(max_weight - items[i], -1, -1):
            if memo[j] > 0:
                new_value = memo[j] + item_values[i]
                if memo[j + items[i]] < new_value:
                    memo[j + items[i]] = new_value
    max_value = 0
    for i in range(0, max_weight + 1):
        if memo[i] > max_value:
            max_value = memo[i]

    return max_value


if __name__ == '__main__':
    # [weight, ...]
    items_info = [2, 2, 4, 6, 3]
    items_values = [9, 2, 4, 6, 3]
    capacity = 9
    print(check_weight(items_info, items_values, capacity))
