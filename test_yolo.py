from ultralytics import YOLO


# Load your pose model
model = YOLO('yolov8n-pose.pt')

# Run prediction
results = model(source=0, show=True, conf=0.3, save=True)

# TODO: parse the results into posture.
