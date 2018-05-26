# -*- coding: utf-8 -*-

"""
Module implementing ModeSelect.
"""
import sys
import os
import numpy as np
import cv2
from functools import partial

from PyQt5.QtCore import  Qt
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QFileDialog, QTableWidget
from PyQt5 import QtCore, QtWidgets
from Ui_ModeSelect import Ui_Dialog
from Ui_LabelMode import Ui_LabelModeWindow
from Ui_InspectionMode import Ui_InspectionModeWindow
from Ui_LabelType import Ui_LabelTypeDialog


g_width = 4896
g_height = 3034
g_top_margin = 48
g_buttom_margin = 104
g_left_margin = 48
g_right_margin = 48
g_piece_size = 480
g_rows = 6
g_cols = 10
g_padding = 0

g_w = 8
g_v_width = int(g_width/g_w)
g_v_height = int(g_height/g_w)
g_v_top_margin = int(g_top_margin/g_w)
g_v_right_margin = int(g_right_margin/g_w)
g_v_buttom_margin = int(g_buttom_margin/g_w)
g_v_left_margin = int(g_left_margin/g_w)
g_v_piece_size = int(480/g_w)

g_record = np.zeros((6,10))
g_el_dir = 'E:/el/'
g_label_dir = g_el_dir+'labels/'

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

class MainAreaSize():
    def __init__(self):
        self.pic_width = g_width
        self.pic_height = g_height
        self.pic_top_margin = g_top_margin
        self.pic_right_margin = g_right_margin
        self.pic_buttom_margin = g_buttom_margin
        self.pic_left_margin = g_left_margin
        self.pic_piece_size = g_piece_size
        self.w = 8
        self.rows = 6
        self.cols = 10
        self.hMargin = 30
        self.vMargin = 60
        self.recalcSize()
    
    def recalcSize(self):
        self.width = int(self.pic_width/self.w)
        self.height = int(self.pic_height/self.w)
        self.top_margin = int(self.pic_top_margin/self.w)
        self.right_margin = int(self.pic_right_margin/self.w)
        self.buttom_margin = int(self.pic_buttom_margin/self.w)
        self.left_margin = int(self.pic_left_margin/self.w)
        self.piece_size = int(self.pic_piece_size/self.w)
    
    def updateW(self, w):
        self.w = w
        self.recalcSize()

#####################################
#   图片操作区域
#####################################
class Ui_MainWidget(QTableWidget):
    def __init__(self, area, parent=None):
        super(Ui_MainWidget,self).__init__(parent)
        #self.setObjectName("myQWidget")
        
        self.area = area
        
        self.setGeometry(QtCore.QRect(0, 0, area.width, area.height))
        self.setColumnCount(area.cols)
        self.setRowCount(area.rows)
        
        self.setVerticalHeaderLabels(['A','B','C', 'D', 'E', 'F'])
        self.horizontalHeader().setVisible(False)
        self.horizontalHeader().setDefaultSectionSize(area.piece_size)
        self.verticalHeader().setVisible(False)
        self.verticalHeader().setDefaultSectionSize(area.piece_size)
        #self.setStyleSheet("QTableWidget {padding:%dpx %dpx %dpx %dpx; border-image:url(F:/code/python/el/sample.jpg)}"%(area.top_margin, area.right_margin, area.buttom_margin, area.left_margin));
        self.setEditTriggers(QTableWidget.NoEditTriggers)
        self.cellClicked.connect(self.popLabelDialog)
        
        self.clearAllLabels()
        self.prePareDir()

    
    def popLabelDialog(self, x, y):
        print("Click,x="+str(x)+",y="+str(y))
        LabelTypeDialog = QtWidgets.QDialog()
        ui = Ui_LabelTypeDialog()
        ui.setupUi(LabelTypeDialog)
        LabelTypeDialog.show()
        LabelTypeDialog.exec_()
        
        typeLabel = ui.getLabelType()
        print(str(typeLabel))
        newItem = QtWidgets.QTableWidgetItem(g_labels[typeLabel][1])
        newItem.setTextAlignment(Qt.AlignCenter)
        self.setItem(x, y, newItem)
        g_record[x][y] = typeLabel
        if typeLabel == 13:
            g_record[x][y] = -1
    
    def clearAllLabels(self):
        for row in range(0, self.area.rows):
            for col in range(0, self.area.cols):
                newItem = QtWidgets.QTableWidgetItem('')
                newItem.setTextAlignment(Qt.AlignCenter)
                self.setItem(row, col, newItem)
                
        self.initLabelRecord()
    
    def initLabelRecord(self):
        for row in range(0, self.area.rows):
            for col in range(0, self.area.cols):
                g_record[row][col] = -1
    
    def getFilePathNameExt(self, filename):  
        (filepath,tempfilename) = os.path.split(filename);  
        (shotname,extension) = os.path.splitext(tempfilename);  
        return filepath,shotname,extension
        
    def prePareDir(self):
        if not os.path.isdir(g_el_dir):
            os.mkdir(g_el_dir)
            
        if not os.path.isdir(g_label_dir):
            os.mkdir(g_label_dir)
            
        for i in range(0, 12):
            dir_name = g_label_dir + g_labels[i][0]
            if not os.path.isdir(dir_name):
                os.mkdir(dir_name)
            
    def preparePieces(self, filename):
        filepath,shortname,extension = self.getFilePathNameExt(filename)
        if not extension == ".jpg":
            return
        
        img_ori = cv2.imread(filename)
        step_x = int((g_width - g_left_margin - g_right_margin)/g_cols)
        step_y = int((g_height - g_top_margin - g_buttom_margin)/g_rows)
        start_x = g_left_margin
        start_y = g_top_margin
        
        print("===========predict file: %s============"%(filename))
        for row in range(0,self.area.rows):
            start_x = g_left_margin
            
            for col in range(0,self.area.cols):
                if (g_record[row][col] != -1):
                    print("g_record[%d][%d]"%(row, col)+str(g_record[row][col]))
                    piece_file_name = shortname + "_" + str(row+1) + "_" + str(col+1) + extension
                    piece_file_name = g_label_dir+g_labels[int(g_record[row][col])][0] + '/' + piece_file_name
                    new_img = img_ori[start_y-g_padding:start_y+step_y+g_padding, start_x-g_padding:start_x+step_x+g_padding]
                    cv2.imwrite(piece_file_name, new_img)
                start_x += step_x
            start_y += step_y
        
        self.clearAllLabels()
 
