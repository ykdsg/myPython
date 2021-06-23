class Decorator:
    def __init__(self, arg1, arg2):
        print('执行类Decorator的__init__()方法')
        self.arg1 = arg1
        self.arg2 = arg2

    def __call__(self, *args, **kwargs):
        print('执行类Decorator的__call__()方法')

        f = args[0]

        def wrap(*args):
            print('执行wrap()')
            print('装饰器参数：', self.arg1, self.arg2)
            print('执行' + f.__name__ + '()')
            f(*args)
            print(f.__name__ + '()执行完毕')

        return wrap


@Decorator('Hello', 'World')
def example(a1, a2, a3):
    print('传入example()的参数：', a1, a2, a3)


print('装饰完毕')
print('准备调用example()')
example('Wish', 'Happy', 'EveryDay')
print('第一个测试代码执行完毕============================')


def test_demo():
    @Decorator('Hello', 'World')
    def example(a1, a2, a3):
        print('传入example()的参数：', a1, a2, a3)

    print("end----------------")


test_demo()
