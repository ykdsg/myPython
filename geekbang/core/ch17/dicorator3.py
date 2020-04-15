import functools


def repeat(num):
    def my_decorator(func):
        # 内置装饰器functools 会帮助保留原函数的元信息
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(num):
                print('wrapper of decorator')
                func(*args, **kwargs)

        return wrapper

    return my_decorator


# 带自定义参数的装饰器
@repeat(4)
def greet(message):
    print(message)


greet('hello wo')
print("name:", greet.__name__)
help(greet)
