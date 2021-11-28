from typing import List


def check_weight(items_info: List[int], items_values: List[int], capacity: int) -> int:
    item_amount = len(items_info)
    # item_result 放的是累计的货值
    item_result = [[-1] * (capacity + 1) for _ in range(item_amount)]
    item_result[0][0] = 0
    item_result[0][items_info[0]] = items_values[0]

    for row_index in range(1, item_amount):
        for column_index in range(0, capacity + 1):
            pre_row_result = item_result[row_index - 1][column_index]
            if pre_row_result > 0:
                item_result[row_index][column_index] = pre_row_result
                # 如果总量没有超出
                current_capacity = column_index + items_info[row_index]
                if current_capacity <= capacity:
                    item_result[row_index][current_capacity] = pre_row_result + items_values[row_index]

    for column_index in range(capacity, -1, -1):
        if item_result[-1][column_index] > 0:
            return item_result[-1][column_index]


if __name__ == '__main__':
    # [weight, ...]
    items_info = [2, 2, 4, 6, 3]
    items_values = [9, 2, 4, 6, 3]
    capacity = 9
    print(check_weight(items_info, items_values, capacity))
