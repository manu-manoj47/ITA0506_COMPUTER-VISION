import cv2

# Read the image
img = cv2.imread("lena.jpg")

# Check if image is loaded
if img is None:
    print("Error: Image not found!")
    exit()

# Rotate 90 degrees clockwise
clockwise = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# Rotate 90 degrees counter-clockwise
counter_clockwise = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

# Rotate 180 degrees
rotate_180 = cv2.rotate(img, cv2.ROTATE_180)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("90 Degree Clockwise", clockwise)
cv2.imshow("90 Degree Counter-Clockwise", counter_clockwise)
cv2.imshow("180 Degree Rotation", rotate_180)

cv2.waitKey(0)
cv2.destroyAllWindows()