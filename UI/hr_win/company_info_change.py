# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'company_info_change.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListView


class Ui_Form(object):
    def setupUi(self, company_info_change):
        company_info_change.setObjectName("company_info_change")
        company_info_change.resize(792, 569)
        self.formWidget = QtWidgets.QWidget(company_info_change)
        self.formWidget.setGeometry(QtCore.QRect(-40, -20, 861, 621))
        self.formWidget.setObjectName("formWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formWidget)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setContentsMargins(20, 50, 20, 50)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(25)
        self.formLayout.setObjectName("formLayout")
        self.name_label = QtWidgets.QLabel(self.formWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.name_label)
        self.name = QtWidgets.QLineEdit(self.formWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.name.setFont(font)
        self.name.setClearButtonEnabled(True)
        self.name.setObjectName("name")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.name)
        self.id_label = QtWidgets.QLabel(self.formWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.id_label.setFont(font)
        self.id_label.setObjectName("id_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.id_label)
        self.id = QtWidgets.QLineEdit(self.formWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.id.setFont(font)
        self.id.setClearButtonEnabled(True)
        self.id.setObjectName("id")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.id)
        self.location_label = QtWidgets.QLabel(self.formWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.location_label.setFont(font)
        self.location_label.setObjectName("location_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.location_label)
        self.location = QtWidgets.QLineEdit(self.formWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.location.setFont(font)
        self.location.setClearButtonEnabled(True)
        self.location.setObjectName("location")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.location)
        self.phone_label = QtWidgets.QLabel(self.formWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.phone_label.setFont(font)
        self.phone_label.setObjectName("phone_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.phone_label)
        self.phone = QtWidgets.QLineEdit(self.formWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.phone.setFont(font)
        self.phone.setClearButtonEnabled(True)
        self.phone.setObjectName("phone")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.phone)
        self.type_label = QtWidgets.QLabel(self.formWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.type_label.setFont(font)
        self.type_label.setObjectName("type_label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.type_label)
        self.type = QtWidgets.QComboBox(self.formWidget)
        self.type.setView(QListView())
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.type.setFont(font)
        self.type.setObjectName("type")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.type)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.formWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.buttonBox.setFont(font)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.buttonBox)
        self.delete_button = QtWidgets.QPushButton(self.formWidget)
        self.delete_button.setObjectName("delete_button")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.delete_button)

        self.retranslateUi(company_info_change)
        self.type.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(company_info_change)

    def retranslateUi(self, company_info_change):
        _translate = QtCore.QCoreApplication.translate
        company_info_change.setWindowTitle(_translate("company_info_change", "Form"))
        self.name_label.setText(_translate("company_info_change", "<html><head/><body><p><span style=\" color:#d45814;\">* </span><span style=\" color:#202022;\">公司名称</span></p></body></html>"))
        self.id_label.setText(_translate("company_info_change", "<html><head/><body><p><span style=\" color:#d45814;\">* </span><span style=\" color:#202022;\">公司备案号</span></p></body></html>"))
        self.location_label.setText(_translate("company_info_change", "公司地址"))
        self.location.setPlaceholderText(_translate("company_info_change", "详细地址..."))
        self.phone_label.setText(_translate("company_info_change", "联系电话"))
        self.type_label.setText(_translate("company_info_change", "<html><head/><body><p><span style=\" color:#d45814;\">* </span><span style=\" color:#202022;\">公司类型</span></p></body></html>"))
        self.type.setItemText(0, _translate("company_info_change", "农、林、牧、渔业"))
        self.type.setItemText(1, _translate("company_info_change", "采矿业"))
        self.type.setItemText(2, _translate("company_info_change", "制造业"))
        self.type.setItemText(3, _translate("company_info_change", "电力、燃气及水的生产和供应业"))
        self.type.setItemText(4, _translate("company_info_change", "建筑业"))
        self.type.setItemText(5, _translate("company_info_change", "交通运输、仓储和邮政业"))
        self.type.setItemText(6, _translate("company_info_change", "信息传输、计算机服务和软件业"))
        self.type.setItemText(7, _translate("company_info_change", "批发和零售业"))
        self.type.setItemText(8, _translate("company_info_change", "住宿和餐饮业"))
        self.type.setItemText(9, _translate("company_info_change", "金融业"))
        self.type.setItemText(10, _translate("company_info_change", "房地产业"))
        self.type.setItemText(11, _translate("company_info_change", "租赁和商务服务业"))
        self.type.setItemText(12, _translate("company_info_change", "科学研究、技术服务和地质勘查业"))
        self.type.setItemText(13, _translate("company_info_change", "水利、环境和公共设施管理业"))
        self.type.setItemText(14, _translate("company_info_change", "居民服务和其他服务业"))
        self.type.setItemText(15, _translate("company_info_change", "教育"))
        self.type.setItemText(16, _translate("company_info_change", "卫生、社会保障和社会福利业"))
        self.type.setItemText(17, _translate("company_info_change", "文化、体育和娱乐业"))
        self.delete_button.setText(_translate("company_info_change", "注销公司"))
