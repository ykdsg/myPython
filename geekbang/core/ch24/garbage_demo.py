import os
import sys

import psutil


def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024
    print("{}内存使用了{}MB".format(hint, memory))


def func():
    show_memory_info("局部变量初始化")
    a = [i for i in range(10000000)]
    show_memory_info("局部变量创建后")
    return a


def func2():
    show_memory_info("全局变量初始化")
    global a
    a = [i for i in range(10000000)]
    show_memory_info("全局变量创建后")


# python内部引用计数
def jishu():
    a = []
    # getrefcount 本身也会引入一次计数
    print(sys.getrefcount(a))

    def func(a):
        print(sys.getrefcount(a))

    func(a)
    print(sys.getrefcount(a))


if __name__ == "__main__":
    # func()
    # show_memory_info("局部变量完成后")
    # func2()
    # show_memory_info("全局变量完成后")
    # l = func()
    # show_memory_info("列表变量完成后")
    jishu()
