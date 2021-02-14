import numpy as np
from sklearn.datasets import load_diabetes
import matplotlib.pyplot as plt


# 데이터셋 가져오기
diabetes = load_diabetes()

# single perceptron을 통한 back propagation 계산 class
class Neuron:

    def __init__(self):
        self.w = 1.0  # 가중치 초기화
        self.b = 1.0  # bias 초기화

    def forpass(self, x):
        y_hat = x * self.w + self.b  # linear equation 을 만들기
        return y_hat

    def backprop(self, x, err):
        w_grad = x * err  # 출력값과 결과값의 차이를 error라고 가정했을 때, w의 gradient는 다음과 같다.
        b_grad = 1 * err  # bias의 gradient도 마찬가지
        return w_grad, b_grad
    
    def fit(self, x, y, epoch=100):
        for i in range(epoch):
            for x_i, y_i in zip(x, y):
                y_hat = self.forpass(x_i)  # 정방향 계산으로 결과값 얻기
                err = - (y_i - y_hat)      # 계산 결과값과 오차 계산
                w_grad, b_grad = self.backprop(x_i, err)  # 역방향 미분 계산
                self.w -= w_grad  # 가중치 업데이트
                self.b -= b_grad  # bias 업데이트


if __name__ == '__main__':
    print('check dataset shape and target shape')
    print(diabetes.data.shape)
    print(diabetes.target.shape)
    
    # 사용할 데이터 가져오기
    x = diabetes.data[:,2]
    y = diabetes.target

    neuron = Neuron()
    neuron.fit(x, y)

    print('dataset scatter plot')
    plt.scatter(diabetes.data[:,2], diabetes.target)
    pt1 = (-0.1, -0.1 * neuron.w + neuron.b)  # -0.1, -0.1 지점에서 0.15까지 선을 긋기
    pt2 = (0.15, 0.15 * neuron.w + neuron.b)
    plt.plot([pt1[0], pt2[0]],[pt1[1], pt2[1]] )
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()