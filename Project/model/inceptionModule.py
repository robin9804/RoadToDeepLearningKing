"""
데이터 검증에 대해서 input data와 output data를 조작할 부분이 필요하지 않은가 싶다.
1. 모델
2. 입력 데이터 조작 및 출력 데이터 조작 후 오차함수 정의
3. 훈련 및 검증부
4. 결과 시각화(ASM propagation)
"""

import torch
import torch.nn as nn
import torch.nn.functional as F


class InceptionA(nn.Module):
    """
    Inception module, 4개의 브렌치를 활용한 CNN 모듈
    """
    def __init__(self, in_channels):
        super(InceptionA).__init__()
        self.branch1x1 = nn.Conv2d(in_channels, 16, kernel_size=1)  # in=in, out = 16
        
        self.branch5x5_1 = nn.Conv2d(in_channels, 16, kernel_size=1)
        self.branch5x5_2 = nn.Conv2d(16, 24, kernel_size=5, padding=2)  # same padding

        self.branch3x3db1_1 = nn.Conv2d(in_channels, 16, kernel_size=1)
        self.branch3x3db1_2 = nn.Conv2d(16, 24, kernel_size=3, padding=1)
        self.branch3x3db1_3 = nn.Conv2d(24,24, kernel_size=3, padding=1)

        self.branch_pool = nn.Conv2d(in_channels, 24, kernel_size=1)

    def forward(self, x):
        # 1x1 브렌치
        branch1x1 = self.branch1x1(x)

        # 5x5 브렌치
        branch5x5 = self.branch5x5_1(x)
        branch5x5 = self.branch5x5_2(branch5x5)

        branch3x3 = self.branch3x3db1_1(x)
        branch3x3 = self.branch3x3db1_2(branch3x3)
        branch3x3 = self.branch3x3db1_3(branch3x3)

        # 모두 합치기
        branch_pool = F.avg_pool2d(x, kernel_size=3, stride=1, padding=1)
        branch_pool = self.branch_pool(branch_pool)

        outs = [branch1x1, branch5x5, branch3x3, branch_pool]
        return torch.cat(outs, 1)



class Net(nn.Module):
    def __init__(self):
        super(Net).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = nn.Conv2d(88,20, kernel_size=5)

        self.incept1 = InceptionA(in_channels=10)
        self.incept2 = InceptionA(in_channels=20)

        self.mp = nn.MaxPool2d(2)
        self.fc = nn.Linear(1408, 10)  # fully connected layer

    def forward(self, x):
        in_size = x.size(0)

        x = F.relu(self.mp(self.conv1(x)))
        x = self.incept1(x)
        x = F.relu(self.mp(self.conv2(x)))
        x = self.incept2(x)
        x = x.view(in_size, -1)  # FCN에 연결하기 위한 flatten
        x = self.fc(x)

        return F.log_softmax(x)