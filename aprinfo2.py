#!/usr/bin/python
# -*- coding: utf-8 -*-
from AprImport.aprlib import apr
from sys import argv, stdin

if len(argv) >= 2:
    aprfile = argv[1]
    aprreader = apr.Apr(aprfile)
    aprreader.parse()
    for view in aprreader.views():
#        print view.value('Name')
#        print view.value('Theme')
        for th in aprreader.themes(view): 
#            try:
                print th.value('Name')
                print th
#                print th.value('Source').value('Name').value('FileName').value('Path')
##                print th.value('Source').value('Name').value('FileName').value('Path')
#            except:
#                pass
else: print >>sys.stderr, 'Args: <filename>'
