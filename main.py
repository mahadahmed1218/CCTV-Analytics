import cv2
from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# Open webcam
cap = cv2.VideoCapture(0)

# Define MP4 codec (more compatible)
fourcc = cv2.VideoWriter_fourcc(*'avc1')  # H.264 codec
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLOv8 detection
    results = model(frame)
    annotated_frame = results[0].plot()

    # Write frame to file
    out.write(annotated_frame)

    # Show live video
    cv2.imshow('YOLOv8 Detection', annotated_frame)

    # Stop with "q" key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
