import cv2

detector = cv2.CascadeClassifier('fullbody.xml')
img = cv2.imread('images/sample1.jpg', cv2.IMREAD_COLOR)

Id = "out_sampe"

while(True):

    body = detector.detectMultiScale(img, 1.1, 4)
    for (x, y, w, h) in body :
        cv2.rectangle(img, (x,y), (x+w, y+w), (255, 0, 0), 2)

        # lưu ảnh body vào thư mục
        cv2.imwrite(r"images/" + Id + "jpg", img[y:y+h, x:x+w])

        # xem ảnh cắt được 
        cv2.imshow('frame', img)

        # Nhấn q để rời
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()