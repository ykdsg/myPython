from typing import List


def check_weight(items_info: List[int], items_values: List[int], capacity: int):
    item_size = len(items_info)
    # 每一行代表这个物品放进去之后的情况，每一列表示当前重量，值代表当前组合的货物总值
    memo = [[0] * (capacity + 1) for _ in range(item_size)]
    memo[0][0] = 0
    memo[0][items_info[0]] = items_values[0]

    for row_index in range(1, item_size):
        row_weight = items_info[row_index]
        row_value = items_values[row_index]
        if row_weight <= capacity:
            memo[row_index][row_weight] = max(memo[row_index - 1][row_weight], row_value)

        for column_index in range(capacity + 1):
            if memo[row_index - 1][column_index] > 0:
                memo[row_index][column_index] = memo[row_index - 1][column_index]
                weight = column_index + row_weight
                # 如果超重就没必要放了
                if weight <= capacity:
                    memo[row_index][weight] = max(memo[row_index][weight],
                                                  memo[row_index - 1][column_index] + row_value)

        for column_index in range(capacity, -1, -1):
            if memo[item_size - 1][column_index] > 0:
                return memo[item_size - 1][column_index]


if __name__ == '__main__':
    # [weight, ...]
    items_info = [2, 2, 4, 6, 3]
    items_values = [9, 2, 4, 6, 3]
    capacity = 9
    print(check_weight(items_info, items_values, capacity))
