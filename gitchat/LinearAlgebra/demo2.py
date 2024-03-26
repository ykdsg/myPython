import numpy as np

u = np.array([[1, 2, 3]]).T
print(3 * u)

u = np.array([3, 5, 2])
v = np.array([1, 4, 7])
# 内积，向量 u 在向量 v 方向上的投影长度乘上向量 v 的模长
print(np.dot(u, v))
