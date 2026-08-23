import cv2
import numpy as np

# Read image
img = cv2.imread("lena.jpg")

if img is None:
    print("Error: lena.jpg not found")
    exit()

# Kernel
kernel = np.ones((5, 5), np.uint8)

# Opening = Erosion followed by Dilation
opening = cv2.morphologyEx(
    img,
    cv2.MORPH_OPEN,
    kernel
)

cv2.imshow("Original Image", img)
cv2.imshow("Opening", opening)

cv2.imwrite("exp31_opening.jpg", opening)

cv2.waitKey(0)
cv2.destroyAllWindows()