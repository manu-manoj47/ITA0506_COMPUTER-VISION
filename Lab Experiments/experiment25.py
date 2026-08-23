import cv2

# Read image
img = cv2.imread("lena.jpg")

if img is None:
    print("Error: lena.jpg not found")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Calculate X gradient
gx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)

# Calculate Y gradient
gy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Calculate gradient magnitude
gradient = cv2.magnitude(
    gx.astype("float32"),
    gy.astype("float32")
)

# Convert to 8-bit
gradient = cv2.convertScaleAbs(gradient)

cv2.imshow("Original Image", img)
cv2.imshow("Gradient Mask", gradient)

cv2.imwrite("exp25_gradient.jpg", gradient)

cv2.waitKey(0)
cv2.destroyAllWindows()