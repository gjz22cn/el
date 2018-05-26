# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\code\python\el\ModeSelect.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(569, 368)
        Dialog.setSizeGripEnabled(True)
        self.productBtn = QtWidgets.QPushButton(Dialog)
        self.productBtn.setGeometry(QtCore.QRect(320, 270, 100, 50))
        self.productBtn.setStyleSheet("font: 75 12pt \"Adobe Arabic\";")
        self.productBtn.setObjectName("productBtn")
        self.labelBtn = QtWidgets.QPushButton(Dialog)
        self.labelBtn.setGeometry(QtCore.QRect(160, 270, 100, 50))
        self.labelBtn.setStyleSheet("font: 75 12pt \"Adobe Arabic\";")
        self.labelBtn.setObjectName("labelBtn")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 50, 561, 55))
        self.label.setStyleSheet("font: 75 36pt \"Adobe Arabic\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(3, 129, 561, 41))
        self.label_2.setStyleSheet("font: 75 20pt \"Adobe Arabic\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(160, 200, 261, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.windowSize1 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.windowSize1.setStyleSheet("font: 14pt \"AcadEref\";")
        self.windowSize1.setObjectName("windowSize1")
        self.horizontalLayout.addWidget(self.windowSize1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.windowSize2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.windowSize2.setStyleSheet("font: 14pt \"AcadEref\";")
        self.windowSize2.setObjectName("windowSize2")
        self.horizontalLayout.addWidget(self.windowSize2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "太阳能电池板检测系统-工作模式选择"))
        self.productBtn.setText(_translate("Dialog", "生产模式"))
        self.labelBtn.setText(_translate("Dialog", "标签模式"))
        self.label.setText(_translate("Dialog", "太阳能电池板检测系统"))
        self.label_2.setText(_translate("Dialog", "版本号: V1.0.0"))
        self.windowSize1.setText(_translate("Dialog", "小窗口"))
        self.windowSize2.setText(_translate("Dialog", "大窗口"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

