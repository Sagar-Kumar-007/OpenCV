import cv2

cap=cv2.VideoCapture(0)

face_cascade=cv2.CascadeClassifier("HAAR cascades/haarcascades/haarcascade_frontalface_default.xml")

while cap.isOpened():
    status,frame=cap.read()
    frame=cv2.flip(frame,180)
    res=face_cascade.detectMultiScale(frame,1.2,5)
    for (x,y,w,h) in res:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),5)
    cv2.imshow("Video",frame)
    if cv2.waitKey(1) & 0xFF==27:
        break
cv2.destroyAllWindows()