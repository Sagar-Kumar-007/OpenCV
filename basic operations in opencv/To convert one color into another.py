import cv2

img = cv2.imread("Sagar.jpg",1)

img_updated = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # src: The image to which the method is to be applied
cv2.imshow("New image", img_updated)
# cv2.waitKey(0)  # 0: press any key to exit

# To exit the window after pressing a certain key, you can use the ord('name of the key') and equate it to the wait key:

k = cv2.waitKey(0) & 0xFF
print(k)
print(type(k))
if k == ord('s'):    # wait for ESC key to exit
    status = cv2.imwrite("trialcv.jpg",img_updated)
    print(status)
    print("Esc is pressed")