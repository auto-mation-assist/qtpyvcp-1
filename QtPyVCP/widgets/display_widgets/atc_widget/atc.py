import time

from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot


class DynATC(QObject):

    def __init__(self):
        QObject.__init__(self)
        self.atc_rotation = 0

    # Signal sending sum
    # Necessarily give the name of the argument through arguments=['sum']
    # Otherwise it will not be possible to get it up in QML
    sumResult = pyqtSignal(int, arguments=['sum'])

    # Slot for summing two numbers
    @pyqtSlot(int)
    def sum(self):
        self.atc_rotation += 1
        self.sumResult.emit(self.atc_rotation)


if __name__ == "__main__":
    import sys

    # Create an instance of the application
    app = QGuiApplication(sys.argv)

    # Create QML engine
    engine = QQmlApplicationEngine()

    # Create a calculator object
    calculator = DynATC()

    # And register it in the context of QML
    engine.rootContext().setContextProperty("calculator", calculator)
    # Load the qml file into the engine
    engine.load("atc.qml")

    engine.quit.connect(app.quit)
    sys.exit(app.exec_())
