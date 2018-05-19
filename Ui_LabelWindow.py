# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\code\python\el\LabelWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LabelWindow(object):
    def setupUi(self, LabelWindow):
        LabelWindow.setObjectName("LabelWindow")
        LabelWindow.resize(800, 600)
        self.centralWidget = QtWidgets.QWidget(LabelWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.MainWidget = QtWidgets.QWidget(self.centralWidget)
        self.MainWidget.setGeometry(QtCore.QRect(110, 50, 621, 381))
        self.MainWidget.setObjectName("MainWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(250, 500, 54, 12))
        self.label.setObjectName("label")
        LabelWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(LabelWindow)
        QtCore.QMetaObject.connectSlotsByName(LabelWindow)

    def retranslateUi(self, LabelWindow):
        _translate = QtCore.QCoreApplication.translate
        LabelWindow.setWindowTitle(_translate("LabelWindow", "MainWindow"))
        self.label.setText(_translate("LabelWindow", "haha"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LabelWindow = QtWidgets.QMainWindow()
    ui = Ui_LabelWindow()
    ui.setupUi(LabelWindow)
    LabelWindow.show()
    sys.exit(app.exec_())

