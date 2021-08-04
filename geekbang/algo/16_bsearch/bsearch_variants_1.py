from typing import List


# 查找第一个值等于给定值的元素
def bsearch_first(nums: List[int], target: int):
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = start + ((end - start) >> 1)
        if nums[mid] < target:
            start = mid + 1
        elif nums[mid] > target:
            end = mid - 1
        elif nums[mid] == target:
            if mid == 0 or nums[mid - 1] < target:
                return mid
            else:
                end = mid - 1
    return -1


# 查找最后一个值等于给定值的元素
def bsearch_last(nums, target):
    start = 0
    length = len(nums)
    end = length - 1
    while start <= end:
        mid = start + ((end - start) >> 1)
        if nums[mid] < target:
            start = mid + 1
        elif nums[mid] > target:
            end = mid - 1
        elif nums[mid] == target:
            if mid == length - 1 or nums[mid + 1] > target:
                return mid
            else:
                start = mid + 1
    return -1


# 查找最后一个小于等于给定值的元素
def bsearch_last_lessThan(nums, target):
    start = 0
    length = len(nums)
    end = length - 1
    while start <= end:
        mid = start + ((end - start) >> 1)
        if nums[mid] > target:
            end = mid - 1
        else:
            if mid == length - 1 or nums[mid + 1] > target:
                return mid
            else:
                start = mid + 1


if __name__ == '__main__':
    nums = [3, 4, 5, 5, 6, 7, 8, 9, 10]
    first_5 = bsearch_first(nums, 5)
    print(first_5)
    assert first_5 == 2

    last_5 = bsearch_last(nums, 5)
    print(last_5)
    assert last_5 == 3

    nums = [1, 1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10]
    last_less_5 = bsearch_last_lessThan(nums, 5)
    print(last_less_5)
    assert last_less_5 == 7

    nums = [1, 1, 2, 2, 3, 5, 5, 6, 7, 8, 9, 10]
    last_less_5 = bsearch_last_lessThan(nums, 4)
    print(last_less_5)
    assert last_less_5 == 4
