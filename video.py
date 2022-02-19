from typing import List
import terminal as terminal
import cv2 as cv
import numpy as np
from cv2 import VideoWriter, VideoWriter_fourcc



# This is the function that will be called by the main file.
def render(width: int, height: int, FPS: int, seconds: float, filename: str, article: List[dict]):

    # Define the codec and create VideoWriter object
    fourcc = VideoWriter_fourcc(*'XVID')
    video = VideoWriter(f"./{filename}.avi", fourcc, float(FPS), (width, height))

    print(article)

    for paragraph in article:
        text = paragraph["text"]

        text_with_newlines = '\n'.join(text[i:i+30] for i in range(0, len(text), 30))

        duration = int(paragraph["duration"])


        print(text_with_newlines)
        # For every frame of video
        for _ in range(FPS*duration):

            # Create a black background, which serves as the canvas.
            frame = np.zeros((height, width, 3), np.uint8)

            # Do stuff with the video (text, images, etc.)
            # cv.putText(frame, text, (0, int(height / 2)), cv.FONT_HERSHEY_SIMPLEX, 1, (200, 200, 200), 2)

            y0, dy = 50, 20
            for i, line in enumerate(text_with_newlines.split('\n')):
                print(line)
                y = y0 + i*dy
                cv.putText(frame, line, (0, y), cv.FONT_HERSHEY_SIMPLEX, 1, (200, 200, 200), 2)

            # Write the frame into the file
            video.write(frame)

    #Once the loop is done, release the video writer and close the file.
    video.release()

    
# render(1280, 720, 24, 20, "test", ["test", "test2"])