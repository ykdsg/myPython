import concurrent
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Pool
import os
import time


# 用于计算平方
def f(x):
    return x * x


if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # 并行计算
        time1 = time.time()
        res = executor.map(f, range(1, 10001))
        time2 = time.time()
        print(f'计算平方的结果是:{res}')

    print(str(time2 - time1))
