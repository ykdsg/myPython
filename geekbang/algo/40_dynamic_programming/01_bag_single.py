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
        # 这里跟2维数组的时候不太一样，j需要从大到小，如果从小到大，会存在当前的决策影响后面的决策。
        # 比如j=0 ，i=2，items[2]=3, memo[0]==1, 那么memo[0+3]=1 , 当后面j=3 的时候，会发现memo[3]==1 ,但这个结果并不是由上一层决策得来的。而是由本层的前几次决策得来的，并不能用在本层的决策里面。所以这里从大到小的话，就可以规避本层决策相互之间的影响。
        for j in range(max_weight - items[i], -1, -1):
            if memo[j] == 1:
                memo[j + items[i]] = 1

    for i in range(max_weight, -1, -1):
        if memo[i] == 1:
            return i

    return 0


if __name__ == '__main__':
    # [weight, ...]
    items_info = [2, 2, 4, 6, 3]
    max_weight = 9
    print(check_weight(items_info, max_weight))
