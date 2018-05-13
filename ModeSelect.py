# -*- coding: utf-8 -*-

"""
Module implementing ModeSelect.
"""
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow

from Ui_ModeSelect import Ui_Dialog
from Ui_LabelMode import Ui_LabelModeWindow
from Ui_InspectionMode import Ui_InspectionModeWindow

class LabelModeWindow(QMainWindow,Ui_LabelModeWindow):
    def __init__(self):
        super(LabelModeWindow,self).__init__()
        self.setupUi(self)
    
    def display(self):
        self.show()

class InspectionModeWindow(QMainWindow,Ui_InspectionModeWindow):
    def __init__(self):
        super(InspectionModeWindow,self).__init__()
        self.setupUi(self)
    
    def display(self):
        self.show()
        
class ModeSelect(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(ModeSelect, self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    labelModeWindow = LabelModeWindow()
    inspectionModeWindow = InspectionModeWindow()
    dlg = ModeSelect()
    dlg.pushButton.clicked.connect(inspectionModeWindow.display)
    dlg.pushButton_2.clicked.connect(labelModeWindow.display)
    dlg.show()
    sys.exit(app.exec_())
