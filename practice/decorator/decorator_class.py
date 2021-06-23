# https://zhuanlan.zhihu.com/p/93846887


# 类装饰器
class myDecorator(object):
    def __init__(self, f):
        print("inside myDecoratror.init")
        f()
        print("outside myDecoratror.init")

    def __call__(self, *args, **kwargs):
        print("inside myDecorator call")


@myDecorator
def aFunction():
    print("inside aFunction()")


print("Finished decorating aFunction()")

# 这里实际调用的是myDecorator的__call__()方法
# 被装饰后的函数aFunction()实际上已经是类myDecorator的对象
aFunction()

print("first demo end================================")


# 一般用法
class entryExit(object):
    def __init__(self, f):
        self.f = f

    def __call__(self):
        print("Entering", self.f.__name__)
        self.f()
        print("Exited", self.f.__name__)


@entryExit
def func1():
    print("inside func1()")


@entryExit
def func2():
    print("inside func2()")


func1()
func2()
