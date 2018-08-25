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

# Description:
# Tool table viewer/editor.

import os
import sys

import linuxcnc

from PyQt5.QtCore import pyqtSlot, pyqtProperty, Qt, QModelIndex, QAbstractTableModel, QRegExp
from PyQt5.QtGui import QValidator, QRegExpValidator
from PyQt5.QtWidgets import QTableView, QMessageBox, QAbstractItemView, QSpinBox, QDoubleSpinBox, \
    QLineEdit, QStyledItemDelegate

# Set up logging
from QtPyVCP.utilities import logger
from QtPyVCP.utilities.info import Info

LOG = logger.getLogger(__name__)
INFO = Info()


class ItemDelegate(QStyledItemDelegate):
    
    def __init__(self):
        super(ItemDelegate, self).__init__()
        self._padding = ' ' * 2

    def displayText(self, value, locale):

        if type(value) == int:
            return str(value)
        elif type(value) == float:
            return "{0:.4f}".format(value)

        return "{}{}".format(self._padding, value)

    def createEditor(self, parent, option, index):
        if index.column() in (0, 1):

            editor = QSpinBox(parent)
            editor.setMinimum(0)
            editor.setMaximum(100)
            return editor

        elif index.column() in (2, 3):
            editor = QDoubleSpinBox(parent)
            editor.setMinimum(0)
            return editor

        elif index.column() == 4:
            editor = QLineEdit(parent)
            margins = editor.textMargins()
            padding = editor.fontMetrics().width(self._padding) + 1
            margins.setLeft(margins.left() + padding)
            editor.setTextMargins(margins)
            return editor

        return None

    def setEditorData(self, item, index):
        value = index.model().data(index, Qt.EditRole)
        if index.column() in (0, 1, 2, 3):
            item.setValue(value)
        else:
            item.setText(value)

    def setModelData(self, item, model, index):
        if index.column() in (0, 1, 2, 3):
            item.interpretText()
            value = item.value()
        else:
            value = item.text()

        model.setData(index, value, Qt.EditRole)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)


class ToolItem(object):
    def __init__(self, data, parent=None):
        self.parentItem = parent
        self.itemData = data
        self.childItems = []

    def appendChild(self, item):
        self.childItems.append(item)

    def removeChild(self, index):
        self.childItems.pop(index)

    def child(self, row):
        return self.childItems[row]

    def childCount(self):
        return len(self.childItems)

    def columnCount(self):
        return len(self.itemData)

    def data(self, column):
        try:
            return self.itemData[column]
        except IndexError:
            return None

    def parent(self):
        return self.parentItem

    def row(self):
        if self.parentItem:
            return self.parentItem.childItems.index(self)
        return 0


class ToolModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super(ToolModel, self).__init__(parent)
        self.table_header = ["Tool", "Pocket", "Z", "Diameter", "Comment"]

        self.rootItem = ToolItem(self.table_header)
        self.tool_list = list()

    def columnCount(self, parent=None):
        return len(self.table_header)

    def rowCount(self, parent=None):
        return len(self.tool_list)

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.table_header[section]

        return QAbstractTableModel.headerData(self, section, orientation, role)

    def index(self, row, column, parent):
        if not self.hasIndex(row, column, parent):
            return QModelIndex()

        if not parent.isValid():
            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()

        childItem = parentItem.child(row)
        if childItem:
            return self.createIndex(row, column, childItem)
        else:
            return QModelIndex()

    def parent(self, index):
        if not index.isValid():
            return QModelIndex()

        childItem = index.internalPointer()
        parentItem = childItem.parent()

        if parentItem == self.rootItem:
            return QModelIndex()

        return self.createIndex(parentItem.row(), 0, parentItem)

    def data(self, index, role=Qt.DisplayRole):
        return self._data(self.tool_list[index.row()], index.column(), role)

    def _data(self, item, column, role=Qt.DisplayRole):
        if role == Qt.EditRole:
            if column == 0:
                return int(item[0])
            elif column == 1:
                return int(item[1])
            elif column == 2:
                return float(item[2])
            elif column == 3:
                return float(item[3])
            elif column == 4:
                return str(item[4])

        elif role == Qt.DisplayRole:
            if column == 0:
                return item[0]
            elif column == 1:
                return item[1]
            elif column == 2:
                return item[2]
            elif column == 3:
                return item[3]
            elif column == 4:
                return item[4]

        elif role == Qt.TextAlignmentRole:
            if column == 0:
                return Qt.AlignVCenter | Qt.AlignCenter
            elif column == 1:
                return Qt.AlignVCenter | Qt.AlignCenter
            elif column == 2:
                return Qt.AlignVCenter | Qt.AlignRight
            elif column == 3:
                return Qt.AlignVCenter | Qt.AlignRight
            elif column == 4:
                return Qt.AlignVCenter | Qt.AlignLeft
        """
        elif role == Qt.FontRole:

            font = QFont()
            font.setBold(True)
            return font
        """
        return None

    def setData(self, index, value, role):
        self.tool_list[index.row()][index.column()] = value
        return True

    def loadToolTable(self, file):

        parents = [self.rootItem]
        indentations = [0]

        for count, line in enumerate(file):

            # Separate tool data from comments

            tool = []

            comment = ''
            index = line.find(";")  # Find comment start index

            if index == -1:  # Delimiter ';' is missing, so no comments
                line = line.rstrip("\n")
            else:
                comment = (line[index + 1:]).rstrip("\n")
                line = line[0:index].rstrip()

            for offset, i in enumerate(['T', 'P', 'Z', 'D']):
                for word in line.split():
                    if word.startswith(i):
                        item = word.lstrip(i)
                        if i in ('T', 'P'):
                            tool.append(int(item))
                        elif i in ('Z', 'D'):
                            tool.append(float(item))

            tool.append(str(comment))

            # Append a new item to the current parent's list of children.
            parents[-1].appendChild(ToolItem(tool, parents[-1]))

            self.tool_list.append(tool)

    def saveToolTable(self, file):
        for row_index in range(self.rowCount()):
            line = ""
            for col_index in range(self.columnCount()):
                item = self.tool_list[row_index][col_index]
                if item is not None and item != "":
                    if col_index in (range(0, 4)):
                        line += "{}{} ".format(['T', 'P', 'Z', 'D', ';'][col_index], item)
                    else:
                        line += "{}{}".format(['T', 'P', 'Z', 'D', ';'][col_index], item.strip())
            if line:
                line += "\n"
                file.write(line)

        file.flush()
        os.fsync(file.fileno())

    def addTool(self, tool):
        pass

    def removeRow(self, row):
        self.tool_list.pop(row)


