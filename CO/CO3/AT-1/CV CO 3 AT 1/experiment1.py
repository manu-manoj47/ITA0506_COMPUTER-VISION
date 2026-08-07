import cv2
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Hide the Tkinter root window
Tk().withdraw()

# Open file dialog to select an image
image_path = askopenfilename(
    title="Select an Image",
    filetypes=[
        ("Image Files", "*.jpg *.jpeg *.png *.bmp *.tif *.tiff")
    ]
)

# Check if user selected a file
if not image_path:
    print("No image selected.")
    exit()

# Read the image
image = cv2.imread(image_path)

if image is None:
    print("Error: Unable to read the image.")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# -----------------------------
# Harris Corner Detection
# -----------------------------
gray_float = gray.astype("float32")

harris = cv2.cornerHarris(gray_float, 2, 3, 0.04)

harris = cv2.dilate(harris, None)

harris_output = image.copy()

harris_output[harris > 0.01 * harris.max()] = [0, 0, 255]

# -----------------------------
# SIFT Feature Detection
# -----------------------------
try:
    sift = cv2.SIFT_create()
except:
    print("Your OpenCV version does not support SIFT.")
    exit()

keypoints, descriptors = sift.detectAndCompute(gray, None)

sift_output = cv2.drawKeypoints(
    image,
    keypoints,
    None,
    flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
)

# -----------------------------
# Display Results
# -----------------------------
plt.figure(figsize=(14,6))

plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(harris_output, cv2.COLOR_BGR2RGB))
plt.title("Harris Corner Detection")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(sift_output, cv2.COLOR_BGR2RGB))
plt.title("SIFT Feature Detection")
plt.axis("off")

plt.tight_layout()
plt.show()

print("-----------------------------------")
print("Experiment Completed Successfully")
print("Image Selected:", image_path)
print("Total SIFT Keypoints:", len(keypoints))
print("-----------------------------------")