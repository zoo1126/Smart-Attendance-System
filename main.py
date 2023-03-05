import os
import torch.nn.functional as F
import random
import uuid
import time
from ai_model.models.mtcnn import MTCNN
from ai_model.models.inception_resnet_v1 import InceptionResnetV1

import cv2
from PyQt5 import QtCore,Qt, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, Qt, QTimer, QDateTime
from PyQt5.QtWidgets import QLabel,QMessageBox, QWidget, QApplication,  QHeaderView,QMainWindow, QTableWidgetItem, QPushButton

from UI.staff_win.staff_mainwindow import Ui_MainWindow as staff_MainWindow
from UI.staff_win.CoLists import Ui_Form as CoLists
from UI.staff_win.Info_collection import Ui_Form as Info_collection
from UI.staff_win.Clock_in import Ui_Form as Clock_in
from UI.staff_win.Atd_record import Ui_Form as Atd_record
from UI.staff_win.staff_message1 import Ui_Form as Leave
from UI.staff_win.staff_message2 import Ui_Form as Outside
from UI.staff_win.staff_message3 import Ui_Form as Appeal
from UI.staff_win.staff_updatePhone import Ui_Form as update_s_phone
from UI.staff_win.staff_allmessage import Ui_Form as all_message
from UI.staff_win.changepass import Ui_Form as changepass
from UI.staff_win.changeinfo import Ui_Form as changeinfo
from UI.hr_win.hr_mainwindow import Ui_MainWindow as hr_MainWindow
from UI.hr_win.hr_updatePhone import Ui_Form as update_phone
from UI.hr_win.company_login import Ui_Form as company_login
from UI.hr_win.company_info_change import Ui_Form as company_info_change
from UI.hr_win.company_info_show import Ui_Form as company_info_show
from UI.hr_win.staff_apply import Ui_Form as staff_apply
from UI.hr_win.staff_message_management import Ui_Form as staff_message_management
from UI.hr_win.rest_apply import Ui_Form as rest_apply
from UI.hr_win.out_apply import Ui_Form as out_apply
from UI.hr_win.complain import Ui_Form as complain
from UI.hr_win.department import Ui_Form as department
from UI.hr_win.export_dailyAttendance import Ui_Form as export_att
from UI.hr_win.getdailyAttendance import Ui_Form as getdailyAtt
from UI.hr_win.hr_att_visual  import Ui_Form as attendance
from UI.hr_win.hr_updateinfo import Ui_Form as update_info
from UI.hr_win.hr_updatepwd import Ui_Form as update_pwd
from charts_to_UIForm.chartmain_py import chartPy as pyecharts
from charts_to_UIForm.vi_chart_to_calendar import chartPy as calendar
from charts_to_UIForm.vi_chart_to_calendar_staff import chartPy as Atd_record

import sys
from UI.welcomeWindow import Ui_WelcomeWin as welcomewin
from UI.loginWindow import Ui_LoginWin as loginwin
from UI.user_reg import Ui_Form as user_reg
from sql.login import *
from sql.company import *
from sql.reg import *
from sql.updateInfo import *
from sql.apply import *

GLOBAL_PHONE = '1'
staff = []
hr = []
signal = 1

class CommonHelper:
    def __init__(self):
        pass

    @staticmethod
    def readQss(style):
        with open(style, 'r') as f:
            return f.read()


# 注册页面
class NewUser_reg(QMainWindow, user_reg):
    def __init__(self, flag):
        super(NewUser_reg, self).__init__()
        self.setupUi(self)
        self.flag = flag
        self.loginWin = NewLoginWin(signal)

    # 注册信息槽
    def regSlot(self):

        phone = self.lineEdit.text()
        pwd = self.lineEdit_2.text()

        # 员工注册
        if self.radioButton.isChecked():
            ifExist = ifPhone(phone)
            if ifExist:
                QMessageBox.warning(self, "提示", "该用户名已存在", QMessageBox.Yes)
            else:
                result = userReg(phone, pwd, 1)
                if result:
                    QMessageBox.information(self, 'Successfully', '注册成功', QMessageBox.Yes)
                    welcomeWindow.show()
                    self.loginWin = NewLoginWin(signal)
                    self.loginWin.show()
                    self.close()
                else:
                    QMessageBox.warning(self, "警告", "注册失败，请重试", QMessageBox.Yes)

        # HR注册
        elif self.radioButton_2.isChecked():
            ifExist = ifPhone(phone)
            if ifExist:
                QMessageBox.warning(self, "提示", "该用户名已存在", QMessageBox.Yes)
            else:
                result = userReg(phone, pwd, 2)
                if result:
                    QMessageBox.information(self, 'Successfully', '注册成功', QMessageBox.Yes)
                    welcomeWindow.show()
                    self.loginWin = NewLoginWin(signal)
                    self.loginWin.show()
                    self.close()
                else:
                    QMessageBox.warning(self, "警告", "注册失败，请重试", QMessageBox.Yes)
        else:
            QMessageBox.warning(self, "提示", "请选择角色", QMessageBox.Yes)

    # 返回
    def backSlot(self):
        welcomeWindow.show()
        self.close()


# 登录页面
class NewLoginWin(QMainWindow, loginwin):
    def __init__(self, flag):
        super(NewLoginWin, self).__init__()
        self.setupUi(self)
        self.flag = flag
        self.setStyleSheet(style)

    def forgetPswSlot(self):
        #changepsw.show()
        self.close()

    def signupSlot(self):
        self.signupWin = NewUser_reg(signal)
        self.signupWin.show()
        self.close()

    def verifySlot(self):
        global GLOBAL_PHONE
        phoneNum = self.PhoneNumInput.text()
        pwd = self.PwdInput.text()
        if len(phoneNum) != 11 and len(pwd):
            self.warnLabel.show()
        else:
            # 账号检验
            result = staff_login(phoneNum, pwd)
            if result:
                global staff
                staff = list(result)
                GLOBAL_PHONE = phoneNum
                self.staffWin = StaffMainWindow(signal)
                self.staffWin.show()
                self.close()
                welcomeWindow.close()
            else:
                QMessageBox.warning(self, "警告", "登录失败，请重试", QMessageBox.Yes)

    def verifySlot_hr(self):
        global GLOBAL_PHONE
        phoneNum = self.PhoneNumInput.text()
        pwd = self.PwdInput.text()
        if len(phoneNum) != 11 and len(pwd):
            self.warnLabel.show()
        else:
            # 账号检验
            result = hr_login(phoneNum, pwd)
            if result:
                global hr
                GLOBAL_PHONE = phoneNum
                hr = list(result)
                print(hr)
                self.hrWin = MainForm(signal)
                self.hrWin.show()
                self.close()
                welcomeWindow.close()
            else:
                QMessageBox.warning(self, "警告", "登录失败，请重试", QMessageBox.Yes)


