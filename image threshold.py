# The basic concept of the threshold is that more simplify the visual data for analysis. When we convert the image into gray-scale, we have to remember that grayscale still has at least 255 values. The threshold is converted everything to white or black, based on the threshold value. Let's assume we want the threshold to be 125(out of 255), then everything that was under the 125 would be converted to 0 or black, and everything above the 125 would be converted to 255, or white.
import cv2
img=cv2.imread("Sagar.jpg")
status,img1=cv2.threshold(img,thresh=100,maxval=255,type=cv2.THRESH_BINARY)
cv2.imshow("Threshold",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()