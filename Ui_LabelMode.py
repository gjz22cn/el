# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\code\python\el\LabelMode.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog,  QWidget, QMainWindow
from Ui_LabelType import Ui_LabelTypeDialog
from Ui_MainWidget import Ui_MainWidget

class Ui_LabelModeWindow(object):
    def setupUi(self, LabelModeWindow):
        LabelModeWindow.setObjectName("LabelModeWindow")
        LabelModeWindow.resize(953, 768)
        self.centralWidget = QtWidgets.QWidget(LabelModeWindow)
        self.centralWidget.setObjectName("centralWidget")
        
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(850, 500, 160, 41))
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
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(850, 70, 160, 122))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listView = QtWidgets.QListView(self.verticalLayoutWidget)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_4.setGeometry(QtCore.QRect(860, 20, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton.clicked.connect(self.openPicDir)
        print("haha")
        #self.widget = QtWidgets.QWidget(self.centralWidget)
        self.widget = Ui_MainWidget(self.centralWidget)
        self.widget.setGeometry(QtCore.QRect(29, 29, 801, 511))
        #self.widget.setObjectName("myQWidget")
        #self.widget.setStyleSheet("#myQWidget {border-image:url(F:/code/python/el/sample.jpg)}");
        #self.widget.setStyleSheet("background-color:white;")
        LabelModeWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(LabelModeWindow)
        QtCore.QMetaObject.connectSlotsByName(LabelModeWindow)

    def retranslateUi(self, LabelModeWindow):
        _translate = QtCore.QCoreApplication.translate
        LabelModeWindow.setWindowTitle(_translate("LabelModeWindow", "MainWindow"))
        self.pushButton.setText(_translate("LabelModeWindow", "下一张"))
        self.pushButton_2.setText(_translate("LabelModeWindow", "上一张"))
        self.label.setText(_translate("LabelModeWindow", "标签列表"))
        self.pushButton_3.setText(_translate("LabelModeWindow", "确认"))
        self.pushButton_4.setText(_translate("LabelModeWindow", "打开文件夹"))
    
    def openPicDir(self):
         self.picDir = QFileDialog.getExistingDirectory(self, "Open a folder", "E:/")
    
    def mousePressEvent(self, event):
        print("mousePressEvent")
        
    def mouseDoubleClickEvent(self, event):
        print("double Click")
        LabelTypeDialog = Ui_LabelTypeDialog()
        LabelTypeDialog.show()
        LabelTypeDialog.exec_()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LabelModeWindow = QtWidgets.QMainWindow()
    ui = Ui_LabelModeWindow()
    ui.setupUi(LabelModeWindow)
    LabelModeWindow.show()
    sys.exit(app.exec_())

