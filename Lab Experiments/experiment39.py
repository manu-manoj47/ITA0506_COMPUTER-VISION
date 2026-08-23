import cv2

# Open the video
cap = cv2.VideoCapture("video.mp4")

# Check whether video is opened
if not cap.isOpened():
    print("Error: vehicles.mp4 not found")
    exit()

# Create background subtractor
background_subtractor = cv2.createBackgroundSubtractorMOG2(
    history=500,
    varThreshold=50,
    detectShadows=True
)

while True:

    # Read one frame
    ret, frame = cap.read()

    if not ret:
        break

    # Remove background
    mask = background_subtractor.apply(frame)

    # Remove shadows and small noise
    _, threshold = cv2.threshold(
        mask,
        200,
        255,
        cv2.THRESH_BINARY
    )

    # Find contours
    contours, _ = cv2.findContours(
        threshold,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    # Detect vehicle-like objects
    for contour in contours:

        area = cv2.contourArea(contour)

        # Ignore very small objects
        if area > 500:

            x, y, w, h = cv2.boundingRect(contour)

            # Draw rectangle
            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            # Display label
            cv2.putText(
                frame,
                "Vehicle",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

    # Show result
    cv2.imshow("Vehicle Detection", frame)

    # Press ESC to exit
    if cv2.waitKey(30) & 0xFF == 27:
        break

# Release video
cap.release()

# Close windows
cv2.destroyAllWindows()