import numpy as np
import sounddevice as sd
import threading

class SoundPlayer:
    def play_tone(self, frequency: float, duration: float = 1.5, volume: float = 0.3, on_finished=None):
        def _play():
            fs = 44100
            t = np.linspace(0, duration, int(fs*duration), False)
            wave = np.sin(2 * np.pi * frequency * t) * volume
            sd.play(wave, fs)
            sd.wait()
            if callable(on_finished):
                on_finished()
        threading.Thread(target=_play, daemon=True).start()