import cv2 as cv

# read images
# img = cv.imread('images/cat.77.jpg')
# cv.imshow('Cat', img)
# read video
capture = cv.VideoCapture('videos/Wildlife.wmv')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) and 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
