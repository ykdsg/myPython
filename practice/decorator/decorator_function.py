# 函数装饰器
def wrapper(func):
    # 用*修饰的参数将会被认为是列表，而将所有元素取出作为位置参数；
    # 用**修饰的参数会被认为是字典，而将所有键和值取出作为关键字参数。
    def inner(*args, **kwargs):
        print("inside wrapper")
        func(*args, **kwargs)

    return inner


@wrapper
def func1(a, b, c):
    print('a=', a, 'b=', 'c=', c)


func1(1, b='boy', c='cat')


@wrapper
def func2(v1, v2):
    print(v1, v2)


func2(100, 200)
