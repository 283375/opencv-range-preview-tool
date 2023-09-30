from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtWidgets import QGridLayout, QLabel, QSlider, QWidget


class RangeEditorComponent(QWidget):
    valueChanged = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.sliderLabels: list[QSlider] = []
        self.sliders: list[QSlider] = []
        self.sliderValueLabels: list[QLabel] = []

        self.gridLayout = QGridLayout(self)

    def addSlider(self, label: str, slider: QSlider):
        sliderObjectName = slider.objectName()

        sliderLabel = QLabel(label, self)
        if sliderObjectName:
            sliderLabel.setObjectName(f"{sliderObjectName}Label")
        self.sliderLabels.append(sliderLabel)

        slider.valueChanged.connect(self.valueChanged)
        self.sliders.append(slider)

        valueLabel = QLabel(self)
        if sliderObjectName:
            valueLabel.setObjectName(f"{sliderObjectName}ValueLabel")
        valueLabel.setMinimumWidth(self.fontMetrics().horizontalAdvance("999") + 2)
        valueLabel.setText(str(slider.value()))
        self.sliderValueLabels.append(valueLabel)
        slider.valueChanged.connect(self.updateSliderValueLabel)

        row = self.gridLayout.rowCount()
        self.gridLayout.addWidget(sliderLabel, row, 0)
        self.gridLayout.addWidget(slider, row, 1)
        self.gridLayout.addWidget(valueLabel, row, 2)

    @Slot(int)
    def updateSliderValueLabel(self, v: int):
        slider: QSlider = self.sender()

        valueLabel = None
        if slider.objectName():
            labelObjectName = f"{slider.objectName()}ValueLabel"
            valueLabel: QLabel | None = self.findChild(QLabel, labelObjectName)

        if valueLabel is None:
            sliderIndex = self.sliders.index(slider)
            valueLabel = self.sliderValueLabels[sliderIndex]

        valueLabel.setText(str(slider.value()))


class RgbRangeEditor(RangeEditorComponent):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.rSlider = QSlider(Qt.Orientation.Horizontal, self)
        self.rSlider.setObjectName("rSlider")
        self.gSlider = QSlider(Qt.Orientation.Horizontal, self)
        self.gSlider.setObjectName("gSlider")
        self.bSlider = QSlider(Qt.Orientation.Horizontal, self)
        self.bSlider.setObjectName("bSlider")

        for slider in [self.rSlider, self.gSlider, self.bSlider]:
            slider.setMinimum(0)
            slider.setMaximum(255)

        self.addSlider("R", self.rSlider)
        self.addSlider("G", self.gSlider)
        self.addSlider("B", self.bSlider)

    def value(self):
        return [self.rSlider.value(), self.gSlider.value(), self.bSlider.value()]


class HsvRangeEditor(RangeEditorComponent):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.hSlider = QSlider(Qt.Orientation.Horizontal, self)
        self.hSlider.setObjectName("hSlider")
        self.sSlider = QSlider(Qt.Orientation.Horizontal, self)
        self.sSlider.setObjectName("sSlider")
        self.vSlider = QSlider(Qt.Orientation.Horizontal, self)
        self.vSlider.setObjectName("vSlider")

        self.hSlider.setMinimum(0)
        self.hSlider.setMaximum(179)
        for slider in [self.sSlider, self.vSlider]:
            slider.setMinimum(0)
            slider.setMaximum(255)

        self.addSlider("H", self.hSlider)
        self.addSlider("S", self.sSlider)
        self.addSlider("V", self.vSlider)

    def value(self):
        return [self.hSlider.value(), self.sSlider.value(), self.vSlider.value()]
