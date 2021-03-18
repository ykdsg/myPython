from typing import List


# 查找第一个值等于给定值的元素
# 这个算是比较简洁的写法，但是不容易理解
def bsearch_first(nums: List[int], target: int):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if nums[mid] >= target:
            high = mid - 1
        # 这里通过low 不断逼近第一个值
        else:
            low = mid + 1

    if low < len(nums) and nums[low] == target:
        return low
    return -1


def bsearch_last(num: List[int], target: int):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if nums[mid] <= target:
            low = mid + 1
        else:
            high = mid - 1

    if high > 0 and nums[high] == target:
        return high
    return -1


# 查找最后一个小于等于给定值的元素
def bsearch_last_lessThan(num: List[int], target: int):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if nums[mid] > target:
            high = mid - 1
        else:
            # 下一位大于target说明是最后一个满足条件的元素了
            if mid + 1 == len(nums) or num[mid + 1] > target:
                return mid
            else:
                low = mid + 1
    return -1


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
