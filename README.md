# Music Transcriber: Audio to MIDI Converter

A Python-based music transcription tool that analyzes an audio file, visualizes its spectrogram,
detects note onserts & pitches, and converts the result into a playable MIDI file.

## Features
- Load and process audio files (.wav, .mp3, etc.)
- Generate and display a log-frequency spectrogram
- Detect note onsets using signal energy changes (transients)
- Estimate fundamental pitch for each note
- Convert detected notes into a MIDI file

## Dependencies
System Requirements:
- Python 3.9+

Libraries:
- Librosa – Audio loading, signal processing, onset and pitch detection
- NumPy - Numerical computations and array handling
- Matplotlib - Spectrogram visualization
- pretty_midi - MIDI file creation and export

## Installation
```bash
pip install numpy librosa matplotlib pretty_midi
```

## Author(s)
Andrew Phan
https://www.linkedin.com/in/the-phan-man/