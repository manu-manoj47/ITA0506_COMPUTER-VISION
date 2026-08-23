import cv2

# Read the input image
img = cv2.imread("lena.jpg")

# Check image
if img is None:
    print("Error: lena.jpg not found")
    exit()

# Get image dimensions
height, width = img.shape[:2]

# Load YuNet face detector
detector = cv2.FaceDetectorYN.create(
    "face_detection_yunet_2023mar.onnx",
    "",
    (width, height),
    0.9,
    0.3,
    5000
)

# Detect faces
_, faces = detector.detect(img)

# Draw detected faces
if faces is not None:

    for face in faces:

        x = int(face[0])
        y = int(face[1])
        w = int(face[2])
        h = int(face[3])

        # Draw rectangle
        cv2.rectangle(
            img,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        # Display label
        cv2.putText(
            img,
            "Face",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

# Display result
cv2.imshow("Face Detection", img)

# Save result
cv2.imwrite("exp38_face_detection.jpg", img)

# Wait for key
cv2.waitKey(0)

# Close windows
cv2.destroyAllWindows()