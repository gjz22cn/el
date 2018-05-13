# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\code\python\el\InspectionMode.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_InspectionModeWindow(object):
    def setupUi(self, InspectionModeWindow):
        InspectionModeWindow.setObjectName("InspectionModeWindow")
        InspectionModeWindow.resize(800, 600)
        self.centralWidget = QtWidgets.QWidget(InspectionModeWindow)
        self.centralWidget.setObjectName("centralWidget")
        InspectionModeWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(InspectionModeWindow)
        QtCore.QMetaObject.connectSlotsByName(InspectionModeWindow)

    def retranslateUi(self, InspectionModeWindow):
        _translate = QtCore.QCoreApplication.translate
        InspectionModeWindow.setWindowTitle(_translate("InspectionModeWindow", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InspectionModeWindow = QtWidgets.QMainWindow()
    ui = Ui_InspectionModeWindow()
    ui.setupUi(InspectionModeWindow)
    InspectionModeWindow.show()
    sys.exit(app.exec_())

