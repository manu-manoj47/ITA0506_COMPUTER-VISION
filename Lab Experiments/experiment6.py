import cv2

cap = cv2.VideoCapture("sample.mp4")

if not cap.isOpened():
    print("❌ Error: Cannot open sample.mp4")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("✅ End of video.")
        break

    cv2.imshow("Video", frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()