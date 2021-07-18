from typing import List


def merge_sort(a: List[int]):
    n = len(a)
    merge_sortc(a, 0, n - 1)


def merge_sortc(a: List[int], start: int, end: int):
    if start >= end:
        return
    mid: int = (start + end) // 2
    merge_sortc(a, start, mid)
    merge_sortc(a, mid + 1, end)
    merge(a, start, mid, end)


def merge(a: List[int], start: int, mid: int, end: int):
    i = start
    j = mid + 1
    tmp = []
    while i <= mid and j <= end:
        if a[i] < a[j]:
            tmp.append(a[i])
            i += 1
        else:
            tmp.append(a[j])
            j += 1

    rest_start = i if i <= mid else j
    rest_end = mid if i <= mid else end
    tmp.extend(a[rest_start:rest_end + 1])  # 右边是不包含的，所以这里需要+1
    a[start:end + 1] = tmp


if __name__ == '__main__':
    test_list = [2, 1, 5, 7, 9, 5, 6, 8]
    right_list = [1, 2, 5, 5, 6, 7, 8, 9]
    # bubble_sort(test_list)
    merge_sort(test_list)
    print(test_list)
    # selection_sort(test_list)
    assert test_list == right_list
