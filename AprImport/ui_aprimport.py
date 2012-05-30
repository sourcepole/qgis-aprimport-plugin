# -*- coding: utf-8 -*-

"""
Module implementing AprImport.
"""

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from qgis.core import *
from qgis.gui import *

from forms.Ui_ui_aprimport import Ui_AprImport
from aprlib.apr import Apr

class AprImportDialog(QDialog, Ui_AprImport):
    """
    Class documentation goes here.
    """
    def __init__(self, iface,  parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.iface = iface
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
        
        QApplication.setOverrideCursor(Qt.WaitCursor)        
        self.parseApr(self.fileName)
        QApplication.restoreOverrideCursor()
        
    
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
        self.loadLayers()
    
    @pyqtSignature("")
    def on_buttonBox_rejected(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        QApplication.restoreOverrideCursor()
        self.close()
        
    def parseApr(self,  fileName=None):
        aprFile = fileName
        try:
            self.aprreader = Apr(aprFile)
            self.aprreader.parse()
            for view in self.aprreader.views():
                viewItem = QTreeWidgetItem(self.treeWidget)      
                viewItem.setText(0, view.value('Name'))
                self.treeWidget.addTopLevelItem(viewItem)
                for th in view.refs('Theme'):
                    try:
                        layerItem = QTreeWidgetItem(viewItem)
                        viewItem.addChild(layerItem)
                        layerItem.setText(0,  th.value('Name'))
                        layerItem.setDisabled(True)
                        layerItem.setTextColor(QColor(255, 0, 0, 127))
                    except:
                        pass
        except:
            QMessageBox.information(None, 'Error',  'Error while reading APR-File')
            
            
            
    def  loadLayers(self):
        layerList = []
        error = False
        for view in self.aprreader.views():
            itemList = self.treeWidget.selectedItems()
            if  view.value('Name')== itemList[0].text(0):
                for theTheme in view.refs('Theme'):
                    print theTheme.value('Name')
                    try:
                        themeType =  theTheme.ref('Source').ref('Name').value('OwnerClass')
                        fileName = theTheme.ref('Source').ref('Name').ref('FileName').value('Path')
                        layerName = theTheme.value('Name')                        
                    except:
                        themeType = None

                    if themeType == 'ShpSrc':
                        vLayer = QgsVectorLayer(fileName, layerName, "ogr")
                        if not vLayer.isValid():
                            print "Layer failed to load!"
                            error = True
                        else:
                            layerList.append(vLayer)
                    elif themeType == 'GSrc':
                        fileInfo = QFileInfo(fileName)
                        baseName = fileInfo.baseName()
                        rlayer = QgsRasterLayer(fileName, baseName)
                        if not rlayer.isValid():
                            print "Layer failed to load!"
                            error = True
                        else:
                            layerList.append(vLayer)
                        
        layerList.reverse()
        
        for layer in layerList:
            QgsMapLayerRegistry.instance().addMapLayer(layer)             
            
                
        if error:
            QMessageBox.information(None, 'Error', 'Es konnten nicht alle Layer geladen werden. Eine Liste der fehlerhaften Layer folgt in der nächsten Version')
#                
                

