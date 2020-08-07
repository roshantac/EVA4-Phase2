"""Code to calculate the mean and standard deviation of dataset.

Author: Srinivasan G
"""
import os
from PIL import Image
import numpy as np
import time


def find_mean_standard_deviation(image_dir):
    """Return the mean and standard deviation of dataset.

    Mean and Standard Deviation required for image normalization.

    Args:
        image_dir: Input directory containing all image

    Returns:
        None

    Raises:
        No Exception
    """
    since = time.time()

    n = 0
    s = np.zeros(3)
    sq = np.zeros(3)

    #data_dir = os.chdir(image_dir)
    image_folders = os.listdir(image_dir)
    print(f'Sub-folders: {image_folders}')

    for sub_dir in image_folders:
        temp = image_dir + sub_dir
        for image_name in os.listdir(temp):
            if image_name.endswith(".jpg"):
                img = Image.open(temp + "/" + image_name)
                x = np.array(img)/255
                s += x.sum(axis=(0, 1))
                sq += np.sum(np.square(x), axis=(0, 1))
                n += x.shape[0]*x.shape[1]
    mean = s/n
    std_deviation = np.sqrt((sq/n - np.square(mean)))

    print(f'Mean: {mean}')
    print(f'Std: {std_deviation}')
    # print(mean, sq/n, std_deviation, n)

    time_elapsed = time.time() - since
    print('Processing completed in {:.0f}m {:.0f}s'.format(
        time_elapsed // 60, time_elapsed % 60))
