import cv2
import numpy as np

# Read image
img = cv2.imread("lena.jpg")

if img is None:
    print("Error: lena.jpg not found")
    exit()

# Kernel
kernel = np.ones((5, 5), np.uint8)

# Dilation
dilation = cv2.dilate(img, kernel, iterations=1)

cv2.imshow("Original Image", img)
cv2.imshow("Dilation", dilation)

cv2.imwrite("exp30_dilation.jpg", dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()