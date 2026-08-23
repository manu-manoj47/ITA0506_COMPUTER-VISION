import cv2
import numpy as np

# Read image
img = cv2.imread("lena.jpg")

if img is None:
    print("Error: lena.jpg not found")
    exit()

# Create kernel
kernel = np.ones((5, 5), np.uint8)

# Erosion
erosion = cv2.erode(img, kernel, iterations=1)

cv2.imshow("Original Image", img)
cv2.imshow("Erosion", erosion)

cv2.imwrite("exp29_erosion.jpg", erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()