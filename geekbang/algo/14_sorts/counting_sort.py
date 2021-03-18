import itertools
from typing import List


# 计数排序
def counting_sort(a: List[int]):
    if len(a) <= 1: return

    counts = [0] * (max(a) + 1)
    for num in a:
        counts[num] += 1
    counts = list(itertools.accumulate(counts))
    a_sorted = [0] * len(a)
    for num in a:
        index = counts[num] - 1
        a_sorted[index] = num
        counts[num] -= 1
    a[:] = a_sorted


if __name__ == '__main__':
    test_list = [2, 1, 5, 7, 9, 5, 6, 8]
    right_list = [1, 2, 5, 5, 6, 7, 8, 9]
    # bubble_sort(test_list)
    counting_sort(test_list)
    # selection_sort(test_list)
    assert test_list == right_list
    print(test_list)
