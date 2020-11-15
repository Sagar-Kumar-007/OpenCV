import cv2
import numpy as np

# Creating a black background
img = np.zeros((512, 512,3),np.uint8) # Note that you are giving 3 channels for BGR


# Defining a function for the mouse event:
def func(event, x, y,flag,param):
    if cv2.EVENT_MOUSEMOVE == event:
        cv2.circle(img, (x, y), 10, color=(255, 0, 0), thickness=5)


# Set mouse callback:
# First you need to create a new window using the method namedWindow
cv2.namedWindow("Image")
cv2.setMouseCallback("Image", func) # This uses a function with 5 parameters: Event (mention the event you want to set), coordinates of the mouse etc.
while 1:
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break
cv2.destroyAllWindows()
