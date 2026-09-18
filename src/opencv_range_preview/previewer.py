import cv2
import numpy as np
from PIL import Image
from PySide6.QtCore import Property, QObject, QSize, QUrl, Signal, Slot
from PySide6.QtGui import QColor, QImage, QPixmap
from PySide6.QtQuick import QQuickImageProvider
from typing_extensions import override

from opencv_range_preview.maskers import HsvMasker, Masker, RgbMasker


def arrayToPixmap(array: np.ndarray) -> QPixmap:
    # QImage assumes tightly packed rows, which slices/views don't guarantee.
    array = np.ascontiguousarray(array)
    if array.ndim == 2:
        height, width = array.shape
        image = QImage(
            array.data, width, height, width, QImage.Format.Format_Grayscale8
        )
    else:
        rgb = cv2.cvtColor(array, cv2.COLOR_BGR2RGB)
        height, width, channels = rgb.shape
        image = QImage(
            rgb.data, width, height, channels * width, QImage.Format.Format_RGB888
        )
    return QPixmap.fromImage(image.copy())


class PreviewProvider(QQuickImageProvider):
    def __init__(self):
        # the stubs only expose the enum on the base class
        super().__init__(QQuickImageProvider.ImageType.Pixmap)

        self.pixmaps: dict[str, QPixmap] = {"orig": QPixmap(), "mask": QPixmap()}

    @override
    def requestPixmap(self, id: str, size: QSize, requestedSize: QSize):
        # QML appends ?v=<version> to force the Image item to reload
        key = id.split("?", 1)[0]
        return self.pixmaps.get(key, QPixmap())


class Previewer(QObject):
    origChanged = Signal()
    maskChanged = Signal()

    def __init__(self, parent: QObject | None = None):
        super().__init__(parent)

        self.provider: PreviewProvider = PreviewProvider()
        self.bgrImage: np.ndarray | None = None
        self.maskers: dict[str, Masker] = {"hsv": HsvMasker(), "rgb": RgbMasker()}
        self.mode: str = "hsv"
        self.colorMask: bool = False
        self.bgColor: tuple[int, int, int] = (255, 255, 255)

        self._origVersion: int = 0
        self._maskVersion: int = 0

    @Property(int, notify=origChanged)
    def origVersion(self):
        return self._origVersion

    @Property(int, notify=maskChanged)
    def maskVersion(self):
        return self._maskVersion

    @Slot(QUrl)
    def loadImage(self, url: QUrl):
        try:
            with Image.open(url.toLocalFile()) as pilImage:
                rgbImage = np.array(pilImage.convert("RGB"), np.uint8)
        except (FileNotFoundError, OSError):
            return

        self.bgrImage = cv2.cvtColor(rgbImage, cv2.COLOR_RGB2BGR)
        self.provider.pixmaps["orig"] = arrayToPixmap(self.bgrImage)
        self._origVersion += 1
        self.origChanged.emit()

        self.updateMask()

    @Slot(str, list, list)
    def setRange(self, mode: str, lower: list[int], upper: list[int]):
        if not (masker := self.maskers.get(mode)):
            return

        self.mode = mode
        for key, lo, hi in zip(masker.CHANNELS, lower, upper, strict=True):
            masker.data[key] = [int(lo), int(hi)]

        self.updateMask()

    @Slot(bool)
    def setColorMask(self, enabled: bool):
        self.colorMask = enabled
        self.updateMask()

    @Slot(QColor)
    def setBackgroundColor(self, color: QColor):
        self.bgColor = (color.blue(), color.green(), color.red())
        if self.colorMask:
            self.updateMask()

    def updateMask(self):
        if self.bgrImage is None:
            return

        mask = self.maskers[self.mode].mask(self.bgrImage)
        if self.colorMask:
            masked = np.where(
                mask[:, :, np.newaxis] != 0,
                self.bgrImage,
                np.array(self.bgColor, np.uint8),
            )
            self.provider.pixmaps["mask"] = arrayToPixmap(masked)
        else:
            self.provider.pixmaps["mask"] = arrayToPixmap(mask)
        self._maskVersion += 1
        self.maskChanged.emit()
