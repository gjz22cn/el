# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\code\python\el\LabelMode.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_MainWidget import Ui_MainWidget

class Ui_LabelModeWindow(object):
    def setupUi(self, LabelModeWindow):
        LabelModeWindow.setObjectName("LabelModeWindow")
        LabelModeWindow.resize(1433, 785)
        self.centralWidget = QtWidgets.QWidget(LabelModeWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(1250, 710, 160, 41))
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
        self.pushButton_4.setGeometry(QtCore.QRect(1250, 670, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        
        #self.tableWidget = QtWidgets.QTableWidget(self.centralWidget)
        self.tableWidget = Ui_MainWidget(self.centralWidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 1224, 758))
        
        
        self.horizontalLayoutWidget.raise_()
        self.pushButton_4.raise_()
        self.tableWidget.raise_()
        self.pushButton_2.raise_()
        LabelModeWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(LabelModeWindow)
        QtCore.QMetaObject.connectSlotsByName(LabelModeWindow)

    def retranslateUi(self, LabelModeWindow):
        _translate = QtCore.QCoreApplication.translate
        LabelModeWindow.setWindowTitle(_translate("LabelModeWindow", "MainWindow"))
        self.pushButton.setText(_translate("LabelModeWindow", "下一张"))
        self.pushButton_2.setText(_translate("LabelModeWindow", "上一张"))
        self.pushButton_4.setText(_translate("LabelModeWindow", "打开文件夹"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LabelModeWindow = QtWidgets.QMainWindow()
    ui = Ui_LabelModeWindow()
    ui.setupUi(LabelModeWindow)
    LabelModeWindow.show()
    sys.exit(app.exec_())

