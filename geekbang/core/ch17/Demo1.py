def func(message):
    print('got a message:{}'.format(message))


# 函数赋予变量
send_message = func
send_message('hello world')


def get_message(message):
    return 'got a message:' + message


def root_call(func, message):
    print(func(message))
