# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AprImportDialog
                                 A QGIS plugin
 Imports Layer-Data from ArcView APR-
                             -------------------
        begin                : 2012-05-22
        copyright            : (C) 2012 by Dr. Horst Düster/Sourcepole AG
        email                : horst.duester@sourcepole.ch
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4 import QtCore, QtGui
from forms.Ui_ui_aprimport import Ui_AprImport
# create the dialog for zoom to point
class AprImportDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_AprImport()
        self.ui.setupUi(self)
