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

AUTOCORRELATION_LENGTH = 90
HL_LENGTH = 6

def signal2tokens(signals:list) -> list:
  token_sequences = []
  for idx, signal in enumerate(signals):
    autocorrelations = []
    for i in range(1080 - (AUTOCORRELATION_LENGTH - 1)):
        autocorrelations.append(getAutocorrelation(signal[i:i+AUTOCORRELATION_LENGTH]))   
    ## DEBUG: autocorrelations
    # positions = range(1080 - (AUTOCORRELATION_LENGTH - 1))
    # plt.plot(positions, autocorrelations)
    # plt.savefig(f'./byproduct/0/autocorrelations/autocorrelation-{idx+1}.jpg')
    # plt.clf()

    min_positions = argrelextrema(np.array(autocorrelations), np.less)
    token_sequence = get_token_sequence(signal, min_positions)

def getAutocorrelation(signal:list) -> int:
    sum = 0
    signal_length = len(signal)
    for diff in range(signal_length):
       for i in range(signal_length - diff):
           sum = sum + signal[i] * signal[i + diff]
    return sum

def get_token_sequence(signal, min_positions):
  pass