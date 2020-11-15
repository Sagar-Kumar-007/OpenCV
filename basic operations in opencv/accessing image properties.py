import cv2

img = cv2.imread("Sagar.jpg", 1)

# In OpenCV, images are generally stored in the Numpy ndarray. To get the image shape or size, use ndarray.shape to find the dimension of the image.
print(f"Dimensions: {img.shape}")
print(f"Height: {img.shape[0]}")
print(f"Width: {img.shape[1]}")
print(f"Channels (color): {img.shape[2]}")  # For RGB it is 3 and none for BW image
print(f"Image size: {img.size}")