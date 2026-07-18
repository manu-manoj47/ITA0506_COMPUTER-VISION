import cv2
import numpy as np

# Read the image
img = cv2.imread("lena.jpg")

# Check if image is loaded
if img is None:
    print("Error: Image not found!")
    exit()

# Get image dimensions
rows, cols = img.shape[:2]

# Translation matrix
# Move image 100 pixels to the right and 50 pixels down
M = np.float32([
    [1, 0, 100],
    [0, 1, 50]
])

# Apply translation
translated = cv2.warpAffine(img, M, (cols, rows))

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Translated Image", translated)

cv2.waitKey(0)
cv2.destroyAllWindows()