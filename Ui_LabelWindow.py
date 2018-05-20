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
        self.tableWidget = QtWidgets.QTableWidget(self.centralWidget)
        self.tableWidget.setGeometry(QtCore.QRect(85, 51, 621, 431))
        self.tableWidget.setRowCount(6)
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(480)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(5)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(480)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        LabelWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(LabelWindow)
        self.tableWidget.itemDoubleClicked.connect(self.test)
        QtCore.QMetaObject.connectSlotsByName(LabelWindow)

    def retranslateUi(self, LabelWindow):
        _translate = QtCore.QCoreApplication.translate
        LabelWindow.setWindowTitle(_translate("LabelWindow", "MainWindow"))
    
    def test(self, Item=None):
        print("adsfa")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LabelWindow = QtWidgets.QMainWindow()
    ui = Ui_LabelWindow()
    ui.setupUi(LabelWindow)
    LabelWindow.show()
    sys.exit(app.exec_())

