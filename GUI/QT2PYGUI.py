# -*- coding: utf-8 -*-

import sys, string, os


# Local variables...

script = 'pyuic4 -o'
uiFile = ' Bonsall_UI.ui'
pyFile = ' Bonsall_UI.py'

script = script + pyFile + uiFile

print script

os.system(script)

