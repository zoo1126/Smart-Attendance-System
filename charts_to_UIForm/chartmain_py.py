from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QDialog, QApplication, QHBoxLayout, QWidget, QGridLayout, QLabel, QSpinBox, \
    QSpacerItem, QSizePolicy, QComboBox
from random import randint


from UI.hr_win.visualize_att import Ui_Form as visualize_att

class chartPy(visualize_att):
    def __init__(self,parent=None):
        super(chartPy,self).__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):

        self.webView=QWebEngineView()
        self.webView.load(QUrl('file:///'+'js/dailyAttendance.html'))
        self.gridLayout_4.addWidget(self.webView)










