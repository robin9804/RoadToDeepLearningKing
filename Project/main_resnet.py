"""
Depth 추정 문제를 regression을 통해서 해결하는 모델
Resnet50과 efficeint net L2 등을 활용하여 홀로그램 데이터의 auto-focusing을 훈련한다.
"""
from __future__ import print_function

import numpy as np
import os
import torch
import torch.optim as optim
import torch.backends.cudnn as cudnn
from torch.utils.data import DataLoader
from torchvision import transforms
import matplotlib.pyplot as plt

import gc

import argparse

# custom program loader
from model import SimpleModel, Resnet
import Dataloader


# argparser를 활용한
# Training settings
parser = argparse.ArgumentParser(description='PyTorch Super Res Example')
parser.add_argument('--batchSize', type=int, default=2, help='training batch size')
parser.add_argument('--nEpochs', type=int, default=500, help='number of epochs to train for')
parser.add_argument('--start_iter', type=int, default=1, help='Starting Epoch')
parser.add_argument('--lr', type=float, default=1e-4, help='Learning Rate. Default=0.01')
parser.add_argument('--gpu_mode', type=bool, default=True)
parser.add_argument('--data_dir', type=str, default='/data/MNIST')
parser.add_argument('--model_type', type=str, default='SimpleNet')
parser.add_argument('--save_folder', default='Save/', help='Location to save checkpoint models')


def print_network(net):
    num_params = 0
    for param in net.parameters():
        num_params += param.numel()
    print(net)
    print('Total number of parameters: %d' % num_params)


def checkpoint(epoch):
    model_out_path = opt.save_folder + opt.model_type + "_epoch_{}.pth".format(
        epoch)
    torch.save(model.state_dict(), model_out_path)
    print("Checkpoint saved to {}".format(model_out_path))


# parser argments
opt = parser.parse_args()       # parser 객체 선언

batch_size = opt.batchSize
nEpochs = opt.nEpochs
learning_rate = opt.lr
data_dir = './data/MNIST/mnist_train.csv'  #os.path.join(opt.data_dir, 'mnist_train.csv')
test_dir = './data/MNIST/mnist_test.csv'  #os.path.join(opt.data_dir, 'mnist_test.csv')

device = 'cuda'


cudnn.benchmark = True          # cudnn 사용 여부
torch.cuda.empty_cache()        # CUDA에 캐시 제거하는것
print(opt)

cuda = opt.gpu_mode
if cuda and not torch.cuda.is_available():
    raise Exception('No GPU found, please run with out CUDA')

# load data
transform = transforms.Compose(
    [ transforms.ToTensor(),
      transforms.Resize(512),
      transforms.Normalize(0.5, 0.5)  # 1 channel 이라서 [1]
     ])


train_dataset = Dataloader.MNIST(data_dir, transform=transform)
test_dataset = Dataloader.MNIST(test_dir, transform=transform)

train_loader = DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(dataset=test_dataset, batch_size=batch_size, shuffle=True)

###############
# Load models #
###############

#model = SimpleModel.SimpleNet()
model = Resnet.ResNet18()
model.to(device)

###################
# Set up training #
###################

# cross entropy loss 설정
loss = torch.nn.CrossEntropyLoss()
loss.to(device)

# optimizer 설정
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

#################
# Training loop #
#################
epoch_loss_list = []


model.train()
for i in range(10):
    epoch_loss = 0

    for k, data in enumerate(train_loader):
        target, image = data
        target = target.to(device)
        image = image.to(device)

        optimizer.zero_grad()

        prediction = model(image)

        losses = loss(prediction, target)

        epoch_loss += losses.data
        losses.backward()
        optimizer.step()

        gc.collect()
        torch.cuda.empty_cache()

        if k % 10 == 0:
            print("===> Epoch[{}]({}/{}): Loss_recon: {:.4f}".format(i, k, len(train_loader), losses.data))

    epoch_loss_list.append(epoch_loss)
    print("===> Epoch {} Complete: Avg. Loss: {:.4f}".format(i, epoch_loss / len(train_loader)))


#################
# Validation loop #
#################

model.eval()
test_loss = 0
test_accuracy = 0

for target, data in test_loader:
    target = target.to(device)
    data = data.to(device)

    outputs = model(data)

    test_loss = loss(outputs, target).item()
    pred = outputs.data.max(1, keepdim=True)[1]
    test_accuracy += pred.eq(target.data.view_as(pred)).sum()

test_loss /= len(test_loader.dataset)
print('Test set: Average loss: {:.4f}, Accuracy: {:.0f}%)'.format(test_loss, 100. * test_accuracy / len(test_loader.dataset)))


plt.plot(epoch_loss_list)
plt.show()