import matplotlib.pyplot as plt
import librosa.display

def plot_spectrogram(spectrogram, sample_rate):
    """
        Plots a readable time-frequency spectrogram of an audio signal.

        Parameters:
        - spectrogram (np.ndarray): 2D array of the audio's amplitude, obtained from the short-time Fourier transform.
        - sample_rate (int): The audio file's sample rate.
    """
    # Sets the spectrogram's resolution (width & height)
    plt.figure(figsize=(10,4))

    # Displays the spectrogram
    img = librosa.display.specshow(spectrogram, sr=sample_rate, y_axis="log", x_axis="time", cmap="inferno")

    # Labels the x and y axes
    plt.xlabel("Time (s)")
    plt.ylabel("Frequency (Hz)")

    # Labels the color scale
    plt.colorbar(img, format="%+2.f dBFS")
    
    # Opens a window for the spectrogram
    plt.show()