import textwrap
from typing import List
import terminal as terminal
import cv2 as cv
import numpy as np
from cv2 import VideoWriter, VideoWriter_fourcc


def scale_image(img, width, height):
    img_height, img_width = img.shape[:2]

    if img_height > height and img_width > width:
        # crop the image from center
        img = img[int(img_height/2 - height/2):int(img_height/2 + height/2),
                  int(img_width/2 - width/2):int(img_width/2 + width/2)]
        return img

    elif img_height > height and img_width < width:
        ratio = width/img_width
        img = cv.resize(img, (int(img_width*ratio), int(img_height*ratio)))
        return img

    elif img_height < height and img_width > width:
        ratio = height/img_height
        img = cv.resize(img, (int(img_width*ratio), int(img_height*ratio)))
        return img

    else:
        ratio = max(height/img_height, width/img_width)
        img = cv.resize(img, (int(img_width*ratio), int(img_height*ratio)))
        return img


def crop_image(img, width, height):
    # crop the image from center
    img_height, img_width = img.shape[:2]
    img = img[int(img_height/2 - height/2):int(img_height/2 + height/2),
              int(img_width/2 - width/2):int(img_width/2 + width/2)]
    return img


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

        # Read the image file
        img = cv.imread(f"./images/{filename}.jpg")

        # Resize the image be be bigger than the canvas in order to crop it
        img = scale_image(img, width, height)

        # Crop the image to be the same size as the canvas
        img = crop_image(img, width, height)

        # For every frame of video
        for _ in range(int(FPS*duration)):
            terminal.clear()
            terminal.statement(f"Rendering {filename}...")
            terminal.statement(
                f"{rendered_frames}/{total_frames} frames rendered")
            terminal.progress(rendered_frames, total_frames, length=24)

            # Create a black background, which serves as the canvas.
            frame = np.zeros((height, width, 3), np.uint8)

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
