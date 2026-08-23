import cv2

# Open video
cap = cv2.VideoCapture("sample.mp4")

frames = []

# Read all frames
while True:
    ret, frame = cap.read()

    if not ret:
        break

    frames.append(frame)

cap.release()

# Play frames in reverse
for frame in reversed(frames):

    cv2.imshow("Reverse Video", frame)

    if cv2.waitKey(30) & 0xFF == 27:
        break

cv2.destroyAllWindows()