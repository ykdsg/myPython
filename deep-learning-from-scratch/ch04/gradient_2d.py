# coding: utf-8
# cf.http://d.hatena.ne.jp/white_wheels/20100327/p3
import numpy as np
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D


# %%
def _numerical_gradient_no_batch(f, x):
    h = 1e-4 # 0.0001
    grad = np.zeros_like(x)
    
    for idx in range(x.size):
        tmp_val = x[idx]
        x[idx] = float(tmp_val) + h
        fxh1 = f(x) # f(x+h)
        
        x[idx] = tmp_val - h 
        fxh2 = f(x) # f(x-h)
        grad[idx] = (fxh1 - fxh2) / (2*h)
        
        x[idx] = tmp_val # 还原值
        
    return grad


def numerical_gradient(f, X):
    if X.ndim == 1:
        return _numerical_gradient_no_batch(f, X)
    else:
        grad = np.zeros_like(X)
        
        for idx, x in enumerate(X):
            grad[idx] = _numerical_gradient_no_batch(f, x)
        
        return grad


def function_2(x):
    if x.ndim == 1:
        return np.sum(x**2)
    else:
        return np.sum(x**2, axis=1)


def tangent_line(f, x):
    d = numerical_gradient(f, x)
    print(d)
    y = f(x) - d*x
    return lambda t: d*t + y
     
if __name__ == '__main__':
    x0 = np.arange(-2, 2.5, 0.25)
    x1 = np.arange(-2, 2.5, 0.25)
    # meshgrid 网格化函数，将x0 作为行进行扩展，行数是x1 长度，将x1 作为列进行列扩展，列数是x0 长度
    X, Y = np.meshgrid(x0, x1)

    # 将多维数组 X 转换为一维数组
    X = X.flatten()
    Y = Y.flatten()

    arrayX = np.array([X, Y])
    print("arrayX shape ", arrayX.shape)
    grad = numerical_gradient(function_2, arrayX)
    
    plt.figure()
    U = -grad[0]
    V = -grad[1]
    # plt.quiver(X, Y, U, V, **kwargs)
    # X, Y：箭头起点的坐标（网格点位置）。
    # U, V：箭头的方向分量（分别对应 x 和 y 方向，通过numerical_gradient函数进行计算得出）。
    plt.quiver(X, Y, U, V, angles="xy", color="#666666")  # ,headwidth=10,scale=40,color="#444444")
    plt.xlim([-2, 2])
    plt.ylim([-2, 2])
    plt.xlabel('x0')
    plt.ylabel('x1')
    plt.grid()
    plt.legend()
    plt.draw()
    plt.show()