import cv2
import numpy as np

# Read the image
img = cv2.imread("lena.jpg")

# Check if image is loaded
if img is None:
    print("Image not found!")
else:
    # Create a 5x5 kernel
    kernel = np.ones((5, 5), np.uint8)

    # Perform dilation
    dilated = cv2.dilate(img, kernel, iterations=1)

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Dilated Image", dilated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()