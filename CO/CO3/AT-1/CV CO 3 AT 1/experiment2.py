import cv2
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Hide tkinter window
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

# Histogram Equalization
hist_eq = cv2.equalizeHist(gray)

# Contrast Adjustment
alpha = 1.8
beta = 20

contrast = cv2.convertScaleAbs(gray, alpha=alpha, beta=beta)

# Create SIFT detector
sift = cv2.SIFT_create()

kp1, des1 = sift.detectAndCompute(gray, None)
kp2, des2 = sift.detectAndCompute(hist_eq, None)
kp3, des3 = sift.detectAndCompute(contrast, None)

img1 = cv2.drawKeypoints(gray, kp1, None)
img2 = cv2.drawKeypoints(hist_eq, kp2, None)
img3 = cv2.drawKeypoints(contrast, kp3, None)

plt.figure(figsize=(18,6))

plt.subplot(1,3,1)
plt.imshow(img1,cmap='gray')
plt.title("Original Image")

plt.subplot(1,3,2)
plt.imshow(img2,cmap='gray')
plt.title("Histogram Equalization")

plt.subplot(1,3,3)
plt.imshow(img3,cmap='gray')
plt.title("Contrast Adjustment")

plt.tight_layout()
plt.show()

print("----------------------------------")
print("Original Features :", len(kp1))
print("Histogram Equalization Features :", len(kp2))
print("Contrast Adjustment Features :", len(kp3))
print("----------------------------------")