# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AprImport
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
 This script initializes the plugin, making it known to QGIS.
"""
def name():
    return "ArcView-APR Import"
def description():
    return "Imports Layer-Data from ArcView APR-"
def version():
    return "Version 0.1"
def icon():
    return "icon.png"
def qgisMinimumVersion():
    return "1.0"
def classFactory(iface):
    # load AprImport class from file AprImport
    from aprimport import AprImport
    return AprImport(iface)
