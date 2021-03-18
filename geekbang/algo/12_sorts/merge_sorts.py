from typing import List


def merge_sort(a: List[int]):
    merge_sort_c(a, 0, len(a) - 1)


def merge_sort_c(a: List[int], low: int, high: int):
    if low >= high:
        return
    mid = (low + high) // 2
    merge_sort_c(a, low, mid)
    merge_sort_c(a, mid + 1, high)
    merge(a, low, mid, high)


def merge(a: List[int], low: int, mid: int, high: int):
    i, j = low, mid + 1
    tmp = []
    while i <= mid and j <= high:
        if a[i] <= a[j]:
            tmp.append(a[i])
            i += 1
        else:
            tmp.append(a[j])
            j += 1

    start = i if i <= mid else j
    end = mid if i <= mid else high
    tmp.extend(a[start:end + 1])
    a[low:high + 1] = tmp


if __name__ == '__main__':
    test_list = [2, 1, 5, 7, 9, 5, 6, 8]
    right_list = [1, 2, 5, 5, 6, 7, 8, 9]
    # bubble_sort(test_list)
    merge_sort(test_list)
    # selection_sort(test_list)
    assert test_list == right_list
    print(test_list)
