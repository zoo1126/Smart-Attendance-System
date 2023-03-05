# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Atd_record.ui'
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
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 2, 1, 1)
        self.startdate = QtWidgets.QDateEdit(self.widget)
        self.startdate.setDisplayFormat('yyyy-MM')
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
        self.gridLayout.addWidget(self.startdate, 3, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 4, 1, 1)
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
        self.enddate.setDisplayFormat('yyyy-MM')
        self.gridLayout.addWidget(self.enddate, 3, 5, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 6, 1, 1)
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
        self.label_3.setText(_translate("Form", "申请日期"))
        self.startdate.setDisplayFormat(_translate("Form", "yyyy-M-d"))
        self.label_5.setText(_translate("Form", "至"))
        self.enddate.setDisplayFormat(_translate("Form", "yyyy-M-d"))
        self.pushButton.setText(_translate("Form", "确定"))