from ultralytics import YOLO

# Load your pose model
model = YOLO('yolov8n-pose.pt')

# Run prediction
path_to_image = 'https://ultralytics.com/images/bus.jpg'
results = model(path_to_image, show=True, save=True)

# TODO: parse the results into posture.
