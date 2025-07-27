from note import Note

NOTE_FREQUENCIES = {
    "E1": 41.20, "A1": 55.00, "D2": 73.42, "G2": 98.00,
    "E2": 82.41, "A2": 110.00, "D3": 146.83, "G3": 196.00,
    "B3": 246.94, "E4": 329.63, "D4": 293.66, "A3": 220.00,
    # Extend as needed!
}

TUNING_PRESETS = {
    'Guitar Standard': ["E2", "A2", "D3", "G3", "B3", "E4"],
    'Drop D': ["D2", "A2", "D3", "G3", "B3", "E4"],
    'DADGAD': ["D2", "A2", "D3", "G3", "A3", "D4"],
    'Bass Standard': ["E1", "A1", "D2", "G2"],
    # Add more tunings here
}

class Tuning:
    def __init__(self, name: str, string_notes: list):
        self.name = name
        self.string_notes = [Note(note, NOTE_FREQUENCIES[note]) for note in string_notes]

    @classmethod
    def preset(cls, preset_name: str):
        if preset_name not in TUNING_PRESETS:
            raise ValueError(f"Unknown preset {preset_name}")
        return cls(preset_name, TUNING_PRESETS[preset_name])