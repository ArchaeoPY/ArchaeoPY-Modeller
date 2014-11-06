# -*- coding: utf-8 -*-
"""
Created on Wed Nov 05 10:50:37 2014

@author: FPopecarter and JCHarris
"""
#import core modules
import os
import sys
import glob
import numpy as np
import re
import atexit
import shutil

#Import GUI related modules
from PyQt4 import QtCore
from PyQt4 import QtGui
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

from matplotlib.backends.backend_qt4 import NavigationToolbar2QT as NavigationToolbar
# For creating simple dialogs
#from formlayout import fedit

# import the MainWindow widget from the converted .ui files
from GUI.MainUI import Ui_MainWindow

from Res.res2d import res2D
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
        self.doubleSpinBox_traverselength.setEnabled(True) #Length of traverse (relative units)
        self.doubleSpinBox_traverselength.setValue(10.0) #Sets the default value for traverse length to be 10 (relative units)
        self.doubleSpinBox_traverselength.setSingleStep(1.0) 
        self.doubleSpinBox_samplingint.setEnabled(True)
        self.doubleSpinBox_samplingint.setValue(0.1)
        self.doubleSpinBox_samplingint.setSingleStep(0.1)
        
        #Disables magnetometry parameters--irrelevant for res modelling
        self.doubleSpinBox_traverseint.setDisabled(True)
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
        
    def enable_3DRes(self):
        #Enable / Disable relevant survey Parameters
        self.doubleSpinBox_traverselength.setEnabled(True)
        self.doubleSpinBox_traverseint.setEnabled(True)
        self.doubleSpinBox_samplingint.setEnabled(True)
        
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
        self.doubleSpinBox_length.setEnabled(True)
        self.doubleSpinBox_width.setEnabled(True)
        self.doubleSpinBox_depthextent.setEnabled(True)
        
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
        
    def tar_data_files(self, output_name, files):
        if not os.path.isfile(output_name):
            tar = tarfile.open(output_name, "w:gz")
            for name in files:
                arcname = os.path.basename(name)
                tar.add(name,arcname=arcname)
            tar.close()  
        
    def put_file(self, file_path, cloud_path):
        k = Key(self.bucket)
        string = str(self.project_code) + '/' + cloud_path
        print string
        if self.bucket.get_key(string) == None or self.overwrite:
            k.key = string
            k.set_contents_from_filename(file_path)
            

        
    def Warning_Dialog(self, title, text):
        message = QtGui.QMessageBox.warning(self,str(title),str(text))
        
    def display_points(self, x, y):
        print 'display updating with Northings/Eastings'
#        self.Eastings = GPSMainWindow.data[:,1]
#        self.Northings = GPSMainWindow.data[:,0]
        self.mpl.canvas.ax.clear()
        self.mpl.canvas.ax.axis('equal')
        print 'canvas cleared'
        print len(x), 'points'
        self.mpl.canvas.ax.plot(x,y, 'o', ms=1, color='black')
         # reset the axes limits
        self.mpl.canvas.ax.set_xlim(xmin=np.min(x), xmax=(np.max(x)))
        self.mpl.canvas.ax.set_ylim(ymin=np.min(y), ymax=(np.max(y)))
        self.mpl.canvas.ax.grid(True)
        self.mpl.canvas.draw()
        print 'canvas drawn'
        
    def display_b_points(self):
        print 'display updating with Northings/Eastings'
