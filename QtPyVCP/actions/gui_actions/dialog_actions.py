#!/usr/bin/env python
# coding: utf-8

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

# Description:
#   LinuxCNC coolant actions

import os
import imp
import glob
import inspect

from PyQt5.QtWidgets import QDialog

# Set up logging
from QtPyVCP.utilities import logger
LOG = logger.getLogger(__name__)

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
DIALOG_DIR = os.path.abspath(os.path.join(THIS_DIR, '../../widgets/dialogs'))
print THIS_DIR
print DIALOG_DIR

DIALOGS = {}

def registerDialog(pyfile):
        """
        Load a .py file, performs some sanity checks to try and determine
        if the file actually contains a valid VCPMainWindow subclass, and if
        the checks pass, create and return an instance.

        This is an internal method, users will usually want to use `loadVCP` instead.

        Parameters
        ----------
        pyfile : str
            The path to a .py file to load.
        opts : OptDict
            A OptDict of options to pass to the VCPMainWindow subclass.

        Returns
        -------
        VCPMainWindow instance
        """
        module_name = os.path.splitext(os.path.basename(pyfile))[0]
        module = imp.load_source('QtPyVCP.widgets.dialogs.' + module_name, pyfile)

        for name, obj in inspect.getmembers(module):
            if inspect.isclass(obj) and issubclass(obj, QDialog):
                try:
                    print obj.id
                    DIALOGS[obj.id] = obj()
                except:
                    pass

def show(dialog_name):
    print "Show dialog:", dialog_name
    DIALOGS[dialog_name].show()

print "################"
for file in glob.glob(DIALOG_DIR + '/*.py'):
    print file
    print "################"
    registerDialog(file)

print DIALOGS
