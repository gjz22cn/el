# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import * 
import produce_pattern
import Ui_LabelMode
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 371)
        self.mainWindow = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 501, 351))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.systemName = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.systemName.sizePolicy().hasHeightForWidth())
        self.systemName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.systemName.setFont(font)
        self.systemName.setAlignment(QtCore.Qt.AlignCenter)
        self.systemName.setObjectName("systemName")
        self.verticalLayout.addWidget(self.systemName)
        self.version = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.version.sizePolicy().hasHeightForWidth())
        self.version.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.version.setFont(font)
        self.version.setAlignment(QtCore.Qt.AlignCenter)
        self.version.setObjectName("version")
        self.verticalLayout.addWidget(self.version)
        self.workPattern = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.workPattern.setFont(font)
        self.workPattern.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.workPattern.setObjectName("workPattern")
        self.verticalLayout.addWidget(self.workPattern)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.producePattern = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.producePattern.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"font: bold 14px;\n"
"min-width: 10em;\n"
"padding: 6px;")
        self.producePattern.setDefault(True)
        self.producePattern.setFlat(False)
        self.producePattern.setObjectName("producePattern")
        self.horizontalLayout.addWidget(self.producePattern)
        self.markPattern = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.markPattern.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"font: bold 14px;\n"
"min-width: 10em;\n"
"padding: 6px;")
        self.markPattern.setObjectName("markPattern")
        self.horizontalLayout.addWidget(self.markPattern)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.producePattern.clicked.connect(self.toProducePattern)
        self.markPattern.clicked.connect(self.toMarkPattern)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
#        Form.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "太阳能电池板检测系统"))
        self.systemName.setText(_translate("MainWindow", "太阳能电池板检测系统"))
        self.version.setText(_translate("MainWindow", "版本：V1.0.0"))
        self.workPattern.setText(_translate("MainWindow", "请选择工作模式："))
        self.producePattern.setText(_translate("MainWindow", "生产模式"))
        self.markPattern.setText(_translate("MainWindow", "标签模式"))
    def toProducePattern(self):
        print("----produce pattern")
        
        self.mainWindow.hide()            #如果没有self.form.show()这一句，关闭Demo1界面后就会关闭程序
        self.produce= QtWidgets.QMainWindow()
        ui = produce_pattern.Produce_PatternWindow()
        ui.setupUi(self.produce)
        self.produce.show()
        print("----produce end")
#        self.mainWindow.show()
        
    def toMarkPattern(self):
        print("----mark pattern")
        
        self.mainWindow.hide()            #如果没有self.form.show()这一句，关闭Demo1界面后就会关闭程序
        self.mark= QtWidgets.QMainWindow()
        ui = Ui_LabelMode.Ui_LabelModeWindow()
        ui.setupUi(self.mark)
        self.mark.show()
        print("----mark end")
#        self.mainWindow.show()
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    mainPage = QtWidgets.QMainWindow()#创建一个窗体
    ui = Ui_MainWindow()#创建一个自定义的对象
    ui.setupUi(mainPage)#将对象绑定到窗体上
    mainPage.show()#窗体显示出来 
    sys.exit(app.exec_())
    pass

