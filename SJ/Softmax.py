# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rd8SoGGTVK8zQP7AVkHP90TYQWjYF73w

Data Loader
기존의 데이터를 가져오는 구조: 넘파이에서 csv를 읽어서 torch로 가져와 학습을 진행
Data Loader를 이용하면 가져와진 데이터에 자동으로 셔플링, 미니배치를 사용하여 학습이 가능 -> 성능향상

일반적을 데이터 샘플이 60개가 넘어가면 모집단의 통계적 특성을 반영하는 것으로 알려져 있다.!

용어 정리
epoch : 모든 트레이닝 데이터가 학습이 끝날 때 까지의 roop 횟수
iteration : 미니배치에서 데이터들이 학습이 끝날 때 까지의 roop 횟수

Dataloader
원래 데이터 -> Random shupple -> mini batch
"""

from torch import nn, optim, from_numpy
import numpy as np
import torch
from google.colab import drive
from torch.utils.data import Dataset
from torch.utils.data import DataLoader

class DiabetesDataset(Dataset):
  def __init__(self):
    #bring the dataset in google drive
    xy = np.loadtxt('/content/gdrive/My Drive/Colab Notebooks/data/diabetes.csv.gz', delimiter = ',', dtype = np.float32)
    
    self.len = xy.shape[0]
    self.x_data = from_numpy(xy[:, 0:-1])
    self.y_data = from_numpy(xy[:, [-1]])
  def __getitem__(self, index):
    #return the sample of index
    return self.x_data[index], self.y_data[index]
  def __len__(self):
    return self.len

dataset = DiabetesDataset()
#DataLoader -> 미니배치로 관리해주는 함수
#num_workers -> the number of CPU used in decoding of data
train_loader = DataLoader(dataset = dataset, batch_size = 32, shuffle = True, num_workers = 2)
#Testing Dataloader
for epoch in range(2):
  for i, data in enumerate(train_loader, 0):
    #get the inputs/ data = X, Y
    inputs, labels = data
    #wrap them in variable
    inputs, labels = torch.tensor(inputs), torch.tensor(labels)

    print(f'Epoch : {i}, inputs {inputs.data}, Labels : {labels.data}')

class Model(nn.Module):
  def __init__(self):
    super(Model, self).__init__()
    self.l1 = nn.Linear(8, 6)
    self.l2 = nn.Linear(6, 4)
    self.l3 = nn.Linear(4, 1)
    self.sigmoid = nn.Sigmoid()

  def forward(self, x):
    o1 = self.sigmoid(self.l1(x))
    o2 = self.sigmoid(self.l2(o1))
    y_pred = self.sigmoid(self.l3(o2))

    return y_pred

model = Model()

criterion = nn.BCELoss(reduction='mean')
optimizer = optim.Adam(model.parameters(), lr = 0.1)

#Training loop
for epoch in range(100):
  for i, data in enumerate(train_loader, 0):

    inputs, labels = data

    y_pred = model(inputs)

    loss = criterion(y_pred, labels)
    print(f'Epoch {epoch+1} | Batch: {i+1} Loss: {loss.item():.4f}')

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

"""Softmax

