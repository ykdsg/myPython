def decorator(func):
    # 接受任意数量和类型的参数
    def wrapper(*args, **kwargs):
        print('wrapper of decorator')
        func(*args, **kwargs)

    return wrapper


@decorator
def greet(message1, message2):
    print(message1, message2)


greet('hello', ' world')
