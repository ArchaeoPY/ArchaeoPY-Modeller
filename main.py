# -*- coding: utf-8 -*-
"""
Created on Wed Nov 05 10:50:37 2014

@author: FPopecarter
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
from formlayout import fedit

# import the MainWindow widget from the converted .ui files
from GUI.MainUI import Ui_MainWindow

#Imports button related tools
#from includes.Buttons import Button_Definitions

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
        print 'cleaning up tempfile'
        print self.tempfile
        if os.path.isdir(self.tempfile):
            shutil.rmtree(self.tempfile)
    
    def enable_file_processing(self):
        self.Push_cor_GNSS.setEnabled(True)
        self.Push_display_barty_points.setEnabled(True)
        
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
        
    def internet_off(self):
        message = QtGui.QMessageBox.critical(self,
                            "Critial",
                            "Unable to connect to AWS Cloud\n\nSorry, this means processing will have to wait\n\nYour computer just isn't big enough") 
   
    def put_cloud_data(self):
       #Searches Directory for GNSS, Bart1, Bart2 files
        put_cloud_list =[('Number of Fields', 1),
               ('Overwrite Data', False)]
        fields,self.overwrite = fedit(put_cloud_list, title="Put_cloud_data",
                           comment="Select the required options then select files")
        
        for i in range(fields):
            filename = unicode(QtGui.QFileDialog.getOpenFileName(self,
                        "Select Bart1 data file","", "*Bart1.txt"))
            print filename
            if filename:
                self.projectname = os.path.dirname(filename)
                self.dirname = os.path.dirname(filename)
                self.filename = os.path.basename(filename)
                #moves to project folder
                os.chdir(self.projectname)
                print 'changed directory'
                print self.projectname
                print self.dirname
                print self.filename
                print self.projectname.split('/')
                self.projectname = self.projectname.split('/')[-1]
                print self.projectname
                #Produces list of Barty1 files inside project folder
                files = glob.glob(str(self.projectname)+'*'+'Bart1'+'*'+'.txt')
                print files
                self.progressBar.setRange(1,len(files))
                self.progressBarValue = 1
                self.progressBar.setValue(self.progressBarValue)
                for line in files:
                    traverse_no = str(line[len(self.projectname):-9])
                    b1_path,b2_path,g_path = CartEasyN_filenames(self.dirname, self.projectname, traverse_no)
                    if not b1_path:
                        continue
                    self.tempfile = tempfile.mkdtemp()
                    tar_path, cpath = cloud_path(self.tempfile, self.projectname, traverse_no)
                    self.tar_data_files(tar_path,[b1_path,b2_path,g_path]) 
                    self.put_file(tar_path,cpath)
                    self.progressBarValue += 1
                    self.progressBar.setValue(self.progressBarValue)
                    #Forces the GUI to update on progress bar value change
                    QtCore.QCoreApplication.instance().processEvents()
                
                QtGui.QMessageBox.warning(self,'Upload Complete','Sucessfully Uploaded ' + str(self.projectname))
                #Enable Load Field Button
                self.push_load_field.setEnabled(True)
                
    def load_field(self):
        ''' Copies Data from AWS S3 to Picloud
            Untars the files
        '''
        
        #Initiates Queues early
        file_list_q = cloud.queue.get(cap('file_list'+ self.UUID,39))
        untar_list_q = cloud.queue.get(cap('untar_list'+ self.UUID,39))
        self.pros_list_q = cloud.queue.get(cap('processing_list'+ str(uuid.uuid1()),39))
        
        field = self.bucket.list(prefix = self.project_code, delimiter='/')
        field_list = [0]
        for a in field:
            temp = a.name
            temp2 = temp.split('/')
            if len(temp2) > 3:
                field_list.append(temp)
            
        print field_list
        get_field_list =[('Choose Field', field_list)]
        field = fedit(get_field_list, title="Choose a field",
                           comment="Choose the Field you want to Process")
        
        self.progressBar.setRange(1,1000)
        self.progressBarValue = 10
        self.progressBar.setValue(self.progressBarValue)
        
        field = [field[0]]
        try:
            field = int(field[0])
            
        except:
            field = str(field[0])
            
        if type(field) == str:
            field = field
        else:
            field = field_list[int(field)+1]
        print field
        
        #Updates Progress Bar
        self.progressBarValue += 10
        self.progressBar.setValue(self.progressBarValue)
        QtCore.QCoreApplication.instance().processEvents()
                
        self.field = str(field)
        self.field = self.field.strip()
        self.field = self.field.split('/')
        self.field = self.field[-2]
        
        if self.field[-1] != '/':
            print self.field
            self.field = self.field + '/'
            print self.field
        
        print self.field
        #Inititates Class
        bucketfroms3_q = Bucket_from_S3_Q() 
        
                #Updates Progress Bar
        self.progressBarValue += 10
        self.progressBar.setValue(self.progressBarValue)
        QtCore.QCoreApplication.instance().processEvents()
        
        #Sets field to be environment variable
        os.environ["CARTEASYN_F"] = str(self.field)
        
        #This a much more sensible way of getting information to Queue classes...
        #except it doesn't work
        bucketfroms3_q.field=str(self.field)
        
                #Updates Progress Bar
        self.progressBarValue += 10
        self.progressBar.setValue(self.progressBarValue)
        QtCore.QCoreApplication.instance().processEvents()
        
        file_list_t = bucket.list(prefix = str(field), delimiter=str('_.tar.gz'))
        
                #Updates Progress Bar
        self.progressBarValue += 10
        self.progressBar.setValue(self.progressBarValue)
        QtCore.QCoreApplication.instance().processEvents()
        
         #Attatches Queue to transfer data from AWS to picloud Bucket
        file_list_q.attach(bucketfroms3_q, output_queues=[untar_list_q], readers_per_job=4, _env='CartEasyN', _os_env_vars=os.environ.keys())        

        #Updates Progress Bar
        self.progressBarValue += 10
        self.progressBar.setValue(self.progressBarValue)
        QtCore.QCoreApplication.instance().processEvents()
        
        #Starts Untaring Queue
        untar_list_q.attach(Bucket_Untar, output_queues=[self.pros_list_q], readers_per_job=4, _env='CartEasyN', _os_env_vars=os.environ.keys())        
        
                #Updates Progress Bar
        self.progressBarValue += 10
        self.progressBar.setValue(self.progressBarValue)
        QtCore.QCoreApplication.instance().processEvents()
        
        #Starts filling Queue after attatching
        for a in file_list_t:
            #Updates Progress Bar
            self.progressBarValue += 1
            self.progressBar.setValue(self.progressBarValue)
            QtCore.QCoreApplication.instance().processEvents()
            
            temp = str(a.name)
            print temp
            if str('_.tar.gz') in temp:
                #temp = [str(self.UUID) +',' + str(temp)]
                file_list_q.push([temp])
                
        
        #Fills rest of Progress Bar
        #Keeps people happy
        for i in xrange(self.progressBarValue,1000):
            self.progressBarValue += 1
            self.progressBar.setValue(self.progressBarValue)
            QtCore.QCoreApplication.instance().processEvents()
            
        QtGui.QMessageBox.warning(self,'Field Loaded','Loaded Field ' + str(field))
        self.enable_file_processing()
        
    def data_SourceFile(self):
        #Used to Load data from Directory
        self.B1_ars=[]
        self.B2_ars=[]
        self.G_ars=[]
        self.GNSS_xy=[]
        g_x = np.empty(0)
        g_y = np.empty(0)
        
        filename = unicode(QtGui.QFileDialog.getOpenFileName(self,
           "Select Bart1 data file","", "*Bart1.txt"))
        if filename:
            print filename
            self.projectname = os.path.dirname(filename)
            self.dirname = os.path.dirname(filename)
            self.filename = os.path.basename(filename)
            #moves to project folder
            os.chdir(self.projectname)
            #determines project title from filename
            ####****Might need to change this****#######
            print self.projectname
            print os.sep
            self.projectname = self.projectname.split(os.sep)[-1]
            print self.projectname
            #Produces list of Barty1 files inside project folder
            files = glob.glob(str(self.projectname)+'*'+'Bart1'+'*'+'.txt')
            print files
            #Initialises ProgressBar to range
            self.progressBar.setRange(1,len(files))
            self.progressBarValue = 1
            self.progressBar.setValue(self.progressBarValue)
            for line in files:
                traverse_no = str(line[len(self.projectname):-9])
                b1_path,b2_path,g_path = CartEasyN_filenames(self.dirname, self.projectname, traverse_no)
                b1, b2, g = load_barty(b1_path), load_barty(b2_path), load_GNSS(g_path)
                if type(b2) != bool and type(g) != bool:
                    self.B1_ars.append(b1)
                    self.B2_ars.append(b2)
                    self.G_ars.append(g)
                    if len(g) > 2:
                        GNSS_xy = GNSS_xy_calc(g)
                        g_x = np.concatenate((g_x, GNSS_xy[:,1]))
                        g_y = np.concatenate((g_y, GNSS_xy[:,2]))
                self.progressBarValue += 1
                self.progressBar.setValue(self.progressBarValue)
                #Forces the GUI to update on progress bar value change
                QtCore.QCoreApplication.instance().processEvents()
                
            print np.shape(g_x), np.shape(g_y)
            g_x, g_y = np.array(g_x, dtype=float), np.array(g_y, dtype=float)
            self.display_points(g_x,g_y)
            self.Enable_buttons()
        
    
    def load_cloud_points(self):
        
        ''' Processes GNSS Points on Picloud
            Saves as Numpy Array
            Amalgamates GNSS XY Arrays
            Downloads from Picloud
            Displays Points
        '''
        
        self.progressBar.setRange(1,100)
        self.progressBarValue = 1       
        
        print 'loading cloud points'
        cloudgnss_xy = Cloud_GNSS_XY()
        
        cloudgnss_xy.field = self.field
        cloudgnss_xy.project = self.project_code
        cloudgnss_xy.UUID = self.UUID
        
        cloud_gnss_amalg = Cloud_GNSS_amalg()
        #Currently assumes Previous Job (load field) has run
        #self.pros_list_q = cloud.queue.get(cap('processing_list'+ self.UUID,39))
        self.g_amalg_q = cloud.queue.get(cap('G_amalg'+ str(uuid.uuid1()),39))
        self.bart_pros_list_q = cloud.queue.get(cap('bart_pros_list'+ str(uuid.uuid1()),39))
        
        self.pros_list_q.attach(cloudgnss_xy, output_queues=[self.g_amalg_q,self.bart_pros_list_q], max_parallel_jobs=4, readers_per_job=2, _env='CartEasyN', os_env_vars=os.environ.keys())
        self.g_amalg_q.attach(cloud_gnss_amalg, max_parallel_jobs=1, readers_per_job=1, _type='f2', _env='CartEasyN', _os_env_vars=os.environ.keys())        

        queue = cloud.queue.get(cap('GNSS_amalg_done'+ self.UUID,39))
        
        while True:
            gnns_xy_path = queue.pop(max_count =1, timeout=1)
            print gnns_xy_path
            try:
                gnns_xy_path = str(gnns_xy_path[0])
                print gnns_xy_path
                break
            except:
                print 'going round the loop'
                
            self.progressBarValue += 1
            self.progressBar.setValue(self.progressBarValue)
            #Forces the GUI to update on progress bar value change
            QtCore.QCoreApplication.instance().processEvents()
        #Remove Uneccessary Queues
        self.pros_list_q.delete()
        self.g_amalg_q.delete()
        temp_file = tempfile.mkstemp()[1]
        
        cloud.bucket.get(gnns_xy_path,file_path = temp_file)
        
        GNSS_xy = np.load(temp_file)
        
        self.display_points(GNSS_xy[:,0],GNSS_xy[:,1])
        
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
        
    
    def calculate_barty_locs(self):
        print 'defining'
        #Converts GNSS location & time to Barty Location
#        self.B1_ars = np.array(self.B1_ars, dtype=str)
#        self.B2_ars = np.array(self.B2_ars, dtype=str)
#        self.G_ars = np.array(self.G_ars, dtype=str)
        print 'converted'
        self.progressBar.setRange(0,len(self.B1_ars))
        self.progressBarValue = 0
        self.progressBar.setValue(self.progressBarValue)
        self.sens1 = np.empty([0,4])
        self.sens2 = np.empty([0,4])
        self.sens3 = np.empty([0,4])
        self.sens4 = np.empty([0,4])
        print 'starting'
        #Process Barty1 and Barty2 concurrently if present
        line_count = 0
        print len(self.B1_ars), len(self.B2_ars), len(self.G_ars), len(self.GNSS_xy)
        for lineB1 in self.B1_ars:
            print line_count
            lineB2 = self.B2_ars[line_count]
            lineG = self.GNSS_xy[line_count]
            try:
                sens1, sens2 = barty_gps_xy(lineG, lineB1, Logger=1)
                sens3, sens4 = barty_gps_xy(lineG, lineB2, Logger=2)
                print np.shape(sens1)
                self.sens1=np.vstack((self.sens1,sens1))
                self.sens2=np.vstack((self.sens2,sens2))
                self.sens3=np.vstack((self.sens3,sens3))
                self.sens4=np.vstack((self.sens4,sens4))
            except:
                print 'somethngs looking a bit weird'
                
            print np.shape(self.sens1)
            line_count += 1
            
            self.progressBarValue += 1
            self.progressBar.setValue(self.progressBarValue)
            #Forces the GUI to update on progress bar value change
            QtCore.QCoreApplication.instance().processEvents()
        self.display_b_points()
    
        
    def Button_Definitions(self):
        self.firstrun=True        
        
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
        a.setToolTip('returns axes to original position')
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
        #self.Button_layout.addWidget(self.navi_toolbar)
        self.Button_Definitions()


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