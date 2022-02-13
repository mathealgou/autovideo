import terminal as terminal
from typing import List
import cv2 as cv
import numpy as np
from cv2 import VideoWriter, VideoWriter_fourcc

# This is the function that will be called by the main file.
def render(width, height, FPS, seconds, filename, article):

    # Security measures
    if type(width) is not int:
        terminal.error("width must be an integer")
        return "Error: width must be an integer"
    if type(height) is not int:
        terminal.error("height must be an integer")
        return "Error: height must be an integer"
    if type(FPS) is not int:
        terminal.error("FPS must be an integer")
        return "Error: FPS must be an integer"
    if type(seconds) is not int:
        terminal.error("seconds must be an integer")
        return "Error: seconds must be an integer"
    if type(filename) is not str:
        terminal.error("filename must be a string")
        return "Error: filename must be a string"
    if type(article) is not list:
        terminal.error("article must be a list")
        return "Error: article must be a list"
    if type(article[0]) is not str:
        terminal.error("article must be a list of strings")
        return "Error: article must be a list of strings"
    # End of security measures

    # Define the codec and create VideoWriter object
    fourcc = VideoWriter_fourcc(*'XVID')
    video = VideoWriter(f"./{filename}.avi", fourcc, float(FPS), (width, height))


    
    # For every frame of video
    for _ in range(FPS*seconds):

        # Create a black background, which serves as the canvas.
        frame = np.zeros((height, width, 3), np.uint8)

        # Do stuff with the video (text, images, etc.)
        cv.putText(frame, "Test", (640, 360), cv.FONT_HERSHEY_SIMPLEX, 1, (200, 200, 200), 2)

        # Write the frame into the file
        video.write(frame)
    #Once the loop is done, release the video writer and close the file.
    video.release()

    
render(1280, 720, 24, 20, "test", ["test", "test2"])