import cv2
import numpy as np
cap=cv2.VideoCapture(0)
'''img=cv2.imread("red1.jpg")
img=cv2.resize(img,(int(img.shape[0]*0.5),int(img.shape[0]*0.5)))
lower_red=np.array([0,150,0])
upper_red=np.array([170,255,255])
hsv1=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
mask1 = cv2.inRange(hsv1, lower_red, upper_red)
cv2.imshow("Video", mask1)
cv2.waitKey(0)
cv2.destroyAllWindows()'''


while cap.isOpened():
    _,frame=cap.read()
    frame = cv2.flip(frame, 180)
    # First convert BGR image to HSV because color detection is better in hsv than in bgr
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # Now set the hsv (hue, saturation, value) to the color that you wanted to detect.
    lower_red1=np.array([0,120,50])
    upper_red1=np.array([5,255,255])
    lower_red2=np.array([175,120,50])
    upper_red2=np.array([180,255,255])
    # Now we filter out the hsv frame with red color
    mask1=cv2.inRange(hsv,lower_red1,upper_red1)
    mask2=cv2.inRange(hsv,lower_red2,upper_red2)
    # Now we combine all the red colors
    mask=mask1+mask2
    mask=cv2.erode(mask,np.ones((5,5),np.uint8),iterations=1)
    mask=cv2.dilate(mask,np.ones((5,5),np.uint8),iterations=1)
    cv2.imshow("Video",mask)
    if cv2.waitKey(1) & 0xFF==27:
        break
cv2.destroyAllWindows()