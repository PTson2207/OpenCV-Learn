import cv2


frameWidth = 640
frameHeight = 480
numberCascade = cv2.CascadeClassifier("Resource/haarcascade_russian_plate_number.xml")
color = (255, 0, 255)

#cap = cv2.VideoCapture("videos/car_plate.mp4")
#bạn phải có video về biển số xe để máy có thể detection
cap.set(10, frameWidth)
cap.set(14, frameHeight)
cap.set(10, 150)
while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberPlate = numberCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in numberPlate:
        area = w*h
        if area >  500:
            cv2.rectangle(img, (x,y),(x+w, y+h), (255, 0, 255), 2)
            cv2.putText(img, "Number Plate", (x, y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color, 2)
            imgRoi = img[y:y+h, x:x+w]
            cv2.imshow("ROI", imgRoi)

    cv2.imshow("result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break