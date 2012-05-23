#!/usr/bin/python
# -*- coding: utf-8 -*-
from aprlib import apr
from sys import argv, stdin

if len(argv) >= 2:
    aprfile = argv[1]
    aprreader = apr.Apr(aprfile)
    aprreader.parse()
    for view in aprreader.views():
        print view.value('Name')
        print view.value('Theme')
        for th in aprreader.themes(view): print th
else: print >>sys.stderr, 'Args: <filename>'
