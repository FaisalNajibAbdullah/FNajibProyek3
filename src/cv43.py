import cv2 as cv

import numpy as np


img = cv.imread('najib.jpg',0)

_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)


cv.imshow("Image", img)

cv.imshow("THRESH_BINARY", th1)


cv.waitKey(0)

cv.destroyAllWindows()


