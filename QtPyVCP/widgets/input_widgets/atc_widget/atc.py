import os

# Workarround for nvidia propietary drivers

import ctypes
import ctypes.util

ctypes.CDLL(ctypes.util.find_library("GL"), mode=ctypes.RTLD_GLOBAL)

# end of Workarround

from hal import component, HAL_BIT, HAL_IN

from PyQt5.QtCore import pyqtSignal, pyqtSlot, QUrl
from PyQt5.QtQuickWidgets import QQuickWidget

WIDGET_PATH = os.path.dirname(os.path.abspath(__file__))


def _initComp():
    halcomp = component("atc_widget")

    halcomp.newpin("fwd", HAL_BIT, HAL_IN)
    halcomp.newpin("rev", HAL_BIT, HAL_IN)
    halcomp.ready()

    return halcomp


class DynATC(QQuickWidget):

    def __init__(self, parent=None):

        super(DynATC, self).__init__(parent)

        self.rootContext().setContextProperty("atc_spiner", self)

        url = QUrl.fromLocalFile(os.path.join(WIDGET_PATH, "atc.qml"))
        self.setSource(url)

        try:
            self.halcomp = _initComp()
        except Exception as e:
            self.halcomp = None

        self.atc_tool = 0
        self.atc_previous_tool = 0
        self.atc_rotation = 0

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

    pinSig = pyqtSignal(arguments=['get_pins'])
    # Slot for summing two numbers
    @pyqtSlot()
    def get_pins(self):

        if self.halcomp is not None:
            self.atc_tool = self.halcomp["fwd"]
            if self.atc_tool != self.atc_previous_tool:
                self.rotateSig.emit(self.atc_rotation)
                self.atc_previous_tool = self.atc_tool

            self.atc_tool = self.halcomp["rev"]
            if self.atc_tool != self.atc_previous_tool:
                self.rotateSig.emit(self.atc_rotation)
                self.atc_previous_tool = self.atc_tool
