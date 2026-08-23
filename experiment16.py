import cv2

# Read the image
img = cv2.imread("lena.jpg")

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection
edges = cv2.Canny(gray, 100, 200)

# Display the images
cv2.imshow("Original Image", img)
cv2.imshow("Canny Edge Detection", edges)

# Save the output
cv2.imwrite("exp16_canny.jpg", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()