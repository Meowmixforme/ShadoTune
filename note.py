class Note:
    def __init__(self, name: str, frequency: float):
        self.name = name
        self.frequency = frequency

    def __repr__(self):
        return f"{self.name} ({self.frequency:.2f} Hz)"