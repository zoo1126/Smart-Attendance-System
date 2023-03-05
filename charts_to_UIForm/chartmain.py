import sys

import numpy as np
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from UI.hr_win.visualize_att import Ui_Form as visualize_att

class Mychart(visualize_att):
    def __init__(self,parent=None):
        super(Mychart,self).__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        webSettings=QWebEngineSettings.globalSettings()
        webSettings.setAttribute(QWebEngineSettings.JavascriptEnabled,True)
        webSettings.setAttribute(QWebEngineSettings.PluginsEnabled, True)
        webSettings.setAttribute(QWebEngineSettings.JavascriptCanOpenWindows, True)

        self.webView=QWebEngineView()
        self.webView.load(QUrl('file:///'+'js/chart.html'))
        self.gridLayout_4.addWidget(self.webView)

        self.timer=QTimer()
        self.timer.timeout.connect(self.slotTimeout)

    def slotTimeout(self):
        js="setValue({},{})".format(list(np.random.randint(20,100,4)),list(np.random.randint(20,100,4)))

        self.webView.page().runJavaScript(js)

