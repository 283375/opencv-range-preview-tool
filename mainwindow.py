from PySide6.QtCore import Slot
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QMainWindow, QFileDialog

from PIL import Image

from mainwindow_ui import Ui_MainWindow

import numpy as np
import cv2


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.qImage = None
        self.pilImage = None
        self.bgrImageArray = None
        self.hsvImageArray = None

        self.rangeEditor.valueChanged.connect(self.mask)

    @Slot()
    def on_loadImageButton_clicked(self):
        imageFileName, _ = QFileDialog.getOpenFileName(
            self, None, "", "Image (*.png *.jpg *.jpeg);;All (*.*)"
        )
        if not imageFileName:
            return

        self.pilImage = Image.open(imageFileName)
        self.qImage = self.pilImage.toqimage()
        self.bgrImageArray = np.array(self.pilImage, np.uint8)
        self.bgrImageArray = cv2.cvtColor(self.bgrImageArray, cv2.COLOR_RGB2BGR)
        self.hsvImageArray = cv2.cvtColor(self.bgrImageArray, cv2.COLOR_BGR2HSV)

        self.img_origLabel.setPixmap(self.pilImage.toqpixmap())

        self.mask()

    def mask(self):
        if not self.pilImage:
            return

        masked = cv2.inRange(
            self.hsvImageArray,
            *[np.array(v, np.uint8) for v in self.rangeEditor.value()]
        )
        self.img_maskedBwLabel.setPixmap(Image.fromarray(masked, "L").toqpixmap())
