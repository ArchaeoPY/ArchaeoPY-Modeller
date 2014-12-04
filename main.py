# -*- coding: utf-8 -*-
"""
Created on Wed Nov 05 10:50:37 2014

@author: FPopecarter and JCHarris
"""
#import core modules
import os
import sys
#import glob
import numpy as np
#import re
import atexit
#import shutil

#Import GUI related modules
from PyQt4 import QtCore
from PyQt4 import QtGui
import matplotlib.pyplot as plt
#import matplotlib.mlab as mlab

from matplotlib.backends.backend_qt4 import NavigationToolbar2QT as NavigationToolbar
# For creating simple dialogs
#from formlayout import fedit

# import the MainWindow widget from the converted .ui files
from GUI.MainUI import Ui_MainWindow

from Res.res2d import res2D
from Res.res2dpseudo import res2Dpseudo
#Imports button related tools
#from includes.Buttons import Button_Definitions

#Creates Main UI window
class ModellerMainWindow(QtGui.QMainWindow, Ui_MainWindow):
    """Customization for Qt Designer created window"""
    
    def definitions(self):
        self.s3 = ""
        self.bucket = ""
        self.project_code = ""
        self.overwrite = False
        self.file_list = ""
        self.tempfile = ""
    
    def cleanup(self):
        print 'closing'

    #Defines 2D Res modelling component of UI window: what parameters the user can select.
    def enable_2DRes(self):
        #Enable / Disable relevant survey Parameters
        self.doubleSpinBox_xlength.setEnabled(True) #Length of traverse (relative units)
        self.doubleSpinBox_xlength.setValue(10.0) #Sets the default value for traverse length to be 10 (relative units)
        self.doubleSpinBox_xlength.setSingleStep(1.0) 
        self.doubleSpinBox_xsample.setEnabled(True)
        self.doubleSpinBox_xsample.setValue(0.1)
        self.doubleSpinBox_xsample.setSingleStep(0.05)
        
        #Disables magnetometry parameters--irrelevant for res modelling
        self.doubleSpinBox_ylength.setDisabled(True)
        self.doubleSpinBox_ysample.setDisabled(True)
        self.doubleSpinBox_fieldinclination.setDisabled(True)
        
        #Enable / Disable instrument parameters
        self.comboBox_array.setEnabled(True)        
        self.doubleSpinBox_a.setEnabled(True)
        self.doubleSpinBox_a.setValue(1.0)
        self.doubleSpinBox_a.setSingleStep(0.1)
        self.doubleSpinBox_a1.setEnabled(True)
        self.doubleSpinBox_a1.setValue(1.0)
        self.doubleSpinBox_a1.setSingleStep(0.1)
        self.doubleSpinBox_a2.setEnabled(True)
        self.doubleSpinBox_a2.setValue(1.0)
        self.doubleSpinBox_a2.setSingleStep(0.1)
        
        self.doubleSpinBox_lowersensor.setDisabled(True)
        self.doubleSpinBox_uppersensor.setDisabled(True)
        self.doubleSpinBox_ylength.setDisabled(True)
        self.doubleSpinBox_ysample.setDisabled(True)
        
        #Enable / Disable Feature Parameters
        self.comboBox_conductivity.setEnabled(True)
        self.doubleSpinBox_depth.setEnabled(True)
        self.doubleSpinBox_depth.setValue(1.0)
        self.doubleSpinBox_depth.setSingleStep(0.1)
        
        self.doubleSpinBox_magsus.setDisabled(True)
        self.doubleSpinBox_length.setDisabled(True)
        self.doubleSpinBox_width.setDisabled(True)
        self.doubleSpinBox_strike.setDisabled(True)
        self.doubleSpinBox_depthextent.setDisabled(True)
        
        #Modifys ComboBox
        self.comboBox_array.clear()
        self.comboBox_array.addItems(('TP Long','TP Broad','W Long','W Broad','SQ Alpha','SQ Beta', 'SQ Gamma', 'TZ Long', 'TZ Broad', 'TZ Theta'))

    def enable_2DRespseudo(self):
        #Enable / Disable relevant survey Parameters
        self.doubleSpinBox_xlength.setEnabled(True) #Length of traverse (relative units)
        self.doubleSpinBox_xlength.setValue(10.0) #Sets the default value for traverse length to be 10 (relative units)
        self.doubleSpinBox_xlength.setSingleStep(1.0) 
        self.doubleSpinBox_xsample.setEnabled(True)
        self.doubleSpinBox_xsample.setValue(0.1)
        self.doubleSpinBox_xsample.setSingleStep(0.05)
        
        #Disables magnetometry parameters--irrelevant for res modelling
        self.doubleSpinBox_traverseint.setDisabled(True)
        self.doubleSpinBox_fieldinclination.setDisabled(True)
        
        #Enable / Disable instrument parameters
        self.comboBox_array.setEnabled(True)        
        self.doubleSpinBox_a.setEnabled(True)
        self.doubleSpinBox_a.setValue(0.5)
        self.doubleSpinBox_a.setSingleStep(0.5)
        self.doubleSpinBox_a1.setEnabled(True)
        self.doubleSpinBox_a1.setValue(10.0)
        self.doubleSpinBox_a1.setSingleStep(0.5)
        self.doubleSpinBox_a2.setEnabled(True)
        self.doubleSpinBox_a2.setValue(0.5)
        self.doubleSpinBox_a2.setSingleStep(0.1)
        
        self.doubleSpinBox_lowersensor.setDisabled(True)
        self.doubleSpinBox_uppersensor.setDisabled(True)
        self.doubleSpinBox_ylength.setDisabled(True)
        self.doubleSpinBox_ysample.setDisabled(True)
        
        #Enable / Disable Feature Parameters
        self.comboBox_conductivity.setEnabled(True)
        self.doubleSpinBox_depth.setEnabled(True)
        self.doubleSpinBox_depth.setValue(1.0)
        self.doubleSpinBox_depth.setSingleStep(0.1)
        
        self.doubleSpinBox_magsus.setDisabled(True)
        self.doubleSpinBox_length.setDisabled(True)
        self.doubleSpinBox_width.setDisabled(True)
        self.doubleSpinBox_strike.setDisabled(True)
        self.doubleSpinBox_depthextent.setDisabled(True)
        
        #Modifys ComboBox
        self.comboBox_array.clear()
        self.comboBox_array.addItems(('TP Long','TP Broad','W Long','W Broad','SQ Alpha','SQ Beta', 'SQ Gamma'))
        
    def enable_3DRes(self):
        #Enable / Disable relevant survey Parameters
        self.doubleSpinBox_xlength.setEnabled(True) #Length of traverse (relative units)
        self.doubleSpinBox_xlength.setValue(10.0) #Sets the default value for traverse length to be 10 (relative units)
        self.doubleSpinBox_xlength.setSingleStep(1.0) 
        self.doubleSpinBox_xsample.setEnabled(True)
        self.doubleSpinBox_xsample.setValue(0.1)
        self.doubleSpinBox_xsample.setSingleStep(0.05)

        self.doubleSpinBox_ylength.setEnabled(True) #Length of traverse (relative units)
        self.doubleSpinBox_ylength.setValue(10.0) #Sets the default value for traverse length to be 10 (relative units)
        self.doubleSpinBox_ylength.setSingleStep(1.0) 
        self.doubleSpinBox_ysample.setEnabled(True)
        self.doubleSpinBox_ysample.setValue(0.1)
        self.doubleSpinBox_ysample.setSingleStep(0.05)
        
        self.doubleSpinBox_fieldinclination.setDisabled(True)
        
        #Enable / Disable instrument parameters
        self.comboBox_array.setEnabled(True)
        self.doubleSpinBox_a.setEnabled(True)
        self.doubleSpinBox_a1.setEnabled(True)
        self.doubleSpinBox_a2.setEnabled(True)
        
        self.doubleSpinBox_lowersensor.setDisabled(True)
        self.doubleSpinBox_uppersensor.setDisabled(True)
        
        #Enable / Disable Feature Parameters
        self.comboBox_conductivity.setEnabled(True)
        self.doubleSpinBox_depth.setEnabled(True)
        self.doubleSpinBox_depth.setSingleStep(0.5)
        self.doubleSpinBox_length.setEnabled(True)
        self.doubleSpinBox_length.setValue(1.0)
        self.doubleSpinBow_length.setSingleStep(0.5)
        self.doubleSpinBox_width.setEnabled(True)
        self.doubleSpinBox_width.setValue(1.0)
        self.doubleSpinBox_width.setValue(0.5)
        self.doubleSpinBox_depthextent.setEnabled(True)
        self.doubleSpinBox_depthextent.setValue(1.0)
        self.doubleSpinBox_SingleStep(0.5)
        
        self.doubleSpinBox_magsus.setDisabled(True)
        self.doubleSpinBox_strike.setDisabled(True)
        
        #Modifys ComboBox
        self.comboBox_array.clear()
        self.comboBox_array.addItems(('TP Long','TP Broad','W Long','W Broad','SQ Alpha','SQ Beta', 'SQ Gamma', 'TZ Long', 'TZ Broad', 'TZ Theta'))
        
    
    def enable_3DMag(self):
        #Enable / Disable relevant survey Parameters
        self.doubleSpinBox_traverselength.setEnabled(True)
        self.doubleSpinBox_traverseint.setEnabled(True)
        self.doubleSpinBox_samplingint.setEnabled(True)
        self.doubleSpinBox_fieldinclination.setEnabled(True)
        
        #Enable / Disable instrument parameters
        self.comboBox_array.setEnabled(True)
        self.doubleSpinBox_lowersensor.setEnabled(True)
        self.doubleSpinBox_uppersensor.setEnabled(True)
        
        self.doubleSpinBox_a.setDisabled(True)
        self.doubleSpinBox_a1.setDisabled(True)
        self.doubleSpinBox_a2.setDisabled(True)
        
        #Enable / Disable Feature Parameters
        self.doubleSpinBox_depth.setEnabled(True)
        self.doubleSpinBox_length.setEnabled(True)
        self.doubleSpinBox_width.setEnabled(True)
        self.doubleSpinBox_depthextent.setEnabled(True)
        self.doubleSpinBox_magsus.setEnabled(True)
        self.doubleSpinBox_strike.setEnabled(True)
        
        self.comboBox_conductivity.setDisabled(True)
        
        #Modifys ComboBox
        self.comboBox_array.clear()
        self.comboBox_array.addItems(('Vertical', 'Total', 'Horizontal X', 'Horizontal Y'))
        
    def enable_2DMag(self):
        #Enable / Disable relevant survey Parameters
        self.doubleSpinBox_traverselength.setEnabled(True)
        self.doubleSpinBox_traverseint.setEnabled(True)
        self.doubleSpinBox_samplingint.setEnabled(True)
        self.doubleSpinBox_fieldinclination.setEnabled(True)
        
        #Enable / Disable instrument parameters
        self.comboBox_array.setEnabled(True)
        self.doubleSpinBox_lowersensor.setEnabled(True)
        self.doubleSpinBox_uppersensor.setEnabled(True)
        
        self.doubleSpinBox_a.setDisabled(True)
        self.doubleSpinBox_a1.setDisabled(True)
        self.doubleSpinBox_a2.setDisabled(True)
        
        #Enable / Disable Feature Parameters
        self.doubleSpinBox_depth.setEnabled(True)
        self.doubleSpinBox_length.setEnabled(True)
        self.doubleSpinBox_width.setEnabled(True)
        self.doubleSpinBox_depthextent.setEnabled(True)
        self.doubleSpinBox_magsus.setEnabled(True)
        self.doubleSpinBox_strike.setEnabled(True)
        
        self.comboBox_conductivity.setDisabled(True)
        
        #Modifys ComboBox
        self.comboBox_array.clear()
        self.comboBox_array.addItems(('Vertical', 'Total', 'Horizontal X', 'Horizontal Y'))
        
    def Warning_Dialog(self, title, text):
        message = QtGui.QMessageBox.warning(self,str(title),str(text))
        
    def MagRes2D3Dtoggle(self):
        print 'Toggled'
        
        if self.radioButton_mag.isChecked():
            if self.radioButton_2d.isChecked():
                self.ClearPlot()                
                self.enable_2DMag()
            else:
                self.ClearPlot()                 
                self.enable_3DMag()
        else:
            if self.radioButton_2d.isChecked():
                self.ClearPlot() 
                self.enable_2DRes()
            elif self.radioButton_3d.isChecked():
                self.ClearPlot() 
                self.enable_3DRes()
            else:
                self.ClearPlot() 
                self.enable_2DRespseudo()
        
                
        print self.radioButton_mag.isChecked(),self.radioButton_res.isChecked()

    def CalculateFields(self):
        
        if self.radioButton_mag.isChecked():
            if self.radioButton_2d.isChecked():
                self.calculate_2DMag()
            else:
                self.calculate_3DMag()
        else:
            if self.radioButton_2d.isChecked():
                self.calculate_2DRes()
            elif self.radioButton_3d.isChecked():
                self.calculate_3DRes()
            else:
                self.calculate_2DRespseudo()
        
    def calculate_2DRes(self):
        #Assign user input to be run through 2DRes Algorithms
        array = ['tp_long','tp_broad','wenner_long','wenner_broad','square_a','square_b','square_g','trap_l','trap_b','trap_t'][self.comboBox_array.currentIndex()]
        a = self.doubleSpinBox_a.value()
        a1 = self.doubleSpinBox_a1.value()
        a2 = self.doubleSpinBox_a2.value()
        
        #Create an array of x positions
        stop = self.doubleSpinBox_traverselength.value()/2.0
        sample = self.doubleSpinBox_samplingint.value()
        x = np.arange(-stop,stop+sample,sample)
        
        conductivity = [1.0e+6,1.0e-6][self.comboBox_conductivity.currentIndex()] #Sphere Conductivity
        contrast = (conductivity - 1.0)/(1 + (2* conductivity)) #Contrast Factor
        
        z = self.doubleSpinBox_depth.value() #Sphere Depth
        
        output = res2D(array, a, a1, a2, x, contrast, z) #Send to res2D
        
        #Defines variables for saving
        self.x = x
        self.y = output
        self.header = "array, a, a1, a2, conductivity, z \n " + str(array) + ',' + str(a) + ',' + str(a1) + ',' + str(a2) + ',' + str(conductivity) + ',' + str(z) + "\n"
        
        self.xtitle = 'Relative Position (x)'
        self.ytitle = 'Relative Response'
        self.title = 'Resistivity Profile with ' + str(array) + ' over ' + str(conductivity) + ' ohm/m sphere.'
        self.plot_2d()
        
    def calculate_2DRespseudo(self):
        #Assign user input to be run through 2DRes Algorithms   
        array = ['tp_long','tp_broad','wenner_long','wenner_broad','square_a','square_b','square_g'][self.comboBox_array.currentIndex()]
        a = self.doubleSpinBox_a.value()
        a1 = self.doubleSpinBox_a1.value()
        a2 = self.doubleSpinBox_a2.value()
        array_range = np.arange(a, a1 + a2, a2) 

        #Create an array of x positions        
        stop = self.doubleSpinBox_traverselength.value()/2.0
        sample = self.doubleSpinBox_samplingint.value()
        x = np.arange(-stop,stop+sample,sample)
        
        conductivity = [1.0e+6,1.0e-6][self.comboBox_conductivity.currentIndex()] #Sphere Conductivity
        contrast = (conductivity - 1.0)/(1 + (2* conductivity)) #Contrast Factor
        
        z = self.doubleSpinBox_depth.value() #Sphere Depth
        
        self.output = res2Dpseudo(array, array_range, x, contrast, z)
        self.xtitle = 'Relative Position (x)'
        self.ytitle = 'Relative Depth'
        self.title = 'Resistivity Pseudosection With ' + str(array) + ' Over ' + str(conductivity) + ' Ohm/m Sphere.'
        self.arrayrange = array_range        
        
        #Defines variables for saving
        #self.x = x
        #self.y = output
        #self.header = "array, a, a1, a2, conductivity, z \n " + str(array) + ',' + str(a) + ',' + str(a1) + ',' + str(a2) + ',' + str(conductivity) + ',' + str(z) + "\n"
        
        self.plot_2dpseudo()    
 
    def calculate_3DRes(self): #NOT YET IMPLEMENTED!!!!
        #Assign user input to be run through 3DRes Algorithms        
        array = ['tp_long','tp_broad','wenner_long','wenner_broad','square_a','square_b','square_g','trap_l','trap_b','trap_t'][self.comboBox_array.currentIndex()]
        a = self.doubleSpinBox_a.value()
        a1 = self.doubleSpinBox_a1.value()
        a2 = self.doubleSpinBox_a2.value()
        
        #Greate grid of x and y positions
        x_length = self.doubleSpinBox_xlength.value()
        x_step = self.doubleSpinBox_xsample.value()
        x_grid_pos = np.arange(np.divide(x_step,2.0), x_length, x_step)
        y_length = self.doubleSpinBox_ylength.value()
        y_step = self.doubleSpinBox_ysample.value()
        y_grid_pos = np.arange(np.divide(y_step,2.0), y_length, y_step)
        xgrid, ygrid = np.meshgrid(x_grid_pos, y_grid_pos)   
        
        #Fill Bounding Box with Spheres
                
        
        conductivity = [1.0e+6,1.0e-6][self.comboBox_conductivity.currentIndex()]
        contrast = (conductivity - 1.0)/(1 + (2* conductivity))
        
        z = self.doubleSpinBox_depth.value() #Depth to top of bounding box
        z1 = self.doubleSpinBox_depthextent.value() #Depth to bottom of bounding box
        
        #output = res2D(array, a, a1, a2, x, contrast, z)
        
        #Defines variables for saving
        #self.x = x
        #self.y = output
        #self.header = "array, a, a1, a2, conductivity, z \n " + str(array) + ',' + str(a) + ',' + str(a1) + ',' + str(a2) + ',' + str(conductivity) + ',' + str(z) + "\n"
        
        #self.xtitle = 'Relative Position (x)'
        #self.ytitle = 'Relative Response'
        #self.title = 'Resistivity Pseudosection with ' + str(array) + ' over ' + str(conductivity) + ' ohm/m sphere.'
        #self.plot_2d()
       
    def save_csv(self):
        
        fname = QtGui.QFileDialog.getSaveFileName(self, 'Save File', 
                '*.csv')
        print fname, str(fname)
        output_text = np.column_stack((self.x,self.y))
        np.savetxt(str(fname),output_text,fmt ='%1.2f',delimiter=',', header = self.header)
        
    def copy_to_clipboard(self):
        pixmap = QtGui.QPixmap.grabWidget(self.mpl.canvas)
        QtGui.QApplication.clipboard().setPixmap(pixmap)
        
    def ClearPlot(self):
        self.mpl.canvas.ax.clear()
        self.mpl.canvas.draw()
        
    def plot_2d(self):        
        self.mpl.canvas.ax.plot(self.x,self.y)
        self.mpl.canvas.ax.axis('auto')
        #self.mpl.canvas.ax.set_xlim(xmin=np.min(self.x), xmax=(np.max(self.x)))
        self.mpl.canvas.ax.set_ylim(ymin=np.min(self.y), ymax=(np.max(self.y)))
        self.mpl.canvas.ax.set_autoscale_on(True)
        self.mpl.canvas.ax.autoscale_view(True,True,True)
        self.mpl.canvas.ax.set_xlabel(self.xtitle, size = 15)
        self.mpl.canvas.ax.set_ylabel(self.ytitle, size = 15)
        self.mpl.canvas.ax.set_title(self.title, size = 15)
        self.mpl.canvas.draw()
    
    def plot_2dpseudo(self):
        self.ClearPlot()
        temp = np.flipud(self.output)
        self.mpl.canvas.ax.imshow(temp, interpolation='none', cmap=plt.cm.Greys,aspect='auto',origin='upper')
        self.mpl.canvas.ax.set_xlabel(self.xtitle, size = 15)
        self.mpl.canvas.ax.set_ylabel(self.ytitle, size = 15)
        self.mpl.canvas.ax.set_title(self.title, size = 15)
        
        self.cb = plt.colorbar(self.mpl.canvas.ax.imshow(self.output,cmap=plt.cm.Greys), ticks=self.arrayrange)
        
        #self.mpl.canvas.colorbar(self.mpl.canvas.ax.imshow(self.output,cmap=plt.cm.Greys), ticks=self.arrayrange)
        self.mpl.canvas.draw()
        
    def Button_Definitions(self):
        self.firstrun=True        
        QtCore.QObject.connect(self.radioButton_mag, QtCore.SIGNAL("toggled(bool)"), self.MagRes2D3Dtoggle)
        QtCore.QObject.connect(self.radioButton_2d, QtCore.SIGNAL("toggled(bool)"), self.MagRes2D3Dtoggle)
        
        self.pushButton_plot.clicked.connect(self.CalculateFields)
        self.pushButton_clear.clicked.connect(self.ClearPlot)
        QtGui.QShortcut(QtGui.QKeySequence("Ctrl+P"),self, self.CalculateFields)
        
        self.action_Save_Data.triggered.connect(self.save_csv)
        QtGui.QShortcut(QtGui.QKeySequence("Ctrl+S"),self, self.save_csv)
        
        QtGui.QShortcut(QtGui.QKeySequence("Ctrl+C"),self, self.copy_to_clipboard)
        # Buttons in Toolbar
        #self.push_put_data.clicked.connect(self.put_cloud_data)
        #self.push_load_field.clicked.connect(self.load_field)
        #self.Push_cor_GNSS.clicked.connect(self.load_cloud_points)
        #self.Push_cor_GNSS.clicked.connect(self.Process_GNSS)
        #self.Push_display_barty_points.clicked.connect(self.calculate_barty_locs)
