import cv2

# Read image
img = cv2.imread("lena.jpg")

if img is None:
    print("Error: lena.jpg not found")
    exit()

# Add watermark text
watermark = "OPEN CV"

cv2.putText(
    img,
    watermark,
    (50, 450),
    cv2.FONT_HERSHEY_SIMPLEX,
    1.5,
    (255, 255, 255),
    3
)

# Display
cv2.imshow("Watermarked Image", img)

# Save
cv2.imwrite("exp26_watermark.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()