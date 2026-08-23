import cv2

# Read image
img = cv2.imread("lena.jpg")

# Check whether image is loaded
if img is None:
    print("Error: lena.jpg not found")
    exit()

# Create a copy of the image
result = img.copy()

# Define rectangle coordinates
x1 = 100
y1 = 100
x2 = 300
y2 = 300

# Draw rectangle around selected object
cv2.rectangle(
    result,
    (x1, y1),
    (x2, y2),
    (0, 255, 0),
    3
)

# Extract the selected region
extracted_object = img[y1:y2, x1:x2]

# Display original image with rectangle
cv2.imshow("Rectangle Selection", result)

# Display extracted object
cv2.imshow("Extracted Object", extracted_object)

# Save images
cv2.imwrite("exp40_rectangle.jpg", result)
cv2.imwrite("exp40_extracted_object.jpg", extracted_object)

# Wait for key press
cv2.waitKey(0)

# Close windows
cv2.destroyAllWindows()