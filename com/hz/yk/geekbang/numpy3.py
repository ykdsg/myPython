import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.amin(a))
# 延着 axis=0 轴的最小值
print(np.amin(a, 0))
print(np.amin(a, 1))
print(np.amax(a))
print(np.amax(a, 0))
print(np.amax(a, 1))

x = np.array([[0, 1], [2, 3]])
print(np.sum(x, axis=0))
print(np.sum(x, axis=1))
print(np.amin(x, axis=0))
print(np.amin(x, axis=1))