class ToolTable(QTableView):

    def __init__(self, parent=None):
        super(ToolTable, self).__init__(parent)
        self.parent = parent

        self.cmd = linuxcnc.command()

        self.model = ToolModel(self)

        delegate = ItemDelegate()

        self.setItemDelegate(delegate)

        self.setModel(self.model)
        self.horizontalHeader().setStretchLastSection(True)
        self.setAlternatingRowColors(True)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.verticalHeader().hide()

        self.tool_table_file = INFO.getToolTableFile()

        self.tool_table_loaded = False
        self.loadToolTable()
        self.tool_table_loaded = True

    @pyqtSlot()
    def loadToolTable(self):
        if self.tool_table_loaded and not self.ask_dialog(
                "Do you wan't to re-load the tool table?\n all unsaved changes will be lost."):
            return

        if len(self.model.tool_list):
            self.removeAllTools(confirm=False)

        fn = self.tool_table_file

        if fn is None:
            return

        if not os.path.exists(fn):
            LOG.warning("Tool table does not exist")
            return

        LOG.debug("Loading tool table: {0}".format(fn))

        with open(fn, "r") as f:
            self.model.loadToolTable(f)

    @pyqtSlot()
    def saveToolTable(self):
        if not self.ask_dialog("Do you wan't to save and load this tool table into the system?"):
            return

        fn = self.tool_table_file

        if fn is None:
            return

        LOG.debug("Saving tool table as: {0}".format(fn))

        with open(fn, "w") as f:
            self.model.saveToolTable(f)

        self.cmd.load_tool_table()

    @pyqtSlot()
    def insertToolAbove(self):
        row_num = self.selectedRow()
        self.model.insertRow(row_num, self.newRow(row_num))
        self.selectRow(row_num)

    @pyqtSlot()
    def insertToolBelow(self):
        row_num = self.selectedRow() + 1
        self.model.insertRow(row_num, self.newRow(row_num))
        self.selectRow(row_num)

    @pyqtSlot()
    def deleteSelectedTool(self):
        current_row = self.selectedRow()
        current_tool = self.model.tool_list[current_row][0]

        if not self.ask_dialog("Do yo wan't to delete T{} ?".format(current_tool)):
            return

        indexes = self.selectionModel().selectedRows()
        for index in sorted(indexes):
            self.model.removeRow(index.row())

    @pyqtSlot()
    def removeAllTools(self, confirm=True):
        if confirm:
            if not self.ask_dialog("Do yo wan't to delete the whole tool table?"):
                return

        for i in reversed(range(self.model.rowCount() + 1)):
            self.model.removeRow(i)

    def ask_dialog(self, message):
        box = QMessageBox.question(self.parent,
                                   'Are you sure?',
                                   message,
                                   QMessageBox.Yes,
                                   QMessageBox.No)
        if box == QMessageBox.Yes:
            return True
        else:
            return False

    def newRow(self, row_num=0):
        new_data = [row_num, row_num, 0.0, 0.0, 'New Tool']
        row_items = [item for item in new_data]
        return row_items

    def selectedRow(self):
        return self.selectionModel().currentIndex().row()
