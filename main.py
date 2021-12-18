import cv2
import csv
from modules.video2signal import video2signal


if __name__ == '__main__':

    cap = cv2.VideoCapture('video.mp4')
    signals = video2signal(cap)
    cap.release()


    with open('./signal.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerows(signals)
    
