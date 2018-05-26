# -*- coding: utf-8 -*-

"""
Module implementing ModeSelect.
"""
import sys
import os
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QFileDialog
from PyQt5 import QtCore, QtWidgets
from Ui_ModeSelect import Ui_Dialog
from Ui_LabelMode import Ui_LabelModeWindow
from Ui_InspectionMode import Ui_InspectionModeWindow

g_width = 4896
g_height = 3034
g_top_margin = 48
g_buttom_margin = 104
g_left_margin = 48
g_right_margin = 48
g_rows = 6
g_cols = 10
g_padding = 0

g_labels = [['0_good','良品'], 
           ['1_liefeng','裂缝'],  
           ['2_quejiao', "缺角"], 
           ['3_duanshan',"断栅"], 
           ['4_xuhan',"虚焊"], 
           ['5_duanlu',"断路"], 
           ['6_hundang',"混档"], 
           ['7_heixinheiban',"黑心黑斑"], 
           ['8_tongxinyuan',"同心圆"], 
           ['9_heibian',"黑边" ], 
           ['10_heijiao', "黑角"], 
           ['11_liangban', "亮斑"], 
           ['12_huahen', "划痕"], 
           ['', '']]
           
class LabelModeWindow(QMainWindow,Ui_LabelModeWindow):
    def __init__(self):
        w = 8
        self.width = g_width/w
        self.height = g_height/w
        self.top_margin = g_top_margin/w
        self.right_margin = g_right_margin/w
        self.buttom_margin = g_buttom_margin/w
        self.left_margin = g_left_margin/w
        self.piece_size = 480/w
        
        self.rowCnt = g_rows
        self.colCnt = g_cols
        self.hMargin = 30
        self.vMargin = 60
        
        self.fileIndex = 0
        self.picDir = ''
        self.filePath = ''
        
        super(LabelModeWindow,self).__init__()
        self.setupUi(self)
        
        #禁止改变窗口大小
        self.setFixedSize(self.width+2*self.hMargin, self.height+2*self.vMargin)
        
        self.openDirBtn.clicked.connect(self.openPicDir)
        self.saveBtn.clicked.connect(self.savePieces)
        self.prePicBtn.clicked.connect(self.prePic)
        self.nextPicBtn.clicked.connect(self.nextPic)
        
    def display(self):
        self.show()
    
    def openPicDir(self):
         self.picDir = QFileDialog.getExistingDirectory(self, "Open a folder", "F:/")
         print(self.picDir)
         self.fileList = os.listdir(self.picDir)
         self.fileCnt = len(self.fileList)
         self.fileIndex = 0
         self.nextPic()
                
    def nextPic(self):
        if self.picDir == '':
            return
        self.fileIndex = self.fileIndex + 1
        if self.fileIndex == self.fileCnt:
            self.fileIndex = self.fileCnt -1
        self.loadPic()
        
    def prePic(self):
        if self.picDir == '':
            return
        self.fileIndex = self.fileIndex - 1
        if self.fileIndex == -1:
            self.fileIndex = 0
        self.loadPic()
        
    def loadPic(self): 
        self.filePath = self.picDir+'/'+self.fileList[self.fileIndex]
        filepath,shortname,extension = self.getFilePathNameExt(self.filePath)
        if not extension == ".jpg":
            return
        self.mainWidget.setStyleSheet("QTableWidget {padding:%dpx %dpx %dpx %dpx; border-image:url(%s)}"%(self.top_margin, self.right_margin, self.buttom_margin, self.left_margin, self.filePath))
        #self.tableWidget.clearAllLabels()
        self.fileLabel.setText("文件名： "+self.filePath)
        
    
    def getFilePathNameExt(self, filename):  
        (filepath,tempfilename) = os.path.split(filename);  
        (shotname,extension) = os.path.splitext(tempfilename);  
        return filepath,shotname,extension
    
    def savePieces(self):
        self.mainWidget.preparePieces(self.filePath)

class InspectionModeWindow(QMainWindow,Ui_InspectionModeWindow):
    def __init__(self):
        super(InspectionModeWindow,self).__init__()
        self.setupUi(self)
    
    def display(self):
        self.show()
        
class ModeSelect(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(ModeSelect, self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    labelModeWindow = LabelModeWindow()
    inspectionModeWindow = InspectionModeWindow()
    dlg = ModeSelect()
    dlg.pushButton.clicked.connect(inspectionModeWindow.display)
    dlg.pushButton_2.clicked.connect(labelModeWindow.display)
    dlg.show()
    sys.exit(app.exec_())
