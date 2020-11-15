import cv2

img = cv2.imread("Sagar.jpg", 1)
img = cv2.resize(img, (int(img.shape[0] * 0.5), int(img.shape[1] * 0.5)))
cv2.circle(img, (100, 100), 100, (0, 0, 255), 5)  # Thickness ==> +ve : Outline    -ve : Fill
cv2.rectangle(img, (0, 0), (50, 50), (255, 0, 0), -1)
cv2.ellipse(img, (205, 205), (50, 25), 45, 0, 360, (235, 255, 0), -1)
cv2.line(img, (0, 0), (255, 255), (0, 255, 200), 10)
cv2.imshow("Drawing functions", img)  # Note that all the drawings are stored in the same image itself.
cv2.waitKey(0)
cv2.destroyAllWindows()
