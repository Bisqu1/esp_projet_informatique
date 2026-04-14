from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QColor
import sys
import loi_physique

# ---- ZONE VISUELLE ----
class ZoneVisuelle(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

    def paintEvent(self, event):
        painter = QPainter(self)
        w = self.width()
        h = self.height()

        # Ciel
        painter.setBrush(QColor(135, 206, 235))
        painter.setPen(Qt.NoPen)
        painter.drawRect(0, 0, w, h)

        # Sol
        painter.setBrush(QColor(34, 139, 34))
        painter.drawRect(0, int(h * 0.7), w, int(h * 0.3))

        # Rivière
        painter.setBrush(QColor(0, 100, 200))
        painter.drawRect(int(w * 0.2), int(h * 0.6), int(w * 0.6), int(h * 0.15))

        # Barrage
        painter.setBrush(QColor(120, 120, 120))
        painter.drawRect(int(w * 0.45), int(h * 0.4), int(w * 0.08), int(h * 0.25))