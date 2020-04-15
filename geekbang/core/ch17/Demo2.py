def func(message):
    def get_message(message):
        print('got a message:{}'.format(message))

    return get_message(message)


# 在函数中定义函数，就是函数的嵌套
func('hello world')


def fun_closure():
    def get_message(message):
        print('got a message:{}'.format(message))

    return get_message


# 函数的返回值也是函数（闭包）
send_message = fun_closure()
send_message('hello world')
