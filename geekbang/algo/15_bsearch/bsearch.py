from typing import List


# 二分查找法
def bsearch(nums: List[int], target: int) -> int:
    if len(nums) < 1:
        return -1

    low = 0
    high = len(nums) - 1
    # 这里需要注意是<= ，不能直接用<
    while low <= high:
        # 这里没用用(low+high)//2 是考虑到加法可能导致int长度溢出，所以优化成下面的写法
        mid = low + ((high - low) >> 1)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
    return -1


if __name__ == '__main__':
    nums = [3, 4, 5, 6, 7, 8, 9, 10]
    index_5 = bsearch(nums, 5)
    assert index_5 == 2
    print(index_5)
    index_1 = bsearch(nums, 1)
    assert index_1 == -1
