import cv2
import csv
from modules.video2signal import video2signal


def convert_video_to_signal_csv(video_name, save=True):

    cap = cv2.VideoCapture(video_name)
    print('Convert video to signal')
    signals = video2signal(cap)
    cap.release()
    print('Convert done.')

    if save:
        with open('./signal.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerows(signals)

if __name__ == '__main__':

   convert_video_to_signal_csv('video.mp4', save=False)
    
