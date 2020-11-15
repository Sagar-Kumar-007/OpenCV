import cv2

img = cv2.imread('Sagar.jpg', 1)

edges = cv2.Canny(img, 100, 200, L2gradient=True)  # L2gradient uses a more complicated formula to detect edges but it requires high computation power

cv2.imshow("Edges",edges)

cv2.waitKey(0)
cv2.destroyAllWindows()