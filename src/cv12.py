import cv2

img = cv2.imread('najib.jpg', 1)

img = cv2.line(img, (0,0), (255,255), (100, 20, 71), 10)

img = cv2.arrowedLine(img, (0,0), (255,255), (255, 0, 0), 10)

img = cv2.rectangle(img, (384, 0), (210, 210), (0, 255, 255), -1)

cv2.imshow('image', img)

cv2.waitKey(0)

cv2.destroyAllWindows()