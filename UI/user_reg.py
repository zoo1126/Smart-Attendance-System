# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_reg.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import re

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(990, 634)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 30, 281, 71))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(360, 120, 151, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 460, 111, 41))
        self.pushButton_2.setStyleSheet("background-color:orange;\n"
"    color:white;\n"
"border:0px;\n"
"border-radius:8px;\n"
"\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(310, 460, 111, 41))
        self.pushButton.setStyleSheet("background-color:green;\n"
"    color:white;\n"
"border:0px;\n"
"border-radius:8px;\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(280, 200, 381, 231))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setStyleSheet("border:1px solid #ccc;\n"
"border-radius:4px;\n"
"color:#555;\n"
"padding: 6px 12px;\n"
"")
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 2)
        self.radioButton_2 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 4, 2, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setStyleSheet("border:1px solid #ccc;\n"
"border-radius:4px;\n"
"color:#555;\n"
"padding: 6px 12px;\n"
"")
        self.lineEdit_3.setInputMask("")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setClearButtonEnabled(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 3, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton.setStyleSheet("")
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 4, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setTabletTracking(False)
        self.lineEdit.setStyleSheet(" border:1px solid #ccc;\n"
" border-radius:4px;\n"
" color:#555;\n"
" padding: 6px 12px;\n"
"")
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setFrame(True)
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.warninglabel = QtWidgets.QLabel(Form)
        self.warninglabel.setGeometry(QtCore.QRect(670, 230, 218, 15))
        self.warninglabel.setMaximumSize(QtCore.QSize(16777215, 20))
        self.warninglabel.setStyleSheet("color:red\n"
"")
        self.warninglabel.setObjectName("warninglabel")
        self.warninglabel_2 = QtWidgets.QLabel(Form)
        self.warninglabel_2.setGeometry(QtCore.QRect(670, 280, 218, 20))
        self.warninglabel_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.warninglabel_2.setStyleSheet("color:red\n"
"")
        self.warninglabel_2.setObjectName("warninglabel_2")
        self.warninglabel_3 = QtWidgets.QLabel(Form)
        self.warninglabel_3.setGeometry(QtCore.QRect(670, 340, 207, 20))
        self.warninglabel_3.setMaximumSize(QtCore.QSize(16777215, 20))
        self.warninglabel_3.setStyleSheet("color:red\n"
"")
        self.warninglabel_3.setObjectName("warninglabel_3")

        self.warninglabel.hide()
        self.warninglabel_2.hide()
        self.warninglabel_3.hide()

        self.retranslateUi(Form)
        self.pushButton_2.clicked.connect(Form.backSlot)
        self.pushButton.clicked.connect(Form.regSlot)
        self.lineEdit.editingFinished.connect(Form.checkPhone)
        self.lineEdit_2.editingFinished.connect(Form.checkPwd)
        self.lineEdit_3.editingFinished.connect(Form.checkPPwd)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "智慧考勤系统"))
        self.label_2.setText(_translate("Form", "欢迎使用"))
        self.pushButton_2.setText(_translate("Form", "取消"))
        self.pushButton.setText(_translate("Form", "注册"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "请输入密码"))
        self.radioButton_2.setText(_translate("Form", "HR"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "重新输入密码"))
        self.label_3.setText(_translate("Form", "账  号："))
        self.label_4.setText(_translate("Form", "密  码："))
        self.radioButton.setText(_translate("Form", "员工"))
        self.lineEdit.setPlaceholderText(_translate("Form", "请输入手机号"))
        self.label_6.setText(_translate("Form", "用户角色："))
        self.label_5.setText(_translate("Form", "确认密码："))
        self.warninglabel.setText(_translate("Form", "*手机号为11位"))
        self.warninglabel_2.setText(_translate("Form", "*密码必须包含大小写字母和数字"))
        self.warninglabel_3.setText(_translate("Form", "*两次密码输入不一致"))

    def checkPhone(self):
        phoneNum = self.PhoneNumInput.text()
        if len(phoneNum) != 11:
            self.warnLabel.show()
        else:
            self.warnLabel.hide()

    def checkPhone(self):
        phone = self.lineEdit.text()
        if len(phone) == 0:
            self.warninglabel.setText("*手机号不能为空！")
            self.warninglabel.show()
        else:
            ret = re.match(r"^1[35678]\d{9}$", phone)
            if ret == None:
                self.warninglabel.setText("*请输入正确格式的手机号")
                self.warninglabel.show()
            else:
                self.warninglabel.hide()

    def checkPwd(self):
        pwd = self.lineEdit_2.text()
        if len(pwd) == 0:
            self.warninglabel_2.setText("*密码不得为空！")
            self.warninglabel_2.show()
        else:
            ret = re.match("^(?:(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])).*$", pwd)
            if ret == None:
                self.warninglabel_2.setText("*密码必须包含大小写字母和数字！")
                self.warninglabel_2.show()
            else:
                self.warninglabel_2.hide()

    def checkPPwd(self):
        pwd = self.lineEdit_2.text()
        repwd = self.lineEdit_3.text()
        if len(repwd) == 0:
            self.warninglabel_3.setText("*密码不得为空！")
            self.warninglabel_3.show()

        else:
            if pwd and repwd and pwd != repwd:
                self.warninglabel_3.setText("*两次输入密码不一致！")
                self.warninglabel_3.show()
            else:
                self.warninglabel_3.hide()
