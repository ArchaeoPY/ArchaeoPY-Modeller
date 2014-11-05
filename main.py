# -*- coding: utf-8 -*-
"""
Created on Tue Nov 04 19:20:16 2014

@author: Chrys
"""

import os

from PyQt4 import QtGui
from PyQt4 import uic

class myDialog(QtGui.QDialog):
  def __init__(self, parent=None):
    QtGui.QDialog.__init__(self, parent)
    uic.loadUi(os.path.join(os.path.dirname(os.path.abspath(__file__)),"Modeller.ui"), self)