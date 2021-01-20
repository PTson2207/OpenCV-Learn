import cv2 as cv
# thay doi kich thuoc hinh anh, ti le
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] *scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Photo
img = cv.imread('images/dog.16.jpg')
cv.imshow('Dog', img)

relized_img = rescaleFrame(img)
cv.imshow('Image',relized_img)


# Reding Videos
capture = cv.VideoCapture('videos/Wildlife.wmv')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, scale=.5)
    cv.imshow('Video', frame)
    cv.imshow('Video Relized', frame_resized)
    if cv.waitKey(20) and 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()