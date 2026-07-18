import cv2

# Read the image
img = cv2.imread("lena.jpg")

# Check if image is loaded
if img is None:
    print("Image not found!")
else:
    # Apply Gaussian Blur
    blur = cv2.GaussianBlur(img, (15, 15), 0)

    # Display original and blurred images
    cv2.imshow("Original Image", img)
    cv2.imshow("Gaussian Blur Image", blur)

    cv2.waitKey(0)
    cv2.destroyAllWindows()