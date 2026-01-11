import pretty_midi
import librosa
from pathlib import Path

def notes_to_midi(notes, name):
    """
        
    """
    midi_file = pretty_midi.PrettyMIDI()
    instrument = pretty_midi.Instrument()
    for note in notes:
        midi_num = librosa.note_to_midi(note.pitch)
        midi_note = pretty_midi.containers.Note(100, midi_num, note.onset, note.onset + note.duration)
        instrument.notes.append(midi_note)
    midi_file.instruments.append(instrument)
    midi_file.write(name)
    pass