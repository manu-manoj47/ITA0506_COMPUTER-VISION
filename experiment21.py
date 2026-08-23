import cv2
import numpy as np

# Read image
img = cv2.imread("lena.jpg")

if img is None:
    print("Error: lena.jpg not found")
    exit()

# Laplacian mask including diagonal neighbors
kernel = np.array([
    [1, 1, 1],
    [1, -8, 1],
    [1, 1, 1]
], dtype=np.float32)

# Apply Laplacian mask
laplacian = cv2.filter2D(img, -1, kernel)

# Sharpen
sharpened = cv2.addWeighted(img, 1, laplacian, 1, 0)

cv2.imshow("Original Image", img)
cv2.imshow("Diagonal Laplacian Sharpening", sharpened)

cv2.imwrite("exp21_diagonal_laplacian.jpg", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()