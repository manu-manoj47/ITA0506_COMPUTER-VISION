import cv2
import numpy as np

# Read image
img = cv2.imread("lena.jpg")

if img is None:
    print("Error: lena.jpg not found")
    exit()

# Kernel
kernel = np.ones((5, 5), np.uint8)

# Morphological gradient
gradient = cv2.morphologyEx(
    img,
    cv2.MORPH_GRADIENT,
    kernel
)

cv2.imshow("Original Image", img)
cv2.imshow("Morphological Gradient", gradient)

cv2.imwrite("exp33_morphological_gradient.jpg", gradient)

cv2.waitKey(0)
cv2.destroyAllWindows()