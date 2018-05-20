from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QTableWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_LabelType import Ui_LabelTypeDialog

'''
class Ui_MainWidget(QWidget):
    def __init__(self, parent=None):
        super(Ui_MainWidget,self).__init__(parent)
        #self.setObjectName("myQWidget")
        self.setGeometry(QtCore.QRect(0, 0, 801, 511))
        
        self.setAutoFillBackground(True)
        palette = QtGui.QPalette()
        pixmap = QtGui.QPixmap('F:/code/python/el/sample.jpg').scaled(self.size())
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(pixmap)) 
        self.setPalette(palette)
        
        
        
        #self.setStyleSheet("#myQWidget {background-image:url(F:/code/python/el/sample.jpg)}");
        
        self.grid = QGridLayout()
        self.grid.setSpacing(0)
        self.setLayout(self.grid) 
        pos = [(i, j) for i in range(6) for j in range(10)]
        for i in range(len(pos)):
            self.grid.addWidget(QLabel('haha'), pos[i][0], pos[i][1])
    
    def mouseDoubleClickEvent(self, event):
        print("double1 Click")
        location = self.grid.getItemPosition(idx)
        print("at row/col", location[:2])
'''

class Ui_MainWidget(QTableWidget):
    def __init__(self, parent=None):
        super(Ui_MainWidget,self).__init__(parent)
        #self.setObjectName("myQWidget")
        g_width,  g_height= 4896,  3034
        g_top_margin,  g_right_margin,  g_buttom_margin,  g_left_margin = 48,  48,  104,  48
        self.setGeometry(QtCore.QRect(0, 0, 1224, 758))
        
        self.setColumnCount(10)
        self.setRowCount(6)
        
        self.setVerticalHeaderLabels(['A','B','C', 'D', 'E', 'F'])
        self.horizontalHeader().setVisible(False)
        self.horizontalHeader().setDefaultSectionSize(120)
        self.verticalHeader().setVisible(False)
        self.verticalHeader().setDefaultSectionSize(120)
        self.setStyleSheet("QTableWidget {padding:12px 12px 26px 12px; border-image:url(F:/code/python/el/sample.jpg)}");
        self.setEditTriggers(QTableWidget.NoEditTriggers)
        self.cellClicked.connect(self.popLabelDialog)

    
    def popLabelDialog(self, x, y):
        print("double1 Click,x="+str(x)+",y="+str(y))
        LabelTypeDialog = QtWidgets.QDialog()
        ui = Ui_LabelTypeDialog()
        ui.setupUi(LabelTypeDialog)
        LabelTypeDialog.show()
        LabelTypeDialog.exec_()
        print(ui.return_strings())
        self.setItem(x, y, QtWidgets.QTableWidgetItem(ui.return_strings()))
