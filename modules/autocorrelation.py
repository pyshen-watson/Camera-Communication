import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from scipy.signal import argrelextrema

DELIMITER_DA = [-1, -1, -1,  1,  1,  1, -1,  1,  1,  1, -1,  1,  1, -1,  1]
DELIMITER_DB = [ 1,  1,  1, -1, -1, -1,  1, -1, -1, -1,  1, -1, -1,  1, -1]
DELIMITER_FA = [-1, -1, -1, -1,  1, -1,  1, -1, -1,  1,  1, -1, -1,  1]
DELIMITER_FB = [ 1,  1,  1,  1, -1,  1, -1,  1,  1, -1, -1,  1,  1, -1]
BIT_0        = [ 1,  1,  1,  1,  1,  1,  1, -1, -1, -1, -1, -1, -1, -1]
BIT_1        = [-1, -1, -1, -1, -1, -1, -1,  1,  1,  1,  1,  1,  1,  1]


def getAutocorrelation(signal:list) -> int:
    sum = 0
    signal_length = len(signal)
    for diff in range(signal_length):
       for i in range(signal_length - diff):
           sum = sum + signal[i] * signal[i + diff]
    return sum

def draw_autocorrelation(signal:list, delimiter_length:int, idx:int):
    s = [(1 if p >= 128 else -1) for p in signal]
    autocorrelations = []
    for i in range(1080 - (delimiter_length - 1)):
        autocorrelations.append(getAutocorrelation(s[i:i+delimiter_length]))    
    positions = range(1080 - (delimiter_length - 1))
    min_positions = argrelextrema(np.array(autocorrelations), np.less)
    print(min_positions)
    plt.plot(positions, autocorrelations)
    # plt.savefig(f'./byproduct/0/autocorrelations/autocorrelation-{idx}.jpg')
    plt.clf()
    
