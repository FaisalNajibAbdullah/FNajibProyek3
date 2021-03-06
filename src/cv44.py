import cv2 as cv

import numpy as np


img = cv.imread('najib.jpg',0)

_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2);


cv.imshow("Image", img)

cv.imshow("THRESH_BINARY", th1)

cv.imshow("ADAPTIVE_THRESH_MEAN_C", th2)


cv.waitKey(0)

cv.destroyAllWindows()