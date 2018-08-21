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
    halcomp.newpin("count", HAL_BIT, HAL_IN)
    halcomp.ready()

    return halcomp


class DynATC(QQuickWidget):

    def __init__(self, parent=None):

        super(DynATC, self).__init__(parent)

        self.engine().rootContext().setContextProperty("atc_spiner", self)
        url = QUrl.fromLocalFile(os.path.join(WIDGET_PATH, "atc.qml"))
        self.setSource(url)

        try:
            self.halcomp = _initComp()
        except Exception as e:
            self.halcomp = None

        self.fwd_pin = 0
        self.rev_pin = 0

        self.atc_counter_pin = 0
        self.prev_atc_counter_pin = 0

        self.atc_position = 0

    rotateFwdSig = pyqtSignal(int, arguments=['rotate_forward'])
    @pyqtSlot()
    def rotate_forward(self):
        self.rotateFwdSig.emit(self.atc_position)
        self.atc_position += 1

    rotateRevSig = pyqtSignal(int, arguments=['rotate_reverse'])
    @pyqtSlot()
    def rotate_reverse(self):
        self.rotateRevSig.emit(self.atc_position)
        self.atc_position -= 1

    pinSig = pyqtSignal(arguments=['get_pins'])
    @pyqtSlot()
    def get_pins(self):
        if self.halcomp is None:
            return

        self.fwd_pin = self.halcomp["fwd"]
        if self.fwd_pin == 1 and self.turn_next:
            self.rotateFwdSig.emit(self.atc_position)
            self.atc_position += 1

        self.rev_pin = self.halcomp["rev"]
        if self.rev_pin == 1 and self.turn_next:
            self.rotateRevSig.emit(self.atc_position)
            self.atc_position += 1

        self.atc_counter_pin = self.halcomp["count"]
        if self.atc_counter_pin != self.prev_atc_counter_pin:
            self.prev_atc_counter_pin = self.atc_counter_pin
