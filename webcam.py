import cv2

class Webcam:

    def __init__(self):
        self._cap = None
        
    def __enter__(self):
        self._cap = cv2.VideoCapture(0)
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self._cap.release()
    
    def read(self):
        return self._cap.read()
