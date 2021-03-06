#!/usr/bin/env python

import linuxcnc
from PyQt5.QtWidgets import QSlider
from PyQt5.QtCore import pyqtSlot, pyqtProperty

from QtPyVCP.actions import bindWidget

class ActionSlider(QSlider):
    """docstring for ActionSlider."""
    def __init__(self, parent=None):
        super(ActionSlider, self).__init__(parent)

        self._action_name = ''

    @pyqtProperty(str)
    def actionName(self):
        """The fully qualified name of the action the slider should trigger.

        Returns:
            str : The action name.
        """
        return self._action_name

    @actionName.setter
    def actionName(self, action_name):
        """Sets the name of the action the slider should trigger.

        Args:
            action_name (str) : A fully qualified action name.
        """
        self._action_name = action_name
        bindWidget(self, action_name)
