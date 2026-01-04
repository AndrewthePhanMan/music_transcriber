import librosa
import numpy as np

def find_onsets(audio, sample_rate):
    """

    """
    onset_frames = librosa.onset.onset_detect(y=audio, sr=sample_rate)
    onset_times = librosa.frames_to_time(onset_frames)
    return onset_times