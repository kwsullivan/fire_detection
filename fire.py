import cv2
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
from colorama import Fore, Back, Style

# Implements a fire detection algorithm using back projection and
# various optimizations explained throughout
def fire_detection(space, threshold, input_file, output_file, sample_file, testing_truth):
    # Read in images
    source = cv2.imread(input_file)
    sample = cv2.imread(sample_file)
    if source is None:
        print("Image is none.")
    if sample is None:
        print("Sample is none.")

    # Convert to appropriate colour space (defaults to YCC if unspecified)
    if (space == "HSV"):
        source_converted = cv2.cvtColor(source, cv2.COLOR_BGR2HSV)
        sample_converted = cv2.cvtColor(sample, cv2.COLOR_BGR2HSV)
    elif(space == "YCC"):
        source_converted = cv2.cvtColor(source, cv2.COLOR_BGR2YCR_CB)
        sample_converted = cv2.cvtColor(sample, cv2.COLOR_BGR2YCR_CB)
    else:
        source_converted = cv2.cvtColor(source, cv2.COLOR_BGR2YCR_CB)
        sample_converted = cv2.cvtColor(sample, cv2.COLOR_BGR2YCR_CB)

    # Gather the histogram of the sample image
    if(space == "YCC"):
        sample_hist = cv2.calcHist([sample_converted], [0, 1], None, [16, 235], [16, 240, 16, 240])
    elif(space == "HSV"):
        sample_hist = cv2.calcHist([sample_converted], [0, 1], None, [16, 235], [16, 240, 16, 240])

    # Normalize the histogram from 0-255 range
    cv2.normalize(sample_hist, sample_hist, 0, 255, cv2.NORM_MINMAX)

    # Blur image to produce a smoother mask
    # source_converted = cv2.blur(source_converted, (20,20))
    
    # Gets the back projection from the converted image and sample histogram
    # with preset nominal values
    if(space == "YCC"):
        dst = cv2.calcBackProject([source_converted], [0, 1], sample_hist, [16, 235, 16, 235], 1)
    elif(space == "HSV"):
        dst = cv2.calcBackProject([source_converted], [0, 1], sample_hist, [0, 180, 0, 256], 1)
    
    # Applies the morphing style onto the mask with specified kernel size
    disc = cv2.getStructuringElement(cv2.MORPH_DILATE, (5, 5))
    cv2.filter2D(dst, -1, disc, dst)

    # Binary threshold mask applied to original image to create a mask
    ret, thresh = cv2.threshold(dst, threshold, 255, 0)
    thresh = cv2.merge((thresh, thresh, thresh))
    
    # Creates a closure property on the image
    #kernel = np.ones((15, 15), np.uint8)
    #thresh = cv2.dilate(thresh, kernel, iterations=1)
    #thresh = cv2.erode(thresh, kernel, iterations=1)

    res = cv2.bitwise_and(source, thresh)

    # Stacks all images in one file for simple analysis of algorithm

    if(testing_truth):
        cv2.imwrite(output_file, thresh)
    else:
        res = np.concatenate((source, thresh, res), axis=1)
        cv2.imwrite(output_file, res)
    

# Tests the effectiveness of the image against a ground truth image by
# calculating the difference of the images
# and calculating the difference in black pixels between the images
def image_testing(image, ground_truth):

    truth = cv2.imread(ground_truth)
    image = cv2.imread(image)

    if image.shape == truth.shape:
        truth = cv2.bitwise_not(truth) # inverts binary mask

        white_pixels_truth = np.sum(truth == 255)
        black_pixels_truth = np.sum(truth == 0)

        difference = cv2.absdiff(image, truth)

        white_pixels_diff = np.sum(difference == 255)
        black_pixels_image = np.sum(difference == 0)
    
        calc = ((black_pixels_truth - black_pixels_image) / black_pixels_truth) * 100
        return calc
    return -1

# Prints out the results in colour coding formatted to correlate with its strength
def test_results(result):

    print('This image is', end='')

    if(result >= 90):
        print(Fore.GREEN, Style.BRIGHT, end='')
    elif(70 <= result < 80):
        print(Fore.GREEN, Style.NORMAL, end='')
    elif(60 <= result < 70):
        print(Fore.YELLOW, Style.BRIGHT, end='')
    elif(50 <= result < 60):
        print(Fore.YELLOW, Style.NORMAL, end='')
    else:
        print(Fore.RED, Style.NORMAL, end='')
    
    print('{}%'.format(round(result, 2)), end='')
    print(Style.RESET_ALL, end='')
    print(' of the ground truth.')

if len(sys.argv) == 7:
    fire_detection(sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4], sys.argv[5], 1)
    res = image_testing(sys.argv[4], sys.argv[6])
    
    if res < 0:
        print(Fore.RED, 'Error:',Style.RESET_ALL, 'Images are not the same shape and could not be compared')
    else:
        test_results(res)
else:
    fire_detection(sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4], sys.argv[5], 0)