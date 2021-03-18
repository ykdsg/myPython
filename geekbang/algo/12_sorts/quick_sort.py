from typing import List


def sort(a: List[int]):
    quick_sort(a, 0, len(a) - 1)


def quick_sort(a: List[int], start: int, end: int):
    if start >= end:
        return

    # 这一步将数组分成3部分，start到p-1 都是小于a[p]的，p+1到end 都是比a[p] 大的。
    p = partition(a, start, end)
    # 注意这里一定要用p-1和p+1，不然就会无限循环，因为每次都是选择最后一个数字来排序，就会一直排一直排
    quick_sort(a, start, p - 1)
    quick_sort(a, p + 1, end)


def partition(a: List[int], start: int, end: int) -> int:
    # 选取最后一个值作为区分点
    pivot = a[end]
    # 表示最后区分点的位置
    p_index = start
    # 将<pivot 的放入左边区域
    for i in range(start, end):
        if a[i] < pivot:
            a[p_index], a[i] = a[i], a[p_index]
            p_index += 1
    # 因为选择了a[end]作为最后一个点，所以这里需要把他放入正确的分割点位置，上面调整的时候并没有到end 的位置，因为rang 没有右包围
    a[p_index], a[end] = a[end], a[p_index],
    return p_index


if __name__ == '__main__':
    test_list = [2, 1, 5, 7, 9, 5, 6, 8]
    right_list = [1, 2, 5, 5, 6, 7, 8, 9]
    # bubble_sort(test_list)
    sort(test_list)
    # selection_sort(test_list)
    assert test_list == right_list
    print(test_list)
