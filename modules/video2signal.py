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
        signal = []

        original_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        thresholded_row_imgs = []
        row_otsu_thresholds = []

        # otsu_threshold, image_result = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # otsu threshold every row 
        for row in range(ROWSIZE):
            row_otsu_threshold, thresholded_row_img = cv2.threshold(original_img[row:row+1, 0:COLSIZE], 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            thresholded_row_imgs.append(thresholded_row_img)
            row_otsu_thresholds.append(row_otsu_threshold)

        # concat all row images
        # thresholded_img = thresholded_row_imgs[0] 
        # for r in thresholded_row_imgs:
        #     thresholded_img = cv2.vconcat([thresholded_row_img, r])

        thresholded_img = cv2.vconcat([r for r in thresholded_row_imgs])
        cv2.imwrite('first-frame.jpg', thresholded_img)

        # img_array = np.reshape(signal, (1080, 1920))
        # Signalize
        # white_in_col = []
        # for col in range(COLSIZE):
        #     count = 0
        #     for row in range(ROWSIZE):
        #         if thresholded_img[row][0, col] >= 128:
        #             count  = count + 1
        #     sig = 255 if count > ROWSIZE / 2 else 0


            signal.append(sig)

        # cv2.imwrite('frame_1.jpg', )    
        signals.append(signal)
        
       
        
        break

    return signals