from typing import List

inversion_num = 0


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
            # 计算a_cursor 这边有多少个比b_cursor大
            inversion_num += mid - a_cursor + 1
            tmp.append(nums[b_cursor])
            b_cursor += 1

    if a_cursor <= mid:
        tmp.extend(nums[a_cursor: mid + 1])

    if b_cursor <= end:
        tmp.extend(nums[b_cursor: end + 1])

    nums[start:end + 1] = tmp


def merge_sort_counting(nums: List, start: int, end: int):
    if start >= end:
        return
    mid = (start + end) // 2
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
