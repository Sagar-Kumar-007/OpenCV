# Template matching is a technique that is used to find the location of template images in a larger image. OpenCV provides the cv2.matchTemplates() function for this purpose. It simply slides the template images over the input image and compares the templates and patch under the input image.
# Steps to match a template:
#   Convert the original image into grayscale image... We convert it into grayscale because template matching works for grayscale images.
#   Take a template which is to be searched and convert it into grayscale
#   Search for the template in the image
#   If the accuracy is greater than the threshold, then mark that points

import cv2
import numpy as np

img_bgr = cv2.imread("Sagar.jpg", 1)
template = cv2.imread("template.jpg", 0)
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
# We want height and width of the template because we will draw a rectangle on the area where the image matches the template.
height, width = template.shape
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)  # TM_CCORR and TM_CCOEFF make the most likely match to the brightest pixel while TM_SQDIFF is the opposite: darkest values are likely matches
# Set a threshold
threshold = 0.8
loc = np.where(res >= threshold)
print(loc)  # (y,x)

for pt in zip(*loc[::-1]):
    print(pt)
    cv2.rectangle(img_bgr, pt, ((pt[0] + width), (pt[1] + height)), (0, 0, 255), 5)
cv2.imshow("Image", img_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
