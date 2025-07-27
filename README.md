# ShadoTune

**ShadoTune** is a Python-based guitar & bass tuner application featuring a stylish frequency visualiser, alternate tunings, and a simple graphical interface.  
Built with PySide6 and sounddevice, it is ideal for practice, instrument setup, or simply tuning up.


<img width="836" height="563" alt="Screenshot 2025-07-27 141015" src="https://github.com/user-attachments/assets/b579dee6-1e0c-4153-b7b7-bb6b265de7f2" />


## Features

- Choose **Guitar** or **Bass**
- Select from standard, Drop D, DADGAD, or bass tunings
- Click a string button to play the reference note
- Animated sinewave visualiser moves in real time with the note's frequency
- Easily extendable: add new tunings, instruments, or visualisation styles

 ## Libraries Used

- **Python 3.8+** – main programming language
- **PySide6 (Qt for Python)** – graphical user interface
- **sounddevice** – audio playback for reference notes
- **numpy** – efficient numerical operations for sound generation and animation

## Installation

1. Download or clone this repository.
2. Ensure you have Python 3.8+ installed, then run:

   ```sh
   pip install -r requirements.txt
   ```

## Usage

```sh
python main.py
```

- Select your instrument and preferred tuning from the dropdown menus.
- Click any string button to play its reference note.
- Watch the frequency visualiser animate in sync with the note.

## Extending

- Add new tunings in `tuning.py` (edit `TUNING_PRESETS`).
- Create new instruments by subclassing `Instrument` in `instrument.py`.
- Customise the visualisation in `frequency_visualizer.py`.


## Licence

MIT Licence (see LICENSE file for details).
