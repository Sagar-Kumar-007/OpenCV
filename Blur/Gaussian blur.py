# Image smoothing is a technique which helps in reducing the noise in the images. Image may contain various type of noise because of camera sensor. It basically eliminates the high frequency (noise, edge) content from the image so edges are slightly blurred in this operation. OpenCV provide gaussianblur() function to apply smoothing on the images.
import cv2

img = cv2.imread("Sagar.jpg", 1)
img=cv2.resize(img,(int(img.shape[0]*0.5),int(img.shape[1]*0.5)))
img1 = cv2.GaussianBlur(img,(5,5),cv2.BORDER_DEFAULT)
cv2.imshow("Blured image", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
