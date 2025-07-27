import sys
from PySide6.QtWidgets import QApplication
from gui import TunerGUI

def main():
    app = QApplication(sys.argv)
    window = TunerGUI()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()