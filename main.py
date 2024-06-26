from ultralytics import YOLO
from pynput.keyboard import Key, Controller
from webcam import Webcam


# Detect posture from webcam.
model = YOLO('yolov8n-pose.pt')
with Webcam() as wc:
    success, img = wc.read()
    results = model(img, stream=True)


# TODO: parse posture from `results`.


# Control keyboard with posture.
kbd = Controller()
for _ in range(5):
    kbd.press('a')
    kbd.release('a')