output label이 다차원 벡터인 경우에 Softmax를 사용한다.
Softmax는 입력된 값에 대하여 확률로 만들어 주며, 미분이 가능한 최대값을 뽑을 수 있게 해준다.
수식상에 들어가는 exp은 작은 것은 더 작게, 큰 것은 더 크게 해주는 효과를 가진다. 
Loss function으로는 Cross-Entropy를 사용한다.
"""



from torch import nn, optim
import torch

x_data = [[1, 2], [2, 3], [3, 1], [4, 3], [5, 3], [6, 2]]
y_data = [[0], [0], [0], [1], [1], [1]]

x_data = torch.tensor(x_data).float()
y_data = torch.tensor(y_data).float()


class Model(nn.Module):
  def __init__(self):
    super(Model, self).__init__()
    self.linear = nn.Linear(2, 1)
    self.sigmoid = nn.Sigmoid()
  def forward(self, x):
    return self.sigmoid(self.linear(x)) 

model = Model()

criterion = nn.BCELoss(reduction = 'mean')
optimizer = optim.Adam(model.parameters(), lr = 0.01)

for epoch in range(100):
  y_pred = model(x_data)

  loss = criterion(y_pred, y_data)

  optimizer.zero_grad()
  loss.backward()
  optimizer.step()
  if epoch%10 == 0:
    print(f'Epoch : {epoch}, Loss : {loss.item()}')

import torch
from torch import nn, optim

x_train = [[1, 2, 1, 1],
           [2, 1, 3, 2],
           [3, 1, 3, 4],
           [4, 1, 5, 5],
           [1, 7, 5, 5],
           [1, 2, 5, 6],
           [1, 6, 6, 6],
           [1, 7, 7, 7]]
y_train = [2, 2, 2, 1, 1, 1, 0, 0]
x_train = torch.FloatTensor(x_train)
y_train = torch.LongTensor(y_train)

class Model(nn.Module):
  def __init__(self):
    super(Model, self).__init__()
    self.linear = nn.Linear(4, 3)
    self.soft = nn.Softmax()
  def forward(self, x):
    o1 = self.linear(x)
    o2 = self.soft(o1)
    return o2

model = Model()

criterion = nn.CrossEntropyLoss(reduction = 'mean')
optimizer = optim.Adam(model.parameters(), lr = 0.01)

for epoch in range(100):

  y_pred = model(x_train)

  loss = criterion(y_pred, y_train)

  optimizer.zero_grad()
  loss.backward()
  optimizer.step()

  if (epoch % 10 == 0):
    print(f'epoch : {epoch}, Loss : {loss.item()}')

import torch
from torch import nn, optim, cuda
from torch.utils import data
from torchvision import datasets, transforms
import torch.nn.functional as F
import time
from six.moves import urllib 


#Training settings
batch_size = 64
device = 'cuda' if cuda.is_available() else 'cpu'
print('Training MNIST Model on {} \n {}'.format(device, '='*44))

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)

#MNIST Dataset
train_dataset = datasets.MNIST(root='./mnist_dataset/', train = True, transform = transforms.ToTensor(), download = True)

test_dataset = datasets.MNIST(root = './mnist_data/', train = False, transform = transforms.ToTensor(),  download = True)

#Data Loader
train_loader = torch.utils.data.DataLoader(dataset=train_dataset, batch_size = batch_size, shuffle = True)
test_loader = torch.utils.data.DataLoader(dataset= test_dataset, batch_size = batch_size, shuffle = False)

class Net(nn.Module):
  def __init__(self):
    super(Net, self).__init__()
    self.l1 = nn.Linear(784, 520)
    self.l2 = nn.Linear(520, 320)
    self.l3 = nn.Linear(320, 240)
    self.l4 = nn.Linear(240, 120)
    self.l5 = nn.Linear(120, 10)

  def forward(self, x):
    #Flatten the data
    x = x.view(-1, 784)
    x = F.relu(self.l1(x))
    x = F.relu(self.l2(x))
    x = F.relu(self.l3(x))
    x = F.relu(self.l4(x))
    return self.l5(x)

model = Net()
model.to(device)

criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr = 0.01, momentum = 0.5)

def train(epoch):
  model.train()
  for batch_idx, (data, target) in enumerate(train_loader):
    data, target = data.to(device), target.to(device)
    optimizer.zero_grad()
    output = model(data)
    loss = criterion(output, target)
    loss.backward()
    optimizer.step()

    if batch_idx % 10 == 0:
      print('Train Epoch : {} | Batch Status : {}/{} ({:.0f}%) | Loss : ({:.6f})'.format(epoch, batch_idx*len(data)
              ,len(train_loader.dataset), 100.*batch_idx/len(train_loader), loss.item()))

def test():
  model.eval()
  test_loss = 0
  correct = 0
  for data, target in test_loader:
    data, target = data.to(device), target.to(device)
    output = model(data)
    test_loss += criterion(output, target)
    pred = output.data.max(1, keepdim = True)[1]
    correct += pred.eq(target.data.view_as(pred)).cpu().sum()
  
  test_loss /= len(test_loader.dataset)
  
  print(f'\n==============================\nTest set: Average loss: {test_loss:.4f}, Accuracy : {correct}/{len(test_loader.dataset)}'
        f'({100.*correct/len(test_loader.dataset):.0f}%)')

for epoch in range(1, 10):
    train(epoch)
    test()

print(len(train_loader))



