import cv2
import numpy as np
from tqdm import tqdm



def video2frames(cap:cv2.VideoCapture) -> list:

    frames = []
    while cap.isOpened():

        ret, frame = cap.read()

        if not ret:
            break

        frames.append(frame)

    return frames

def video2signal(cap:cv2.VideoCapture) -> list:

    frames = video2frames(cap)
    ROWSIZE, COLSIZE = frames[0].shape[0:2]
    

    signals = []

    for frame in tqdm(frames):

        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        image_results = []
        otsu_thresholds = []

        # Normalize and thresholding
        for row in range(ROWSIZE):
            otsu_threshold, image_result = cv2.threshold(img[row:row+1, 0:COLSIZE], 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            image_results.append(image_result)
            otsu_thresholds.append(otsu_threshold)
        
        # Signalize
        white_in_col = []
        for col in range(COLSIZE):
            count = 0
            for row in range(ROWSIZE):
                if image_results[row][0, col] >= 128:
                    count  = count + 1
            sig = 1 if count > ROWSIZE else 0
            signals.append(sig)

    return signals