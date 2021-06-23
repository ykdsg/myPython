# 给定两个数组，编写一个函数来计算它们的交集。
# 输入: nums1 = [1,2,2,1], nums2 = [2,2]
# 输出: [2,2]

def intersect(nums1: list, nums2: list):
    n1Map = {}
    for num in nums1:
        if num in n1Map.keys():
            n1Map[num] += 1
        else:
            n1Map[num] = 1

    k = 0
    for num in nums2:
        if (num in n1Map.keys()) and n1Map[num] > 0:
            n1Map[num] -= 1
            nums2[k] = num
            k += 1

    return nums2[:k]


# 排序之后使用双指针的解法
def intersectSequence(nums1: list, nums2: list):
    n1 = n2 = k = 0
    nums1.sort()
    nums2.sort()
    while n1 < len(nums1) and n2 < len(nums2):
        if (nums1[n1] < nums2[n2]):
            n1 += 1
        elif (nums1[n1] > nums2[n2]):
            n2 += 1
        else:
            nums2[k] = nums2[n1]
            n1 += 1
            n2 += 1
            k += 1
    return nums2[:k]


if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [5, 2, 2, 1, 6]
    print(intersect(nums1, nums2))

    # 因为上面排序的时候复用了内存空间，所以这里重新初始化下
    nums1 = [1, 2, 2, 1]
    nums2 = [5, 2, 2, 1, 6]
    print(intersectSequence(nums1, nums2))
