from PyQt5.QtWidgets import QTableWidget
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import  Qt
from Ui_LabelType import Ui_LabelTypeDialog

g_labels = [['0_good','良品'], 
           ['1_liefeng','裂缝'],  
           ['2_quejiao', "缺角"], 
           ['3_duanshan',"断栅"], 
           ['4_xuhan',"虚焊"], 
           ['5_duanlu',"断路"], 
           ['6_hundang',"混档"], 
           ['7_heixinheiban',"黑心黑斑"], 
           ['8_tongxinyuan',"同心圆"], 
           ['9_heibian',"黑边" ], 
           ['10_heijiao', "黑角"], 
           ['11_liangban', "亮斑"], 
           ['12_huahen', "划痕"]]
           
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
        newItem = QtWidgets.QTableWidgetItem(g_labels[ui.getLabelType()][1])
        newItem.setTextAlignment(Qt.AlignCenter)
        self.setItem(x, y, newItem)
    
    def clearAllLabels(self):
        for row in range(1, 7):
            for col in range(1, 11):
                newItem = QtWidgets.QTableWidgetItem('')
                newItem.setTextAlignment(Qt.AlignCenter)
                self.setItem(row, col, newItem)
