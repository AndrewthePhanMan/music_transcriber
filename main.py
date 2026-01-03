from processor import load_audio, compute_spectrogram
from visualizer import plot_spectrogram

path = r"C:\Users\andre\OneDrive\Desktop\music_transcriber\audio\HDVTH_150_loop_melody_soulfullead_Dmaj.wav"

def main():
    """
        Loads a string path to an audio sample and generates a spectrogram analyzing its melodic/frequency content.
    """
    audio, sample_rate = load_audio(path)
    spectrogram = compute_spectrogram(audio)
    plot_spectrogram(spectrogram, sample_rate)

if __name__ == "__main__":
    main()