import cv2

# Read image
img = cv2.imread("lena.jpg")

if img is None:
    print("Image not found!")
else:
    cv2.imshow("Original Image", img)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale Image", gray)

    cv2.waitKey(0)
    cv2.destroyAllWindows()