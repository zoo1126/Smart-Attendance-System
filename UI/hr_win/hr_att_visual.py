# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hr_att_visual.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from sql.company import *
from sql.dailyAttendance_sql import *
from charts.dailyAttendance import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QValidator,QRegExpValidator
from PyQt5.QtCore import QRegExp

class Ui_Form(object):
    currentSelectedStaff=None
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(922, 648)
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_3 = QtWidgets.QWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.lineEdit.setFont(font)
        self.lineEdit.setMaxLength(11)
        self.lineEdit.setObjectName("lineEdit")
        reg = QRegExp('[1][35678][0-9]{9}$')
        vali = QRegExpValidator(self)
        vali.setRegExp(reg)
        self.lineEdit.setValidator(vali)
        self.gridLayout_6.addWidget(self.lineEdit, 2, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"    background-color:DarkSeaGreen;\n"
"    color:white;\n"
"    border-radius:8px;\n"
"    border:2px groove gray;\n"
"    border-style:outset;\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.searchAll)
        self.gridLayout_6.addWidget(self.pushButton_4, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    background-color:Chocolate;\n"
"    color:white;\n"
"    border-radius:8px;\n"
"    border:2px groove gray;\n"
"    border-style:outset;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.searchbyphone)
        self.gridLayout_6.addWidget(self.pushButton_3, 2, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.widget_4)
        self.listWidget = QtWidgets.QListWidget(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.widget_3)
        self.widget = QtWidgets.QWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.widget.setFont(font)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setObjectName("widget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.radioButton = QtWidgets.QRadioButton(self.widget_5)
        self.radioButton.setObjectName("radioButton")
        self.buttonGroup = QtWidgets.QButtonGroup(Form)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton)
        self.gridLayout_5.addWidget(self.radioButton, 0, 1, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget_5)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.buttonGroup.addButton(self.radioButton_2)
        self.gridLayout_5.addWidget(self.radioButton_2, 0, 0, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.widget_5)
        self.radioButton_3.setObjectName("radioButton_3")
        self.buttonGroup.addButton(self.radioButton_3)
        self.buttonGroup.buttonClicked.connect(self.changeSorting)
        self.gridLayout_5.addWidget(self.radioButton_3, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.widget_5)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_4.setObjectName("gridLayout_4")

        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    background-color:orange;\n"
"    color:white;\n"
"    border-radius:8px;\n"
"    border:2px groove gray;\n"
"    border-style:outset;\n"
"}")
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.resetSelection)
        self.gridLayout_4.addWidget(self.pushButton_2, 0, 7, 1, 1)
        self.startdate = QtWidgets.QDateEdit(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.startdate.setFont(font)
        self.startdate.setDate(QtCore.QDate.currentDate())
        self.startdate.setStyleSheet("QDateEdit{\n"
"    border-radius:5px;\n"
"    border:1px groove gray;    \n"
"    border-style:outset;\n"
"}")
        self.startdate.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(1752, 9, 14), QtCore.QTime(0, 0, 0)))
        self.startdate.setCalendarPopup(True)
        self.startdate.setObjectName("startdate")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startdate.sizePolicy().hasHeightForWidth())
        self.startdate.setSizePolicy(sizePolicy)
        self.gridLayout_4.addWidget(self.startdate, 0, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setStyleSheet("QComboBox{\n"
"    border-radius:5px;\n"
"    border:1px groove gray;    \n"
"    border-style:outset;\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.gridLayout_4.addWidget(self.comboBox, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.label_3.setSizePolicy(sizePolicy)
        self.gridLayout_4.addWidget(self.label_3, 0, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color:green;\n"
"    color:white;\n"
"    border-radius:8px;\n"
"    border:2px groove gray;\n"
"    border-style:outset;\n"
"}")
        self.pushButton.setCheckable(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.showvisualization)
        self.gridLayout_4.addWidget(self.pushButton, 0, 6, 1, 1)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_6 = QtWidgets.QWidget(self.widget)
        self.widget_6.setObjectName("widget_6")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.widget_6)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.widget_6)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.widget)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.sort_all()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setPlaceholderText(_translate("Form", "输入手机号搜索"))
        self.pushButton_4.setText(_translate("Form", "全部"))
        self.label.setText(_translate("Form", "手机号"))
        self.pushButton_3.setText(_translate("Form", "搜索"))
        self.radioButton.setText(_translate("Form", "按部门查看"))
        self.radioButton_2.setText(_translate("Form", "按全公司查看"))
        self.radioButton_3.setText(_translate("Form", "按员工查看"))
        self.pushButton_2.setText(_translate("Form", "重置"))
        self.startdate.setDisplayFormat(_translate("Form", "yyyy-M-d"))
        self.label_2.setText(_translate("Form", "部门"))
        self.comboBox.setItemText(0, _translate("Form", "全部"))
        self.label_3.setText(_translate("Form", "日期"))
        self.pushButton.setText(_translate("Form", "查询"))


    def gettablewidget(self):
        return self.tableWidget

    def sethr_phone(self, hr_phone):
        self.hr_phone = hr_phone
        self.com_id = findCom_idbyhr_id(self.hr_phone)[0][0]
        # self.widget_3.setcom_id(self.com_id)

    def gethr_phone(self):
        return self.hr_phone

    def getcom_id(self):
        return findCom_idbyhr_id(self.hr_phone)[0][0]

    def changeSorting(self):
        currentradiobutton=self.buttonGroup.checkedButton()
        if currentradiobutton==self.radioButton:
            print("depart")
            self.sort_depart()
        elif currentradiobutton==self.radioButton_3:
            print('individual')
            self.sort_individual()
        else:
            print('all')
            self.sort_all()

    def sort_all(self):
        self.widget_3.setVisible(False)
        self.label_2.setVisible(False)
        self.comboBox.setVisible(False)
        self.startdate.setDisplayFormat('yyyy-MM-dd')


    def sort_depart(self):
        self.widget_3.setVisible(False)
        self.label_2.setVisible(True)
        self.comboBox.setVisible(True)
        self.startdate.setDisplayFormat('yyyy-MM-dd')
        dep_list=findDeps(self.getcom_id())
        self.comboBox.clear()
        self.comboBox.addItem('全部')
        for onedep in dep_list:
            self.comboBox.addItem(onedep[2])

    def sort_individual(self):

        self.widget_3.setVisible(True)
        self.label_2.setVisible(False)
        self.comboBox.setVisible(False)
        self.startdate.setDisplayFormat('yyyy-MM')
        staff_list=allStaffFind(self.getcom_id())
        self.listWidget.clear()
        if staff_list is not None:
            for onestaff in staff_list:
                if onestaff[6] is not None:
                    depname=findDepbyId(onestaff[6],self.getcom_id())[2]
                else:
                    depname="无归属"
                print(onestaff[0]+"-"+onestaff[2]+"-"+depname)
                self.listWidget.addItem(onestaff[0]+"-"+onestaff[2]+"-"+depname)

            self.listWidget.itemClicked.connect(self.printitem)
            self.startdate.setDisplayFormat('yyyy-MM')


    def resetSelection(self):
        self.startdate.setDate(QtCore.QDate.currentDate())
        if self.comboBox.isVisible():
            self.comboBox.setCurrentIndex(0)
        if self.widget_3.isVisible():
            self.lineEdit.setText(None)
            self.searchAll()
            self.listWidget.clearSelection()

    def searchbyphone(self):
        phone=self.lineEdit.text()
        stafflist=staffFindbyPhone(phone,self.getcom_id())
        self.listWidget.clear()
        if stafflist is not None:
            for onestaff in stafflist:
                if onestaff[6] is not None:
                    depname=findDepbyId(onestaff[6],self.getcom_id())[2]
                else:
                    depname="无归属"
                self.listWidget.addItem(onestaff[0] + "-" + onestaff[2] + "-" + depname)
            self.listWidget.itemClicked.connect(self.printitem)
            self.startdate.setDisplayFormat('yyyy-MM')

    def searchAll(self):
        staff_list = allStaffFind(self.getcom_id())
        self.listWidget.clear()
        if staff_list is not None:
            for onestaff in staff_list:
                if onestaff[6] is not None:
                    depname=findDepbyId(onestaff[6],self.getcom_id())[2]
                else:
                    depname="无归属"
                self.listWidget.addItem(onestaff[0] + "-" + onestaff[2] + "-" + depname)
            self.listWidget.itemClicked.connect(self.printitem)
            self.startdate.setDisplayFormat('yyyy-MM')



    def printitem(self):
        self.currentSelectedStaff=self.listWidget.currentItem().text()


    def showvisualization(self):
        if not self.widget_3.isVisible() and not self.comboBox.isVisible():
            starttime=self.startdate.date().toString('yyyy-MM-dd')+' 00:00:00'
            endtime = self.startdate.date().toString('yyyy-MM-dd') + ' 23:59:59'
            dic=countAllDailyAtt(self.getcom_id(),starttime,endtime)
            num=countAllstaff(self.getcom_id())
            att_ok_num=att_late_num=att_out_num=att_rest_num=0
            if dic.keys().__contains__(1):
                att_ok_num=dic.get(1)
            if dic.keys().__contains__(2):
                att_late_num=dic.get(2)
            if dic.keys().__contains__(3):
                att_rest_num=dic.get(3)
            if dic.keys().__contains__(4):
                att_out_num=dic.get(4)
            att_no_num=num-att_ok_num-att_rest_num-att_out_num-att_late_num
            list=[att_no_num,att_ok_num,att_late_num,att_rest_num,att_out_num]
            print(list)
            if self.widget_6.findChild(QWebEngineView,'webView') is not None:
                child=self.widget_6.findChild(QWebEngineView,'webView')
                child.setParent(None)
                self.gridLayout_7.removeWidget(child)
                child.deleteLater()
                showALLAtt(list,self.gridLayout_7)
            else:
                showALLAtt(list, self.gridLayout_7)
        elif not self.widget_3.isVisible() and self.comboBox.isVisible():
            depname = self.comboBox.currentText()
            starttime = self.startdate.date().toString('yyyy-MM-dd') + ' 00:00:00'
            endtime = self.startdate.date().toString('yyyy-MM-dd') + ' 23:59:59'
            dic = countDepDailyAtt(self.getcom_id(), depname, starttime, endtime)
            if self.comboBox.currentText()=='全部':
                num = countAllstaff(self.getcom_id())
            else:
                num = countDepstaff(self.comboBox.currentText(),self.getcom_id())
            att_ok_num = att_late_num = att_out_num = att_rest_num = 0
            if dic.keys().__contains__(1):
                att_ok_num = dic.get(1)
            if dic.keys().__contains__(2):
                att_late_num = dic.get(2)
            if dic.keys().__contains__(3):
                att_rest_num = dic.get(3)
            if dic.keys().__contains__(4):
                att_out_num = dic.get(4)
            att_no_num = num - att_ok_num - att_rest_num - att_out_num - att_late_num
            list = [att_no_num, att_ok_num, att_late_num, att_rest_num, att_out_num]

            if self.widget_6.findChild(QWebEngineView, 'webView') is not None:
                child = self.widget_6.findChild(QWebEngineView, 'webView')
                child.setParent(None)
                self.gridLayout_7.removeWidget(child)
                child.deleteLater()
                showDepAtt(list, self.gridLayout_7)

            else:
                showDepAtt(list, self.gridLayout_7)
        elif self.widget_3.isVisible() and not self.comboBox.isVisible():
            if self.currentSelectedStaff is not None:
                staffmessage=self.currentSelectedStaff.split("-")
                staffphone=staffmessage[0]
                lastday=self.startdate.date().daysInMonth()
                dateMonth=self.startdate.date().toString("yyyy-MM")
                starttime = self.startdate.date().toString('yyyy-MM') + '-01 00:00:00'
                endtime = self.startdate.date().toString('yyyy-MM') + '-' + str(lastday) + ' 23:59:59'
                att_list=findIndDailyAtt(self.getcom_id(),staffphone,starttime,endtime)
                dic={}
                for oneatt in att_list:
                    dic[str(oneatt[2].date())]=oneatt[3]
                data=[]
                for i in range (1,lastday+1):
                    if i/10==0:
                        day="0"+str(i)
                    else:
                        day=str(i)
                    date=self.startdate.date().toString('yyyy-MM')+"-"+day
                    if dic.keys().__contains__(date):
                        data.append([date,dic.get(date)])
                    else:
                        data.append([date,0])
                if self.widget_6.findChild(QWebEngineView, 'webView') is not None:
                    child = self.widget_6.findChild(QWebEngineView, 'webView')
                    child.setParent(None)
                    self.gridLayout_7.removeWidget(child)
                    child.deleteLater()
                    showIndAtt(data, dateMonth,self.gridLayout_7)

                else:
                    showIndAtt(data, dateMonth, self.gridLayout_7)







