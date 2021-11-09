max_weight = 0
item_list = None


def check_weight(current_index: int, current_weight: int, items: list, count: int, package_weight: int):
    if current_weight == package_weight or current_index >= count:
        global max_weight
        if current_weight >= max_weight:
            max_weight = current_weight
            print("temp max weight:", max_weight)
            print("item list:", item_list)

        return

    # 这里需要数组配合下标的方式，这样在递归的时候，能够保留之前的数据栈
    # 当前物品不放的情况：
    item_list[current_index] = 0
    check_weight(current_index + 1, current_weight, items, count, package_weight)

    # 如果条件允许，当前物品放入的情况
    next_weight = current_weight + items[current_index]
    if next_weight <= package_weight:
        item_list[current_index] = 1
        check_weight(current_index + 1, next_weight, items, count, package_weight)


if __name__ == '__main__':
    items = [4, 5, 8, 2, 3, 6, 7, 9]
    package_weight = 20

    print('--- list ---')
    print(items)

    item_list = [0] * len(items)
    check_weight(0, 0, items, len(items), package_weight)
    print('max weight:', max_weight)
