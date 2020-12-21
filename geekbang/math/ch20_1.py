import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def flip_coin(times):
    data_array = np.empty(times)
    weight_array = np.empty(times)
    weight_array.fill(1 / times)

    for i in range(0, times):
        data_array[i] = random.randint(0, 1)

    data_frame = pd.DataFrame(data_array)
    data_frame.plot(kind='hist', legend=False)
    data_frame.plot(kind='hist', legend=False, weights=weight_array).set_ylabel("Probability")  # 获取正反面统计概率的直方图
    plt.show()


flip_coin(1000)
