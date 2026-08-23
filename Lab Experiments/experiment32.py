import cv2
import numpy as np

# Read image
img = cv2.imread("lena.jpg")

if img is None:
    print("Error: lena.jpg not found")
    exit()

# Kernel
kernel = np.ones((5, 5), np.uint8)

# Closing = Dilation followed by Erosion
closing = cv2.morphologyEx(
    img,
    cv2.MORPH_CLOSE,
    kernel
)

cv2.imshow("Original Image", img)
cv2.imshow("Closing", closing)

cv2.imwrite("exp32_closing.jpg", closing)

cv2.waitKey(0)
cv2.destroyAllWindows()