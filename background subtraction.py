import cv2

cap=cv2.VideoCapture(0)
subtract = cv2.createBackgroundSubtractorMOG2()
while cap.isOpened():
    status,frame=cap.read()
    foreground=subtract.apply(frame)
    cv2.imshow("Foreground",foreground)
    cv2.imshow("Video",frame)
    if cv2.waitKey(1) & 0xFF==27:
        break
cv2.destroyAllWindows()