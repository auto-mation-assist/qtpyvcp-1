import os

from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QUrl
from PyQt5.QtQuickWidgets import QQuickWidget

WIDGET_PATH = os.path.dirname(os.path.abspath(__file__))

class DynATC(QQuickWidget):

    def __init__(self, parent=None):
        super(DynATC, self).__init__(parent)
        self.atc_rotation = 0

        url = QUrl.fromLocalFile(os.path.join(WIDGET_PATH, "atc.qml"))
        self.setSource(url)

        self.rootContext().setContextProperty("atc_holder", self)
        self.rotateResult = pyqtSignal(int, arguments=['rotate'])

    # Slot for summing two numbers
    @pyqtSlot(int)
    def rotate(self):
        self.atc_rotation += 1
        self.rotateResult.emit(self.atc_rotation)
