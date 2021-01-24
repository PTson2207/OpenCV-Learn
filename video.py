import cv2

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
while True:
    succes, frame = video.read()
    if not succes:
        break

    cv2.imshow("frame", frame)
    k = cv2.waitKey(1) & 0xff
    
    if k == 27:
        break
    

cv2.destroyAllWindows()
video.release()