#####################################
#    标签模式主窗口
#     width： 图片区域宽度
#     heiht:   图片区域高度
#####################################
class LabelModeWindow(QMainWindow,Ui_LabelModeWindow):
    def __init__(self):        
        self.area = MainAreaSize()       
        self.fileIndex = 0
        self.picDir = ''
        self.filePath = ''
        
        super(LabelModeWindow,self).__init__()
        
    def display(self, modeSelect):
        self.area = modeSelect.getAreaInfo()
        self.setupUi(self)
        
        self.mainWidget = Ui_MainWidget(self.area, self.centralWidget)
        self.mainWidget.setGeometry(QtCore.QRect(self.area.hMargin, 30, self.area.width, self.area.height))
        self.mainWidget.setObjectName("mainWidget")
        
        #禁止改变窗口大小
        #self.setFixedSize(self.width(), self.height())
        self.setFixedSize(self.area.width+2*self.area.hMargin, self.area.height+2*self.area.vMargin)
        
        self.openDirBtn.clicked.connect(self.openPicDir)
        self.saveBtn.clicked.connect(self.savePieces)
        self.prePicBtn.clicked.connect(self.prePic)
        self.nextPicBtn.clicked.connect(self.nextPic)
        
        self.show()
    
    def openPicDir(self):
         self.picDir = QFileDialog.getExistingDirectory(self, "打开图片文件夹", "F:/")
         print(self.picDir)
         self.fileList = os.listdir(self.picDir)
         self.fileCnt = len(self.fileList)
         self.fileIndex = -1
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
        self.mainWidget.setStyleSheet("QTableWidget {padding:%dpx %dpx %dpx %dpx; border-image:url(%s)}"%(self.area.top_margin, self.area.right_margin, self.area.buttom_margin, self.area.left_margin, self.filePath))
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
    def __init__(self, parent=None):
        self.w = 8
        self.winMode = 'small'
        self.area = MainAreaSize()
        self.area.updateW(self.w)
        super(ModeSelect, self).__init__(parent)
        self.setupUi(self)
        self.windowSize1.toggled.connect(self.windowSize1Func)
        self.windowSize2.toggled.connect(self.windowSize2Func)
        self.windowSize1.toggle()
    
    def windowSize1Func(self):
        if self.windowSize1.isChecked():  
            self.winMode = 'small'
        self.changeWinSize()
            
    def windowSize2Func(self):
        if self.windowSize2.isChecked():  
            self.winMode = 'medium'
        self.changeWinSize()
    
    def changeWinSize(self):
        if self.winMode == 'small':
            self.w = 8
        elif self.winMode == 'medium':
            self.w = 4
        
        self.area.updateW(self.w)
    
    def getAreaInfo(self):
        return self.area

def enterProductMode():
    inspectionModeWindow = InspectionModeWindow()
    inspectionModeWindow.display()

def enterLabelMode():
    print("enterLabelMode()")
    labelModeWindow = LabelModeWindow()
    labelModeWindow.display()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    inspectionModeWindow = InspectionModeWindow()
    labelModeWindow = LabelModeWindow()
    dlg = ModeSelect()
    dlg.productBtn.clicked.connect(inspectionModeWindow.display)
    dlg.labelBtn.clicked.connect(partial(labelModeWindow.display, dlg))
    dlg.show()
    sys.exit(app.exec_())
