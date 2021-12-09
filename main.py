import cv2
from SignDetector import SignDetector

ports = [1, 0, 99, 100]

for port in ports:
    try:
        cap = cv2.VideoCapture(port)
        detector = SignDetector(cap)
        detector.detect()
    except:
        print(f'No camera at {port}.')
