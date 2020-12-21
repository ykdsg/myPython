# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def trim(s):
    while s[:1] == ' ':
        s = s[1:]

    while s[-1:] == ' ':
        s = s[:-1]
    return s


def test_trim():
    if trim('hello  ') != 'hello':
        print('测试失败!')
    elif trim('  hello') != 'hello':
        print('测试失败!')
    elif trim('  hello  ') != 'hello':
        print('测试失败!')
    elif trim('  hello  world  ') != 'hello  world':
        print('测试失败!')
    elif trim('') != '':
        print('测试失败!')
    elif trim('    ') != '':
        print('测试失败!')
    else:
        print('测试成功!')


# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    if not L:
        return (None, None)

    min = L[0]
    max = L[0]
    for x in L:
        if x < min:
            min = x

        if x > max:
            max = x

    return (min, max)


def test_findMinAndMax():
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


# 杨辉三角定义如下：
#
#           1
#          / \
#         1   1
#        / \ / \
#       1   2   1
#      / \ / \ / \
#     1   3   3   1
#    / \ / \ / \ / \
#   1   4   6   4   1
#  / \ / \ / \ / \ / \
# 1   5   10  10  5   1
# 把每一行看做一个list，试写一个generator，不断输出下一行的list
def triangles():
    yield [1]
    n = [1, 1]
    yield n
    while True:
        m = []
        i = 0
        while i < len(n):
            if i == 0 or i == (len(n) - 1):
                m.append(1)
            if i + 1 < len(n):
                m.append(n[i] + n[i + 1])
            i = i + 1
        yield m
        n = m


# 使用了更简洁的思路和zip内置函数
def triangles2():
    n = [1]
    while True:
        yield n
        n = [sum(i) for i in zip([0] + n, n + [0])]


def test_triangles():
    n = 0
    results = []
    for t in triangles2():
        results.append(t)
        n = n + 1
        if n == 10:
            break

    for t in results:
        print(t)

    if results == [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
        [1, 5, 10, 10, 5, 1],
        [1, 6, 15, 20, 15, 6, 1],
        [1, 7, 21, 35, 35, 21, 7, 1],
        [1, 8, 28, 56, 70, 56, 28, 8, 1],
        [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
    ]:
        print('测试通过!')
    else:
        print('测试失败!')


# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
    return name[0].upper() + name[1:].lower()


# 利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():
    ax = 0

    def counter():
        # nonlocal 声明可以让我们编写函数来修改内部变量的值
        nonlocal ax
        ax = ax + 1
        return ax

    return counter


def test_create_counter():
    counterA = createCounter()
    print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
    counterB = createCounter()
    if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
        print('测试通过!')
    else:
        print('测试失败!')


if __name__ == '__main__':
    # test_trim()
    # test_findMinAndMax()
    # test_triangles()
    test_create_counter()
