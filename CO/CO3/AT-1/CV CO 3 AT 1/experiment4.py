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

# Mean Filter
mean = cv2.blur(gray,(5,5))

# Gaussian Filter
gaussian = cv2.GaussianBlur(gray,(5,5),0)

# Median Filter
median = cv2.medianBlur(gray,5)

# SIFT Detector
sift = cv2.SIFT_create()

kp1, des1 = sift.detectAndCompute(mean,None)
kp2, des2 = sift.detectAndCompute(gaussian,None)
kp3, des3 = sift.detectAndCompute(median,None)

img1 = cv2.drawKeypoints(mean,kp1,None)
img2 = cv2.drawKeypoints(gaussian,kp2,None)
img3 = cv2.drawKeypoints(median,kp3,None)

plt.figure(figsize=(18,6))

plt.subplot(1,3,1)
plt.imshow(img1,cmap='gray')
plt.title("Mean Filter")

plt.subplot(1,3,2)
plt.imshow(img2,cmap='gray')
plt.title("Gaussian Filter")

plt.subplot(1,3,3)
plt.imshow(img3,cmap='gray')
plt.title("Median Filter")

plt.tight_layout()
plt.show()

print("--------------------------------")
print("Mean Filter Keypoints :", len(kp1))
print("Gaussian Filter Keypoints :", len(kp2))
print("Median Filter Keypoints :", len(kp3))
print("--------------------------------")