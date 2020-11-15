import cv2

cap = cv2.VideoCapture(0)

while 1:
    status, frame = cap.read()
    frame1 = cv2.Canny(frame, 100, 100)
    cv2.imshow("Original video",frame)
    cv2.imshow("Realtime edge detection",frame1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()