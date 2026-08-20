import cv2
import numpy as np

img = cv2.imread("lena.jpg")

rows, cols = img.shape[:2]

src = np.float32([[0,0],[cols-1,0],[0,rows-1],[cols-1,rows-1]])
dst = np.float32([[50,50],[cols-50,30],[30,rows-30],[cols-30,rows-50]])

H, status = cv2.findHomography(src, dst)

result = cv2.warpPerspective(img, H, (cols, rows))

cv2.imshow("Original", img)
cv2.imshow("Homography", result)

cv2.waitKey(0)
cv2.destroyAllWindows()