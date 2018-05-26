# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\code\python\el\LabelMode.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from Ui_MainWidget import Ui_MainWidget
from PyQt5.QtWidgets import QWidget

class Ui_LabelModeWindow(QWidget):
    def setupUi(self, LabelModeWindow):
        LabelModeWindow.setObjectName("LabelModeWindow")
        LabelModeWindow.resize(self.width+2*self.hMargin, self.height+2*self.vMargin)

        self.centralWidget = QtWidgets.QWidget(LabelModeWindow)
        self.centralWidget.setObjectName("centralWidget")
        #self.mainWidget = QtWidgets.QTableWidget(self.centralWidget)
        self.mainWidget = Ui_MainWidget(self.centralWidget)
        self.mainWidget.setGeometry(QtCore.QRect(self.hMargin, 30, self.width, self.height))
        self.mainWidget.setObjectName("mainWidget")
        self.mainWidget.setColumnCount(self.colCnt)
        self.mainWidget.setRowCount(self.rowCnt)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(self.hMargin, self.height+40, self.width, 40))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.winSizeBtn1 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.winSizeBtn1.setObjectName("winSizeBtn1")
        self.horizontalLayout.addWidget(self.winSizeBtn1)
        self.winSizeBtn2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.winSizeBtn2.setObjectName("winSizeBtn2")
        self.horizontalLayout.addWidget(self.winSizeBtn2)
        self.openDirBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.openDirBtn.setObjectName("openDirBtn")
        self.horizontalLayout.addWidget(self.openDirBtn)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.saveBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.saveBtn.setObjectName("saveBtn")
        self.horizontalLayout.addWidget(self.saveBtn)
        self.prePicBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.prePicBtn.setObjectName("prePicBtn")
        self.horizontalLayout.addWidget(self.prePicBtn)
        self.nextPicBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.nextPicBtn.setObjectName("nextPicBtn")
        
        self.horizontalLayout.addWidget(self.nextPicBtn)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(2, self.height+90, self.width+2*self.hMargin-4, 26))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.infoLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.infoLayout.setContentsMargins(0, 0, 0, 0)
        self.infoLayout.setObjectName("infoLayout")
        self.fileLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.fileLabel.setObjectName("fileLabel")
        self.infoLayout.addWidget(self.fileLabel)
        self.saveDirLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.saveDirLabel.setObjectName("saveDirLabel")
        self.infoLayout.addWidget(self.saveDirLabel)
        LabelModeWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(LabelModeWindow)
        QtCore.QMetaObject.connectSlotsByName(LabelModeWindow)

    def retranslateUi(self, LabelModeWindow):
        _translate = QtCore.QCoreApplication.translate
        LabelModeWindow.setWindowTitle(_translate("LabelModeWindow", "太阳能电池板检测系统-标签模式"))
        self.winSizeBtn1.setText(_translate("LabelModeWindow", "小窗口"))
        self.winSizeBtn2.setText(_translate("LabelModeWindow", "大窗口"))
        self.openDirBtn.setText(_translate("LabelModeWindow", "打开文件夹"))
        self.pushButton_3.setText(_translate("LabelModeWindow", "选择保存目录"))
        self.saveBtn.setText(_translate("LabelModeWindow", "保存"))
        self.prePicBtn.setText(_translate("LabelModeWindow", "上一张"))
        self.nextPicBtn.setText(_translate("LabelModeWindow", "下一张"))
        self.fileLabel.setText(_translate("LabelModeWindow", "文件名： "))
        self.saveDirLabel.setText(_translate("LabelModeWindow", "保存目录： "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LabelModeWindow = QtWidgets.QMainWindow()
    ui = Ui_LabelModeWindow()
    ui.setupUi(LabelModeWindow)
    LabelModeWindow.show()
    sys.exit(app.exec_())

