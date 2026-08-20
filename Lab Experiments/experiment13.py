import cv2
import numpy as np

cap = cv2.VideoCapture("sample.mp4")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    rows, cols = frame.shape[:2]

    pts1 = np.float32([[50,50],[cols-50,50],[50,rows-50],[cols-50,rows-50]])
    pts2 = np.float32([[0,0],[cols,0],[100,rows],[cols-100,rows]])

    matrix = cv2.getPerspectiveTransform(pts1, pts2)

    result = cv2.warpPerspective(frame, matrix, (cols, rows))

    cv2.imshow("Perspective Video", result)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()