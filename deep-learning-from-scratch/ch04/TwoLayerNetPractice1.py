import numpy as np

from common.functions import sigmoid, softmax, cross_entropy_error
from common.gradient import numerical_gradient_practices1


class TwoLayerNetPractice1:
    def __init__(self, input_size, hidden_size, output_size, weight_init_std=0.01):
        """

        :param input_size: 输入层神经元数
        :param hidden_size: 隐藏层的神经元数
        :param output_size: 输出层的神经元数
        :param weight_init_std:
        """
        self.params = {}
        self.params['W1'] = weight_init_std * np.random.randn(input_size, hidden_size)
        # 权重个数跟当前输出个数一致
        self.params['b1'] = np.zeros(hidden_size)
        self.params['W2'] = weight_init_std * np.random.randn(hidden_size, output_size)
        self.params['b2'] = np.zeros(output_size)

    # 正向求结果
    def predict(self, x):
        W1, W2 = self.params['W1'], self.params['W2']
        b1, b2 = self.params['b1'], self.params['b2']

        a1 = np.dot(x, W1) + b1
        z1 = sigmoid(a1)
        a2 = np.dot(z1, W2) + b2
        y = softmax(a2)

        return y

    # x:输入数据, t:监督数据
    def loss(self, x, t):
        y = self.predict(x)
        return cross_entropy_error(y, t)

    # 准确率计算
    def accuracy(self, x, t):
        y = self.predict(x)

        y = np.argmax(y, axis=1)
        t = np.argmax(t, axis=1)

        return np.sum(y == t) / y.shape[0]

    # x:输入数据, t:监督数据
    # 梯度计算
    def numerical_gradient(self, x, t):
        loss_W = lambda W: self.loss(x, t)

        grads = {}
        grads['W1'] = numerical_gradient_practices1(loss_W, self.params['W1'])
        grads['b1'] = numerical_gradient_practices1(loss_W, self.params['b1'])
        grads['W2'] = numerical_gradient_practices1(loss_W, self.params['W2'])
        grads['b2'] = numerical_gradient_practices1(loss_W, self.params['b2'])

        return grads


net = TwoLayerNetPractice1(input_size=784, hidden_size=100, output_size=10)
net.params['W1'].shape  # (784, 100)
net.params['b1'].shape  # (100,)
net.params['W2'].shape  # (100, 10)
net.params['b2'].shape  # (10,)

x = np.random.rand(100, 784)  # 伪输入数据（100笔）
t = np.random.rand(100, 10)  # 伪正确解标签（100笔）

grads = net.numerical_gradient(x, t)  # 计算梯度

grads['W1'].shape  # (784, 100)
grads['b1'].shape  # (100,)
grads['W2'].shape  # (100, 10)
grads['b2'].shape  # (10,)
