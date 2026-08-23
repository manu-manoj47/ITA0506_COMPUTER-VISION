import cv2

# Read image
img = cv2.imread("lena.jpg")

if img is None:
    print("Error: lena.jpg not found")
    exit()

# Blur image
blur = cv2.GaussianBlur(img, (0, 0), 5)

# High-boost filtering
high_boost = cv2.addWeighted(img, 2.0, blur, -1.0, 0)

cv2.imshow("Original Image", img)
cv2.imshow("High Boost Image", high_boost)

cv2.imwrite("exp24_highboost.jpg", high_boost)

cv2.waitKey(0)
cv2.destroyAllWindows()