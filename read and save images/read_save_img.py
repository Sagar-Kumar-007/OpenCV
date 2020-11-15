import cv2

img = None

def open_img():
    # Opening/ Reading an image
    global img
    img = cv2.imread('Sagar.jpg', 1)  # Note that the image is stored in the form of a 2D matrix with values having the color intensity
    # 1: RGB    0: BW
    # To display the image

    cv2.imshow('image', img)  # In this method, we give a name called the winname and mat refers to the matrix

    cv2.waitKey(5000)  # This is necessary to be required so that the image do not close immediately... parameter given is in time (milliseconds)

    cv2.destroyAllWindows()


def save_img():
    # cv2.imwrite() is used to save the image. Parameters can be file location, the matrix containing the image
    # It returns true or false as the status
    status = cv2.imwrite("image_saved_cv.jpg", img)
    print(f"Save status: {status}")


if __name__ == "__main__":
    open_img()
    save_img()
