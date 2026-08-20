import cv2
import numpy as np

img = cv2.imread("lena.jpg")

rows, cols = img.shape[:2]

src = np.float32([[0,0],[cols-1,0],[0,rows-1],[cols-1,rows-1]])
dst = np.float32([[40,40],[cols-40,20],[20,rows-20],[cols-20,rows-40]])

H = cv2.getPerspectiveTransform(src, dst)

output = cv2.warpPerspective(img, H, (cols, rows))

cv2.imshow("DLT Transformation", output)

cv2.waitKey(0)
cv2.destroyAllWindows()