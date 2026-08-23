import cv2

# Read image
img = cv2.imread("lena.jpg")

if img is None:
    print("Error: lena.jpg not found")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Sobel X
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)

# Sobel Y
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Combine X and Y
sobel_xy = cv2.magnitude(
    sobel_x.astype("float32"),
    sobel_y.astype("float32")
)

# Convert to 8-bit
sobel_xy = cv2.convertScaleAbs(sobel_xy)

# Display
cv2.imshow("Original Image", img)
cv2.imshow("Sobel XY", sobel_xy)

# Save
cv2.imwrite("exp19_sobel_xy.jpg", sobel_xy)

cv2.waitKey(0)
cv2.destroyAllWindows()