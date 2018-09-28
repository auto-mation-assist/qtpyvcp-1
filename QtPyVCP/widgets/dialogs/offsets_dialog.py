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

from linuxcnc import command

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QComboBox, QDialog, QHBoxLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout

from QtPyVCP.utilities.info import Info


class OffsetsDialog(QDialog):

    def __init__(self, parent):
        super(OffsetsDialog, self).__init__(parent=parent, flags=Qt.Popup)

        info = Info()

        self.cmd = command

        axis_list = info.getAxisList()

        self.axis_combo = QComboBox()
        for axis in axis_list:
            self.axis_combo.addItem(axis.upper(), axis)

        coords_msg = QLabel("Coordinate relative to workpiece:")
        system_msg = QLabel("Coordinate System:")

        self.coords_input = QLineEdit('0.0000')
        self.coords_input.setInputMask('000009.00000')

        self.system_combo = QComboBox()

        systems = {"P0": "P0 Current",
                   "P1": "P1 G54",
                   "P2": "P1 G55",
                   "P3": "P1 G56",
                   "P4": "P1 G57",
                   "P5": "P1 G58",
                   "P6": "P1 G59",
                   "P7": "P1 G59.1",
                   "P8": "P1 G59.1",
                   "P9": "P1 G59.3"
                   }

        for key, value in systems.items():
            self.system_combo.addItem(value, key)

        close_button = QPushButton("Close")
        set_button = QPushButton("Set")

        mainLayout = QVBoxLayout()
        buttonLayout = QHBoxLayout()

        buttonLayout.addWidget(close_button)
        buttonLayout.addWidget(set_button)

        mainLayout.addWidget(self.axis_combo, alignment=Qt.AlignTop)
        mainLayout.addWidget(coords_msg, alignment=Qt.AlignLeft | Qt.AlignTop)
        mainLayout.addWidget(self.coords_input, alignment=Qt.AlignTop)
        mainLayout.addWidget(system_msg, alignment=Qt.AlignLeft | Qt.AlignTop)
        mainLayout.addWidget(self.system_combo, alignment=Qt.AlignBottom)
        mainLayout.addLayout(buttonLayout)

        self.setLayout(mainLayout)
        self.setWindowTitle("Regular Offsets")

        set_button.clicked.connect(self.set_method)
        close_button.clicked.connect(self.close_method)

    def set_method(self):
        system = self.system_combo.currentData()
        axis = self.axis_combo.currentData()
        coords = self.coords_input.text()

        offset_cmd = command("G10 L20 {} {}{}"
                             .format(system,
                                     axis,
                                     coords
                                     )
                             )

        self.cmd.mdi(offset_cmd)

    def close_method(self):
        self.hide()
