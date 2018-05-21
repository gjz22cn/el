from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QTableWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_LabelType import Ui_LabelTypeDialog

class Ui_MainWidget(QTableWidget):
    def __init__(self, parent=None):
        super(Ui_MainWidget,self).__init__(parent)
        #self.setObjectName("myQWidget")
        g_width,  g_height= 4896,  3034
        g_top_margin,  g_right_margin,  g_buttom_margin,  g_left_margin = 48,  48,  104,  48
        w = 8
        self.width = g_width/w
        self.height = g_height/w
        self.top_margin = g_top_margin/w
        self.right_margin = g_right_margin/w
        self.buttom_margin = g_buttom_margin/w
        self.left_margin = g_left_margin/w
        self.piece_size = 480/w
        
        
        
        self.setGeometry(QtCore.QRect(0, 0, self.width, self.height))
        
        self.setColumnCount(10)
        self.setRowCount(6)
        
        self.setVerticalHeaderLabels(['A','B','C', 'D', 'E', 'F'])
        self.horizontalHeader().setVisible(False)
        self.horizontalHeader().setDefaultSectionSize(self.piece_size)
        self.verticalHeader().setVisible(False)
        self.verticalHeader().setDefaultSectionSize(self.piece_size)
        self.setStyleSheet("QTableWidget {padding:%dpx %dpx %dpx %dpx; border-image:url(F:/code/python/el/sample.jpg)}"%(self.top_margin, self.right_margin, self.buttom_margin, self.left_margin));
        self.setEditTriggers(QTableWidget.NoEditTriggers)
        self.cellClicked.connect(self.popLabelDialog)

    
    def popLabelDialog(self, x, y):
        print("Click,x="+str(x)+",y="+str(y))
        LabelTypeDialog = QtWidgets.QDialog()
        ui = Ui_LabelTypeDialog()
        ui.setupUi(LabelTypeDialog)
        LabelTypeDialog.show()
        LabelTypeDialog.exec_()
        print(ui.getLabelType())
        self.setItem(x, y, QtWidgets.QTableWidgetItem(ui.getLabelType()))
