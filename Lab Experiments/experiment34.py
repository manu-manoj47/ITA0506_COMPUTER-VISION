import cv2
import numpy as np

# Read image
img = cv2.imread("lena.jpg")

if img is None:
    print("Error: lena.jpg not found")
    exit()

# Kernel
kernel = np.ones((15, 15), np.uint8)

# Top Hat
top_hat = cv2.morphologyEx(
    img,
    cv2.MORPH_TOPHAT,
    kernel
)

cv2.imshow("Original Image", img)
cv2.imshow("Top Hat", top_hat)

cv2.imwrite("exp34_top_hat.jpg", top_hat)

cv2.waitKey(0)
cv2.destroyAllWindows()