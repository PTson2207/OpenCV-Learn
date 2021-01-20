import cv2 as cv

img = cv.imread('images/dog.57.jpg')
cv.imshow('Dog', img)

# Converting to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# Blur
# blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# Edge Casecode
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

#Dilating the image
dilated = cv.dilate(canny, (3, 3), iterations=1)
cv.imshow('Dilated', dilated)

# Erading
eroded = cv.erode(dilated, (3, 3), iterations=1)
cv.imshow('Erode', eroded)

#Resize
resize = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resize', resize)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

print(img.shape)

cv.waitKey(0)