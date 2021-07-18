from typing import List


# 插入排序
# 将数组的数据分为2个区间，前面的区间代表已经排好序的，从后面区间拿出一个数据插入到前面区间的合适位置(跟前面那个数比较，如果小于前一个数，就向前冒泡到正确的位置)
def insert_sort(a: List[int]):
    n = len(a)
    if n <= 1:
        return
    for i in range(1, n):
        value = a[i]  # 记录下当前值，因为和这个位置可能被前面一个值后移占用
        j = i - 1
        while j >= 0 and a[j] > value:  # 当a[j] 比value大的时候，数据要往后移，也就是找到value 需要在有序区间的位置
            a[j + 1] = a[j]  # 把j这个位置的值，挪到j+1的位置
            j -= 1

        # 因为上面程序最后一步操作了j-1 ，所以真实的位置应该+1回去
        a[j + 1] = value


if __name__ == '__main__':
    test_list = [2, 1, 5, 7, 9, 5, 6, 8]
    right_list = [1, 2, 5, 5, 6, 7, 8, 9]
    # bubble_sort(test_list)
    insert_sort(test_list)
    # selection_sort(test_list)
    assert test_list == right_list
    print(test_list)
