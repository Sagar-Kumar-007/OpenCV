import cv2

cap = cv2.VideoCapture(0)
# VideoCapture(0) opens the camera and captures a frame...if filename is given, video will play
'''status,frame=cap.read()   # Single frame and also the first frame
cv2.imshow("Image",frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
# print(frame)
'''  # The code in the string is to capture the first frame or say take a photo.
# To display a video, you can capture each frame and use imshow to view the frame in a while loop

while True:
    status, frame = cap.read()
    # We can manipulate the image for each frame
    # cv2.rectangle(frame,(10,10),(50,50),(0,0,255),3)
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Video", frame)
    if cv2.waitKey(1) & 0xFF == ord('s'):   # Note that we are updating / closing the frame every 1 millisecond for continuous capture. If set to zero, the frame will not update till you press any key.
        break
cap.release() # When everything is done, release the capture.
cv2.destroyAllWindows()