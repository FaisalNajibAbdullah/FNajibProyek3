import numpy as np

import cv2

img = cv2.imread('messi5.jpg')

print(img.shape)

print(img.size)

print(img.dtype)

b,g,r = cv2.split(img)

img = cv2.merge((b,g,r))

bola = img[280:340, 330:390]

img[273:333, 100:160] = bola

cv2.imshow('image', img)

cv2.waitKey(0)

cv2.destroyAllWindows()