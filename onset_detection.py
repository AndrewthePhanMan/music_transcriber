import librosa
import numpy as np

def find_onsets(audio, sample_rate, hop_length=512):
    """

    """
    audio_length = len(audio) / sample_rate
    onset_frames = librosa.onset.onset_detect(y=audio, sr=sample_rate, hop_length=hop_length, backtrack=True)
    onset_times = librosa.frames_to_time(onset_frames, sr=sample_rate, hop_length=hop_length)
    onset_times = onset_times[onset_times <= audio_length]
    return onset_times