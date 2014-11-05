# -*- coding: utf-8 -*-

import sys, string, os


# Local variables...

script = 'pyuic4 -o'
uiFile = ' MainUI.ui'
pyFile = ' MainUI.py'

script = script + pyFile + uiFile

print script

os.system(script)

