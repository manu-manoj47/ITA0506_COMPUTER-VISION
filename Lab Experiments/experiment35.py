import cv2
import numpy as np

# Read image
img = cv2.imread("lena.jpg")

if img is None:
    print("Error: lena.jpg not found")
    exit()

# Kernel
kernel = np.ones((15, 15), np.uint8)

# Black Hat
black_hat = cv2.morphologyEx(
    img,
    cv2.MORPH_BLACKHAT,
    kernel
)

cv2.imshow("Original Image", img)
cv2.imshow("Black Hat", black_hat)

cv2.imwrite("exp35_black_hat.jpg", black_hat)

cv2.waitKey(0)
cv2.destroyAllWindows()