# CAMERA CLASS

import time
import cv2
def init_camera():
    global camera
    camera = cv2.VideoCapture(1)
    time.sleep(1)
    
def capture():
    global camera
    ret, frame = camera.read()
    return frame
def show():
    global camera
    ret, frame = cap.read()
    cv2.imshow('Camera',frame)

if __name__ == "__main__":
    init_camera()
    while(True):
        ret, frame = camera.read()
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    camera.release()
    cv2.destroyAllWindows()
