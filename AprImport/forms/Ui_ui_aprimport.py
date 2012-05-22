# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/hdus/dev/qgis-aprimport-plugin/AprImport/forms/ui_aprimport.ui'
#
# Created: Tue May 22 14:36:31 2012
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
        AprImport.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(AprImport)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.retranslateUi(AprImport)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AprImport.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AprImport.reject)
        QtCore.QMetaObject.connectSlotsByName(AprImport)

    def retranslateUi(self, AprImport):
        AprImport.setWindowTitle(QtGui.QApplication.translate("AprImport", "AprImport", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    AprImport = QtGui.QDialog()
    ui = Ui_AprImport()
    ui.setupUi(AprImport)
    AprImport.show()
    sys.exit(app.exec_())

