import cv2

# Read image
img = cv2.imread("lena.jpg")

if img is None:
    print("Error: lena.jpg not found")
    exit()

# Crop a portion
crop = img[100:300, 100:300]

# Copy and paste at another location
img[200:400, 300:500] = crop

# Display
cv2.imshow("Crop Copy Paste", img)

# Save
cv2.imwrite("exp27_crop_copy_paste.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()