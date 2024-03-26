import numpy as np
from scipy import linalg

A = np.array([[2, 1], [1, 2]])
# 求特征值和特征向量
evalue, evector = linalg.eig(A)
print(evalue)
print(evector)
