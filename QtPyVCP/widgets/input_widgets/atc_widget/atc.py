import os

# Workarround for nvidia propietary drivers

import ctypes
import ctypes.util

ctypes.CDLL(ctypes.util.find_library("GL"), mode=ctypes.RTLD_GLOBAL)

# end of Workarround

from hal import component, component_exists, HAL_BIT, HAL_IN

from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QUrl, QObject
from PyQt5.QtQuickWidgets import QQuickWidget

WIDGET_PATH = os.path.dirname(os.path.abspath(__file__))


class DynATC(QQuickWidget):

    def __init__(self, parent=None):
        super(DynATC, self).__init__(parent)

        try:
            self.halcomp = self._initComp()
        except Exception as e:
            self.halcomp = None

        url = QUrl.fromLocalFile(os.path.join(WIDGET_PATH, "atc.qml"))
        self.rootContext().setContextProperty("atc_spiner", self)

        self.setSource(url)

        self.atc_tool = 0
        self.atc_previous_tool = 0
        self.atc_rotation = 0

    def _initComp(self):

        halcomp = component("lol")

        if not component_exists("lol"):
            print("NONONONO")

        halcomp.newpin("fwd", HAL_BIT, HAL_IN)
        halcomp.newpin("rev", HAL_BIT, HAL_IN)
        # halcomp.ready()

        return halcomp

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
        if self.halcomp is None:
            return

        self.atc_tool = self.halcomp["fwd"]
        if self.atc_tool != self.atc_previous_tool:
            self.rotateSig.emit(self.atc_rotation)
            self.atc_previous_tool = self.atc_tool

        self.atc_tool = self.halcomp["rev"]
        if self.atc_tool != self.atc_previous_tool:
            self.rotateSig.emit(self.atc_rotation)
            self.atc_previous_tool = self.atc_tool
