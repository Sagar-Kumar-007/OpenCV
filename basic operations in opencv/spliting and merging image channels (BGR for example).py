import cv2

img = cv2.imread("Sagar.jpg", 1)

#  r, g, b = cv2.split(img)  # This can be used to split the matrix but this is a slow process. Use array indexing whenever possible.

# Array indexing:

# print(img)
r = img[0, :, :]
g = img[:, 0, :]
b = img[:, :, 0]
print(r)
print(g)
print(b)
cv2.imshow("Split_channel", b)

cv2.waitKey(5000)

cv2.destroyAllWindows()