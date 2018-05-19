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
        LabelTypeDialog.resize(400, 300)
        LabelTypeDialog.setSizeGripEnabled(True)

        self.retranslateUi(LabelTypeDialog)
        QtCore.QMetaObject.connectSlotsByName(LabelTypeDialog)

    def retranslateUi(self, LabelTypeDialog):
        _translate = QtCore.QCoreApplication.translate
        LabelTypeDialog.setWindowTitle(_translate("LabelTypeDialog", "Dialog"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LabelTypeDialog = QtWidgets.QDialog()
    ui = Ui_LabelTypeDialog()
    ui.setupUi(LabelTypeDialog)
    LabelTypeDialog.show()
    sys.exit(app.exec_())

