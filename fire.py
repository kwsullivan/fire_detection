import cv2
import sys
import numpy as np
import matplotlib.pyplot as plt

def read_values(command_line):
    

# Implements a fire detection algorithm using back projection and 
# various optimizations explained throughout
def fire_detection(space, threshold, input_file, output_file, sample_file):
    
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
    
    # Gets the back projection from the converted image and sample histogram 
    # with preset nominal values
    if(space == "YCC"):
        dst = cv2.calcBackProject([source_converted], [0, 1], sample_hist, [16, 235, 16, 235], 1)
    elif(space == "HSV"):
        dst = cv2.calcBackProject([source_converted], [0, 1], sample_hist, [0, 180, 0, 256], 1)
    
    # Applies the morphing style onto the mask with specified kernel size
    disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (10, 10))
    cv2.filter2D(dst, -1, disc, dst)

    # Binary threshold mask applied to original image to create a mask
    ret, thresh = cv2.threshold(dst, threshold, 255, 0)
    thresh = cv2.merge((thresh, thresh, thresh))
    
    # Mask is dilated to create a more monolithic region
    kernel = np.ones((8, 8), np.uint8)
    thresh = cv2.dilate(thresh, kernel, iterations=1)

    res = cv2.bitwise_and(source, thresh)

    # Stacks all images in one file for simple analysis of algorithm
    #res = np.vstack((source, thresh, res))

    # Writes the image to a file
    cv2.imwrite(output_file, thresh)

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
        print("Truth:", black_pixels_truth)
        print("Image:", black_pixels_image)

        calc = ((black_pixels_truth - black_pixels_image) / black_pixels_truth) * 100
        return calc

        #cv2.imwrite('truth.png', truth)
        #cv2.imwrite('diff.png', difference)
        #cv2.imshow('inverted', image)
        #cv2.waitKey(0)
    else:
        return -1



#for i in str(sys.argv):
print('{}'.format(str(sys.argv)))
#for i in str(sys.argv):
print('{}'.format(str(sys.argv[0])))
print('{}'.format(len(sys.argv)))
lenght = len(sys.argv)
for arg in range(len(sys.argv)):
    print('here')

space       = sys.argv[1]
threshold   = sys.argv[2]
input_file  = sys.argv[3]
output_file = sys.argv[4]
sample_file = sys.argv[5]

fire_detection(space, threshold, input_file, output_file, sample_file)
#fire_detection("YCC", 50, "./fire_grdtruths/s1.jpg", "./output/output_thresh1.jpg", "sample_fire_images.png")
"""
calc = image_testing("./output/output_thresh1.jpg","./fire_grdtruths/s1_flameB.tif")
if calc == -1:
    print('Error: Images are not the same shape and could not be compared')
else:
    print('This image is {}% of the ground truth.'.format(round(calc, 2)))
"""