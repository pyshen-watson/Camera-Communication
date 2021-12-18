import cv2
import numpy as np

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

    for frame in frames:

        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Normalize and thresholding
        img = (img - np.mean(img, axis=1, keepdims=True)) / np.std(img, axis=1, keepdims=True)
        img = np.clip(img*1024*1024, 0, 255)

        # Signalize
        white_in_col = np.sum(img, axis=0) / 255
        isWhite = lambda white : 1 if white >= ROWSIZE / 2 else 0
        sig = [isWhite(col) for col in white_in_col]
        
        signals.append(sig)

    return signals