# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'staff_message2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(856, 627)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 500, 111, 41))
        self.pushButton_2.setStyleSheet("background-color:orange;\n"
"    color:white;\n"
"border:0px;\n"
"border-radius:8px;\n"
"\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(260, 500, 111, 41))
        self.pushButton.setStyleSheet("background-color:green;\n"
"    color:white;\n"
"border:0px;\n"
"border-radius:8px;\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(110, 40, 641, 431))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 13, 3, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 5, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 13, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 15, 0, 1, 2)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(11)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 9, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 9, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 13, 4, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color:blue")
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 7, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 8, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 11, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 14, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 13, 0, 1, 1)
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(188)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateTimeEdit_2.sizePolicy().hasHeightForWidth())
        self.dateTimeEdit_2.setSizePolicy(sizePolicy)
        self.dateTimeEdit_2.setMinimumSize(QtCore.QSize(154, 0))
        self.dateTimeEdit_2.setCalendarPopup(True)
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.gridLayout.addWidget(self.dateTimeEdit_2, 13, 5, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 5, 1, 1, 1)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.layoutWidget)
        self.dateTimeEdit.setMinimumSize(QtCore.QSize(188, 0))
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout.addWidget(self.dateTimeEdit, 13, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 6, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 12, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem7, 10, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 11, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem8, 4, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 16, 0, 1, 6)

        self.retranslateUi(Form)
        # self.pushButton_2.clicked.connect(Form.cancelSlot)
        self.pushButton.clicked.connect(Form.submitSlot)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_2.setText(_translate("Form", "取消"))
        self.pushButton.setText(_translate("Form", "申请"))
        self.label_7.setText(_translate("Form", "至"))
        self.label_9.setText(_translate("Form", "姓  名："))
        self.label_2.setText(_translate("Form", "01758951"))
        self.label_8.setText(_translate("Form", "外勤工作详细："))
        self.label_14.setText(_translate("Form", "2022-1-1 10：00"))
        self.label_13.setText(_translate("Form", "申请时间："))
        self.label_11.setText(_translate("Form", "外勤"))
        self.label_12.setText(_translate("Form", "外勤地点："))
        self.label_6.setText(_translate("Form", "申请事项："))
        self.label_5.setText(_translate("Form", "外勤时间："))
        self.label.setText(_translate("Form", "1712190520"))
        self.label_10.setText(_translate("Form", "张三"))
        self.label_4.setText(_translate("Form", "公司编号："))
        self.label_3.setText(_translate("Form", "员工编号："))
