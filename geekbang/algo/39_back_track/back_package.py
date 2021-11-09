# 背包问题

max_weight = 0
item_list = None


# cw:物品重量和，
def check_weight(current_index: int, current_weight: int, items: list, item_count: int, package_weight: int):
    # 退出条件：
    # current_weight == package_weight 表示装满了
    # current_index == item_count 表示考察完所有物品
    if current_weight == package_weight or current_index == item_count:
        global max_weight
        if current_weight > max_weight:
            max_weight = current_weight
            print('current max weight:', max_weight)
            print('composition:', item_list)
        return

    # 对于一个物品而言，只有两种情况，不装入背包和装入背包两种情况。对应的就是f(i+1, cw, items, n, w)和f(i+1, cw + items[i], items, n, w)两个函数。
    # 不装这块的时候，考察后续的情况
    item_list[current_index] = 0
    check_weight(current_index + 1, current_weight, items, item_count, package_weight)

    # 如果装上这块还没超出重量，继续考察下一块
    if current_weight + items[current_index] <= package_weight:
        item_list[current_index] = 1
        check_weight(current_index + 1, current_weight + items[current_index], items, item_count, package_weight)


if __name__ == '__main__':
    items = [4, 5, 8]
    print('--- list ---')
    print(items)

    item_list = [0] * len(items)
    check_weight(0, 0, items, len(items), 10)
    print('max weight:', max_weight)
