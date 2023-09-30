from PySide6.QtWidgets import QWidget, QButtonGroup
from PySide6.QtCore import Signal

from rangeEditor_ui import Ui_RangeEditor


class RangeEditor(Ui_RangeEditor, QWidget):
    valueChanged = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.colorModeButtonGroup = QButtonGroup(self)
        self.colorModeButtonGroup.addButton(self.hsvButton, 0)
        self.colorModeButtonGroup.addButton(self.rgbButton, 1)

        self.colorModeButtonGroup.idToggled.connect(
            self.lowerStackedWidget.setCurrentIndex
        )
        self.colorModeButtonGroup.idToggled.connect(
            self.upperStackedWidget.setCurrentIndex
        )

        self.colorModeButtonGroup.idToggled.connect(self.valueChanged)
        self.upperHsvRangeEditor.valueChanged.connect(self.valueChanged)
        self.upperRgbRangeEditor.valueChanged.connect(self.valueChanged)
        self.lowerHsvRangeEditor.valueChanged.connect(self.valueChanged)
        self.lowerRgbRangeEditor.valueChanged.connect(self.valueChanged)

        self.valueChanged.connect(self.updateValueLabel)

        self.updateValueLabel()

        self.valueLabel.setMinimumWidth(
            self.fontMetrics().horizontalAdvance(
                "UPPER [999, 999, 999], LOWER [999, 999, 999]"
            )
            + 5
        )

    def value(self):
        if self.colorModeButtonGroup.checkedId() == 0:
            return [self.lowerHsvRangeEditor.value(), self.upperHsvRangeEditor.value()]
        elif self.colorModeButtonGroup.checkedId() == 1:
            return [self.lowerRgbRangeEditor.value(), self.upperRgbRangeEditor.value()]
        else:
            return []

    def updateValueLabel(self):
        if value := self.value():
            self.valueLabel.setText(f"LOWER {value[0]}, UPPER {value[1]}")
        else:
            self.valueLabel.setText("...")
