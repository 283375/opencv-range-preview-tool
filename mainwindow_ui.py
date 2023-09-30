# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

from imageLabel import ImageLabel
from rangeEditor import RangeEditor

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 500)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.img_maskedColorLabel = ImageLabel(self.centralwidget)
        self.img_maskedColorLabel.setObjectName(u"img_maskedColorLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_maskedColorLabel.sizePolicy().hasHeightForWidth())
        self.img_maskedColorLabel.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.img_maskedColorLabel, 0, 3, 1, 1)

        self.img_maskedBwLabel = ImageLabel(self.centralwidget)
        self.img_maskedBwLabel.setObjectName(u"img_maskedBwLabel")
        sizePolicy.setHeightForWidth(self.img_maskedBwLabel.sizePolicy().hasHeightForWidth())
        self.img_maskedBwLabel.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.img_maskedBwLabel, 1, 3, 1, 1)

        self.img_colorspaceLabel = ImageLabel(self.centralwidget)
        self.img_colorspaceLabel.setObjectName(u"img_colorspaceLabel")
        sizePolicy.setHeightForWidth(self.img_colorspaceLabel.sizePolicy().hasHeightForWidth())
        self.img_colorspaceLabel.setSizePolicy(sizePolicy)
        self.img_colorspaceLabel.setScaledContents(True)

        self.gridLayout.addWidget(self.img_colorspaceLabel, 1, 2, 1, 1)

        self.img_origLabel = ImageLabel(self.centralwidget)
        self.img_origLabel.setObjectName(u"img_origLabel")
        sizePolicy.setHeightForWidth(self.img_origLabel.sizePolicy().hasHeightForWidth())
        self.img_origLabel.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.img_origLabel, 0, 2, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.rangeEditor = RangeEditor(self.centralwidget)
        self.rangeEditor.setObjectName(u"rangeEditor")

        self.verticalLayout_2.addWidget(self.rangeEditor)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.loadImageButton = QPushButton(self.groupBox)
        self.loadImageButton.setObjectName(u"loadImageButton")

        self.verticalLayout.addWidget(self.loadImageButton)


        self.verticalLayout_2.addWidget(self.groupBox)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.img_maskedColorLabel.setText(QCoreApplication.translate("MainWindow", u"MASKED_COLOR", None))
        self.img_maskedBwLabel.setText(QCoreApplication.translate("MainWindow", u"MASKED_BW", None))
        self.img_colorspaceLabel.setText(QCoreApplication.translate("MainWindow", u"COLORSPACE", None))
        self.img_origLabel.setText(QCoreApplication.translate("MainWindow", u"ORIG", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.loadImageButton.setText(QCoreApplication.translate("MainWindow", u"Load Image", None))
    # retranslateUi

