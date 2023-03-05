# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'staff_apply.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from sql.company import *
from sql.staff_management import *
from sql.staff_sql import *
from PyQt5.QtCore import QTimer,QDateTime
from PyQt5.QtGui import QValidator,QRegExpValidator
from PyQt5.QtCore import QRegExp
from PyQt5.QtWidgets import QMessageBox

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(633, 542)
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        self.gridLayout_3.addWidget(self.tableWidget, 1, 0, 1, 1)

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
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
        self.label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"    border-radius:5px;\n"
"    border:1px groove gray;    \n"
"    border-style:outset;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 3, 1, 1, 1)
        reg = QRegExp('[1][35678][0-9]{9}$')
        vali = QRegExpValidator(self)
        vali.setRegExp(reg)
        self.lineEdit.setValidator(vali)
        self.label_2 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 2, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.widget)
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
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 3, 3, 1, 1)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet("QDateEdit{\n"
"    border-radius:5px;\n"
"    border:1px groove gray;    \n"
"    border-style:outset;\n"
"}")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QtCore.QDate.currentDate())
        self.dateEdit.lineEdit().setVisible(False)
        self.dateEdit.dateChanged.connect(self.onDateChanged)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout_2.addWidget(self.dateEdit, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
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
        self.gridLayout_2.addWidget(self.pushButton, 0, 2, 1, 1)
        self.pushButton.clicked.connect(self.searchstaffapply)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
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
        self.gridLayout_2.addWidget(self.pushButton_2, 0, 3, 1, 1)

        self.pushButton_3 = QtWidgets.QPushButton(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
                                        "    background-color:RoyalBlue;\n"
                                        "    color:white;\n"
                                        "    border-radius:8px;\n"
                                        "    border:2px groove gray;\n"
                                        "    border-style:outset;\n"
                                        "}")
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 0, 4, 1, 1)
        self.pushButton_2.clicked.connect(self.resetSelection)
        self.pushButton_3.clicked.connect(self.showAllStaffManagement_table)
        self.verticalLayout.addWidget(self.widget_2)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "操作"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "申请编号"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "申请人手机号"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "公司统一信用代码"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "申请类型"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "处理状态"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "申请时间"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "处理时间"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Form", "处理人工号"))

        self.label.setText(_translate("Form", "手机号码"))
        self.label_2.setText(_translate("Form", "申请状态"))
        self.comboBox.setItemText(0, _translate("Form", "全部"))
        self.comboBox.setItemText(1, _translate("Form", "未处理"))
        self.comboBox.setItemText(2, _translate("Form", "已同意"))
        self.comboBox.setItemText(3, _translate("Form", "已拒绝"))
        self.label_3.setText(_translate("Form", "申请日期"))
        self.dateEdit.setDisplayFormat(_translate("Form", "yyyy-M-d"))
        self.pushButton.setText(_translate("Form", "搜索"))
        self.pushButton_2.setText(_translate("Form", "重置"))
        self.pushButton_3.setText(_translate("Form", "显示全部内容"))

    def sethr_phone(self, hr_phone):
        self.hr_phone = hr_phone

    def gethr_phone(self):
        return self.hr_phone

    def sethr_id(self, hr_id):
        self.hr_id = hr_id

    def gethr_id(self):
        return self.hr_id

    def getcom_id(self):
        return findCom_idbyhr_id(self.hr_phone)[0][0]


    def onDateChanged(self):
        self.dateEdit.lineEdit().setVisible(True)





    def gettablewidget(self):
        return self.tableWidget

    def showAllStaffManagement_table(self):
        com_id = self.getcom_id()
        print(com_id)

        dep_list = allStaffManagementFind(com_id)
        self.tableWidget.setRowCount(len(dep_list))
        print(len(dep_list))
        x = 0

        for onedep in dep_list:

            for y in range(len(onedep)):
                if y==3:
                    if str(onedep[y])=='0':
                        item = QtWidgets.QTableWidgetItem('申请入职')
                    else :
                        item = QtWidgets.QTableWidgetItem('离职')

                elif y==4:
                    if str(onedep[y])=='0':
                        item = QtWidgets.QTableWidgetItem('未处理')
                        self.tableWidget.setCellWidget(x, 0, self.buttonForRow(False))
                    elif str(onedep[y])=='1':
                        item = QtWidgets.QTableWidgetItem('已同意')
                        self.tableWidget.setCellWidget(x, 0, self.buttonForRow(True))
                    elif str(onedep[y])=='2':
                        item = QtWidgets.QTableWidgetItem('已拒绝')
                        self.tableWidget.setCellWidget(x, 0, self.buttonForRow(True))
                    else:
                        item = QtWidgets.QTableWidgetItem('出错')
                        self.tableWidget.setCellWidget(x, 0, self.buttonForRow(True))
                else:
                    if onedep[y] is not None:
                        item=QtWidgets.QTableWidgetItem(str(onedep[y]))
                    else:
                        item = QtWidgets.QTableWidgetItem(None)
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(x, y + 1, item)
            x = x + 1


    def buttonForRow(self,iscope):
        widget = QtWidgets.QWidget()
        hLayout = QtWidgets.QHBoxLayout()
        # 修改
        if not iscope:
            self.agreeBtn = QtWidgets.QPushButton('同意')
            self.agreeBtn.setStyleSheet(''' text-align : center;
                                                  background-color : green;
                                                  height : 30px;
                                                  border-style: outset;
                                                  font : 13px  ''')
            self.agreeBtn.clicked.connect(self.AgreeButton)
            # 删除
            self.refuseBtn = QtWidgets.QPushButton('拒绝')
            self.refuseBtn.setStyleSheet(''' text-align : center;
                                            background-color : orange;
                                            height : 30px;
                                            border-style: outset;
                                            font : 13px; ''')

            self.refuseBtn.clicked.connect(self.RefuseButton)
            hLayout.addWidget(self.agreeBtn)
            hLayout.addWidget(self.refuseBtn)
        self.deleteBtn = QtWidgets.QPushButton('移除')
        self.deleteBtn.setStyleSheet(''' text-align : center;
                                                            background-color : LightCoral;
                                                            height : 30px;
                                                            border-style: outset;
                                                            font : 13px; ''')

        self.deleteBtn.clicked.connect(self.DeleteButton)

        hLayout.addWidget(self.deleteBtn)
        hLayout.setContentsMargins(2, 2, 2, 2)

        widget.setLayout(hLayout)
        return widget

    def AgreeButton(self):
        button = self.sender()
        if button:
            # 确定位置的时候这里是关键
            row = self.tableWidget.indexAt(button.parent().pos()).row()
            time = QDateTime.currentDateTime()  # 获取现在的时间
            currenttime = time.toString('yyyy-MM-dd hh:mm:ss')  # 设置显示时间的格式

            sign1=updateStaffManagementwithcom(self.getcom_id(),self.tableWidget.item(row,2).text(),1, currenttime, self.gethr_id(), self.tableWidget.item(row,1).text())

            if sign1:
                onedep=staffManagementFindex(self.tableWidget.item(row,1).text())
                for y in range(len(onedep)):
                    if y == 3:
                        if str(onedep[y]) == '0':
                            item = QtWidgets.QTableWidgetItem('申请入职')
                        else:
                            item = QtWidgets.QTableWidgetItem('离职')
                    elif y == 4:
                        if str(onedep[y]) == '0':
                            item = QtWidgets.QTableWidgetItem('未处理')
                            self.tableWidget.setCellWidget(row, 0, self.buttonForRow(False))
                        elif str(onedep[y]) == '1':
                            item = QtWidgets.QTableWidgetItem('已同意')
                            self.tableWidget.setCellWidget(row, 0, self.buttonForRow(True))
                        elif str(onedep[y]) == '2':
                            item = QtWidgets.QTableWidgetItem('已拒绝')
                            self.tableWidget.setCellWidget(row, 0, self.buttonForRow(True))
                        else:
                            item = QtWidgets.QTableWidgetItem('出错')
                            self.tableWidget.setCellWidget(row, 0, self.buttonForRow(True))
                    else:
                        item = QtWidgets.QTableWidgetItem(str(onedep[y]))
                    item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                    self.tableWidget.setItem(row, y + 1, item)
            else:
                QMessageBox.warning(self,'失败','该员工申请同意失败!',QMessageBox.Yes)

                
    def RefuseButton(self):
        button = self.sender()
        if button:
            # 确定位置的时候这里是关键
            row = self.tableWidget.indexAt(button.parent().pos()).row()
            time = QDateTime.currentDateTime()  # 获取现在的时间
            currenttime = time.toString('yyyy-MM-dd hh:mm:ss')  # 设置显示时间的格式
            sign1 = updateStaffManagement(2, currenttime, self.gethr_id(), self.tableWidget.item(row, 1).text())
            if sign1:
                onedep = staffManagementFindex(self.tableWidget.item(row, 1).text())
                for y in range(len(onedep)):
                    if y == 3:
                        if str(onedep[y]) == '0':
                            item = QtWidgets.QTableWidgetItem('申请入职')
                        else:
                            item = QtWidgets.QTableWidgetItem('离职')

                    elif y == 4:
                        if str(onedep[y]) == '0':
                            item = QtWidgets.QTableWidgetItem('未处理')
                            self.tableWidget.setCellWidget(row, 0, self.buttonForRow(False))
                        elif str(onedep[y]) == '1':
                            item = QtWidgets.QTableWidgetItem('已同意')
                            self.tableWidget.setCellWidget(row, 0, self.buttonForRow(True))
                        elif str(onedep[y]) == '2':
                            item = QtWidgets.QTableWidgetItem('已拒绝')
                            self.tableWidget.setCellWidget(row, 0, self.buttonForRow(True))
                        else:
                            item = QtWidgets.QTableWidgetItem('出错')
                            self.tableWidget.setCellWidget(row, 0, self.buttonForRow(True))
                    else:
                        item = QtWidgets.QTableWidgetItem(str(onedep[y]))
                    item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                    self.tableWidget.setItem(row, y + 1, item)
            else:
                QMessageBox.warning(self,'失败','该员工申请拒绝失败！',QMessageBox.Yes)


    def DeleteButton(self):
        button = self.sender()
        if button:
            # 确定位置的时候这里是关键
            res = QMessageBox.question(self, '移除', '确定移除该条记录吗？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if res == QMessageBox.No:
                return
            row = self.tableWidget.indexAt(button.parent().pos()).row()
            res = deleteStaffManagement(self.tableWidget.item(row,1).text())
            print(res)
            if res:
                self.tableWidget.removeRow(row)
            else:
                print("error delete")

    def resetSelection(self):
        self.lineEdit.clear()
        self.dateEdit.setDate(QtCore.QDate.currentDate())
        self.dateEdit.lineEdit().setVisible(False)
        self.comboBox.setCurrentIndex(0)

    def searchstaffapply(self):
        com_id=self.getcom_id()
        phone_flag=state_flag=date_flag=False
        phone=self.lineEdit.text()
        if phone is None or len(phone)==0:
            phone_flag=False
            print("非精确搜索")
        else:
            phone_flag=True
        state_txt=self.comboBox.currentText()
        if state_txt=='全部':
            state = -1
            state_flag=False
        elif state_txt == '未处理':
            state = 0
            state_flag=True
        elif state_txt == '已同意':
            state = 1
            state_flag = True
        elif state_txt == '已拒绝':
            state = 2
            state_flag = True
        else:
            print("error")
            return
        print(state)
        if self.dateEdit.lineEdit().isVisible():

            date=self.dateEdit.date().toString('yyyy-MM-dd')
            print(date)
            date_flag=True
        else:
            date_flag=False
        if phone_flag and state_flag and date_flag:
            dep_list = staffManagementFindbyDate_and_Phone_and_State(com_id,date,phone,state)
            print("手机和日期和状态精确搜索")
            self.showSelectedApply(dep_list)
        elif phone_flag and date_flag and not state_flag:
            dep_list=staffManagementFindbyDate_and_Phone(com_id,date,phone)
            print("手机日期精确搜索")
            self.showSelectedApply(dep_list)
        elif phone_flag and  not date_flag and state_flag:
            dep_list=staffManagementFindbyState_and_Phone(com_id,phone,state)
            print("手机状态精确搜索")
            self.showSelectedApply(dep_list)
        elif  not phone_flag and date_flag and state_flag:
            dep_list=staffManagementFindbyDate_and_State(com_id,date,state)
            print("状态日期精确搜索")
            self.showSelectedApply(dep_list)
        elif  not phone_flag and not date_flag and state_flag:
            dep_list=staffManagementFindbyState(com_id,state)
            print("状态精确搜索")
            self.showSelectedApply(dep_list)
        elif  not phone_flag and date_flag and not state_flag:
            dep_list=staffManagementFindbyDate(com_id,date)
            print("日期精确搜索")
            self.showSelectedApply(dep_list)
        elif  phone_flag and not date_flag and not state_flag:
            dep_list=staffManagementFindbyPhone(com_id,phone)
            print("手机精确搜索")
            self.showSelectedApply(dep_list)
        else:
            self.showAllStaffManagement_table()



    def showSelectedApply(self,dep_list):
        self.tableWidget.setRowCount(len(dep_list))
        print(len(dep_list))
        x = 0

        for onedep in dep_list:

            for y in range(len(onedep)):
                if y==3:
                    if str(onedep[y])=='0':
                        item = QtWidgets.QTableWidgetItem('申请入职')
                    else :
                        item = QtWidgets.QTableWidgetItem('离职')

                elif y==4:
                    if str(onedep[y])=='0':
                        item = QtWidgets.QTableWidgetItem('未处理')
                        self.tableWidget.setCellWidget(x, 0, self.buttonForRow(False))
                    elif str(onedep[y])=='1':
                        item = QtWidgets.QTableWidgetItem('已同意')
                        self.tableWidget.setCellWidget(x, 0, self.buttonForRow(True))
                    elif str(onedep[y])=='2':
                        item = QtWidgets.QTableWidgetItem('已拒绝')
                        self.tableWidget.setCellWidget(x, 0, self.buttonForRow(True))
                    else:
                        item = QtWidgets.QTableWidgetItem('出错')
                        self.tableWidget.setCellWidget(x, 0, self.buttonForRow(True))
                else:
                    if onedep[y] is not None:
                        item=QtWidgets.QTableWidgetItem(str(onedep[y]))
                    else:
                        item = QtWidgets.QTableWidgetItem(None)
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(x, y + 1, item)
            x = x + 1