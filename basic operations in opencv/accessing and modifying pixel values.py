import cv2

img_matrix = cv2.imread("Sagar.jpg", 1)  # imread() returns an image matrix with rgb values if the image is colored and the intensity of the light if it is a grayscale image

# Accessing pixel values:

pixel = img_matrix[100, 100]
print(pixel)  # Prints RGB values

img_matrix_BW = cv2.imread("Sagar.jpg",0) # BW image
pixel = img_matrix_BW[100, 100]
print(pixel)  # Prints intensity of the light.

# Modifying this can change the image visually