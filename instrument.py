from tuning import Tuning

class Instrument:
    def __init__(self, name: str, tuning: Tuning):
        self.name = name
        self.tuning = tuning

    def set_tuning(self, tuning: Tuning):
        self.tuning = tuning

class Guitar(Instrument):
    def __init__(self, tuning: Tuning = Tuning.preset('Guitar Standard')):
        super().__init__('Guitar', tuning)

class Bass(Instrument):
    def __init__(self, tuning: Tuning = Tuning.preset('Bass Standard')):
        super().__init__('Bass', tuning)