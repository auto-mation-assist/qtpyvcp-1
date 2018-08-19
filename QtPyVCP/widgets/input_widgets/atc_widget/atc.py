import os

# Workarround for nvidia propietary drivers

import ctypes
import ctypes.util
ctypes.CDLL(ctypes.util.find_library("GL"), mode=ctypes.RTLD_GLOBAL)

# end of Workarround

from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QUrl
from PyQt5.QtQuickWidgets import QQuickWidget

WIDGET_PATH = os.path.dirname(os.path.abspath(__file__))


class DynATC(QQuickWidget):

    changeResult = pyqtSignal(int, arguments=['change'])

    def __init__(self, parent=None):
        super(DynATC, self).__init__(parent)

        url = QUrl.fromLocalFile(os.path.join(WIDGET_PATH, "atc.qml"))
        self.setSource(url)

        self.rootContext().setContextProperty("main", self)

        self.atc_rotation = 0

    # Slot for summing two numbers
    @pyqtSlot(int)
    def rotate_atc(self):
        self.changeResult.emit(self.atc_rotation)
        self.atc_rotation += 1
