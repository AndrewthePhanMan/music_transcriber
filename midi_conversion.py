import pretty_midi
import librosa

def notes_to_midi(notes, midi_name, instrument_name="Acoustic Grand Piano"):
    """
        Converts and writes out the list of notes into a playable MIDI file.

        Parameters:
        - notes (list): List of note objects.
        - midi_name (str): Name of the midi file.
        - instrument_name (str): Name of the instrument.
    """
    # 
    for note in notes:
        if note.pitch is None:
            continue
    
    # 
    midi_file = pretty_midi.PrettyMIDI()
    instrument = pretty_midi.Instrument(program=pretty_midi.instrument_name_to_program(instrument_name))
    for note in notes:
        midi_num = librosa.note_to_midi(note.pitch)
        midi_note = pretty_midi.containers.Note(100, midi_num, note.onset, note.onset + note.duration)
        instrument.notes.append(midi_note)
    midi_file.instruments.append(instrument)
    midi_file.write(f"{midi_name}.mid")