# Usage:
#
# python3 script.py --input original.png --output modified.png
# Based on: https://github.com/mostafaGwely/Structural-Similarity-Index-SSIM-

# 1. Import the necessary packages
from skimage.measure import compare_ssim
import argparse
import imutils
import cv2

'''
# 2. Construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--first", required=True, help="Directory of the image that will be compared")
ap.add_argument("-s", "--second", required=True, help="Directory of the image that will be used to compare")
args = vars(ap.parse_args())

# 3. Load the two input images
imageA = cv2.imread(args["first"])
imageB = cv2.imread(args["second"])
'''

import os

target_dir = './Test_results/VTON_in2000_step200k_mesh/test/try-on/'
gt_dir = './data_2000/test/image/'

count = 0
tot_score = 0

for filename in os.listdir(target_dir):
    imageA = cv2.imread(target_dir + filename)
    imageB = cv2.imread(gt_dir + filename)

    # 4. Convert the images to grayscale
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

    # 5. Compute the Structural Similarity Index (SSIM) between the two
    #    images, ensuring that the difference image is returned
    (score, diff) = compare_ssim(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")
    count += 1
    tot_score += score
    #print(score)

score = tot_score / count

# 6. You can print only the score if you want
print("SSIM: {}".format(score))