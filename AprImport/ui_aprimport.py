# -*- coding: utf-8 -*-

"""
Module implementing AprImport.
"""

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from forms.Ui_ui_aprimport import Ui_AprImport
from aprlib.apr import Apr

class AprImportDialog(QDialog, Ui_AprImport):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.fileName = ''
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)             
        
    
    @pyqtSignature("")
    def on_toolButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.treeWidget.clear()
        settings = QSettings()
        mySettings = "ArcView-Import-Plugin"
        myDir = settings.value(mySettings+"/lastDirectory").toString()
        self.fileName = QFileDialog.getOpenFileName(None, 'Open APR-File',myDir, 'ArcView-Project (*.apr)' )
        settings.setValue(mySettings+"/lastDirectory",  QFileInfo(self.fileName).dir().path())        
        self.lneAprFileName.setText(self.fileName)
        self.parseApr(self.fileName)

        
    
    @pyqtSignature("QModelIndex")
    def on_treeWidget_doubleClicked(self, index):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSignature("")
    def on_buttonBox_accepted(self):
        """
        Slot documentation goes here.
        """
        pass
    
    @pyqtSignature("")
    def on_buttonBox_rejected(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.close()
        
    def parseApr(self,  fileName=None):
        QApplication.setOverrideCursor(Qt.WaitCursor)
        aprFile = fileName
<<<<<<< HEAD
        try:
            aprreader = Apr(aprFile)
            aprreader.parse()
            viewItem = QTreeWidgetItem(self.treeWidget)      
            for view in aprreader.views():
                print view.value('Name')
                print view.value('Theme')
                viewItem.setText(0, view.value('Name'))
    
                layerItem = QTreeWidgetItem(viewItem)
                for th in aprreader.themes(view): 
                    try:
                        print '+++'+th.value('Name')
                        print '---'+th.value('Source').value('Name').value('FileName').value('Path')
                        layerItem.setText(0,  th.value('Name'))
                        layerItem.setText(1,  th.value('Source').value('Name').value('FileName').value('Path'))
                    except:
                        QApplication.restoreOverrideCursor()
                        pass
                        
                QApplication.restoreOverrideCursor()
        except:
            QMessageBox.information(None, 'Error',  'Error while reading APR-File')
            QApplication.restoreOverrideCursor()
                    
=======
        aprreader = Apr(aprFile)
        aprreader.parse()
        for view in aprreader.views():
            print view.value('Name')
            for theme in view.refs('Theme'):
                try:
                   print theme.ref('Source').ref('Name').ref('FileName').value('Path')
                except:
                  pass
>>>>>>> e6bd9660720e9475a942bd8c0f4b5e2282b5a783