#        self.Eastings = GPSMainWindow.data[:,1]
#        self.Northings = GPSMainWindow.data[:,0]
        self.mpl.canvas.ax.clear()
        self.mpl.canvas.ax.axis('equal')
        print 'canvas cleared'
        self.mpl.canvas.ax.plot(self.sens1[:,1],self.sens1[:,2], 'o', ms=1, color='red')
        self.mpl.canvas.ax.plot(self.sens2[:,1],self.sens2[:,2], 'o', ms=1, color='blue')
        self.mpl.canvas.ax.plot(self.sens3[:,1],self.sens3[:,2], 'o', ms=1, color='green')
        self.mpl.canvas.ax.plot(self.sens4[:,1],self.sens4[:,2], 'o', ms=1, color='yellow')
         # reset the axes limits
        #self.mpl.canvas.ax.set_xlim(xmin=np.min(self.sens1[:,1]), xmax=(np.max(self.sens1[:,1])))
        #self.mpl.canvas.ax.set_ylim(ymin=np.min(self.sens1[:,2]), ymax=(np.max(self.sens1[:,2])))
        self.mpl.canvas.ax.grid(True)
        self.mpl.canvas.draw()
        print 'canvas drawn'  
        
    def MagRes2D3Dtoggle(self):
        print 'Toggled'
        
        if self.radioButton_mag.isChecked():
            if self.radioButton_2d.isChecked():
                self.enable_2DMag()
            else:
                self.enable_3DMag()
        else:
            if self.radioButton_2d.isChecked():
                self.enable_2DRes()
            else:
                self.enable_3DRes()
                
        print self.radioButton_mag.isChecked(),self.radioButton_res.isChecked()
        
    def ClearPlot(self):
        self.mpl.canvas.ax.clear()
        self.mpl.canvas.draw()
        
    def CalculateFields(self):
        
        if self.radioButton_mag.isChecked():
            if self.radioButton_2d.isChecked():
                self.calculate_2DMag()
            else:
                self.calculate_3DMag()
        else:
            if self.radioButton_2d.isChecked():
                self.calculate_2DRes()
            else:
                self.calculate_3DRes()
        
    def calculate_2DRes(self):
        
        array = ['tp_long','tp_broad','wenner_long','wenner_broad','square_a','square_b','square_g','trap_l','trap_b','trap_t'][self.comboBox_array.currentIndex()]
        a = self.doubleSpinBox_a.value()
        a1 = self.doubleSpinBox_a1.value()
        a2 = self.doubleSpinBox_a2.value()
        
        stop = self.doubleSpinBox_traverselength.value()/2.0
        sample = self.doubleSpinBox_samplingint.value()
        x = np.arange(-stop,stop+sample,sample)
        
        conductivity = [1.0e+6,1.0e-6][self.comboBox_conductivity.currentIndex()]
        contrast = (conductivity - 1.0)/(1 + (2* conductivity))
        
        z = self.doubleSpinBox_depth.value()
        
        output = res2D(array, a, a1, a2, x, contrast, z)
        
        #Defines variables for saving
        self.x = x
        self.y = output
        self.header = "array, a, a1, a2, conductivity, z \n " + str(array) + ',' + str(a) + ',' + str(a1) + ',' + str(a2) + ',' + str(conductivity) + ',' + str(z) + "\n"
        
        self.plot_2d()
        
    def calculate_2DRespseudosections(self):
   
        array = ['tp_long','tp_broad','wenner_long','wenner_broad','square_a','square_b','square_g','trap_l','trap_b','trap_t'][self.comboBox_array.currentIndex()]
        a = 
        a1 = 
        a2 = 
        
        stop = self.doubleSpinBox_traverselength.value()/2.0
        sample = self.doubleSpinBox_samplingint.value()
        x = np.arange(-stop,stop+sample,sample)
        
        conductivity = [1.0e+6,1.0e-6][self.comboBox_conductivity.currentIndex()]
        contrast = (conductivity - 1.0)/(1 + (2* conductivity))
        
        z = self.doubleSpinBox_depth.value()
        
        output = 
        
        #Defines variables for saving
        self.x = x
        self.y = output
        self.header = "array, a, a1, a2, conductivity, z \n " + str(array) + ',' + str(a) + ',' + str(a1) + ',' + str(a2) + ',' + str(conductivity) + ',' + str(z) + "\n"
        
        self.plot_2d()     
        
    def save_csv(self):
        
        fname = QtGui.QFileDialog.getSaveFileName(self, 'Save File', 
                '*.csv')
        print fname, str(fname)
        output_text = np.column_stack((self.x,self.y))
        np.savetxt(str(fname),output_text,fmt ='%1.2f',delimiter=',', header = self.header)
        
    def copy_to_clipboard(self):
        pixmap = QtGui.QPixmap.grabWidget(self.mpl.canvas)
        QtGui.QApplication.clipboard().setPixmap(pixmap)
        
    def plot_2d(self):
        self.mpl.canvas.ax.plot(self.x,self.y)
        #self.mpl.canvas.ax.axis('equal')
        #self.mpl.canvas.ax.set_xlim(xmin=np.min(x), xmax=(np.max(x)))
        #self.mpl.canvas.ax.set_ylim(ymin=np.min(y), ymax=(np.max(y)))
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
        self.navi_toolbar.clear()
        
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