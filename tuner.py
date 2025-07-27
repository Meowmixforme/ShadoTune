from instrument import Guitar, Bass
from tuning import Tuning
from sound_player import SoundPlayer

class Tuner:
    def __init__(self):
        self.instruments = {
            'Guitar': Guitar(),
            'Bass': Bass()
        }
        self.sound_player = SoundPlayer()
        self.selected_instrument = self.instruments['Guitar']

    def set_instrument(self, instrument_name: str):
        if instrument_name not in self.instruments:
            raise ValueError("Unknown instrument")
        self.selected_instrument = self.instruments[instrument_name]

    def set_tuning(self, tuning_name: str):
        tuning = Tuning.preset(tuning_name)
        self.selected_instrument.set_tuning(tuning)

    def play_note_for_string(self, string_index: int, on_finished=None):
        note = self.selected_instrument.tuning.string_notes[string_index]
        self.sound_player.play_tone(note.frequency, on_finished=on_finished)
        return note.frequency

    def get_strings(self):
        return self.selected_instrument.tuning.string_notes