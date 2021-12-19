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
    for idx, frame in enumerate(tqdm(frames)):
        signal = []

        original_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        thresholded_row_imgs = []

        # otsu threshold every row 
        for row in range(ROWSIZE):
            row_otsu_threshold, thresholded_row_img = cv2.threshold(original_img[row:row+1, 0:COLSIZE], 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            thresholded_row_imgs.append(thresholded_row_img)

        thresholded_img = cv2.vconcat([r for r in thresholded_row_imgs])
        # cv2.imwrite('first-frame.jpg', thresholded_img)

        # Signalize
        img_array = np.reshape(thresholded_img, (1920, 1080))
        for col in range(COLSIZE):
            count = 0
            for row in range(ROWSIZE):
                if img_array[row, col] >= 128:
                    count  = count + 1
            sig = 255 if count > ROWSIZE / 2 else 0
            signal.append(sig)
        array = np.reshape(signal, (1, 1080))
        cv2.imwrite(f'./frames/14/frame_{idx+1}.jpg', array)    
        signals.append(signal)

    return signals