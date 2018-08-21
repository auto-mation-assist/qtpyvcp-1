import os
import hal

# Workarround for nvidia propietary drivers

import ctypes
import ctypes.util
ctypes.CDLL(ctypes.util.find_library("GL"), mode=ctypes.RTLD_GLOBAL)

# end of Workarround

from PyQt5.QtCore import pyqtSignal, pyqtSlot, QUrl, QObject
from PyQt5.QtQuickWidgets import QQuickWidget

WIDGET_PATH = os.path.dirname(os.path.abspath(__file__))


class DynATC(QQuickWidget, QObject):

    def __init__(self, parent=None):
        super(DynATC, self).__init__(parent)

        url = QUrl.fromLocalFile(os.path.join(WIDGET_PATH, "atc.qml"))
        self.setSource(url)

        self.rootContext().setContextProperty("main", self)

        self.atc_tool = 0
        self.atc_previous_tool = 0
        self.atc_rotation = 0

        self.halcomp = None

        self._initComp()

    def _initComp(self):

        self.halcomp = hal.component("atc_widget")
        self.halcomp.newpin("tool", hal.HAL_FLOAT, hal.HAL_IN)

        self.halcomp.ready()

    rotateFwdSig = pyqtSignal(int, arguments=['rotate_forward'])
    # Slot for summing two numbers
    @pyqtSlot(int)
    def rotate_forward(self, value):
        self.rotateFwdSig.emit(self.atc_rotation)
        self.atc_rotation += 1

    rotateRevSig = pyqtSignal(int, arguments=['rotate_reverse'])
    # Slot for summing two numbers
    @pyqtSlot(int)
    def rotate_reverse(self, value):
        self.rotateRevSig.emit(self.atc_rotation)
        self.atc_rotation -= 1


    """
    pinSig = pyqtSignal(arguments=['get_pins'])
    # Slot for summing two numbers
    @pyqtSlot()
    def get_pins(self):
        self.atc_tool = self.halcomp["tool"]
        if self.atc_tool != self.atc_previous_tool:
            self.rotateSig.emit(self.atc_rotation)
            self.atc_previous_tool = self.atc_tool
    """