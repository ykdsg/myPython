# 定制类相关学习
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017590712115904
class Student(object):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return 'Student object (name:%s)' % self.name

    # __str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串
    __repr__ = __str__


s = Student('Mark')
print(s)


# 将Fib 当做迭代器，__iter__ 返回self，所以需要实现__next__
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if (self.a > 1000):
            raise StopIteration()
        return self.a


# for n in Fib():
#     print(n)

# __iter__ 直接返回一个生成器
class Fib2(object):
    def __init__(self):
        self.a, self.b = 1, 1

    def __iter__(self):
        while self.a < 1000:
            yield self.a
            self.a, self.b = self.b, self.a + self.b

    # 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


f = Fib2()
for n in f:
    print(n)

print(f[4])
# 能够简单支持切片，但是没有对step处理，也没对负数处理
print(f[2:8])
