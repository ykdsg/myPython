def my_decorator(func):
    def wrapper():
        print('wrapper of decorator')
        func()

    return wrapper


def greet():
    print('hello world')


greet = my_decorator(greet)
greet()


# 装饰器的语法糖，效果跟上面的一致
@my_decorator
def greet2():
    print('hello world2')


greet2()


# 带有参数的装饰器
def decorator2(func):
    def wrapper(message):
        print('wrapper of decorator')
        func(message)

    return wrapper


@decorator2
def greet3(message):
    print(message)


greet3('hello world3')
