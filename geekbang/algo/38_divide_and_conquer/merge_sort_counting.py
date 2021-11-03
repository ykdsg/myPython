inversion_num = 0


# 处理两块有序数组区间
def merge(nums, start, mid, end):
    global inversion_num
    a_cursor = start
    b_cursor = mid + 1
    tmp = []
    while a_cursor <= mid and b_cursor <= end:
        if nums[a_cursor] <= nums[b_cursor]:
            tmp.append(nums[a_cursor])
            a_cursor += 1
        else:
            # 统计start-mid之间，比num[b_cursor]大的元素个数
            inversion_num += mid - a_cursor + 1
            tmp.append(nums[b_cursor])
            b_cursor += 1

    while (a_cursor <= mid):
        tmp.append(nums[a_cursor])
        a_cursor += 1

    while (b_cursor <= end):
        tmp.append(nums[b_cursor])
        b_cursor += 1

    # 从tmp 拷贝回原数组
    nums[start:end + 1] = tmp


def merge_sort_counting(nums: list, start: int, end: int):
    if start >= end:
        return
    mid: int = (start + end) // 2
    merge_sort_counting(nums, start, mid)
    merge_sort_counting(nums, mid + 1, end)
    merge(nums, start, mid, end)


if __name__ == '__main__':
    print('--- count inversion number using merge sort ---')
    # nums = [5, 0, 4, 2, 3, 1, 6, 8, 7]
    nums = [5, 0, 4, 2, 3, 1, 3, 3, 3, 6, 8, 7]
    print('nums  : {}'.format(nums))
    merge_sort_counting(nums, 0, len(nums) - 1)
    print('sorted: {}'.format(nums))
    print('inversion number: {}'.format(inversion_num))
