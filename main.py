import cv2
import csv
from modules.video2signal import video2signal


if __name__ == '__main__':

    cap = cv2.VideoCapture('video.mp4')
    print('Convert video to signal')
    signals = video2signal(cap)
    cap.release()
    print('Convert done.')


    with open('./signal.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerows(signals)
    
