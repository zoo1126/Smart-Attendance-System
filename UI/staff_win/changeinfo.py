# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'changeinfo.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(866, 639)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 490, 111, 41))
        self.pushButton_2.setStyleSheet("background-color:orange;\n"
"    color:white;\n"
"border:0px;\n"
"border-radius:8px;\n"
"\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(280, 490, 111, 41))
        self.pushButton.setStyleSheet("background-color:green;\n"
"    color:white;\n"
"border:0px;\n"
"border-radius:8px;\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(90, 110, 681, 341))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 4, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 8, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_6.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_6.setStyleSheet("border:1px solid #ccc;\n"
"border-radius:4px;\n"
"color:#555;\n"
"padding: 6px 12px;\n"
"")
        self.lineEdit_6.setInputMask("")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_6.setClearButtonEnabled(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 10, 1, 1, 6)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_4.setTabletTracking(False)
        self.lineEdit_4.setStyleSheet(" border:1px solid #ccc;\n"
" border-radius:4px;\n"
" color:#555;\n"
" padding: 6px 12px;\n"
"")
        self.lineEdit_4.setInputMask("")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setFrame(True)
        self.lineEdit_4.setDragEnabled(False)
        self.lineEdit_4.setClearButtonEnabled(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 6, 1, 1, 3)
        self.label_12 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 10, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 2, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 2, 5, 1, 2)
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setMinimumSize(QtCore.QSize(140, 0))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 5, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setStyleSheet("background: transparent;\n"
"color:green")
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 4, 6, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 2, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 2, 1, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 6, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 5)
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 8, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.widget)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 8, 1, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(250, 40))
        self.lineEdit_5.setStyleSheet("border:1px solid #ccc;\n"
"border-radius:4px;\n"
"color:#555;\n"
"padding: 6px 12px;\n"
"")
        self.lineEdit_5.setInputMask("")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_5.setClearButtonEnabled(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 6, 5, 1, 2)
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 5, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 9, 0, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout.addWidget(self.radioButton_3, 8, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 7, 0, 1, 1)

        self.retranslateUi(Form)
        # self.pushButton_2.clicked.connect(Form.cancelSlot)
        self.pushButton.clicked.connect(Form.updateSlot)
        self.pushButton_3.clicked.connect(Form.openUPSlot)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_2.setText(_translate("Form", "取消"))
        self.pushButton.setText(_translate("Form", "更新"))
        self.label_5.setText(_translate("Form", "手机号："))
        self.label_7.setText(_translate("Form", "性  别："))
        # self.lineEdit_6.setPlaceholderText(_translate("Form", "文惠人才公寓10A"))
        # self.lineEdit_4.setPlaceholderText(_translate("Form", "张三"))
        self.label_12.setText(_translate("Form", "联系地址："))
        self.label_13.setText(_translate("Form", "职   位："))
        self.label_4.setText(_translate("Form", "公司名称："))
        self.label_14.setText(_translate("Form", "普通职员"))
        # self.label_9.setText(_translate("Form", "18758598172"))
        self.pushButton_3.setText(_translate("Form", "修改账号"))
        self.label_15.setText(_translate("Form", "所在部门："))
        # self.label_16.setText(_translate("Form", "财务部"))
        self.label_8.setText(_translate("Form", "邮  箱："))
        # self.label_2.setText(_translate("Form", "东南科技有限公司"))
        self.radioButton_2.setText(_translate("Form", "女"))
        self.radioButton.setText(_translate("Form", "男"))
        # self.lineEdit_5.setPlaceholderText(_translate("Form", "124343@qq.com"))
        # self.label.setText(_translate("Form", "1712190520"))
        self.label_3.setText(_translate("Form", "员工编号："))
        self.label_6.setText(_translate("Form", "姓  名："))
        self.radioButton_3.setText(_translate("Form", "未知"))