#        self.Push_Desample.clicked.connect(self.remove_collinears)
#        self.Push_Greyscale.clicked.connect(self.Grid_Data)
#        self.Push_ZMT.clicked.connect(self.ZMT)
#        self.Push_Calibrate.clicked.connect(self.calibrate)      
#        self.Push_Despike.clicked.connect(self.Despike)
        
#        self.Push_Export.clicked.connect(self.import_NMEA)
        
        # Buttons in Menu
#        self.actionOpen_File.triggered.connect(self.data_SourceFile)
#        self.actionDisplay_GreyScale.triggered.connect(self.Grid_Data)
        #QtCore.QObject.connect(self.mplactionQuit, QtCore.SIGNAL('triggered()'), QtGui.qApp, QtCore.SLOT("quit()"))
    
    
    def __init__(self, parent = None):
        # initialization of the superclass
        super(ModellerMainWindow, self).__init__(parent)
        # setup the GUI --> function generated by pyuic4
        self.setupUi(self)
        #Adds a Matplotlib Toolbar to the display, clears the display and adds only the required buttons
        self.navi_toolbar = NavigationToolbar(self.mpl.canvas, self)
        #self.navi_toolbar.clear()
        
 # Add the x,y location widget at the right side of the toolbar
 # The stretch factor is 1 which means any resizing of the toolbar
 # will resize this label instead of the buttons.
