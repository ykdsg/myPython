def findMinAndMax(L):
    min = None
    max = None
    for x in L:
        if not min:
            min = x
        if not max:
            max = x

        if x < min:
            min = x

        if x > max:
            max = x

    return (min, max)


if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
