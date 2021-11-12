def check_weight(items: list, max_weight: int) -> int:
    """
    固定容量的背包，计算能装进背包的物品组合的最大重量

    :param items: 物品重量
    :param max_weight: 背包可承载最大重量
    :return:
    """
    item_count = len(items)
    memo = [[-1] * (max_weight + 1) for i in range(item_count)]
    # 第一行数据需要特殊处理
    memo[0][0] = 1
    memo[0][items[0]] = 1

    for i in range(1, item_count):
        # 不把第i个物品放入的时候，相当于直接继承上一层的数据
        for j in range(max_weight + 1):
            if memo[i - 1][j] == 1:
                memo[i][j] = 1
        # 讲第i个物品放入的时候，可能存在的情况
        for j in range(max_weight - items[i] + 1):
            if memo[i - 1][j] == 1:
                memo[i][j + items[i]] = 1

    for i in range(max_weight, -1, -1):
        if memo[item_count - 1][i] == 1:
            return i

    return 0


if __name__ == '__main__':
    # [weight, ...]
    items_info = [2, 2, 4, 6, 3]
    capacity = 9
    print(check_weight(items_info, capacity))
