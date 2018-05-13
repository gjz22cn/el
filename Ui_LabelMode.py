# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\code\python\el\LabelMode.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LabelModeWindow(object):
    def setupUi(self, LabelModeWindow):
        LabelModeWindow.setObjectName("LabelModeWindow")
        LabelModeWindow.resize(800, 522)
        self.centralWidget = QtWidgets.QWidget(LabelModeWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralWidget)
        self.graphicsView.setGeometry(QtCore.QRect(50, 70, 551, 361))
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(620, 340, 160, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)
        LabelModeWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(LabelModeWindow)
        QtCore.QMetaObject.connectSlotsByName(LabelModeWindow)

    def retranslateUi(self, LabelModeWindow):
        _translate = QtCore.QCoreApplication.translate
        LabelModeWindow.setWindowTitle(_translate("LabelModeWindow", "MainWindow"))
        self.pushButton.setText(_translate("LabelModeWindow", "PushButton"))
        self.pushButton_2.setText(_translate("LabelModeWindow", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LabelModeWindow = QtWidgets.QMainWindow()
    ui = Ui_LabelModeWindow()
    ui.setupUi(LabelModeWindow)
    LabelModeWindow.show()
    sys.exit(app.exec_())

