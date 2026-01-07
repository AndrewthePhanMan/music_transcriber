import librosa
import numpy as np

def find_pitch(audio, sample_rate, onset):
    """

    """
    # Creates a 100 millisecond slice of the audio, beginning from the onset
    start = int(onset * sample_rate)
    end = int((onset + 0.1) * sample_rate) # 100 ms ahead of "start"
    end = min(end, len(audio)) # Checks if "end" goes beyond the audio's length (last note)
    audio_slice = audio[start:end]

    # Checks if the audio_slice is long enough to be analyzed (20 ms)
    if len(audio_slice) < int(0.02 * sample_rate):
        return None

    # 
    pitches = librosa.yin(y=audio_slice, fmin=librosa.note_to_hz("C2"), fmax=librosa.note_to_hz("C7"), sr=sample_rate)
    pitch = np.median(pitches)
    return pitch