# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'staff_updatePhone.ui'
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
        Form.resize(560, 405)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(312, 280, 111, 41))
        self.pushButton_2.setStyleSheet("background-color:orange;\n"
"    color:white;\n"
"border:0px;\n"
"border-radius:8px;\n"
"\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(122, 280, 111, 41))
        self.pushButton.setStyleSheet("background-color:green;\n"
"    color:white;\n"
"border:0px;\n"
"border-radius:8px;\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(110, 70, 341, 191))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 6, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
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
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setStyleSheet("border:1px solid #ccc;\n"
"border-radius:4px;\n"
"color:#555;\n"
"padding: 6px 12px;\n"
"")
        self.lineEdit_3.setInputMask("")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_3.setClearButtonEnabled(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 5, 1, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setStyleSheet("border:1px solid #ccc;\n"
"border-radius:4px;\n"
"color:#555;\n"
"padding: 6px 12px;\n"
"")
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 2)
        self.warninglabel = QtWidgets.QLabel(self.layoutWidget)
        self.warninglabel.setStyleSheet("color:red\n"
"")
        self.warninglabel.setObjectName("warninglabel")
        self.gridLayout.addWidget(self.warninglabel, 4, 1, 1, 2)
        self.warninglabel_2 = QtWidgets.QLabel(self.layoutWidget)
        self.warninglabel_2.setStyleSheet("color:red\n"
"")
        self.warninglabel_2.setObjectName("warninglabel_2")
        self.gridLayout.addWidget(self.warninglabel_2, 6, 1, 1, 2)

        self.warninglabel.hide()
        self.warninglabel_2.hide()

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.updateSlot)
        self.lineEdit_2.editingFinished.connect(Form.checkNPhone)
        self.lineEdit_3.editingFinished.connect(Form.checkNPPhone)
        self.pushButton_2.clicked.connect(Form.closeSlot)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_2.setText(_translate("Form", "取消"))
        self.pushButton.setText(_translate("Form", "修改"))
        self.label_4.setText(_translate("Form", "新账号："))
        self.label_3.setText(_translate("Form", "原账号："))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "重新输入新手机号"))
        self.label_5.setText(_translate("Form", "确认账号："))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "请输入新手机号"))
        self.warninglabel.setText(_translate("Form", "*手机号长度11位！"))
        self.warninglabel_2.setText(_translate("Form", "*两次输入不一致！"))

    def checkNPhone(self):
        phone = self.lineEdit_2.text()
        if len(phone) == 0:
            self.warninglabel.setText("*账号不得为空！")
            self.warninglabel.show()

        else:
            ret = re.match(r"^1[35678]\d{9}$", phone)
            if ret == None:
                self.warninglabel.setText("*请输入正确格式的手机号！")
                self.warninglabel.show()
            else:
                self.warninglabel.hide()


    def checkNPPhone(self):
        phone = self.lineEdit_2.text()
        rephone = self.lineEdit_3.text()
        if len(rephone) == 0:
            self.warninglabel_2.setText("*重新输入不得为空！")
            self.warninglabel_2.show()

        else:
            if phone and rephone and phone != rephone:
                self.warninglabel_2.setText("*两次输入手机号不一致！")
                self.warninglabel_2.show()

            else:
                self.warninglabel_2.hide()
