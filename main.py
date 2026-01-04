from processor import load_audio, compute_spectrogram
from visualizer import plot_spectrogram
from onset_detection import find_onsets

path = r"C:\Users\andre\OneDrive\Desktop\music_transcriber\audio\teateam_melodic loop_kagaminomi_D_128.wav"

def main():
    """
        Loads a string path to an audio sample and generates a spectrogram analyzing its melodic/frequency content.
    """
    audio, sample_rate = load_audio(path)
    spectrogram = compute_spectrogram(audio)
    onset_times = find_onsets(audio, sample_rate)
    plot_spectrogram(spectrogram, sample_rate, onset_times)
    print(onset_times)

if __name__ == "__main__":
    main()