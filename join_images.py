import cv2 as cv
import numpy as np

img = cv.imread('images/dog.57.jpg')

imgHor = np.hstack((img, img))
imgVer = np.vstack((img, img))


cv.imshow("Horizontal", imgHor)
cv.imshow("Vertical",imgVer)

cv.waitKey(0)