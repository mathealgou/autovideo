import textwrap
import time
from typing import List
import terminal as terminal
import cv2 as cv
import numpy as np
from cv2 import VideoWriter, VideoWriter_fourcc


# This is the function that will be called by the main file.
def render(width: int, height: int, FPS: float, seconds: float, filename: str, article: List[dict]):

    # Define the codec and create VideoWriter object
    fourcc = VideoWriter_fourcc(*'XVID')
    video = VideoWriter(f"./{filename}.avi", fourcc,
                        float(FPS), (width, height))

    # calculate the total number of frames to be rendered
    total_frames = 0
    rendered_frames = 0
    for paragraph in article:
        total_frames += paragraph["duration"] * FPS

    for paragraph in article:
        text = paragraph["text"]

        # TODO - Move this to the article parser
        text_with_newlines = textwrap.wrap(text, width=30)

        duration = paragraph["duration"]

        # For every frame of video
        for _ in range(int(FPS*duration)):
            terminal.clear()
            terminal.statement(f"Rendering {filename}...")
            terminal.statement(
                f"{rendered_frames}/{total_frames} frames rendered")
            terminal.progress(rendered_frames, total_frames, length=24)

            # Create a black background, which serves as the canvas.
            frame = np.zeros((height, width, 3), np.uint8)

            # Do stuff with the video (text, images, etc.)

            img = cv.imread(f"./images/{filename}.jpg")

            # Resize the image to fit the screen
            img = cv.resize(img, (width, height))

            # Add the image to the canvas
            frame[0:height, 0:width] = img

            # Define initial vertical offset for the positioning of the text,
            # and the increment on the offset for each line.
            y0, dy = 50, 30

            # cv.putText does not support newlines, so we have to do it manually.
            for i, line in enumerate(text_with_newlines):
                y = y0 + i*dy
                cv.putText(frame, line, (0, y),
                           cv.FONT_HERSHEY_SIMPLEX, 1, (200, 200, 200), 2)

            # Write the frame into the file
            video.write(frame)

            rendered_frames += 1

            # Once the loop is done, release the video writer and close the file.
    video.release()

    terminal.clear()
