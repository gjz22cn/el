# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\code\python\el\LabelType.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LabelTypeDialog(object):
    def setupUi(self, LabelTypeDialog):
        LabelTypeDialog.setObjectName("LabelTypeDialog")
        LabelTypeDialog.resize(400, 231)
        LabelTypeDialog.setSizeGripEnabled(True)
        self.pushButton = QtWidgets.QPushButton(LabelTypeDialog)
        self.pushButton.setGeometry(QtCore.QRect(150, 170, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.liefeng = QtWidgets.QPushButton(LabelTypeDialog)
        self.liefeng.setGeometry(QtCore.QRect(30, 70, 75, 23))
        self.liefeng.setObjectName("liefeng")
        self.liefeng.clicked.connect(self.liefengFunc)
        
        self.xuhan = QtWidgets.QPushButton(LabelTypeDialog)
        self.xuhan.setGeometry(QtCore.QRect(120, 70, 75, 23))
        self.xuhan.setObjectName("xuhan")
        self.xuhan.clicked.connect(self.xuhanFunc)
        
        self.dixiao = QtWidgets.QPushButton(LabelTypeDialog)
        self.dixiao.setGeometry(QtCore.QRect(210, 70, 75, 23))
        self.dixiao.setObjectName("dixiao")
        self.dixiao.clicked.connect(self.dixiaoFunc)
        
        self.duanluduanlu = QtWidgets.QPushButton(LabelTypeDialog)
        self.duanluduanlu.setGeometry(QtCore.QRect(300, 70, 75, 23))
        self.duanluduanlu.setObjectName("duanluduanlu")
        self.duanluduanlu.clicked.connect(self.duanluduanluFunc)

        self.retranslateUi(LabelTypeDialog)
        self.pushButton.clicked.connect(LabelTypeDialog.close)
        QtCore.QMetaObject.connectSlotsByName(LabelTypeDialog)
        self.labelType = ""

    def retranslateUi(self, LabelTypeDialog):
        _translate = QtCore.QCoreApplication.translate
        LabelTypeDialog.setWindowTitle(_translate("LabelTypeDialog", "Dialog"))
        self.pushButton.setText(_translate("LabelTypeDialog", "确定"))
        self.liefeng.setText(_translate("LabelTypeDialog", "裂缝"))
        self.xuhan.setText(_translate("LabelTypeDialog", "虚焊"))
        self.dixiao.setText(_translate("LabelTypeDialog", "低效"))
        self.duanluduanlu.setText(_translate("LabelTypeDialog", "断路短路"))
            
    def liefengFunc(self):
        self.labelType = "liefeng"
            
    def xuhanFunc(self):
        self.labelType = "xuhan"
            
    def dixiaoFunc(self):
        self.labelType = "dixiao"
            
    def duanluduanluFunc(self):
        self.labelType = "duanluduanlu"
    
    def getLabelType(self):
        return self.labelType;


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LabelTypeDialog = QtWidgets.QDialog()
    ui = Ui_LabelTypeDialog()
    ui.setupUi(LabelTypeDialog)
    LabelTypeDialog.show()
    sys.exit(app.exec_())

