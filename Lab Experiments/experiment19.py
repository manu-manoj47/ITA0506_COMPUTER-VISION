import cv2

# Read image
img = cv2.imread("lena.jpg")

if img is None:
    print("Error: lena.jpg not found")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Sobel operator along Y-axis
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Convert to 8-bit
sobel_y = cv2.convertScaleAbs(sobel_y)

# Display
cv2.imshow("Original Image", img)
cv2.imshow("Sobel Y Edge Detection", sobel_y)

# Save
cv2.imwrite("exp18_sobel_y.jpg", sobel_y)

cv2.waitKey(0)
cv2.destroyAllWindows()