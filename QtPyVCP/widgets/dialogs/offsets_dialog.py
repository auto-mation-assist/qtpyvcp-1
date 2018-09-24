#!/usr/bin/env python

#   Copyright (c) 2018 Kurt Jacobson
#      <kurtcjacobson@gmail.com>
#
#   This file is part of QtPyVCP.
#
#   QtPyVCP is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 2 of the License, or
#   (at your option) any later version.
#
#   QtPyVCP is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with QtPyVCP.  If not, see <http://www.gnu.org/licenses/>.

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
                             QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
                             QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
                             QVBoxLayout)

from QtPyVCP.utilities.info import Info


class OffsetsDialog(QDialog):

    def set_method(self):
        print('Set method called.')

    def close_method(self):
        print('Close method called.')

    def __init__(self):
        super(OffsetsDialog, self).__init__()

        info = Info()

        axis_list = info.getAxisList()

        coords_combo = QComboBox()
        for axis in axis_list:
            coords_combo.addItem(axis.upper(), axis)

        coords_msg = QLabel("Coordinate relative to workpiece:")
        system_msg = QLabel("Coordinate System:")

        coords_input = QLineEdit('0.0000')
        coords_input.setInputMask('000009.00000')

        system_combo = QComboBox()
        system_combo.addItem("P0 - Current", "P0")
        system_combo.addItem("P1 - G54", "P1")
        system_combo.addItem("P2 - G55", "P2")
        system_combo.addItem("P3 - G56", "P3")
        system_combo.addItem("P4 - G57", "P4")
        system_combo.addItem("P5 - G58", "P5")
        system_combo.addItem("P6 - G59", "P6")
        system_combo.addItem("P7 - G59.1", "P6")
        system_combo.addItem("P8 - G59.2", "P7")
        system_combo.addItem("P9 - G59.3", "P8")

        close_button = QPushButton("Close")
        set_button = QPushButton("Set")

        mainLayout = QVBoxLayout()
        buttonLayout = QHBoxLayout()

        buttonLayout.addWidget(close_button)
        buttonLayout.addWidget(set_button)

        mainLayout.addWidget(coords_combo, alignment=Qt.AlignTop)
        mainLayout.addWidget(coords_msg, alignment=Qt.AlignLeft | Qt.AlignTop)
        mainLayout.addWidget(coords_input, alignment=Qt.AlignTop)
        mainLayout.addWidget(system_msg, alignment=Qt.AlignLeft | Qt.AlignTop)
        mainLayout.addWidget(system_combo, alignment=Qt.AlignBottom)
        mainLayout.addLayout(buttonLayout)

        self.setLayout(mainLayout)
        self.setWindowTitle("Regular Offsets")

        set_button.clicked.connect(self.set_method)
        close_button.clicked.connect(self.close_method)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = OffsetsDialog()
    sys.exit(dialog.exec_())