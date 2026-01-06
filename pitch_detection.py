import librosa
import numpy as np

def find_pitch(audio, sample_rate, onset):
    """

    """
    start = int(onset * sample_rate)
    end = int((onset + 0.1) * sample_rate) # 100 milliseconds ahead of "start"
    end = min(end, len(audio)) # Checks if "end" goes beyond the audio's length (last note)
    audio_slice = audio[start:end]

    pitches = librosa.yin(y=audio_slice, fmin=librosa.note_to_hz("C2"), fmax=librosa.note_to_hz("C7"), sr=sample_rate)
    return pitches