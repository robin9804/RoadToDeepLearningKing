import torch
import torchvision
import numpy as np
import pandas as pd
from torch.utils.data import Dataset
import os
import scipy.io as sio


class MNIST(Dataset):
    """MNIST dataset to test item"""
    def __init__(self, path, transform=None, resolution=1024):
        raw_data = np.array(pd.read_csv(path), dtype=np.float32)
        self.img = raw_data[:, 1:]
        self.target = raw_data[:, 0]
        self.transform = transform
        self.resolution = resolution

    def __len__(self):
        return len(self.target)

    def __getitem__(self, ind):
        target = self.target[ind]
        target = int(target)
        img = self.img[ind, :]
        img = img.reshape(28, -1)
        if self.transform:
            img = self.transform(img)
        return target, img


class GP_SIDH(Dataset):
    """GP-SIDH Dataset loader"""

    def __init__(self, csv_file, path, transform=None):
        self.data_excel = pd.read_csv(csv_file)
        self.root_dir = path
        self.transform = transform

    def __len__(self):
        return len(self.data_excel) - 1

    def __getitem__(self, idx):
        target = self.data_excel.iloc[idx+1, 1]
        fname = self.data_excel.iloc[idx+1, 0]

        ch_name = os.path.join(self.root_dir, target, fname)

        mat = sio.loadmat(ch_name)
        mat = np.array(mat['ch_new'])

        # extract real, imaginary part
        mat_real = np.real(mat)
        mat_imag = np.imag(mat)

        ch = []
        ch.append(mat_real)
        ch.append(mat_imag)
        ch = np.array(ch)

        return target, ch