# 欢迎界面
class NewWelcomeWin(QMainWindow, welcomewin):
    def __init__(self):
        super(NewWelcomeWin, self).__init__()
        self.setupUi(self)
        # palette = QPalette()
        # pix = QPixmap("./background.jpg")
        # pix = pix.scaled(self.widget.width(), self.widget.height())
        # palette.setBrush(QPalette.Background, QBrush(pix))
        # self.widget.setPalette(palette)

    def signupSlot(self):
        self.signupWin = NewUser_reg(signal)
        self.signupWin.show()
        welcomeWindow.hide()


    def loginSlot(self):
        self.loginWin = NewLoginWin(signal)
        self.loginWin.show()


# HR主界面
class MainForm(QtWidgets.QMainWindow, hr_MainWindow):
    def __init__(self, flag):
        super(MainForm, self).__init__()
        self.setupUi(self)
        self.statusShowTime()
        if len(hr) != 0:
            self.label_2.setText(hr[2] if hr[2] else "暂无")  # name
            self.label_3.setText(hr[0])  # phone
            self.label_4.setText(hr[1] if hr[1] else "暂无")  # id
        self.flag = flag
        self.listWidget.itemClicked.connect(self.companymanagement)
        self.listWidget_2.itemClicked.connect(self.staffmanagement)
        self.listWidget_3.itemClicked.connect(self.askmanagement)
        self.listWidget_4.itemClicked.connect(self.dailyAttmanagement)
        self.listWidget_5.itemClicked.connect(self.updatemanagement)
        if len(hr) != 0:
            if has_company(hr[0]):
                self.listWidget.item(0).setHidden(True)
            else:
                self.listWidget.item(1).setHidden(True)
                self.listWidget.item(2).setHidden(True)
                self.listWidget.item(3).setHidden(True)

    # 退出登录
    def exit(self):
        welcomeWindow.show()
        global hr
        hr = []
        self.close()

    def companymanagement(self):
        currentitem = self.listWidget.currentItem()
        if str(currentitem.text()) == "创建公司":
            if self.tabWidget.findChild(QWidget, "company_apply"):
                self.tabWidget.setCurrentWidget(self.tabWidget.findChild(QWidget, "company_apply"))
            else:
                self.child = ChildrenForm_company_apply(self)
                self.tabWidget.addTab(self.child, "创建公司")
                self.tabWidget.setCurrentWidget(self.child)
        elif str(currentitem.text()) == "编辑公司信息":
            if self.tabWidget.findChild(QWidget, "company_info_change"):
                self.tabWidget.setCurrentWidget(self.tabWidget.findChild(QWidget, "company_info_change"))
            else:
                self.child = ChildrenForm_company_info_change(self)
                self.tabWidget.addTab(self.child, "编辑公司信息")
                self.tabWidget.setCurrentWidget(self.child)
        elif str(currentitem.text()) == "查看公司信息":
            if self.tabWidget.findChild(QWidget, "company_info_show"):
                self.tabWidget.setCurrentWidget(self.tabWidget.findChild(QWidget, "company_info_show"))
            else:
                self.child = ChildrenForm_company_info_show(self)
                self.tabWidget.addTab(self.child, "查看公司信息")
                self.tabWidget.setCurrentWidget(self.child)
        elif str(currentitem.text()) == "部门管理":
            self.child = ChildrenForm_department()
            self.child.sethr_phone(str(self.label_3.text()))
            tablewidget = self.child.gettablewidget()
            #  showAlldepartment(com_id, tablewidget)
            if tablewidget is not None:
                self.child.showAlldepart_table()
            else:
                print("tablewidget为none")

            self.tabWidget.addTab(self.child, "部门管理")
            self.tabWidget.setCurrentWidget(self.child)

    def staffmanagement(self):
        currentitem = self.listWidget_2.currentItem()
        if str(currentitem.text()) == "员工申请管理":
            self.child = ChildrenForm_staff_apply()
            self.child.sethr_phone(str(self.label_3.text()))

            tablewidget = self.child.gettablewidget()
            #  showAlldepartment(com_id, tablewidget)
            if tablewidget is not None:

                self.child.sethr_id(self.label_4.text())
                self.child.showAllStaffManagement_table()
            else:
                print("tablewidget为none")

            self.tabWidget.addTab(self.child, "员工申请管理")
            self.tabWidget.setCurrentWidget(self.child)
        elif str(currentitem.text()) == "员工信息管理":
            self.child = ChildrenForm_staff_message_management()
            self.child.sethr_phone(str(self.label_3.text()))
            tablewidget = self.child.gettablewidget()
            #  showAlldepartment(com_id, tablewidget)

            if tablewidget is not None:
                self.child.sethr_id(self.label_4.text())
                self.child.showAllStaff_table()
            else:
                print("tablewidget为none")
            self.tabWidget.addTab(self.child, "员工信息管理")
            self.tabWidget.setCurrentWidget(self.child)

    def askmanagement(self):
        currentitem = self.listWidget_3.currentItem()
        if str(currentitem.text()) == "请假申请":
            self.child = ChildrenForm_rest_apply()
            self.child.sethr_phone(str(self.label_3.text()))
            tablewidget = self.child.gettablewidget()
            #  showAlldepartment(com_id, tablewidget)
            if tablewidget is not None:
                self.child.sethr_id(self.label_4.text())
                self.child.showAllrestapply_table()
            else:
                print("tablewidget为none")
            self.tabWidget.addTab(self.child, "请假申请")
            self.tabWidget.setCurrentWidget(self.child)
        elif str(currentitem.text()) == "外勤申请":
            self.child = ChildrenForm_out_apply()
            self.child.sethr_phone(str(self.label_3.text()))
            tablewidget = self.child.gettablewidget()
            #  showAlldepartment(com_id, tablewidget)
            if tablewidget is not None:
                self.child.sethr_id(self.label_4.text())
                self.child.showAlloutapply_table()
            else:
                print("tablewidget为none")
            self.tabWidget.addTab(self.child, "外勤申请")
            self.tabWidget.setCurrentWidget(self.child)
        elif str(currentitem.text()) == "申诉":
            self.child = ChildrenForm_complain()
            self.child.sethr_phone(str(self.label_3.text()))
            tablewidget = self.child.gettablewidget()
            #  showAlldepartment(com_id, tablewidget)
            if tablewidget is not None:
                self.child.sethr_id(self.label_4.text())
                self.child.showAllcomplainapply_table()
            else:
                print("tablewidget为none")
            self.tabWidget.addTab(self.child, "申诉")
            self.tabWidget.setCurrentWidget(self.child)

    def dailyAttmanagement(self):
        currentitem = self.listWidget_4.currentItem()
        if str(currentitem.text())=="考勤查询":
            self.child = ChildrenForm_getdailyAtt()
            self.child.sethr_phone(str(self.label_3.text()))
            tablewidget = self.child.gettablewidget()
            if tablewidget is not None:
                self.child.showAllattendance_table()
            else:
                print("tablewidget为none")
            self.tabWidget.addTab(self.child, "考勤查询")
            self.tabWidget.setCurrentWidget(self.child)
        elif str(currentitem.text())=="考勤可视化":
            self.child = ChildrenForm_attendance()
            self.child.sethr_phone(str(self.label_3.text()))
            self.child.showvisualization()
            self.tabWidget.addTab(self.child, "考勤可视化")
            self.tabWidget.setCurrentWidget(self.child)

    def updatemanagement(self):
        currentitem = self.listWidget_5.currentItem()
        if str(currentitem.text()) == "个人信息修改":
            self.child = ChildrenForm_updateinfo(self)
            self.tabWidget.addTab(self.child, "信息修改")
            self.tabWidget.setCurrentWidget(self.child)
        elif str(currentitem.text()) == "密码修改":
            self.child = ChildrenForm_updatepwd(self)
            self.tabWidget.addTab(self.child, "密码修改")
            self.tabWidget.setCurrentWidget(self.child)


