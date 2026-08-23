import cv2
import numpy as np

# Read watch image
img = cv2.imread("watch.jpg")

if img is None:
    print("Error: watch.jpg not found")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Reduce noise
gray = cv2.GaussianBlur(gray, (9, 9), 2)

# Detect circles
circles = cv2.HoughCircles(
    gray,
    cv2.HOUGH_GRADIENT,
    dp=1.2,
    minDist=50,
    param1=100,
    param2=50,
    minRadius=20,
    maxRadius=300
)

# Draw detected circle
if circles is not None:
    circles = np.uint16(np.around(circles))

    for x, y, r in circles[0]:
        cv2.circle(img, (x, y), r, (0, 255, 0), 3)
        cv2.putText(
            img,
            "Watch",
            (x - 50, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

# Display
cv2.imshow("Watch Recognition", img)

# Save
cv2.imwrite("exp36_watch.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()