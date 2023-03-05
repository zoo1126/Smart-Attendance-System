from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QDialog, QApplication, QHBoxLayout, QWidget, QGridLayout, QLabel, QSpinBox, \
    QSpacerItem, QSizePolicy, QComboBox
from random import randint


from UI.staff_win.Atd_record import Ui_Form as Atd_record

class chartPy(Atd_record):
    def __init__(self,parent=None):
        super(chartPy,self).__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):

        self.webView=QWebEngineView()
        self.webView.load(QUrl('file:///'+'js/calendar_label_setting.html'))
        self.gridLayout_4.addWidget(self.webView)










