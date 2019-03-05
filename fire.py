import cv2
import sys
import numpy as np
import matplotlib.pyplot as plt

def fireDetection(space, threshold, input_file, output_file, sample_file):
    
    # Read in images
    source = cv2.imread(input_file)
    sample = cv2.imread(sample_file)

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
        sample_hist = cv2.calcHist([sample_converted], [0, 1], None, [180, 256], [0, 180, 0, 256])

    # Normalize the histogram from 0-255 range
    cv2.normalize(sample_hist, sample_hist, 0, 255, cv2.NORM_MINMAX)

    # Blur image to produce a smoother mask
    source_converted = cv2.blur(source_converted, (15,15))
    
    # Gets the back projection from the converted image and sample histogram with preset nominal values
    if(space == "YCC"):
        dst = cv2.calcBackProject([source_converted], [0, 1], sample_hist, [16, 235, 16, 235], 1)
    elif(space == "HSV"):
        dst = cv2.calcBackProject([source_converted], [0, 1], sample_hist, [0, 180, 0, 256], 1)
    
    # Applies the morphing style onto the mask with specified kernel size
    disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (10, 10))
    cv2.filter2D(dst, -1, disc, dst)

    # threshold and binary AND
    ret, thresh = cv2.threshold(dst, threshold, 255, 0)
    thresh = cv2.merge((thresh, thresh, thresh))
    res = cv2.bitwise_and(source, thresh)

    kernel = np.ones((8, 8), np.uint8)
    #erosion = cv2.erode(res, kernel, iterations = 1)
    dilation = cv2.dilate(thresh, kernel, iterations=1)
    #res = np.vstack((source, thresh, res))

    #cv2.imwrite(output_file, res)
    cv2.imwrite(output_file, thresh)


fireDetection("YCC", 50, "./fire_grdtruths/s1.jpg", "./output/output_thresh1.jpg", "sample_fire_images.png")
"""
truth = cv2.imread("./fire_grdtruths/s1_flameB.tif")
image = cv2.imread("./output/output_thresh.jpg")

if image.shape == truth.shape:
    print("images are equal")
    
    truth = cv2.bitwise_not(truth) # inverts binary mask

    white_pixels_truth = np.sum(truth == 255)
    black_pixels_truth = np.sum(truth == 0)

    difference = cv2.absdiff(image, truth)

    white_pixels_diff = np.sum(difference == 255)
    black_pixels_diff = np.sum(difference == 0)
    print("Number of white pixels truth: ", white_pixels_truth)
    print("Number of white pixels diff: ", white_pixels_diff)
    print("Number of black pixels truth: ", black_pixels_truth)
    print("Number of black pixels diff: ", black_pixels_diff)

    cv2.imwrite('truth.png', truth)
    cv2.imwrite('diff.png', difference)
    #cv2.imshow('inverted', image)
    #cv2.waitKey(0)
else:
    print("images are not equal")
"""