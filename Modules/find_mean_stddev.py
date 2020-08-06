import os
#calculate STd and Mean
from tqdm import notebook
from PIL import Image
import numpy as np

def find_mean_standard_deviation(image_dir) :
    n = 0
    s = np.zeros(3)
    sq = np.zeros(3)

    data_dir = os.chdir(image_dir) 
    image_folders = os.listdir()
    print(image_folders)

    for sub_dir in image_folders :
        temp = image_dir + sub_dir
        current_dir = next(os.walk(temp))[2]
        file_count = 0
        for image_name in os.listdir(temp):
            file_count = file_count + 1
            if image_name.endswith(".jpg"): 
                img = Image.open(temp +"/" +image_name)
                x = np.array(img)/255
                s += x.sum(axis=(0,1))
                sq += np.sum(np.square(x), axis=(0,1))
                n += x.shape[0]*x.shape[1]
            continue
        print(len(current_dir), file_count)
    mean = s/n
    std_deviation = np.sqrt((sq/n - np.square(mean)))
    print(mean, sq/n, std_deviation, n)