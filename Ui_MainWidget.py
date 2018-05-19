from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel
from PyQt5 import QtCore, QtGui

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
