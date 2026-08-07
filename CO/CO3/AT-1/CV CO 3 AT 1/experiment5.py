import cv2
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Hide Tkinter window
Tk().withdraw()

# Select image
image_path = askopenfilename(
    title="Select an Image",
    filetypes=[("Image Files","*.jpg *.jpeg *.png *.bmp")]
)

if not image_path:
    print("No image selected.")
    exit()

image = cv2.imread(image_path)

if image is None:
    print("Unable to load image.")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# -----------------------------
# Image Preprocessing
# -----------------------------
blur = cv2.GaussianBlur(gray,(5,5),0)

# -----------------------------
# Edge Detection
# -----------------------------
edges = cv2.Canny(blur,100,200)

# -----------------------------
# Feature Extraction (SIFT)
# -----------------------------
sift = cv2.SIFT_create()

keypoints, descriptors = sift.detectAndCompute(gray,None)

feature_image = cv2.drawKeypoints(
    image,
    keypoints,
    None,
    flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
)

# -----------------------------
# Shape Detection
# -----------------------------
contours, hierarchy = cv2.findContours(
    edges,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

shape_image = image.copy()

cv2.drawContours(shape_image,contours,-1,(0,255,0),2)

# -----------------------------
# Display Results
# -----------------------------
plt.figure(figsize=(16,10))

plt.subplot(2,2,1)
plt.imshow(gray,cmap='gray')
plt.title("Original Image")
plt.axis("off")

plt.subplot(2,2,2)
plt.imshow(edges,cmap='gray')
plt.title("Edge Detection")
plt.axis("off")

plt.subplot(2,2,3)
plt.imshow(cv2.cvtColor(feature_image,cv2.COLOR_BGR2RGB))
plt.title("SIFT Features")
plt.axis("off")

plt.subplot(2,2,4)
plt.imshow(cv2.cvtColor(shape_image,cv2.COLOR_BGR2RGB))
plt.title("Detected Shapes")
plt.axis("off")

plt.tight_layout()
plt.show()

print("--------------------------------")
print("Total SIFT Features :", len(keypoints))
print("Total Objects Found :", len(contours))
print("--------------------------------")