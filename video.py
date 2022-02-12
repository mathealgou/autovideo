import cv2 as cv
import numpy as np
from cv2 import VideoWriter, VideoWriter_fourcc

# This is the function that will be called by the main file.
def render(width, height, FPS, seconds, filename):
    # Define the codec and create VideoWriter object
    fourcc = VideoWriter_fourcc(*'XVID')
    video = VideoWriter(f"./{filename}.avi", fourcc, float(FPS), (width, height))
    
    # For every frame of video
    for _ in range(FPS*seconds):

        # Create a black background, which serves as the canvas.
        frame = np.zeros((height, width, 3), np.uint8)

        # Do stuff with the video (text, images, etc.)
        cv.putText(frame, "Test", (640, 360), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        # Write the frame into the file
        video.write(frame)
    #Once the loop is done, release the video writer and close the file.
    video.release()

render(1280, 720, 24, 20, "test")