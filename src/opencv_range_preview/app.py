import sys
from pathlib import Path

from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtQuickControls2 import QQuickStyle

from opencv_range_preview.previewer import Previewer

# The default Windows style leaves chrome (tool bar, buttons) light in
# dark mode; Fusion follows the system palette. Must be set before the
# application object is constructed.
QQuickStyle.setStyle("Fusion")

MAIN_QML = Path(__file__).parent / "ui" / "MainWindow.qml"


def loadFail(url: QUrl) -> None:
    print(f"load {url=} fail, exit")
    sys.exit(1)


def main() -> None:
    app = QGuiApplication(sys.argv)

    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.objectCreationFailed.connect(loadFail)

    previewer = Previewer()
    engine.addImageProvider("preview", previewer.provider)
    engine.rootContext().setContextProperty("backend", previewer)

    engine.load(QUrl.fromLocalFile(str(MAIN_QML)))

    sys.exit(app.exec())
