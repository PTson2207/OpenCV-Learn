import cv2 as cv
import numpy as np

img = cv.imread("images/dog.16.jpg")
# lấy tọa đồ bằng cách cho vào paint để biết
width, height = 250,350
pts1 = np.float32([[125,90], [267,89], [126,213],  [267,212]])
pts2 = np.float32([[0,0], [width,0], [0,height], [width, height]])
matrix = cv.getPerspectiveTransform(pts1, pts2)
imgOutput = cv.warpPerspective(img, matrix, (width, height))


cv.imshow('Dog', img)
cv.imshow('Cat anh tu anh goc khi biet toa do', imgOutput)

cv.waitKey(0)