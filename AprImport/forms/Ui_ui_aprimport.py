# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/hdus/dev/qgis-aprimport-plugin/AprImport/forms/ui_aprimport.ui'
#
# Created: Wed May 23 08:07:34 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AprImport(object):
    def setupUi(self, AprImport):
        AprImport.setObjectName(_fromUtf8("AprImport"))
        AprImport.resize(521, 375)
        self.gridLayout = QtGui.QGridLayout(AprImport)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(AprImport)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lneAprFileName = QtGui.QLineEdit(AprImport)
        self.lneAprFileName.setObjectName(_fromUtf8("lneAprFileName"))
        self.horizontalLayout.addWidget(self.lneAprFileName)
        self.toolButton = QtGui.QToolButton(AprImport)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.horizontalLayout.addWidget(self.toolButton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.treeWidget = QtGui.QTreeWidget(AprImport)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.headerItem().setText(0, _fromUtf8("1"))
        self.gridLayout.addWidget(self.treeWidget, 1, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(AprImport)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)

        self.retranslateUi(AprImport)
        QtCore.QMetaObject.connectSlotsByName(AprImport)

    def retranslateUi(self, AprImport):
        AprImport.setWindowTitle(QtGui.QApplication.translate("AprImport", "AprImport", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AprImport", "APR-File:", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton.setText(QtGui.QApplication.translate("AprImport", "...", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    AprImport = QtGui.QDialog()
    ui = Ui_AprImport()
    ui.setupUi(AprImport)
    AprImport.show()
    sys.exit(app.exec_())

