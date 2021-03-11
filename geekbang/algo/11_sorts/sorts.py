"""
    Bubble sort, insertion sort and selection sort
    冒泡排序、插入排序、选择排序

"""
from typing import List


# 冒泡排序
def bubble_sort(a: List[int]):
    len_ = len(a)
    if len_ <= 1:
        return

    for i in range(len_):
        flag = False
        for j in range(len_ - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                flag = True  # 表示有数据交换
        if not flag:  # 如果没有数据交换了说明整体已经是有序了
            break


# 插入排序
# 将数组的数据分为2个区间，前面的区间代表已经排好序的，从后面区间拿出一个数据插入到前面区间的合适位置(跟前面那个数比较，如果小于前一个数，就向前冒泡到正确的位置)
def insert_sort(a: List[int]):
    length = len(a)
    if length <= 1:
        return
    for i in range(1, length):
        value = a[i]
        j = i - 1
        while j >= 0 and a[j] > value:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = value


# 选择排序
# 跟插入排序有点像，也是2个区间，前面区间代表有序，从后面区间中找出最小的一个数，加到前一个区间的最后（跟前面区间最后面一位交换位置）
# 选择排序不是稳定排序，因为每次都要找最小一个数并和前面的元素交换位置，这样破坏了稳定性
# 比如 5，8，5，2，9 这样一组数据，使用选择排序算法来排序的话，第一次找到最小元素 2，与第一个 5 交换位置，那第一个 5 和中间的 5 顺序就变了，所以就不稳定了
def selection_sort(a: List[int]):
    length = len(a)
    if length <= 1:
        return
    for i in range(length):
        min = a[i]
        min_index = i
        for j in range(i + 1, length):
            if min > a[j]:
                min = a[j]
                min_index = j
        if (min_index != i):
            a[i], a[min_index] = a[min_index], a[i]


if __name__ == '__main__':
    test_list = [2, 1, 5, 7, 9, 5, 6, 8]
    right_list = [1, 2, 5, 5, 6, 7, 8, 9]
    # bubble_sort(test_list)
    insert_sort(test_list)
    # selection_sort(test_list)
    assert test_list == right_list
    print(test_list)
