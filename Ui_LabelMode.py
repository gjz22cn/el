# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\code\python\el\LabelMode.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget

class Ui_LabelModeWindow(QWidget):
    def setupUi(self, LabelModeWindow):
        LabelModeWindow.setObjectName("LabelModeWindow")
        LabelModeWindow.resize(self.area.width+2*self.area.hMargin, self.area.height+2*self.area.vMargin)
        self.centralWidget = QtWidgets.QWidget(LabelModeWindow)
        self.centralWidget.setObjectName("centralWidget")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(self.area.hMargin, self.area.height+40, self.area.width, 40))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.openDirBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.openDirBtn.setObjectName("openDirBtn")
        self.horizontalLayout.addWidget(self.openDirBtn)
        self.saveDirBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.saveDirBtn.setObjectName("saveDirBtn")
        self.horizontalLayout.addWidget(self.saveDirBtn)
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
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(2, self.area.height+90, self.area.width+2*self.area.hMargin-4, 26))
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
        self.statusLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.statusLabel.setText("")
        self.statusLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statusLabel.setObjectName("statusLabel")
        self.infoLayout.addWidget(self.statusLabel)
        LabelModeWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(LabelModeWindow)
        QtCore.QMetaObject.connectSlotsByName(LabelModeWindow)

    def retranslateUi(self, LabelModeWindow):
        _translate = QtCore.QCoreApplication.translate
        LabelModeWindow.setWindowTitle(_translate("LabelModeWindow", "太阳能电池板检测系统-标签模式"))
        self.openDirBtn.setText(_translate("LabelModeWindow", "打开文件夹"))
        self.saveDirBtn.setText(_translate("LabelModeWindow", "选择保存目录"))
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

