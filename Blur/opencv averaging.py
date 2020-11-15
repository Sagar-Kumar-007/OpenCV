# Blurring is the commonly used technique for image processing to removing the noise. It is generally used to eliminate the high-frequency content such as noise, edges in the image. The edges are being blurred when we apply blur to the image.
# Opencv Averaging:
# In this technique, the image is convolved with a box filter (normalize). It calculates the average of all the pixels which are under the kernel area and replaces the central element with the calculated average. OpenCV provides the cv2.blur() or cv2.boxFilter() to perform this operation. We should define the width and height of the kernel.

import cv2

img = cv2.imread("Sagar.jpg", 1)
img=cv2.resize(img,(int(img.shape[0]*0.5),int(img.shape[1]*0.5)))
img1 = cv2.blur(img, (3, 3))
cv2.imshow("Blured image", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
