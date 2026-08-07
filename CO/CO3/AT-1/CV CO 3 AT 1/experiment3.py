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

# Scale factors
scales = [0.5, 0.75, 1.0, 1.5]

sift = cv2.SIFT_create()

plt.figure(figsize=(16,10))

for i, scale in enumerate(scales):

    resized = cv2.resize(
        gray,
        None,
        fx=scale,
        fy=scale,
        interpolation=cv2.INTER_LINEAR
    )

    keypoints, descriptors = sift.detectAndCompute(resized, None)

    output = cv2.drawKeypoints(
        resized,
        keypoints,
        None,
        flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
    )

    plt.subplot(2,2,i+1)
    plt.imshow(output, cmap='gray')
    plt.title(f"Scale = {scale}\nKeypoints = {len(keypoints)}")
    plt.axis("off")

    print(f"Scale {scale} : {len(keypoints)} keypoints detected")

plt.tight_layout()
plt.show()