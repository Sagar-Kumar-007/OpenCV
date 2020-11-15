import cv2
cap=cv2.VideoCapture(0)

while cap.isOpened():
    status,frame=cap.read()
    # To mirror the live video
    frame=cv2.flip(frame,180)
    cv2.circle(frame,(100,100),50,(255,0,0),10)
    cv2.imshow("Video",frame)
    if cv2.waitKey(1) & 0xFF==ord('s'):
        break
cv2.destroyAllWindows()