from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor, QPen
from PySide6.QtCore import QTimer
import numpy as np

class FrequencyVisualizer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.frequency = 0
        self.phase = 0
        self.animating = False
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_animation)
        self.timer.start(30)  # Update every 30 ms

    def start_animation(self, frequency):
        self.frequency = frequency
        self.phase = 0
        self.animating = True
        self.update()

    def stop_animation(self):
        self.animating = False
        self.frequency = 0
        self.update()

    def update_animation(self):
        if self.animating and self.frequency > 0:
            self.phase += self.frequency * 0.03
            self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor(20, 20, 30))
        pen = QPen(QColor(0, 255, 180), 2)
        painter.setPen(pen)

        if self.frequency > 0 and self.animating:
            w = self.width()
            h = self.height()
            num_points = w
            amp = h // 3
            freq = self.frequency / 20

            points = []
            for x in range(num_points):
                theta = (x / w) * 2 * np.pi * freq + self.phase
                y = int(h // 2 + amp * np.sin(theta))
                points.append((x, y))

            for i in range(len(points) - 1):
                painter.drawLine(points[i][0], points[i][1], points[i+1][0], points[i+1][1])
        else:
            # Draw a static line when not animating
            w = self.width()
            h = self.height()
            painter.drawLine(0, h // 2, w, h // 2)