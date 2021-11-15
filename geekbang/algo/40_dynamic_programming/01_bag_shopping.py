# 双十一购物问题：假设满200 -50 的优惠，怎样选择大于等于 200 并且最接近 200 的组合是哪一个


def check_weight(item_values: list, capacity: int) -> int:
    # 最大值设置为满减条件的2倍，不然太大了就失去薅羊毛的意义
    max_value = capacity * 2

    item_count = len(item_values)
    memo = [[-1] * (max_value + 1) for i in range(item_count)]
    memo[0][0] = 1
    memo[0][item_values[0]] = 1

    for i in range(1, item_count):
        # 不把第i个物品放入的时候，相当于直接继承上一层的数据
        for j in range(max_value + 1):
            if memo[i - 1][j] == 1:
                memo[i][j] = 1

        # 将第i个物品放入的时候，可能存在的情况，这里需要+1，因为rang 不包括最后一位
        # 这里处理了下，因为最终不可以超过max_weight ，只考察 max_weight - items[i] 之前的数据才有意义
        for j in range(max_value - item_values[i] + 1):
            if memo[i - 1][j] == 1:
                memo[i][j + item_values[i]] = 1

    worth_value = 0
    for i in range(capacity, max_value + 1):
        if memo[item_count - 1][i] == 1:
            worth_value = i
            break
    # 没有可行解
    if worth_value == 0:
        return 0

    final_value = worth_value

    print("worth value:", worth_value)

    for i in range(item_count - 1, 0, -1):
        # 这里倒推回去，如果上一层 worth_value - item_values[i] 是否满足，就说明当前层商品应该购买
        if worth_value - item_values[i] >= 0 and memo[i - 1][worth_value - item_values[i]] == 1:
            print(item_values[i], " ")
            worth_value -= item_values[i]
        # 如果当前层没有放，worth_value就不用减掉货值

    # 上面循环只会进行到第二层，还需要判断下第一层的商品是否放入
    if worth_value != 0:
        print(item_values[0], " ")

    return final_value


if __name__ == '__main__':
    # 每件商品的价格
    items_values = [9, 2, 4, 6, 3, 7, 8, 5]
    # 满减条件
    capacity = 20
    print("final value:", check_weight(items_values, capacity))
