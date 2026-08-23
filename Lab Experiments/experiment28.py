import cv2
import numpy as np

# Read image
img = cv2.imread("lena.jpg")

if img is None:
    print("Error: lena.jpg not found")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Boundary detection kernel
kernel = np.array([
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
])

# Apply convolution
boundary = cv2.filter2D(gray, -1, kernel)

# Convert to absolute values
boundary = cv2.convertScaleAbs(boundary)

cv2.imshow("Original Image", img)
cv2.imshow("Boundary Detection", boundary)

cv2.imwrite("exp28_boundary.jpg", boundary)

cv2.waitKey(0)
cv2.destroyAllWindows()