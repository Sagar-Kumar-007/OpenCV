import cv2

cap = cv2.VideoCapture(0)

point1 = None
point2 = None


def func(event, x, y, flags, params):
    # print(event)
    if event == cv2.EVENT_MOUSEMOVE:
        global point1
        global point2
        point1 = (x-5, y-5)
        point2 = (x + 5, y + 5)


cv2.namedWindow("Video")
cv2.setMouseCallback("Video", func)
while 1:
    status, frame = cap.read()
    # print(status)

    cv2.rectangle(frame, point1, point2, (0, 255, 255), thickness=10)
    cv2.imshow("Video", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
cv2.destroyAllWindows()
