from typing import List


def check_weight(items_info: List[int], capacity: int) -> int:
    row_num = len(items_info)
    item_result = [[-1] * (capacity + 1) for _ in range(row_num)]
    item_result[0][0] = 0
    item_result[0][items_info[0]] = 1

    for row_index in range(1, row_num):
        for column_index in range(capacity + 1):
            if item_result[row_index - 1][column_index] == 1:
                # 当前这块不放的情况
                item_result[row_index][column_index] = 1

                # 当前这块放入的情况
                current_capacity = column_index + items_info[row_index]
                if current_capacity <= capacity:
                    item_result[row_index][current_capacity] = 1

    for column_index in range(capacity, -1, -1):
        if item_result[-1][column_index] == 1:
            return column_index


# 固定容量的背包，计算能装进背包的物品组合的最大重量，有个前提背景是单个物体重量不会超过capacity
if __name__ == '__main__':
    # [weight, ...]
    items_info = [2, 2, 4, 6, 3]
    capacity = 9
    print(check_weight(items_info, capacity))