#        self.navi_toolbar.locLabel = QtGui.QLabel( "", self )
#        self.navi_toolbar.locLabel.setAlignment(QtCore.Qt.AlignLeft)
#        self.navi_toolbar.locLabel.setSizePolicy(
#        QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,
#                           QtGui.QSizePolicy.Expanding))
#        labelAction = self.navi_toolbar.addWidget(self.navi_toolbar.locLabel)
#        labelAction.setVisible(True)
#Adds Buttons
        a = self.navi_toolbar.addAction(self.navi_toolbar._icon('home.png'), 'Home',
                                        self.navi_toolbar.home)
        #a.setToolTip('returns axes to original position')
        a = self.navi_toolbar.addAction(self.navi_toolbar._icon('move.png'), 'Pan',
                                        self.navi_toolbar.pan)
        a.setToolTip('Pan axes with left mouse, zoom with right')
        a = self.navi_toolbar.addAction(self.navi_toolbar._icon('zoom_to_rect.png'), 'Zoom',
                                        self.navi_toolbar.zoom)
        a.setToolTip('Zoom to Rectangle')
        a = self.navi_toolbar.addAction(self.navi_toolbar._icon('filesave.png'), 'Save',
                           self.navi_toolbar.save_figure)
        a.setToolTip('Save the figure')

        #Button_layout is a QT desginer Grid Layout.
        self.toolbar_grid.addWidget(self.navi_toolbar)
        self.Button_Definitions()
        
        #Run Radio Toggle Code to grey / allow relevant options
        self.radioButton_2d.click()
        self.radioButton_res.click()
        self.MagRes2D3Dtoggle()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    
    app.processEvents()
    
    #Creates Window Form     
    form = ModellerMainWindow()
    
    #display form and focus
    form.show()
    #if sys.platform == "darwin":
    form.raise_()
    
    #Something to do with the App & Cleanup?
    app.exec_()
    atexit.register(form.cleanup)