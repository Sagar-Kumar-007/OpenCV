# The median blur operation is quite similar to the Gaussian blur. OpenCV provides the medianblur() function to perform the blur operation. It takes the median of all the pixels under the kernel area, and the central element is replaced with this median value. It is extremely effective for the salt-and-paper noise in the image. The kernel size should be a positive odd integer.
import cv2

img = cv2.imread("Sagar.jpg", 1)
img=cv2.resize(img,(int(img.shape[0]*0.5),int(img.shape[1]*0.5)))
img1 = cv2.medianBlur(img,11)
cv2.imshow("Blured image", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
