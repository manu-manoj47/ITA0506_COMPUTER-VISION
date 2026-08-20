import cv2
import numpy as np

img = cv2.imread("lena.jpg")

rows, cols = img.shape[:2]

pts1 = np.float32([[50,50],[250,50],[50,250],[250,250]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)

output = cv2.warpPerspective(img, matrix, (300,300))

cv2.imshow("Original", img)
cv2.imshow("Perspective", output)

cv2.waitKey(0)
cv2.destroyAllWindows()