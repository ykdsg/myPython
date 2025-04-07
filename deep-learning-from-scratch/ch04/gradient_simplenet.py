# coding: utf-8
import sys, os
sys.path.append(os.pardir)  # 为了导入父目录中的文件而进行的设定
import numpy as np
from common.functions import softmax, cross_entropy_error
from common.gradient import numerical_gradient


class simpleNet:
    def __init__(self):
        self.W = np.random.randn(2,3)

    def predict(self, x, w):
        return np.dot(x, w)

    # 损失函数
    def loss(self, x, t, w):
        z = self.predict(x, w)
        y = softmax(z)
        loss = cross_entropy_error(y, t)

        return loss


# x 标识输入信号
x = np.array([0.6, 0.9])
# t标识正确的标签
t = np.array([0, 0, 1])

net = simpleNet()
print("net.W:", net.W)

f = lambda w: net.loss(x, t, w)
dW = numerical_gradient(f, net.W)

print(dW)
