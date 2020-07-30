# @uther : Roshan


import csv
from PIL import Image
import torch
from torch.utils.data import Dataset
from torch.utils.data import DataLoader, random_split
import numpy as np


class DroneDataset(Dataset):
	def __init__(self, train=True, transform = None):
		self.train = train
		self.transform = transform
		if (self.train == True):
			data_file = open('trainData.csv','r')
		else:
			data_file = open('testData.csv','r')
		
		self.data = list(csv.reader(data_file))
		self.classes = ("Flying Birds", "Large QuadCopters", "Small QuadCopters", "Winged Drones")

	def __len__(self):
		return len(self.data)

	def __getitem__(self,idx):
		imgLoc, target =self.data[idx][0], self.data[idx][2]
		image = np.array(Image.open("/content/drive/My Drive/Phase2_S2/final_images/"+imgLoc))
		if (len(image.shape) == 2) or (len(image.shape)==3 and image.shape[-1]==1):
			image =np.stack((image,)*3, axis =-1)
		if self.transform :
			image = self.transform(Image.fromarray(image))
		return image, target
