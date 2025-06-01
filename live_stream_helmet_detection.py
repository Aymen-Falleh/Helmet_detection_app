import cv2
from ultralytics import YOLO

#Use the mobile phone as a webcam
# with the app IP Webcam (Android) or similar app
# Replace this with your phone's IP webcam video URL
stream_url = 'http://192.168.1.100:8080/video'  # Adjust the IP and port

# Load your trained YOLO model
model = YOLO("best.pt")

# Open the video stream
cap = cv2.VideoCapture(stream_url)

if not cap.isOpened():
    print("Error: Could not open video stream")
    exit()

print("Starting video stream... Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Run YOLO on the frame
    results = model(frame, stream=True)

    # Plot detections on the frame
    for result in results:
        annotated_frame = result.plot()

    # Show the frame
    cv2.imshow("Helmet Detection - Live Stream", annotated_frame)

    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
cap.release()
cv2.destroyAllWindows()
