import cv2
eye_cascade=cv2.CascadeClassifier("HAAR cascades/haarcascades/haarcascade_eye.xml")
face_cascade=cv2.CascadeClassifier("HAAR cascades/haarcascades/haarcascade_frontalface_default.xml")

cap=cv2.VideoCapture(0)

while cap.isOpened():
    status,frame=cap.read()
    frame=cv2.flip(frame,180)
    face=face_cascade.detectMultiScale(frame,1.2,5)
    eyes=eye_cascade.detectMultiScale(frame,1.2,5)
    for (x,y,w,h) in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0))
    for (x,y,w,h) in eyes:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0))
    cv2.imshow("Video",frame)
    if cv2.waitKey(1) & 0xFF==27:
        break
cv2.destroyAllWindows()