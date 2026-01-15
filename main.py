from processor import load_audio, compute_spectrogram
from visualizer import plot_spectrogram
from onset_detection import find_onsets
from note_list import add_notes
from midi_conversion import notes_to_midi

import librosa
from pathlib import Path

path = r"C:\Users\andre\OneDrive\Desktop\music_transcriber\audio\teateam_melodic loop_kagaminomi_D_128.wav"

def main():
    """
        Loads a string path to an audio sample, generating a spectrogram analyzing its melodic/frequency content.
        Afterward, a MIDI file is created based on the spectrogram's data.
    """
    # Prompts the user for a path to the audio file
    path = input("Enter the path to your audio file: ").replace("\\", "/")

    # Creates variables for the audio, its sample rate, and its duration/length
    audio, sample_rate = load_audio(path)
    audio_duration = librosa.get_duration(y=audio, sr=sample_rate)

    # Creates variables for the spectrogram and a list of onsets
    spectrogram = compute_spectrogram(audio)
    onset_times = find_onsets(audio, sample_rate)

    # Plots the spectrogram with onset markers
    plot_spectrogram(spectrogram, sample_rate, onset_times)

    # Creates a variable for a list of notes
    notes = add_notes(audio, sample_rate, onset_times, audio_duration)

    # Converts the note list to a MIDI file
    midi_name = Path(path).with_suffix(".mid")
    notes_to_midi(notes, midi_name)
    print(f"{midi_name.name} has been exported.")

if __name__ == "__main__":
    main()