class ChildrenForm_company_info_show(QtWidgets.QWidget, company_info_show):
    def __init__(self, MainForm):
        super(ChildrenForm_company_info_show, self).__init__()
        self.setupUi(self)
        self.setStyleSheet(style)
        self.MainForm = MainForm
        info = show_c_info(hr[0])
        if info:
            info = list(info)
            self.name.setText(info[2])
            self.id.setText(info[0])
            self.phone.setText(info[3])
            self.location.setText(info[5])
            self.type.setText(info[4])
        self.update_button.clicked.connect(self.updateC)

    def updateC(self):
        if self.MainForm.tabWidget.findChild(QWidget, "company_info_change"):
            self.MainForm.tabWidget.setCurrentWidget(self.MainForm.tabWidget.findChild(QWidget, "company_info_change"))
        else:
            self.MainForm.child = ChildrenForm_company_info_change()
            self.MainForm.tabWidget.addTab(self.MainForm.child, "编辑公司信息")
            self.MainForm.tabWidget.setCurrentWidget(self.MainForm.child)

class ChildrenForm_company_apply(QtWidgets.QWidget, company_login):
    def __init__(self, MainForm):
        super(ChildrenForm_company_apply, self).__init__()
        self.setupUi(self)
        self.setStyleSheet(style)
        self.MainForm = MainForm
        self.buttonBox.accepted.connect(self.newCompany)

    # 新建公司
    def newCompany(self):
        c_name = self.name.text()
        c_id = self.id.text()
        c_location = self.location.text()
        c_phone = self.phone.text()
        c_type = self.type.currentText()
        if c_name and c_id and c_type:
            if len(c_phone) != 11:
                QMessageBox.warning(self, "提示", "手机号应为11位", QMessageBox.Yes)
            elif new_company(c_name, c_id, c_location, c_phone, c_type, hr[0]):
                res = QMessageBox.information(self, "确认", "公司创建成功！后续部门创建可在部门管理页面中进行", QMessageBox.Yes)
                if res == QMessageBox.Yes:
                    self.MainForm.listWidget.item(0).setHidden(True)
                    self.MainForm.listWidget.item(1).setHidden(False)
                    self.MainForm.listWidget.item(2).setHidden(False)
                    self.MainForm.listWidget.item(3).setHidden(False)
                    self.MainForm.child = ChildrenForm_department()
                    self.MainForm.tabWidget.addTab(self.MainForm.child, "部门管理")
                    self.MainForm.tabWidget.setCurrentWidget(self.MainForm.child)
            else:
                QMessageBox.warning(self, "提示", "创建公司失败，请重试", QMessageBox.Yes)
        else:
            QMessageBox.warning(self, "提示", "必填项不应为空", QMessageBox.Yes)


