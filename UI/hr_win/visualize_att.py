# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visualize_att.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(942, 569)
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.widget_2.setFont(font)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
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
        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
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
        self.gridLayout_2.addWidget(self.pushButton, 0, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
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
        self.gridLayout_2.addWidget(self.pushButton_2, 0, 3, 1, 1)
        self.verticalLayout.addWidget(self.widget_2)
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
        self.startdate = QtWidgets.QDateEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.startdate.setFont(font)
        self.startdate.setStyleSheet("QDateEdit{\n"
"    border-radius:5px;\n"
"    border:1px groove gray;    \n"
"    border-style:outset;\n"
"}")
        self.startdate.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(1752, 9, 14), QtCore.QTime(0, 0, 0)))
        self.startdate.setCalendarPopup(True)
        self.startdate.setObjectName("startdate")
        self.gridLayout.addWidget(self.startdate, 3, 5, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 6, 1, 1)
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
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 3, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 4, 1, 1)
        self.enddate = QtWidgets.QDateEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.enddate.setFont(font)
        self.enddate.setStyleSheet("QDateEdit{\n"
"    border-radius:5px;\n"
"    border:1px groove gray;    \n"
"    border-style:outset;\n"
"}")
        self.enddate.setAccelerated(False)
        self.enddate.setCalendarPopup(True)
        self.enddate.setCurrentSectionIndex(0)
        self.enddate.setObjectName("enddate")
        self.gridLayout.addWidget(self.enddate, 3, 7, 1, 1)
        self.verticalLayout.addWidget(self.widget)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout.addLayout(self.gridLayout_4)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.startdate.dateChanged['QDate'].connect(self.enddate.setDate) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "手机号码"))
        self.pushButton.setText(_translate("Form", "查询"))
        self.pushButton_2.setText(_translate("Form", "重置"))
        self.startdate.setDisplayFormat(_translate("Form", "yyyy-M-d"))
        self.label_5.setText(_translate("Form", "至"))
        self.label_2.setText(_translate("Form", "部门"))
        self.comboBox.setItemText(0, _translate("Form", "全部"))
        self.comboBox.setItemText(1, _translate("Form", "财务部"))
        self.comboBox.setItemText(2, _translate("Form", "工程部"))
        self.comboBox.setItemText(3, _translate("Form", "项目部"))
        self.comboBox.setItemText(4, _translate("Form", "设计部"))
        self.comboBox.setItemText(5, _translate("Form", "秘书部"))
        self.label_3.setText(_translate("Form", "申请日期"))
        self.enddate.setDisplayFormat(_translate("Form", "yyyy-M-d"))
