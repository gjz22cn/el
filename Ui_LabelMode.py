# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\code\python\el\LabelMode.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import os
from PyQt5 import QtCore, QtWidgets
from Ui_MainWidget import Ui_MainWidget
from PyQt5.QtWidgets import QFileDialog, QWidget

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
           
class Ui_LabelModeWindow(QWidget):
    def setupUi(self, LabelModeWindow):
        g_width,  g_height= 4896,  3034
        g_top_margin,  g_right_margin,  g_buttom_margin,  g_left_margin = 48,  48,  104,  48
        w = 8
        self.width = g_width/w
        self.height = g_height/w
        self.top_margin = g_top_margin/w
        self.right_margin = g_right_margin/w
        self.buttom_margin = g_buttom_margin/w
        self.left_margin = g_left_margin/w
        self.piece_size = 480/w
        LabelModeWindow.setObjectName("LabelModeWindow")
        LabelModeWindow.resize(self.width+200, self.height+50)
        self.centralWidget = QtWidgets.QWidget(LabelModeWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(self.width+10, 50, 160, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_4.setGeometry(QtCore.QRect(self.width+10, 10, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        
        #self.tableWidget = QtWidgets.QTableWidget(self.centralWidget)
        self.tableWidget = Ui_MainWidget(self.centralWidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, self.width, self.height))
        
        self.pushButton_4.clicked.connect(self.openPicDir)
        self.pushButton.clicked.connect(self.nextPic)
        self.pushButton_2.clicked.connect(self.prePic)
        
        LabelModeWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(LabelModeWindow)
        QtCore.QMetaObject.connectSlotsByName(LabelModeWindow)
        self.picDir = ''

    def retranslateUi(self, LabelModeWindow):
        _translate = QtCore.QCoreApplication.translate
        LabelModeWindow.setWindowTitle(_translate("LabelModeWindow", "MainWindow"))
        self.pushButton.setText(_translate("LabelModeWindow", "下一张"))
        self.pushButton_2.setText(_translate("LabelModeWindow", "上一张"))
        self.pushButton_4.setText(_translate("LabelModeWindow", "打开文件夹"))
    
    def openPicDir(self):
         self.picDir = QFileDialog.getExistingDirectory(self, "Open a folder", "F:/")
         print(self.picDir)
         self.fileList = os.listdir(self.picDir)
         self.fileCnt = len(self.fileList)
         self.fileIndex = 0
                
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
        self.tableWidget.setStyleSheet("QTableWidget {padding:%dpx %dpx %dpx %dpx; border-image:url(%s)}"%(self.top_margin, self.right_margin, self.buttom_margin, self.left_margin, self.filePath))
        self.tableWidget.clearAllLabels()
    
    def getFilePathNameExt(self, filename):  
        (filepath,tempfilename) = os.path.split(filename);  
        (shotname,extension) = os.path.splitext(tempfilename);  
        return filepath,shotname,extension
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LabelModeWindow = QtWidgets.QMainWindow()
    ui = Ui_LabelModeWindow()
    ui.setupUi(LabelModeWindow)
    LabelModeWindow.show()
    sys.exit(app.exec_())

