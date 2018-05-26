from PyQt5.QtWidgets import QTableWidget
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import  Qt
from Ui_LabelType import Ui_LabelTypeDialog
import numpy as np
import os
import cv2

g_width = 4896
g_height = 3034
g_top_margin = 48
g_buttom_margin = 104
g_left_margin = 48
g_right_margin = 48
g_rows = 6
g_cols = 10
g_padding = 0

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
           
class Ui_MainWidget(QTableWidget):
    def __init__(self, parent=None):
        super(Ui_MainWidget,self).__init__(parent)
        #self.setObjectName("myQWidget")
        
        w = 8
        self.width = g_width/w
        self.height = g_height/w
        self.top_margin = g_top_margin/w
        self.right_margin = g_right_margin/w
        self.buttom_margin = g_buttom_margin/w
        self.left_margin = g_left_margin/w
        self.piece_size = 480/w
        
        
        
        self.setGeometry(QtCore.QRect(0, 0, self.width, self.height))
        
        self.setColumnCount(10)
        self.setRowCount(6)
        
        self.setVerticalHeaderLabels(['A','B','C', 'D', 'E', 'F'])
        self.horizontalHeader().setVisible(False)
        self.horizontalHeader().setDefaultSectionSize(self.piece_size)
        self.verticalHeader().setVisible(False)
        self.verticalHeader().setDefaultSectionSize(self.piece_size)
        #self.setStyleSheet("QTableWidget {padding:%dpx %dpx %dpx %dpx; border-image:url(F:/code/python/el/sample.jpg)}"%(self.top_margin, self.right_margin, self.buttom_margin, self.left_margin));
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
        g_record[x-1][y-1] = typeLabel
        if typeLabel == 13:
            g_record[x-1][y-1] = -1
    
    def clearAllLabels(self):
        for row in range(1, 7):
            for col in range(1, 11):
                newItem = QtWidgets.QTableWidgetItem('')
                newItem.setTextAlignment(Qt.AlignCenter)
                self.setItem(row, col, newItem)
                
        self.initLabelRecord()
    
    def initLabelRecord(self):
        for row in range(0, 6):
            for col in range(0, 10):
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
        for row in range(0,g_rows):
            start_x = g_left_margin
            
            for col in range(0,g_cols):
                if (g_record[row][col] != -1):
                    print("g_record[%d][%d]"%(row, col)+str(g_record[row][col]))
                    piece_file_name = shortname + "_" + str(row+1) + "_" + str(col+1) + extension
                    piece_file_name = g_label_dir+g_labels[int(g_record[row][col])][0] + '/' + piece_file_name
                    new_img = img_ori[start_y-g_padding:start_y+step_y+g_padding, start_x-g_padding:start_x+step_x+g_padding]
                    cv2.imwrite(piece_file_name, new_img)
                start_x += step_x
            start_y += step_y
        
        self.clearAllLabels()
        
