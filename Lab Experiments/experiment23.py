import cv2

# Read image
img = cv2.imread("lena.jpg")

if img is None:
    print("Error: lena.jpg not found")
    exit()

# Blur image
blur = cv2.GaussianBlur(img, (0, 0), 3)

# Unsharp masking
sharpened = cv2.addWeighted(img, 1.5, blur, -0.5, 0)

cv2.imshow("Original Image", img)
cv2.imshow("Unsharp Masking", sharpened)

cv2.imwrite("exp23_unsharp.jpg", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()