class ChildrenForm_company_info_change(QtWidgets.QWidget, company_info_change):
    def __init__(self, MainForm):
        super(ChildrenForm_company_info_change, self).__init__()
        self.setupUi(self)
        self.setStyleSheet(style)
        self.MainForm = MainForm
        info = list(show_c_info(hr[0]))
        if info:
            self.name.setText(info[2])
            self.id.setText(info[0])
            self.phone.setText(info[3])
            self.location.setText(info[5])
            self.type.setCurrentText(info[4])
        self.buttonBox.accepted.connect(self.updateCompany)
        self.delete_button.clicked.connect(self.deleteCompany)

    def updateCompany(self):
        c_name = self.name.text()
        c_id = self.id.text()
        c_location = self.location.text()
        c_phone = self.phone.text()
        c_type = self.type.currentText()
        if c_name and c_id and c_type:
            if len(c_phone) != 11:
                QMessageBox.warning(self, "提示", "手机号应为11位", QMessageBox.Yes)
            elif update_company(c_name, c_id, c_location, c_phone, c_type, hr[0]):
                # 成功，关闭
                QMessageBox.information(self,"确认","修改成功",QMessageBox.Yes)
                QApplication.processEvents()
            else:
                QMessageBox.warning(self, "提示", "修改信息失败，请重试", QMessageBox.Yes)
        else:
            QMessageBox.warning(self, "提示", "必填项不应为空", QMessageBox.Yes)

    def deleteCompany(self):
        reply = QMessageBox.warning(self, "确认", "确认注销公司？", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            if delete_company(hr[0]):
                QMessageBox.information(self, "确认", "公司注销成功", QMessageBox.Yes)
                self.MainForm.listWidget.item(0).setHidden(False)
                self.MainForm.listWidget.item(1).setHidden(True)
                self.MainForm.listWidget.item(2).setHidden(True)
                self.MainForm.listWidget.item(3).setHidden(True)
                index = self.MainForm.tabWidget.currentIndex()
                widget = self.MainForm.tabWidget.widget(index)
                widget.close()
                self.MainForm.tabWidget.removeTab(index)
            else:
                QMessageBox.warning(self, "提示", "公司注销失败", QMessageBox.Yes)


class ChildrenForm_staff_apply(QtWidgets.QWidget, staff_apply):
    def __init__(self):
        super(ChildrenForm_staff_apply, self).__init__()
        self.setupUi(self)


class ChildrenForm_staff_message_management(QtWidgets.QWidget, staff_message_management):
    def __init__(self):
        super(ChildrenForm_staff_message_management, self).__init__()
        self.setupUi(self)


class ChildrenForm_rest_apply(QtWidgets.QWidget, rest_apply):
    def __init__(self):
        super(ChildrenForm_rest_apply, self).__init__()
        self.setupUi(self)


class ChildrenForm_out_apply(QtWidgets.QWidget, out_apply):
    def __init__(self):
        super(ChildrenForm_out_apply, self).__init__()
        self.setupUi(self)


class ChildrenForm_department(QtWidgets.QWidget, department):
    def __init__(self):
        super(ChildrenForm_department, self).__init__()
        self.setupUi(self)


class ChildrenForm_complain(QtWidgets.QWidget, complain):
    def __init__(self):
        super(ChildrenForm_complain, self).__init__()
        self.setupUi(self)


class ChildrenForm_getdailyAtt(QtWidgets.QWidget, getdailyAtt):
    def __init__(self):
        super(ChildrenForm_getdailyAtt, self).__init__()
        self.setupUi(self)


class ChildrenForm_export_att(QtWidgets.QWidget, export_att):
    def __init__(self):
        super(ChildrenForm_export_att, self).__init__()
        self.setupUi(self)


class ChildrenForm_attendance(QtWidgets.QWidget, attendance):
    def __init__(self):
        super(ChildrenForm_attendance, self).__init__()
        self.setupUi(self)

# hr 更新个人信息
class ChildrenForm_updateinfo(QtWidgets.QWidget, update_info):
    def __init__(self, MainForm):
        super(ChildrenForm_updateinfo, self).__init__()
        self.setupUi(self)
        self.MainForm = MainForm
        # global GLOBAL_PHONE
        print(GLOBAL_PHONE)
        self.hrUPWindow = hrUPWindow(self)
        # 实时刷新界面
        QApplication.processEvents()
        self.pushButton_3.clicked.connect(self.openUPSlot)
        # 打开数据库连接
        db, cursor = connect_to_sql()
        sql1 = "select * from company where c_hr_phone={}".format(GLOBAL_PHONE)
        ifExitC = cursor.execute(sql1)
        if ifExitC:
            sql = "select * from hr h,company c where h.hr_phone= c.c_hr_phone and h.hr_phone=%s"
            cursor.execute(sql, GLOBAL_PHONE)
            hr_info = cursor.fetchall()
            print(hr_info)
            for row in hr_info:
                print(row[1])
                self.label_2.setText(row[8])  # 公司
                self.label_9.setText(row[0])  # 手机号
                self.lineEdit_5.setText(row[4])  # 邮箱
                self.lineEdit_4.setText(row[2])  # 姓名
                self.label.setText(row[1])  # 员工编号
                sex = row[5]
                print(sex)
                if sex == 1:
                    self.radioButton.setChecked(True)
                elif sex == 2:
                    self.radioButton_2.setChecked(True)
        else:
            sql = "select * from hr h where hr_phone={}".format(GLOBAL_PHONE)
            cursor.execute(sql)
            hr_info = cursor.fetchall()
            print(hr_info)
            for row in hr_info:
                print(row[1])
                self.label_2.setText('暂无所属公司')  # 公司
                self.label_9.setText(row[0])  # 手机号
                self.lineEdit_5.setText(row[4])  # 邮箱
                self.lineEdit_4.setText(row[2])  # 姓名
                self.label.setText('暂无员工编号')  # 员工编号
                sex = row[5]
                if sex == 1:
                    self.radioButton.setChecked(True)
                elif sex == 2:
                    self.radioButton_2.setChecked(True)
                elif sex == 0:
                    self.radioButton_3.setChecked(True)

    # hr更新个人信息
    def updateSlot(self):
        global GLOBAL_PHONE
        name = self.lineEdit_4.text()
        email = self.lineEdit_5.text()
        sex = 0
        if self.radioButton.isChecked():
            sex = 1
        elif self.radioButton_2.isChecked():
            sex = 2
        else:
            sex = 0
        print(sex)
        result = updateHRInfo(name, email, sex, GLOBAL_PHONE)
        if result:
            QMessageBox.information(self, 'Successfully', '修改成功', QMessageBox.Yes)
        else:
            QMessageBox.warning(self, "提示", "新旧账号不得一致", QMessageBox.Yes)

    def openUPSlot(self):
        self.hrUPWindow.show()

    def exit(self):
        self.MainForm.exit()

    # def cancelSlot(self):

# hr更新账号
class hrUPWindow(QtWidgets.QWidget, update_phone):
    def __init__(self, MainForm):
        global GLOBAL_PHONE
        super(hrUPWindow, self).__init__()
        self.setupUi(self)
        self.MainForm = MainForm
        print("glogal_phone:" + GLOBAL_PHONE)
        self.lineEdit.setText(GLOBAL_PHONE)

    def updateSlot(self):
        global GLOBAL_PHONE
        oldphone = GLOBAL_PHONE
        newphone = self.lineEdit_2.text()

        # 打开数据库连接
        # db, cursor = connect_to_sql()
        if oldphone != newphone:
            # # 查询语句
            # sql1 = "select * from staff where s_phone = {}".format(newphone)
            # sql2 = "select * from hr where hr_phone = {}".format(newphone)
            # # 执行查询
            # ifExist1 = cursor.execute(sql1)
            # ifExist2 = cursor.execute(sql2)
            ifExist = ifPhone(newphone)
            if ifExist:
                QMessageBox.warning(self, "提示", "该账号已绑定其他用户", QMessageBox.Yes)
            else:
                result = updatePhone(newphone, oldphone, 2)
                if result:
                    QMessageBox.information(self, 'Successfully', '修改成功', QMessageBox.Yes)
                    # 退出登录
                    self.close()
                    self.MainForm.exit()


                else:
                    QMessageBox.warning(self, "提示", "修改失败，请重试", QMessageBox.Yes)

        else:
            QMessageBox.warning(self, "提示", "新旧账号不得一致", QMessageBox.Yes)

    def closeSlot(self):
        self.close()

# hr更新密码
class ChildrenForm_updatepwd(QtWidgets.QWidget, update_pwd):
    def __init__(self, MainForm):
        super(ChildrenForm_updatepwd, self).__init__()
        self.setupUi(self)
        self.MainForm = MainForm

    def checkOPwd(self):
        oldpwd = self.lineEdit_5.text()
        flag = checkOldP(oldpwd, GLOBAL_PHONE, 2)
        # # 打开数据库连接
        # db, cursor = connect_to_sql()
        # print(GLOBAL_PHONE)
        # sql = "select hr_passwd from hr where hr_phone = {}".format(GLOBAL_PHONE)
        # # 执行查询
        # cursor.execute(sql)
        # results = cursor.fetchall()
        # pwd = '1'
        # for row in results:
        #     pwd = row[0]
        #     print(pwd)

        if not flag:
            self.warninglabel.setText("*旧密码输入错误！")
            self.warninglabel.show()
        else:
            self.warninglabel.hide()

    def updateSlot(self):
        global GLOBAL_PHONE
        oldpwd = self.lineEdit_5.text()
        newpwd = self.lineEdit_4.text()
        # 打开数据库连接
        db, cursor = connect_to_sql()
        if oldpwd == newpwd:
            QMessageBox.warning(self, "提示", "新旧密码不得一致", QMessageBox.Yes)
        else:
            result = updatePwd(newpwd, GLOBAL_PHONE, 2)
            if result:
                QMessageBox.information(self, 'Successfully', '修改成功', QMessageBox.Yes)
                # 退出登录
                self.MainForm.exit()
                # hrWin.close()
                # welcomeWindow.show()
                # self.close()
            else:
                QMessageBox.warning(self, "提示", "修改失败，请重试", QMessageBox.Yes)
            # try:
            #     update_sql = "update hr set hr_passwd=%s where hr_phone=%s"
            #     data = (newpwd, GLOBAL_PHONE)
            #     cursor.execute(update_sql, data)
            #     db.commit()
            #     QMessageBox.information(self, 'Successfully', '修改成功', QMessageBox.Yes)
            #     # 执行sql语句和实现事件、、、
            #     cursor.close()
            #     db.close()
            #     # 退出登录
            #     welcomeWindow.show()
            #     self.close()
            # except ValueError as e:
            #     db.rollback()
            #     self.ui.textBrowser_log.append("[INFO] 写入数据库失败！", e)


class ChildrenForm_pyecharts(QtWidgets.QWidget, pyecharts):
    def __init__(self):
        super(ChildrenForm_pyecharts, self).__init__()
    # self.setupUi(self)


class ChildrenForm_calendar(QtWidgets.QWidget, calendar):
    def __init__(self):
        super(ChildrenForm_calendar, self).__init__()
    # self.setupUi(self)


# 员工界面
class StaffMainWindow(QtWidgets.QMainWindow, staff_MainWindow):
    def __init__(self, flag):
        super(StaffMainWindow, self).__init__()
        self.setupUi(self)
        self.label_2.setText(staff[2])#姓名
        self.label_3.setText(staff[0])#姓名
        self.label_4.setText(staff[5])#工号
        self.flag = flag
        item = self.listWidget_1.item(0)
        self.listWidget_1.itemClicked.connect(self.applyjob)
        self.listWidget_2.itemClicked.connect(self.info_col)
        self.listWidget_3.itemClicked.connect(self.atd)
        self.listWidget_4.itemClicked.connect(self.leave_and_appeal)
        self.listWidget_5.itemClicked.connect(self.account_manage)

    # 退出登录
    def exit(self):
        welcomeWindow.show()
        global staff
        staff = []
        self.close()

    def applyjob(self):
        currentitem = self.listWidget_1.currentItem()
        if str(currentitem.text()) == "公司列表":
            self.child = ChildrenForm_Colists()
            self.tabWidget.addTab(self.child, "公司列表")
            self.tabWidget.setCurrentWidget(self.child)

    def info_col(self):
        currentitem = self.listWidget_2.currentItem()
        if str(currentitem.text()) == "信息录入":
            self.child = ChildrenForm_info_collcetion()
            self.tabWidget.addTab(self.child, "信息录入")
            self.tabWidget.setCurrentWidget(self.child)

    def atd(self):
        currentitem = self.listWidget_3.currentItem()
        if str(currentitem.text()) == "每日打卡":
            self.child = ChildrenForm_Clock_in()
            self.tabWidget.addTab(self.child, "每日打卡")
            self.tabWidget.setCurrentWidget(self.child)
        elif str(currentitem.text()) == "考勤记录":
            self.child = ChildrenForm_Atd_record()
            self.tabWidget.addTab(self.child, "考勤记录")
            self.tabWidget.setCurrentWidget(self.child)

    def leave_and_appeal(self):
        currentitem = self.listWidget_4.currentItem()
        comid = staff[7]
        print(comid)
        if str(currentitem.text()) == "请假申请":
            if comid == None:
                QMessageBox.warning(self, "提示", "请先加入公司", QMessageBox.Yes)
            else:
                self.child = ChildrenForm_Leave()
                self.tabWidget.addTab(self.child, "请假申请")
                self.tabWidget.setCurrentWidget(self.child)
        elif str(currentitem.text()) == "外勤申请":
            if comid == None:
                QMessageBox.warning(self, "提示", "请先加入公司", QMessageBox.Yes)
            else:
                self.child = ChildrenForm_Outside()
                self.tabWidget.addTab(self.child, "外勤申请")
                self.tabWidget.setCurrentWidget(self.child)
        elif str(currentitem.text()) == "申诉":
            if comid == None:
                QMessageBox.warning(self, "提示", "请先加入公司", QMessageBox.Yes)
            else:
                self.child = ChildrenForm_Appeal()
                self.tabWidget.addTab(self.child, "申诉")
                self.tabWidget.setCurrentWidget(self.child)

        elif str(currentitem.text()) == "我的申请":
            if comid == None:
                QMessageBox.warning(self, "提示", "请先加入公司", QMessageBox.Yes)
            else:
                self.child = ChildrenForm_AllMessage()
                self.tabWidget.addTab(self.child, "我的申请")
                self.tabWidget.setCurrentWidget(self.child)

    def account_manage(self):
        currentitem = self.listWidget_5.currentItem()
        if str(currentitem.text()) == "修改密码":
            self.child = ChildrenForm_Changepass(self)
            self.tabWidget.addTab(self.child, "修改密码")
            self.tabWidget.setCurrentWidget(self.child)
        elif str(currentitem.text()) == "修改个人资料":
            self.child = ChildrenForm_Changeinfo(self)
            self.tabWidget.addTab(self.child, "修改个人资料")
            self.tabWidget.setCurrentWidget(self.child)


class ChildrenForm_Colists(QtWidgets.QWidget, CoLists):
    def __init__(self):
        super(ChildrenForm_Colists, self).__init__()
        self.setupUi(self)
        #搜索公司
        self.pushButton.clicked.connect(self.search)
        self.pushButton_2.clicked.connect(self.reset)
        #获取全部公司
        self.c_list = list(select_all())
        self.init_tablewidget()

    def apply_cp(self):
        reply = QMessageBox.question(self,"确认","确定申请该公司？",QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            row_index = self.tableWidget.currentIndex().row()
            cp_id = self.tableWidget.item(row_index,4).text()
            if apply_company(staff[0], cp_id):
                QMessageBox.information(self,"提示", "已申请成功，请耐心等待审批", QMessageBox.Yes)
            else:
                QMessageBox.warning(self, "警告", "申请失败，请重试", QMessageBox.Yes)
    #搜索
    def search(self):
        name = self.lineEdit.text()
        self.tableWidget.setRowCount(0)
        self.tableWidget.clearContents()
        self.index = 0
        for cp in self.c_list:
            if name in str(cp[0]):
                col_name = QTableWidgetItem(str(cp[0]))
                col_type = QTableWidgetItem(str(cp[1]))
                col_loacation = QTableWidgetItem(str(cp[2]))
                col_id = QTableWidgetItem(str(cp[3]))
                apply_btn = QPushButton("申请")
                apply_btn.clicked.connect(self.apply_cp)
                self.tableWidget.insertRow(int(self.tableWidget.rowCount()))
                self.tableWidget.setItem(self.index, 0, col_name)
                self.tableWidget.setItem(self.index, 1, col_type)
                self.tableWidget.setItem(self.index, 2, col_loacation)
                self.tableWidget.setCellWidget(self.index, 3, apply_btn)
                self.tableWidget.setItem(self.index, 4, col_id)
                self.tableWidget.setColumnHidden(4, True)
                self.tableWidget.setRowHeight(self.index, 40)
                self.index += 1
    def reset(self):
        self.tableWidget.setRowCount(0)
        self.tableWidget.clearContents()
        self.init_tablewidget()
    def init_tablewidget(self):
        if self.c_list:
            self.index = 0
            for cp in self.c_list:
                col_name = QTableWidgetItem(str(cp[0]))
                col_type = QTableWidgetItem(str(cp[1]))
                col_loacation = QTableWidgetItem(str(cp[2]))
                col_id = QTableWidgetItem(str(cp[3]))
                apply_btn = QPushButton("申请")
                apply_btn.clicked.connect(self.apply_cp)
                self.tableWidget.insertRow(int(self.tableWidget.rowCount()))
                self.tableWidget.setItem(self.index, 0, col_name)
                self.tableWidget.setItem(self.index, 1, col_type)
                self.tableWidget.setItem(self.index, 2, col_loacation)
                self.tableWidget.setCellWidget(self.index, 3, apply_btn)
                self.tableWidget.setItem(self.index, 4, col_id)
                self.tableWidget.setColumnHidden(4,True)
                self.tableWidget.setRowHeight(self.index, 40)
                self.index += 1
            self.tableWidget.update()

#信息采集
class ChildrenForm_info_collcetion(QtWidgets.QWidget, Info_collection):
    def __init__(self):
        super(ChildrenForm_info_collcetion, self).__init__()
        self.setupUi(self)
        self.timer_camera = QTimer()
        self.cap = cv2.VideoCapture()
        self.CAM_NUM = 0
        self.collcet_button.clicked.connect(self.showdata)
        self.timer_camera.timeout.connect(self.showcamera)

    def showdata(self):
        if self.timer_camera.isActive() == False:
            flag = self.cap.open(self.CAM_NUM) #打开摄像头
            if flag == False:
                QMessageBox.warning(self,"警告","无法打开摄像头",QMessageBox.Yes)
            else:
                self.timer_camera.start(30)
        else:
            self.timer_camera.stop()
            self.cap.release()
            self.cameraArea.clear()

    def showcamera(self):
        flag,self.image = self.cap.read()
        show = cv2.resize(self.image,(self.cameraArea.width(),self.cameraArea.height()))
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
        self.cameraArea.setPixmap(QtGui.QPixmap.fromImage(showImage))
        imgpath = os.path.join("./ai_model/identity/",staff[0]+".jpg")
        cv2.imwrite(imgpath, self.image)


class ChildrenForm_Clock_in(QtWidgets.QWidget, Clock_in):
    def __init__(self):
        super(ChildrenForm_Clock_in, self).__init__()
        self.setupUi(self)
        self.timer_camera = QTimer()
        self.cap = cv2.VideoCapture()
        self.CAM_NUM = 0
        self.pushButton.clicked.connect(self.showdata)
        self.timer_camera.timeout.connect(self.showcamera)
        self.pushButton_2.clicked.connect(self.mtcnn_facenet)

    def showdata(self):
        if self.timer_camera.isActive() == False:
            flag = self.cap.open(self.CAM_NUM)  # 打开摄像头
            if flag == False:
                QMessageBox.warning(self, "警告", "无法打开摄像头", QMessageBox.Yes)
            else:
                self.timer_camera.start(30)
        else:
            self.timer_camera.stop()
            self.cap.release()
            self.cameraArea_2.clear()

    def showcamera(self):
        flag, self.image = self.cap.read()
        show = cv2.resize(self.image, (self.cameraArea_2.width(), self.cameraArea_2.height()))
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
        self.cameraArea_2.setPixmap(QtGui.QPixmap.fromImage(showImage))
        imgpath = os.path.join("./ai_model/data/", "text" + ".jpg")
        cv2.imwrite(imgpath, self.image)

    def mtcnn_facenet(self):
        mtcnn = MTCNN(keep_all=True)
        resnet = InceptionResnetV1(pretrained='vggface2').eval()
        image1 = cv2.imread('./ai_model/data/text.jpg')
        img1 = mtcnn(image1, save_path='ai_model/data/ceshi.png')#通过MTCNN人脸检测模型，从照片中提取人脸图像
        ebed1 = resnet(img1)#把人脸图像输入到FaceNet，计算Embedding的特征向量
        feature1 = F.normalize(ebed1)  #F.normalize只能处理两维的数据，L2归一化
        dir_path = "D:\\face_project\\ai_model\\identity"
        files = os.listdir(dir_path)
        temp=0
        for file in files:
            image = cv2.imread(dir_path + "\\" + file)
            img = mtcnn(image, save_path='ai_model/data/xunlian.png')
            ebed = resnet(img)
            feature = F.normalize(ebed)
            distance = feature1.mm(feature.t())  # 计算余弦相似度
            if distance>=0.6:
                temp=1
        self.timer_camera.stop()
        self.cap.release()
        self.cameraArea_2.clear()
        if temp:
            self.label_2.setText(staff[2]+"您好")
            QMessageBox.about(self,"欢迎","打卡成功")
        else:
            QMessageBox.warning(self, "警告", "打卡失败，请前往申诉页面",QMessageBox.Yes)

class ChildrenForm_Atd_record(QtWidgets.QWidget, Atd_record):
    def __init__(self):
        super(ChildrenForm_Atd_record, self).__init__()
        self.setupUi(self)


class ChildrenForm_Leave(QtWidgets.QWidget, Leave):
    def __init__(self):
        super(ChildrenForm_Leave, self).__init__()
        self.setupUi(self)
        # global GLOBAL_PHONE
        # global staff
        print(staff)
        print(staff[0])
        self.label_2.setText(staff[7])  # 公司id
        self.label.setText(staff[5])  # 员工id
        self.label_10.setText(staff[2])  # 姓名
        self.label_13.setText(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        self.dateTimeEdit.setDisplayFormat("yyyy-MM-dd HH:mm:ss")  # 设置格式
        self.dateTimeEdit_2.setDisplayFormat("yyyy-MM-dd HH:mm:ss")  # 设置格式
        self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        self.dateTimeEdit_2.setDateTime(QDateTime.currentDateTime())

    def submitSlot(self):
        starttime = self.dateTimeEdit.dateTime()
        endtime = self.dateTimeEdit_2.dateTime()
        start_time = self.dateTimeEdit.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        end_time = self.dateTimeEdit_2.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        demand = self.textEdit.toPlainText()
        apply_time = self.label_13.text()
        print(demand)
        print(start_time)
        if demand == "" or start_time == end_time or starttime > endtime:
            if demand == "":
                QMessageBox.warning(self, "提示", "请假理由不得为空", QMessageBox.Yes)
            elif start_time == end_time:
                QMessageBox.warning(self, "提示", "请假时间必须为时间段", QMessageBox.Yes)
            else:
                QMessageBox.warning(self, "提示", "请假时间开始时间必须早于结束时间", QMessageBox.Yes)
        else:
            result = submitApply(GLOBAL_PHONE, apply_time, demand, start_time, end_time, 1)
            if result:
                QMessageBox.information(self, 'Successfully', '申请成功', QMessageBox.Yes)
            else:
                QMessageBox.warning(self, "提示", "申请失败，请重试！", QMessageBox.Yes)


class ChildrenForm_Outside(QtWidgets.QWidget, Outside):
    def __init__(self):
        super(ChildrenForm_Outside, self).__init__()
        self.setupUi(self)
        self.label_2.setText(staff[7])  # 公司id
        self.label.setText(staff[5])  # 员工id
        self.label_10.setText(staff[2])  # 姓名
        self.label_14.setText(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        self.dateTimeEdit.setDisplayFormat("yyyy-MM-dd HH:mm:ss")  # 设置格式
        self.dateTimeEdit_2.setDisplayFormat("yyyy-MM-dd HH:mm:ss")  # 设置格式
        self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        self.dateTimeEdit_2.setDateTime(QDateTime.currentDateTime())

    def submitSlot(self):
        addr = self.lineEdit.text()
        detail = self.textEdit.toPlainText()
        demand = "外勤地点：" + addr + "。外勤工作详情：" + detail
        print(demand)
        starttime = self.dateTimeEdit.dateTime()
        endtime = self.dateTimeEdit_2.dateTime()
        start_time = self.dateTimeEdit.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        end_time = self.dateTimeEdit_2.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        apply_time = self.label_14.text()
        print(demand)
        print(start_time)
        if detail == "" or addr == "" or start_time == end_time or starttime>endtime:
            if addr == "":
                QMessageBox.warning(self, "提示", "外勤地点不得为空", QMessageBox.Yes)
            elif detail == "":
                QMessageBox.warning(self, "提示", "外勤工作详情不得为空", QMessageBox.Yes)
            elif start_time == end_time:
                QMessageBox.warning(self, "提示", "申请时间必须为时间段", QMessageBox.Yes)
            else:
                QMessageBox.warning(self, "提示", "申请时间开始时间必须早于结束时间", QMessageBox.Yes)
        else:
            result = submitApply(GLOBAL_PHONE, apply_time, demand, start_time, end_time, 2)
            if result:
                QMessageBox.information(self, 'Successfully', '申请成功', QMessageBox.Yes)
            else:
                QMessageBox.warning(self, "提示", "申请失败，请重试！", QMessageBox.Yes)


class ChildrenForm_Appeal(QtWidgets.QWidget, Appeal):
    def __init__(self):
        super(ChildrenForm_Appeal, self).__init__()
        self.setupUi(self)
        self.label_2.setText(staff[7])  # 公司id
        self.label.setText(staff[5])  # 员工id
        self.label_10.setText(staff[2])  # 姓名
        self.label_12.setText(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        self.dateTimeEdit.setDisplayFormat("yyyy-MM-dd HH:mm:ss")  # 设置格式
        self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())

    def submitSlot(self):
        co_time = self.dateTimeEdit.dateTime().toString("yyyy-MM-dd hh:mm:ss")

        demand = self.textEdit.toPlainText()
        apply_time = self.label_12.text()
        print(demand)

        if demand == "":
            QMessageBox.warning(self, "提示", "到勤证明不得为空", QMessageBox.Yes)
        else:
            result = submitApply(GLOBAL_PHONE, apply_time, demand, co_time, co_time, 3)
            if result:
                QMessageBox.information(self, 'Successfully', '申请成功', QMessageBox.Yes)
            else:
                QMessageBox.warning(self, "提示", "申请失败，请重试！", QMessageBox.Yes)

class ChildrenForm_AllMessage(QtWidgets.QWidget, all_message):
    def __init__(self):
        super(ChildrenForm_AllMessage, self).__init__()
        self.setupUi(self)
        # 打开数据库连接
        db, cursor = connect_to_sql()
        sql = "select m_type,m_apply_datetime,m_demand,m_state from message where m_s_phone = {}".format(GLOBAL_PHONE)
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)

        cursor.close()
        db.close()

        if results:
            row = cursor.rowcount
            vol = len(results[0])
            for i in range(row):
                self.tableWidget.insertRow(int(self.tableWidget.rowCount()))

                for j in range(vol):
                    # 设置数据条目
                    temp_data = results[i][j]
                    data = ""
                    if j == 0:
                        if temp_data == 1:
                            data = "请假"
                        elif temp_data == 2:
                            data = "外勤"
                        elif temp_data == 3:
                            data = "补打卡"
                    elif j == 1:
                        data = str(temp_data)
                    elif j == 2:
                        data = str(temp_data)
                    elif j == 3:
                        if temp_data == 1:
                            data = "未处理"
                        elif temp_data == 2:
                            data = "已同意"
                        elif temp_data == 3:
                            data = "已拒绝"
                            # btn = QPushButton("申诉")
                            # # btn.clicked.connect(self.detailMes)
                            # self.tableWidget.setCellWidget(i, 4, btn)

                    print(data)

                    item = QTableWidgetItem(data)
                    print(item)
                    self.tableWidget.setItem(i, j, item)
                    # self.table.setItem(i, j, data)

    def searchSlot(self):
        # 清空表
        self.tableWidget.setRowCount(0)
        self.tableWidget.clearContents()
        strtype = self.comboBox.currentText()
        if strtype == "全部":
            type = 0
        elif strtype == "请假":
            type = 1
        elif strtype == "外勤":
            type = 2
        else:
            type = 3

        strstate = self.comboBox_2.currentText()
        if strstate == "全部":
            state = 0
        elif strstate == "未处理":
            state = 1
        elif strstate == "已同意":
            state = 2
        else:
            state = 3
        # 打开数据库连接

        db, cursor = connect_to_sql()
        if type == 0 and state == 0:
            sql = "select m_type,m_apply_datetime,m_demand,m_state from message where m_s_phone = %s "
            data = GLOBAL_PHONE
        else:
            if state == 0:
                sql = "select m_type,m_apply_datetime,m_demand,m_state from message where m_s_phone = %s and m_type=%s"
                data = (GLOBAL_PHONE, type)
            elif type == 0:
                sql = "select m_type,m_apply_datetime,m_demand,m_state from message where m_s_phone = %s and m_state=%s"
                data = (GLOBAL_PHONE, state)
            else:
                sql = "select m_type,m_apply_datetime,m_demand,m_state from message where m_s_phone = %s and m_type=%s " \
                      "and m_state=%s "
                data = (GLOBAL_PHONE, type, state)

        cursor.execute(sql, data)
        results = cursor.fetchall()
        print(results)

        cursor.close()
        db.close()

        if results:
            row = cursor.rowcount
            vol = len(results[0])
            for i in range(row):
                self.tableWidget.insertRow(int(self.tableWidget.rowCount()))

                for j in range(vol):
                    # 设置数据条目
                    temp_data = results[i][j]
                    data = ""
                    if j == 0:
                        if temp_data == 1:
                            data = "请假"
                        elif temp_data == 2:
                            data = "外勤"
                        elif temp_data == 3:
                            data = "补打卡"
                    elif j == 1:
                        data = str(temp_data)
                    elif j == 2:
                        data = str(temp_data)
                    elif j == 3:
                        if temp_data == 1:
                            data = "未处理"
                        elif temp_data == 2:
                            data = "已同意"
                        elif temp_data == 3:
                            data = "已拒绝"
                            # btn = QPushButton("申诉")
                            # # btn.clicked.connect(self.detailMes)
                            # self.tableWidget.setCellWidget(i, 4, btn)

                    print(data)

                    item = QTableWidgetItem(data)
                    print(item)
                    self.tableWidget.setItem(i, j, item)
# 员工修改密码
class ChildrenForm_Changepass(QtWidgets.QWidget, changepass):
    def __init__(self, MainForm):
        self.MainForm = MainForm
        super(ChildrenForm_Changepass, self).__init__()
        self.setupUi(self)

    def checkOPwd(self):
        global GLOBAL_PHONE
        oldpwd = self.lineEdit_5.text()
        flag = checkOldP(oldpwd, GLOBAL_PHONE, 1)
        # # 打开数据库连接
        # db, cursor = connect_to_sql()
        # print(GLOBAL_PHONE)
        # sql = "select hr_passwd from hr where hr_phone = {}".format(GLOBAL_PHONE)
        # # 执行查询
        # cursor.execute(sql)
        # results = cursor.fetchall()
        # pwd = '1'
        # for row in results:
        #     pwd = row[0]
        #     print(pwd)

        if not flag:
            self.warninglabel.setText("*旧密码输入错误！")
            self.warninglabel.show()
        else:
            self.warninglabel.hide()

    def updateSlot(self):
        global GLOBAL_PHONE
        oldpwd = self.lineEdit_5.text()
        newpwd = self.lineEdit_4.text()
        # # 打开数据库连接
        # db, cursor = connect_to_sql()

        if oldpwd == newpwd:
            QMessageBox.warning(self, "提示", "新旧密码不得一致", QMessageBox.Yes)
        else:
            result = updatePwd(newpwd, GLOBAL_PHONE, 1)
            if result:
                QMessageBox.information(self, 'Successfully', '修改成功', QMessageBox.Yes)
                # 退出登录
                self.MainForm.exit()
            else:
                QMessageBox.warning(self, "提示", "修改密码失败，请重试", QMessageBox.Yes)

#员工修改个人信息
class ChildrenForm_Changeinfo(QtWidgets.QWidget, changeinfo):
    def __init__(self, MainForm):
        super(ChildrenForm_Changeinfo, self).__init__()
        self.MainForm = MainForm
        self.setupUi(self)
        global GLOBAL_PHONE
        print(GLOBAL_PHONE)
        self.staffUPWindow = staffUPWindow(self)

        # 打开数据库连接
        db, cursor = connect_to_sql()
        sql1 = "select * from staff where s_phone={}".format(GLOBAL_PHONE)
        cursor.execute(sql1)
        staff_info = cursor.fetchall()
        print(staff_info)
        for row in staff_info:
            self.label_9.setText(row[0])  # 手机号
            sex = row[10]
            if sex == 1:
                self.radioButton.setChecked(True)
            elif sex == 2:
                self.radioButton_2.setChecked(True)
            else:
                self.radioButton_3.setChecked(True)
            self.lineEdit_4.setText(row[2])  # 姓名
            self.lineEdit_5.setText(row[4])  # 邮箱
            self.lineEdit_6.setText(row[3])  # 地址
            s_po = row[8]
            c_id = row[7]
            d_id = row[6]
            s_id = row[5]
            if c_id == None:
                self.label_2.setText('暂无所属公司')
                self.label_16.setText('暂无所属部门')
                self.label.setText('暂无员工编号')
                self.label_14.setText('暂无职位信息')
            else:
                sql2 = "select * from staff s,company c,department d where s.s_com_id=c.c_id and s.s_depart_id=d.dep_id " \
                       "and d.dep_com_id=c.c_id and s.s_com_id=%s and s.s_depart_id=%s and s.s_id=%s "
                data = (c_id, d_id, s_id)
                cursor.execute(sql2, data)
                all_info = cursor.fetchall()
                print(all_info)
                for row in all_info:
                    self.label_2.setText(row[13])  # 公司
                    self.label_16.setText(row[19])  # 部门
                    self.label.setText(row[5])  # 工号
                    if row[8] == None:
                        self.label_14.setText('暂无职位信息')
                    else:
                        self.label_14.setText(row[8])

    # 员工修改个人信息
    def updateSlot(self):
        global GLOBAL_PHONE
        name = self.lineEdit_4.text()
        email = self.lineEdit_5.text()
        addr = self.lineEdit_6.text()
        sex = 0
        if self.radioButton.isChecked():
            sex = 1
        elif self.radioButton_2.isChecked():
            sex = 2
        else:
            sex = 0
        print(sex)
        result = updateSInfo(name, email, sex, addr, GLOBAL_PHONE)
        if result:
            QMessageBox.information(self, 'Successfully', '修改成功', QMessageBox.Yes)
        else:
            QMessageBox.warning(self, "提示", "修改失败，请重试！", QMessageBox.Yes)

    # 打开修改账号
    def openUPSlot(self):
        self.staffUPWindow.show()

    # 退出登录
    def exit(self):
        self.MainForm.exit()

# 员工更新账号
class staffUPWindow(QtWidgets.QWidget, update_s_phone):
    def __init__(self, MainForm):
        global GLOBAL_PHONE
        super(staffUPWindow, self).__init__()
        self.MainForm = MainForm
        self.setupUi(self)
        print("glogal_phone:" + GLOBAL_PHONE)
        self.lineEdit.setText(GLOBAL_PHONE)

    def updateSlot(self):
        global GLOBAL_PHONE
        oldphone = GLOBAL_PHONE
        newphone = self.lineEdit_2.text()

        # 打开数据库连接
        db, cursor = connect_to_sql()
        if oldphone != newphone:

            ifExist = ifPhone(newphone)
            if ifExist:
                QMessageBox.warning(self, "提示", "该账号已绑定其他用户", QMessageBox.Yes)
            else:
                result = updatePhone(newphone, oldphone, 1)
                if result:
                    QMessageBox.information(self, 'Successfully', '修改成功', QMessageBox.Yes)
                    # 退出登录
                    self.close()
                    self.MainForm.exit()
                else:
                    QMessageBox.warning(self, "提示", "修改失败，请重试", QMessageBox.Yes)
        else:
            QMessageBox.warning(self, "提示", "新旧账号不得一致", QMessageBox.Yes)

    def closeSlot(self):
        self.close()

class ChildrenForm_Atd_record(QtWidgets.QWidget, Atd_record):
    def __init__(self):
        super(ChildrenForm_Atd_record, self).__init__()
        # self.setupUi(self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    # desktop = QApplication.desktop()
    # rect = desktop.frameSize()
    stylefile = './UI/style.qss'
    style = CommonHelper.readQss(stylefile)
    welcomeWindow = NewWelcomeWin()
    welcomeWindow.setStyleSheet(style)
    # welcomeWindow.resize(QSize(rect.width(), rect.height()))
    # palette = QtGui.QPalette()
    # pix = QtGui.QPixmap("./UI/background.jpg")
    # pix = pix.scaled(rect.width(), rect.height())
    # palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(pix))
    # welcomeWindow.setPalette(palette)
    welcomeWindow.show()
    hrWin = MainForm(signal)
    # = MainForm(signal)
    #changepsw = ChildrenForm_updatepwd()
    sys.exit(app.exec_())
