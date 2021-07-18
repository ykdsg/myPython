from typing import List


# nums数组是有序的，而且没有重复数据的时候
def bsearch(nums: List[int], param: int) -> int:
    length = len(nums)
    if length < 1:
        return -1
    start = 0
    end = length - 1

    # 这里需要考虑start=end的情况，比如数组长度为1，start和end都为0
    #
    while start <= end:
        mid = start + ((end - start) >> 1)
        if nums[mid] == param:
            return mid
        elif nums[mid] < param:
            start = mid + 1
        elif nums[mid] > param:
            end = mid - 1

    return -1


if __name__ == '__main__':
    nums = [3, 4, 5, 6, 7, 8, 9, 10]
    index_5 = bsearch(nums, 5)
    assert index_5 == 2
    print(index_5)
    index_1 = bsearch(nums, 1)
    assert index_1 == -1
