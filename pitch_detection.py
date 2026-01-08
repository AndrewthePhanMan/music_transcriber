import librosa
import numpy as np

def find_frequency(audio, sample_rate, onset):
    """
        Identifies the fundamental frequency at a specific onset.

        Parameters:
        - audio (np.ndarray): The numerical array that measures its amplitude over time.
        - sample_rate (int): The audio file's sample rate.
        - onset (float): The location of the onset in seconds.

        Returns:
        - frequency (float): The onset's fundamental frequency.
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
    frequencies = librosa.yin(y=audio_slice, fmin=librosa.note_to_hz("C2"), fmax=librosa.note_to_hz("C7"), sr=sample_rate)
    frequency = np.median(frequencies)
    return frequency

def find_pitch(frequency):
    """
        Finds the associated pitch of a given frequency (e.g. C2, A4, D5).

        Parameters:
        - frequency (float): The frequency (Hz) of the note.

        Returns:
        - pitch (str): The musical note's name (e.g. C2, A4, D5).
    """
    if frequency is None:
        return None
    return librosa.hz_to_note(frequency)