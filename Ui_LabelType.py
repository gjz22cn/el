# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\code\python\el\LabelType.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LabelTypeDialog(QtWidgets.QDialog):
    def setupUi(self, LabelTypeDialog):
        LabelTypeDialog.setObjectName("LabelTypeDialog")
        LabelTypeDialog.resize(400, 300)
        LabelTypeDialog.setSizeGripEnabled(True)
        self.pushButton = QtWidgets.QPushButton(LabelTypeDialog)
        self.pushButton.setGeometry(QtCore.QRect(140, 210, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(LabelTypeDialog)
        self.pushButton.clicked.connect(LabelTypeDialog.close)
        QtCore.QMetaObject.connectSlotsByName(LabelTypeDialog)

    def retranslateUi(self, LabelTypeDialog):
        _translate = QtCore.QCoreApplication.translate
        LabelTypeDialog.setWindowTitle(_translate("LabelTypeDialog", "Dialog"))
        self.pushButton.setText(_translate("LabelTypeDialog", "确定"))
    
    def return_strings(self):
        return "OK!"
        
    def get_data(parent=None): 
        LabelTypeDialog = QtWidgets.QDialog()     
        dialog = Ui_LabelTypeDialog(parent)
        dialog.setupUi(LabelTypeDialog)
        dialog.show()
        dialog.exec_()
        return dialog.return_strings()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LabelTypeDialog = QtWidgets.QDialog()
    ui = Ui_LabelTypeDialog()
    ui.setupUi(LabelTypeDialog)
    LabelTypeDialog.show()
    sys.exit(app.exec_())

