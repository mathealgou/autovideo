import cv2 as cv
import numpy as np
from cv2 import VideoWriter, VideoWriter_fourcc

width = 1280
height = 720
FPS = 24
seconds = 20

fourcc = VideoWriter_fourcc(*'XVID')
video = VideoWriter('./noise.avi', fourcc, float(FPS), (width, height))

def render():
    for _ in range(FPS*seconds):
        frame = np.zeros((height, width, 3), np.uint8)
        # frame = np.random.randint(0, 20, 
        #                           (height, width, 3), 
        #                           dtype=np.uint8)
        cv.putText(frame, "Press q to quit", (10, 20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        video.write(frame)
    video.release()

render()