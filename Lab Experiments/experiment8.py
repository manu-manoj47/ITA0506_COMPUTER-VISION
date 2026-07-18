import cv2

# Read the image
img = cv2.imread("lena.jpg")

# Check if image is loaded
if img is None:
    print("Error: Image not found!")
    exit()

# Scale the image to a bigger size (2x)
bigger = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

# Scale the image to a smaller size (0.5x)
smaller = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Bigger Image", bigger)
cv2.imshow("Smaller Image", smaller)

cv2.waitKey(0)
cv2.destroyAllWindows()