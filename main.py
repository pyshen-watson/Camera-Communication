import cv2
import csv
from modules.video2signal import video2signal
from modules.signal2tokens import signal2tokens


def convert_video_to_signal_csv(video_name, save=True):

    cap = cv2.VideoCapture(video_name)
    print('Convert video to signal')
    signals = video2signal(cap)
    cap.release()
    print('Convert done.')

    print('Convert signals to tokens')
    tokens = get_tokens(signals)
    print('Convert done.')

if __name__ == '__main__':

   convert_video_to_signal_csv('videos/0.mp4', save=True)
    
