# ShadoTune

**ShadoTune** is a Python-based guitar & bass tuner application featuring a stylish frequency visualiser, alternate tunings, and a simple graphical interface.  
Built with PySide6 and sounddevice, it is ideal for practice, instrument setup, or simply tuning up.

## Features

- Choose **Guitar** or **Bass**
- Select from standard, Drop D, DADGAD, or bass tunings
- Click a string button to play the reference note
- Animated sinewave visualiser moves in real time with the note's frequency
- Easily extendable: add new tunings, instruments, or visualisation styles

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

## Name & Legal Note

"ShadoTune" is an original name inspired by classic instrumental guitar bands such as The Shadows and Nokie Edwards.  
No known copyright or trademark exists for this name.

## Licence

MIT Licence (see LICENSE file for details).

## Screenshots

*Add screenshots here if desired.*