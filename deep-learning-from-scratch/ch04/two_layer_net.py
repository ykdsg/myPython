# coding: utf-8
import sys, os

# 交互式解释器中没办法识别，os.pardir（体现为..），因此导入common会报错，只能通过Run python 文件的方式运行
sys.path.append(os.pardir)  # 为了导入父目录的文件而进行的设零碳中国定
from common.functions import *
from common.gradient import numerical_gradient


class TwoLayerNet:

    def __init__(self, input_size, hidden_size, output_size, weight_init_std=0.01):
        """

        :param input_size: 输入层神经元数
        :param hidden_size: 隐藏层的神经元数
        :param output_size: 输出层的神经元数
        :param weight_init_std:
        """
        # 初始化权重
        self.params = {}
        # W 是权重，b 是偏置
        self.params['W1'] = weight_init_std * np.random.randn(input_size, hidden_size)
        self.params['b1'] = np.zeros(hidden_size)
        self.params['W2'] = weight_init_std * np.random.randn(hidden_size, output_size)
        self.params['b2'] = np.zeros(output_size)

    def predict(self, x):
        W1, W2 = self.params['W1'], self.params['W2']
        b1, b2 = self.params['b1'], self.params['b2']
    
        a1 = np.dot(x, W1) + b1
        # 激活函数
        z1 = sigmoid(a1)
        a2 = np.dot(z1, W2) + b2
        # 输出层，分类问题使用softmax 函数
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
        
        accuracy = np.sum(y == t) / float(x.shape[0])
        return accuracy
        
    # x:输入数据, t:监督数据
    # 梯度计算
    def numerical_gradient(self, x, t):
        loss_W = lambda W: self.loss(x, t)

        # 梯度
        grads = {}
        grads['W1'] = numerical_gradient(loss_W, self.params['W1'])
        grads['b1'] = numerical_gradient(loss_W, self.params['b1'])
        grads['W2'] = numerical_gradient(loss_W, self.params['W2'])
        grads['b2'] = numerical_gradient(loss_W, self.params['b2'])
        
        return grads

    # 更高效的梯度计算
    def gradient(self, x, t):
        W1, W2 = self.params['W1'], self.params['W2']
        b1, b2 = self.params['b1'], self.params['b2']
        grads = {}
        
        batch_num = x.shape[0]
        
        # forward
        a1 = np.dot(x, W1) + b1
        z1 = sigmoid(a1)
        a2 = np.dot(z1, W2) + b2
        y = softmax(a2)
        
        # backward
        dy = (y - t) / batch_num
        grads['W2'] = np.dot(z1.T, dy)
        grads['b2'] = np.sum(dy, axis=0)
        
        da1 = np.dot(dy, W2.T)
        dz1 = sigmoid_grad(a1) * da1
        grads['W1'] = np.dot(x.T, dz1)
        grads['b1'] = np.sum(dz1, axis=0)

        return grads


net = TwoLayerNet(input_size=784, hidden_size=100, output_size=10)
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
