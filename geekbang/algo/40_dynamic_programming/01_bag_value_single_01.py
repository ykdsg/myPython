from typing import List


# 0-1背包进一步考虑最大价值，使用1维数组解决
def check_weight(items_info: List[int], items_values, capacity):
    pass


if __name__ == '__main__':
    # [weight, ...]
    items_info = [2, 2, 4, 6, 3]
    items_values = [9, 2, 4, 6, 3]
    capacity = 9
    print(check_weight(items_info, items_values, capacity))
