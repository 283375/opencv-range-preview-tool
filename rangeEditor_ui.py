# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rangeEditor.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QRadioButton, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)

from rangeEditors import (HsvRangeEditor, RgbRangeEditor)

class Ui_RangeEditor(object):
    def setupUi(self, RangeEditor):
        if not RangeEditor.objectName():
            RangeEditor.setObjectName(u"RangeEditor")
        RangeEditor.resize(564, 357)
        self.verticalLayout = QVBoxLayout(RangeEditor)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(RangeEditor)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.hsvButton = QRadioButton(self.widget)
        self.hsvButton.setObjectName(u"hsvButton")
        self.hsvButton.setText(u"HSV")
        self.hsvButton.setChecked(True)

        self.horizontalLayout.addWidget(self.hsvButton)

        self.rgbButton = QRadioButton(self.widget)
        self.rgbButton.setObjectName(u"rgbButton")
        self.rgbButton.setText(u"RGB")

        self.horizontalLayout.addWidget(self.rgbButton)


        self.verticalLayout.addWidget(self.widget)

        self.lowerGroupBox = QGroupBox(RangeEditor)
        self.lowerGroupBox.setObjectName(u"lowerGroupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lowerGroupBox.sizePolicy().hasHeightForWidth())
        self.lowerGroupBox.setSizePolicy(sizePolicy)
        self.lowerGroupBox.setTitle(u"LOWER")
        self.verticalLayout_3 = QVBoxLayout(self.lowerGroupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lowerStackedWidget = QStackedWidget(self.lowerGroupBox)
        self.lowerStackedWidget.setObjectName(u"lowerStackedWidget")
        self.lowerHsvRangeEditor = HsvRangeEditor()
        self.lowerHsvRangeEditor.setObjectName(u"lowerHsvRangeEditor")
        self.lowerStackedWidget.addWidget(self.lowerHsvRangeEditor)
        self.lowerRgbRangeEditor = RgbRangeEditor()
        self.lowerRgbRangeEditor.setObjectName(u"lowerRgbRangeEditor")
        self.lowerStackedWidget.addWidget(self.lowerRgbRangeEditor)

        self.verticalLayout_3.addWidget(self.lowerStackedWidget)


        self.verticalLayout.addWidget(self.lowerGroupBox)

        self.upperGroupBox = QGroupBox(RangeEditor)
        self.upperGroupBox.setObjectName(u"upperGroupBox")
        sizePolicy.setHeightForWidth(self.upperGroupBox.sizePolicy().hasHeightForWidth())
        self.upperGroupBox.setSizePolicy(sizePolicy)
        self.upperGroupBox.setTitle(u"UPPER")
        self.verticalLayout_2 = QVBoxLayout(self.upperGroupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.upperStackedWidget = QStackedWidget(self.upperGroupBox)
        self.upperStackedWidget.setObjectName(u"upperStackedWidget")
        self.upperHsvRangeEditor = HsvRangeEditor()
        self.upperHsvRangeEditor.setObjectName(u"upperHsvRangeEditor")
        self.upperStackedWidget.addWidget(self.upperHsvRangeEditor)
        self.upperRgbRangeEditor = RgbRangeEditor()
        self.upperRgbRangeEditor.setObjectName(u"upperRgbRangeEditor")
        self.upperStackedWidget.addWidget(self.upperRgbRangeEditor)

        self.verticalLayout_2.addWidget(self.upperStackedWidget)


        self.verticalLayout.addWidget(self.upperGroupBox)

        self.valueLabel = QLabel(RangeEditor)
        self.valueLabel.setObjectName(u"valueLabel")
        self.valueLabel.setText(u"...")

        self.verticalLayout.addWidget(self.valueLabel)


        self.retranslateUi(RangeEditor)

        QMetaObject.connectSlotsByName(RangeEditor)
    # setupUi

    def retranslateUi(self, RangeEditor):
        RangeEditor.setWindowTitle(QCoreApplication.translate("RangeEditor", u"Form", None))
    # retranslateUi

