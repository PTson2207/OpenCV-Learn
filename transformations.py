import cv2 as cv
import numpy as np

img = cv.imread('images/cat.36.jpg')
cv.imshow('Cat', img)

def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img, 100, 200)
#cv.imshow("Translated", translated)

def rotation(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotation(img, 45)
cv.imshow('Rotation', rotated)

rotated_rotated = rotation(rotated, 45)
cv.imshow('Rotated Rotation', rotated_rotated)
    



cv.waitKey(0)