import cv2

import numpy as np

from matplotlib import pyplot as plt


img = cv2.imread('smarties.png', cv2.IMREAD_GRAYSCALE)

_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernal = np.ones((5,5), np.uint8)

dilation = cv2.dilate(mask, kernal, iterations=2)

erosion = cv2.erode(mask, kernal, iterations=3)

titles = ['image', 'mask', 'dilation', 'erosion']

images = [img, mask, dilation, erosion]


for i in range(4):

    plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')

    plt.title(titles[i])

    plt.xticks([]),plt.yticks([])

plt.show()
