import cv2

# Read the image
img = cv2.imread("lena.jpg")

# Check if image is loaded
if img is None:
    print("Image not found!")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Canny Edge Detection
    edges = cv2.Canny(gray, 100, 200)

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Grayscale Image", gray)
    cv2.imshow("Canny Edge Detection", edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()