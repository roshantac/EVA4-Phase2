# @uther : roshan
import os
import glob
import csv
import random

def split_test_train_data(rootImageDir, tstRatio = 0.1):
	tstFile = open('testData.csv','w', newline='')
	writertst =csv.writer(tstFile)
	trnFile = open('trainData.csv','w', newline='')
	writertrn =csv.writer(trnFile)
	dirs = os.listdir(rootImageDir)
    # Sorting the list as os.listdir return different order everytime.
	dirs.sort()
	print(dirs)
	dircnt = 0
	for fldr in dirs:
		files = glob.glob(rootImageDir+'/'+fldr+'/*.*')
		folderlen= len(files)
		print(folderlen)
		i = 0
		test=[]
		train=[]
		random.shuffle(files)
		for f in files:
			if (i < folderlen*(1 - tstRatio)):
				train.append(f)
			else:
				test.append(f)
			i+=1
		for filename in train:
			filename = filename.replace('\\','/')
			writertrn.writerow([filename,fldr,dircnt])
		for filename in test:
			filename = filename.replace('\\','/')
			writertst.writerow([filename,fldr,dircnt])
		dircnt +=1

#split_test_train_data('data',0.2)
