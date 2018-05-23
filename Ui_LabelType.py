# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\code\python\el\LabelType.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial

class Ui_LabelTypeDialog(object):
    def setupUi(self, LabelTypeDialog):
        self.LabelTypeDialog = LabelTypeDialog
        LabelTypeDialog.setObjectName("LabelTypeDialog")
        LabelTypeDialog.resize(404, 206)
        LabelTypeDialog.setSizeGripEnabled(True)
        self.good = QtWidgets.QPushButton(LabelTypeDialog)
        self.good.setGeometry(QtCore.QRect(30, 30, 70, 25))
        self.good.setObjectName("good")
        self.liefeng = QtWidgets.QPushButton(LabelTypeDialog)
        self.liefeng.setGeometry(QtCore.QRect(30, 70, 70, 25))
        self.liefeng.setObjectName("liefeng")
        self.quejiao = QtWidgets.QPushButton(LabelTypeDialog)
        self.quejiao.setGeometry(QtCore.QRect(120, 70, 70, 25))
        self.quejiao.setObjectName("quejiao")
        self.duanshan = QtWidgets.QPushButton(LabelTypeDialog)
        self.duanshan.setGeometry(QtCore.QRect(210, 70, 70, 25))
        self.duanshan.setObjectName("duanshan")
        self.duanlu = QtWidgets.QPushButton(LabelTypeDialog)
        self.duanlu.setGeometry(QtCore.QRect(30, 110, 70, 25))
        self.duanlu.setObjectName("duanlu")
        self.hundang = QtWidgets.QPushButton(LabelTypeDialog)
        self.hundang.setGeometry(QtCore.QRect(120, 110, 70, 25))
        self.hundang.setObjectName("hundang")
        self.heixinheiban = QtWidgets.QPushButton(LabelTypeDialog)
        self.heixinheiban.setGeometry(QtCore.QRect(210, 110, 70, 25))
        self.heixinheiban.setObjectName("heixinheiban")
        self.tongxinyuan = QtWidgets.QPushButton(LabelTypeDialog)
        self.tongxinyuan.setGeometry(QtCore.QRect(300, 110, 70, 25))
        self.tongxinyuan.setObjectName("tongxinyuan")
        self.xuhan = QtWidgets.QPushButton(LabelTypeDialog)
        self.xuhan.setGeometry(QtCore.QRect(300, 70, 70, 25))
        self.xuhan.setObjectName("xuhan")
        self.heibian = QtWidgets.QPushButton(LabelTypeDialog)
        self.heibian.setGeometry(QtCore.QRect(30, 150, 70, 25))
        self.heibian.setObjectName("heibian")
        self.heijiao = QtWidgets.QPushButton(LabelTypeDialog)
        self.heijiao.setGeometry(QtCore.QRect(120, 150, 70, 25))
        self.heijiao.setObjectName("heijiao")
        self.liangban = QtWidgets.QPushButton(LabelTypeDialog)
        self.liangban.setGeometry(QtCore.QRect(210, 150, 70, 25))
        self.liangban.setObjectName("liangban")
        self.huahen = QtWidgets.QPushButton(LabelTypeDialog)
        self.huahen.setGeometry(QtCore.QRect(300, 150, 70, 25))
        self.huahen.setObjectName("huahen")
        self.clear = QtWidgets.QPushButton(LabelTypeDialog)
        self.clear.setGeometry(QtCore.QRect(300, 30, 70, 25))
        self.clear.setObjectName("clear")

        self.retranslateUi(LabelTypeDialog)
        self.good.clicked.connect(LabelTypeDialog.close)
        QtCore.QMetaObject.connectSlotsByName(LabelTypeDialog)
        self.setupButtonCallBack()

    def retranslateUi(self, LabelTypeDialog):
        _translate = QtCore.QCoreApplication.translate
        LabelTypeDialog.setWindowTitle(_translate("LabelTypeDialog", "分类"))
        self.good.setText(_translate("LabelTypeDialog", "良品"))
        self.liefeng.setText(_translate("LabelTypeDialog", "裂缝"))
        self.quejiao.setText(_translate("LabelTypeDialog", "缺角"))
        self.duanshan.setText(_translate("LabelTypeDialog", "断栅"))
        self.duanlu.setText(_translate("LabelTypeDialog", "断路"))
        self.hundang.setText(_translate("LabelTypeDialog", "混档"))
        self.heixinheiban.setText(_translate("LabelTypeDialog", "黑心黑斑"))
        self.tongxinyuan.setText(_translate("LabelTypeDialog", "同心圆"))
        self.xuhan.setText(_translate("LabelTypeDialog", "虚焊"))
        self.heibian.setText(_translate("LabelTypeDialog", "黑边"))
        self.heijiao.setText(_translate("LabelTypeDialog", "黑角"))
        self.liangban.setText(_translate("LabelTypeDialog", "亮斑"))
        self.huahen.setText(_translate("LabelTypeDialog", "划痕"))
        self.clear.setText(_translate("LabelTypeDialog", "清除"))
    
    def setupButtonCallBack(self):
        self.good.clicked.connect(partial(self.onButtonClick, 0))
        self.liefeng.clicked.connect(partial(self.onButtonClick, 1))
        self.quejiao.clicked.connect(partial(self.onButtonClick, 2))
        self.duanshan.clicked.connect(partial(self.onButtonClick, 3))
        self.xuhan.clicked.connect(partial(self.onButtonClick, 4))
        self.duanlu.clicked.connect(partial(self.onButtonClick, 5))
        self.hundang.clicked.connect(partial(self.onButtonClick, 6))
        self.heixinheiban.clicked.connect(partial(self.onButtonClick, 7))
        self.tongxinyuan.clicked.connect(partial(self.onButtonClick, 8))
        self.heibian.clicked.connect(partial(self.onButtonClick, 9))
        self.heijiao.clicked.connect(partial(self.onButtonClick, 10))
        self.liangban.clicked.connect(partial(self.onButtonClick, 11))
        self.huahen.clicked.connect(partial(self.onButtonClick, 12))
        self.clear.clicked.connect(partial(self.onButtonClick, 13))
    
    def onButtonClick(self, n):
        print(str(n))
        self.labelType = n
        self.LabelTypeDialog.close()
    
    def getLabelType(self):
        return self.labelType


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LabelTypeDialog = QtWidgets.QDialog()
    ui = Ui_LabelTypeDialog()
    ui.setupUi(LabelTypeDialog)
    LabelTypeDialog.show()
    sys.exit(app.exec_())

