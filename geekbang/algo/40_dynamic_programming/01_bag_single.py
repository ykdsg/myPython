# 使用1维数组来实现动态规划


def check_weight(items: list, max_weight: int) -> int:
    """
    固定容量的背包，计算能装进背包的物品组合的最大重量

    :param items: 物品重量
    :param max_weight: 背包可承载最大重量
    :return:
    """
    item_count = len(items)
    # max_weight + 1，因为最开始前面有个0，0~max_weight，实际上是max_weight + 1个
    memo = [-1] * (max_weight + 1)
    # 第一行数据需要特殊处理
    memo[0] = 1
    memo[items[0]] = 1

    for i in range(1, item_count):
        # 这里就不用考虑第i个物品不放的情况，因为1维的数组相当于已经继承了。
        # 将第i个物品放入的时候，可能存在的情况，这里需要+1，因为rang 不包括最后一位
        # 这里处理了下，因为最终不可以超过max_weight ，只考察 max_weight - items[i] 之前的数据才有意义
        for j in range(max_weight - items[i] + 1):
            if memo[j] == 1:
                memo[j + items[i]] = 1

    for i in range(max_weight, -1, -1):
        if memo[i] == 1:
            return i

    return 0


if __name__ == '__main__':
    # [weight, ...]
    items_info = [2, 2, 4, 6, 3]
    capacity = 9
    print(check_weight(items_info, capacity))
