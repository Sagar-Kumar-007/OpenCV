import cv2

# You can resize an image by specifying its new height and width to the cv2.resize method.

img = cv2.imread("Sagar.jpg",1)

width = int(img.shape[1]*0.5)

height = int(img.shape[0]*0.3)

img1 = cv2.resize(img, (height, width))

cv2.imshow("New picture", img1)

cv2.waitKey(0)
cv2.destroyAllWindows()