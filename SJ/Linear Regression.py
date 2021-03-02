# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KKcu1PeULx_ZAVcnnJVVKtb-d2Vk6dmd
"""

import torch
import numpy as np
import matplotlib.pyplot as plt

x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]

w = torch.tensor([1.0], requires_grad = True)

def forward(x):
  return x*w

def loss(x, y):
  y_pred = forward(x)
  return (y_pred-y)**2

#before training
print('predict (before training)', 4, forward(4).item())

for epoch in range(10):
  for x_val, y_val in zip(x_data, y_data):
    y_pred = forward(x_val)#1) Forward pass
    l = loss(x_val, y_val)#2) compute loss
    l.backward() # 3) Back propagation to update weights
    print('\tgrad', x_val, y_val, w.grad.item())
    w.data = w.data -0.01*w.grad.item()

    # Manually zero the gradients after updating weights
    w.grad.data.zero_()
  print('Epoch: {} | Loss : {}'.format(epoch, l.item()) )

#after training
print("Prediction (after training)",4, forward(4).item())

x_data = [1.0, 2.0, 3.0]
y_data = [0.1, 0.4, 0.9]

w1 = torch.tensor([0.0], requires_grad = True)
w2 = torch.tensor([0.0], requires_grad = True)
b = torch.tensor(0.1)
def forward_quad(x): return w1*x**2+w2*x+b
def loss_quad(x, y):
  y_pred = forward_quad(x)
  return (y_pred - y)**2

optimizer = torch.optim.SGD([w1, w2], lr = 0.001)
#before training
print('predict (before training)', 4, forward_quad(4))

for epoch in range(10):
  for x_val, y_val in zip(x_data, y_data):
    y_pred = forward_quad(x_val)
    l = loss_quad(x_val, y_val)
    
    optimizer.zero_grad()
    l.backward()
    optimizer.step()

#after training
print("Prediction (after training)",4, forward_quad(4).item())

from torch import nn
import torch
from torch import tensor

x_data = tensor([[1.0], [2.0], [3.0]])
y_data = tensor([[2.0], [4.0], [6.0]])

class Model(nn.Module):
  def __init__(self):
    super(Model, self).__init__()
    self.linear = torch.nn.Linear(1, 1)
  def forward(self, x):
    y_pred = self.linear(x)
    return y_pred

model = Model()

criterion = torch.nn.MSELoss(reduction = 'sum')
optimizer = torch.optim.SGD(model.parameters(), lr = 0.01)

for epoch in range(500):
  #1) Forward pass
  y_pred = model(x_data)
  #2) compute and print loss
  loss = criterion(y_pred, y_data)
  print('Epoch: {}, Loss : {}'.format(epoch, loss.item()))

  #Zero gradients, perform a backward pass and update the weights
  optimizer.zero_grad()
  loss.backward()
  optimizer.step()

#After training
hour_var = tensor([4.0])  
y_pred = model(hour_var)
print('Prediction (after training)', 4, model(hour_var).item())

