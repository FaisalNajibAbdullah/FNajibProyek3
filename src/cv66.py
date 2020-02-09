import cv2

import numpy as np

from matplotlib import pyplot as plt


img = cv2.imread("najib.jpg", cv2.IMREAD_GRAYSCALE)

lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)

lap = np.uint8(np.absolute(lap))

sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)


sobelX = np.uint8(np.absolute(sobelX))


titles = ['image', 'Laplacian', 'sobelX']

images = [img, lap, sobelX]


for i in range(3):

    plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')

    plt.title(titles[i])

    plt.xticks([]),plt.yticks([])

plt.show()