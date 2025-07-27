from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox, QHBoxLayout, QMessageBox
)
from PySide6.QtCore import Qt
from tuner import Tuner
from tuning import TUNING_PRESETS
from frequency_visualizer import FrequencyVisualizer

class TunerGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🎸 ShadoTune – Guitar & Bass Tuner")
        self.tuner = Tuner()

        self.instrument_selector = QComboBox()
        self.instrument_selector.addItems(list(self.tuner.instruments.keys()))
        self.instrument_selector.currentTextChanged.connect(self.update_instrument)

        self.tuning_selector = QComboBox()
        self.tuning_selector.addItems(list(TUNING_PRESETS.keys()))
        self.tuning_selector.setCurrentText("Guitar Standard")
        self.tuning_selector.currentTextChanged.connect(self.update_tuning)

        self.strings_layout = QHBoxLayout()
        self.string_buttons = []

        self.visualizer = FrequencyVisualizer()
        self.visualizer.setMinimumHeight(120)
        self.visualizer.setMaximumHeight(160)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("<h2>🎸 ShadoTune</h2>"))
        layout.addWidget(QLabel("Instrument:"))
        layout.addWidget(self.instrument_selector)
        layout.addWidget(QLabel("Tuning:"))
        layout.addWidget(self.tuning_selector)
        layout.addWidget(QLabel("Strings:"))
        layout.addLayout(self.strings_layout)
        layout.addWidget(QLabel("Frequency Visualiser:"))
        layout.addWidget(self.visualizer)
        self.setLayout(layout)

        self.update_strings()

    def update_instrument(self):
        self.tuner.set_instrument(self.instrument_selector.currentText())
        # Default to instrument's standard tuning
        default_tuning = (
            "Guitar Standard" if self.instrument_selector.currentText() == "Guitar" else "Bass Standard"
        )
        self.tuning_selector.setCurrentText(default_tuning)
        self.update_strings()

    def update_tuning(self):
        try:
            self.tuner.set_tuning(self.tuning_selector.currentText())
            self.update_strings()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def update_strings(self):
        # Clear previous buttons
        while self.string_buttons:
            btn = self.string_buttons.pop()
            self.strings_layout.removeWidget(btn)
            btn.setParent(None)

        notes = self.tuner.get_strings()
        for i, note in enumerate(notes):
            btn = QPushButton(str(note))
            btn.clicked.connect(lambda _, idx=i: self.play_and_visualize(idx))
            self.strings_layout.addWidget(btn)
            self.string_buttons.append(btn)

    def play_and_visualize(self, idx):
        note = self.tuner.get_strings()[idx]
        self.visualizer.start_animation(note.frequency)

        def stop_vis():
            self.visualizer.stop_animation()
        # Play sound and stop animation when finished
        self.tuner.play_note_for_string(idx, on_finished=stop_vis)