import cv2

# Read the image
img = cv2.imread("lena.jpg")

# Check if image is loaded
if img is None:
    print("Error: lena.jpg not found")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Sobel operator along X-axis
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)

# Convert result to 8-bit image
sobel_x = cv2.convertScaleAbs(sobel_x)

# Display original image
cv2.imshow("Original Image", img)

# Display Sobel X result
cv2.imshow("Sobel X Edge Detection", sobel_x)

# Save the output
cv2.imwrite("exp17_sobel_x.jpg", sobel_x)

# Wait for key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()