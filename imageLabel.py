from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QPaintEvent, QPixmap
from PySide6.QtWidgets import QLabel


class ImageLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._pixmap = None

    def setPixmap(self, pixmap: QPixmap) -> None:
        self._pixmap = pixmap
        self.repaint()

    def paintEvent(self, event: QPaintEvent) -> None:
        super().paintEvent(event)
        if self._pixmap is not None:
            imageWidth, imageHeight = self._pixmap.width(), self._pixmap.height()
            labelWidth, labelHeight = self.width(), self.height()
            ratio = min(labelWidth / imageWidth, labelHeight / imageHeight)
            newWidth, newHeight = int(imageWidth * ratio), int(imageHeight * ratio)
            newPixmap = self._pixmap.scaledToWidth(
                newWidth, Qt.TransformationMode.SmoothTransformation
            )
            x, y = abs(newWidth - labelWidth) // 2, abs(newHeight - labelHeight) // 2
            QPainter(self).drawPixmap(x, y, newPixmap)
