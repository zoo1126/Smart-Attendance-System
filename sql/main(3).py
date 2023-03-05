import sip
from PyQt5.QtCore import QSize, pyqtSignal, Qt
from PyQt5.QtGui import QPalette, QBrush, QPixmap, QColor
from qtpy import QtGui

from UI.staff_win.staff_mainwindow import Ui_MainWindow as staff_MainWindow
from UI.staff_win.CoLists import Ui_Form as CoLists
from UI.staff_win.Info_collection import Ui_Form as Info_collection
from UI.staff_win.Clock_in import Ui_Form as Clock_in
from UI.staff_win.Atd_record import Ui_Form as Atd_record
from UI.staff_win.staff_message1 import Ui_Form as Leave
from UI.staff_win.staff_message2 import Ui_Form as Outside
from UI.staff_win.staff_message3 import Ui_Form as Appeal
from UI.staff_win.changepass import Ui_Form as changepass
from UI.staff_win.changeinfo import Ui_Form as changeinfo
from UI.hr_win.hr_mainwindow import Ui_MainWindow as hr_MainWindow
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
from UI.hr_win.hr_attendance import Ui_Form as attendance
from UI.hr_win.hr_updateinfo import Ui_Form as update_info
from UI.hr_win.hr_updatepwd import Ui_Form as update_pwd
from charts_to_UIForm.chartmain_py import chartPy as pyecharts
from charts_to_UIForm.vi_chart_to_calendar import chartPy as calendar
from charts_to_UIForm.vi_chart_to_calendar_staff import chartPy as Atd_record
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox, QWidget, QApplication, QMainWindow, QTableWidgetItem, QPushButton, QHBoxLayout
import sys
from UI.welcomeWindow import Ui_WelcomeWin as welcomewin
from UI.loginWindow import Ui_LoginWin as loginwin
from UI.user_reg import Ui_Form as user_reg
import UI.pic_rc
from sql.login import *
from sql.company import *

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
    def loginSlot(self):
        phone = self.lineEdit.text()
        pwd = self.lineEdit_2.text()
        if self.radioButton.isChecked():
            # 员工注册
            welcomeWindow.show()
            self.loginWin.show()
            self.close()
        elif self.radioButton_2.isChecked():
            # HR注册
            welcomeWindow.show()
            self.loginWin.show()
            self.close()
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
        self.ChangePwdButton.hide()

    def forgetPswSlot(self):
        changepsw.show()
        self.close()

    def signupSlot(self):
        self.signupWin = NewUser_reg(signal)
        self.signupWin.show()
        self.close()

    def verifySlot(self):
        phoneNum = self.PhoneNumInput.text()
        pwd = self.PwdInput.text()
        if phoneNum and len(phoneNum)!= 11:
            self.warnLabel.show()
        elif pwd == "":
            QMessageBox.warning(self, "警告", "请输入密码", QMessageBox.Yes)
        else:
            # 账号检验
            result = staff_login(phoneNum, pwd)
            if result:
                global staff
                staff = list(result)
                self.staffWin = StaffMainWindow(signal)
                self.staffWin.show()
                self.close()
                welcomeWindow.close()
            else:
                QMessageBox.warning(self, "警告", "登录失败，请重试", QMessageBox.Yes)

    def verifySlot_hr(self):
        phoneNum = self.PhoneNumInput.text()
        pwd = self.PwdInput.text()
        if len(phoneNum) != 11 and len(pwd):
            self.warnLabel.show()
        else:
            # 账号检验
            result = hr_login(phoneNum, pwd)
            if result:
                global hr
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
        self.label_2.setText(hr[2])  # name
        self.label_3.setText(hr[0])  # phone
        self.label_4.setText(hr[1] if hr[1] else "暂无")  # id
        self.flag = flag
        self.listWidget.itemClicked.connect(self.companymanagement)
        self.listWidget_2.itemClicked.connect(self.staffmanagement)
        self.listWidget_3.itemClicked.connect(self.askmanagement)
        self.listWidget_4.itemClicked.connect(self.dailyAttmanagement)
        self.listWidget_5.itemClicked.connect(self.updatemanagement)
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
            self.tabWidget.addTab(self.child, "部门管理")
            self.tabWidget.setCurrentWidget(self.child)

    def staffmanagement(self):
        currentitem = self.listWidget_2.currentItem()
        if str(currentitem.text()) == "员工申请管理":
            self.child = ChildrenForm_staff_apply()
            self.tabWidget.addTab(self.child, "员工申请管理")
            self.tabWidget.setCurrentWidget(self.child)
        elif str(currentitem.text()) == "员工信息管理":
            self.child = ChildrenForm_staff_message_management()
            self.tabWidget.addTab(self.child, "员工信息管理")
            self.tabWidget.setCurrentWidget(self.child)

    def askmanagement(self):
        currentitem = self.listWidget_3.currentItem()
        if str(currentitem.text()) == "请假申请":
            self.child = ChildrenForm_rest_apply()
            self.tabWidget.addTab(self.child, "请假申请")
            self.tabWidget.setCurrentWidget(self.child)
        elif str(currentitem.text()) == "外勤申请":
            self.child = ChildrenForm_out_apply()
            self.tabWidget.addTab(self.child, "外勤申请")
            self.tabWidget.setCurrentWidget(self.child)
        elif str(currentitem.text()) == "申诉":
            self.child = ChildrenForm_complain()
            self.tabWidget.addTab(self.child, "申诉")
            self.tabWidget.setCurrentWidget(self.child)

    def dailyAttmanagement(self):
        currentitem = self.listWidget_4.currentItem()
        if str(currentitem.text()) == "考勤查询":
            self.child = ChildrenForm_getdailyAtt()
            self.tabWidget.addTab(self.child, "考勤查询")
            self.tabWidget.setCurrentWidget(self.child)
        elif str(currentitem.text()) == "考勤可视化":
            self.child = ChildrenForm_pyecharts()
            self.tabWidget.addTab(self.child, "考勤可视化")
            self.tabWidget.setCurrentWidget(self.child)
        elif str(currentitem.text()) == "导出考勤":
            self.child = ChildrenForm_export_att()
            self.tabWidget.addTab(self.child, "导出考勤")
            self.tabWidget.setCurrentWidget(self.child)

    def updatemanagement(self):
        currentitem = self.listWidget_5.currentItem()
        if str(currentitem.text()) == "个人信息修改":
            self.child = ChildrenForm_updateinfo()
            self.tabWidget.addTab(self.child, "信息修改")
            self.tabWidget.setCurrentWidget(self.child)
        elif str(currentitem.text()) == "密码修改":
            self.child = ChildrenForm_updatepwd()
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
                QMessageBox.information(self, "确认", "修改成功", QMessageBox.Yes)
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


class ChildrenForm_updateinfo(QtWidgets.QWidget, update_info):
    def __init__(self):
        super(ChildrenForm_updateinfo, self).__init__()
        self.setupUi(self)


class ChildrenForm_updatepwd(QtWidgets.QWidget, update_pwd):
    def __init__(self):
        super(ChildrenForm_updatepwd, self).__init__()
        self.setupUi(self)


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
        self.label_2.setText(staff[2])  # 姓名
        self.label_3.setText(staff[0])  # 手机号
        self.label_4.setText(staff[5])  # 工号
        self.flag = flag;
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
        elif str(currentitem.text()) == "工资考勤记录":
            self.child = ChildrenForm_Atd_record()
            self.tabWidget.addTab(self.child, "工资考勤记录")
            self.tabWidget.setCurrentWidget(self.child)

    def leave_and_appeal(self):
        currentitem = self.listWidget_4.currentItem()
        if str(currentitem.text()) == "请假申请":
            self.child = ChildrenForm_Leave()
            self.tabWidget.addTab(self.child, "请假申请")
            self.tabWidget.setCurrentWidget(self.child)
        elif str(currentitem.text()) == "外勤申请":
            self.child = ChildrenForm_Outside()
            self.tabWidget.addTab(self.child, "外勤申请")
            self.tabWidget.setCurrentWidget(self.child)
        elif str(currentitem.text()) == "申诉":
            self.child = ChildrenForm_Appeal()
            self.tabWidget.addTab(self.child, "申诉")
            self.tabWidget.setCurrentWidget(self.child)

    def account_manage(self):
        currentitem = self.listWidget_5.currentItem()
        if str(currentitem.text()) == "修改密码":
            self.child = ChildrenForm_Changepass()
            self.tabWidget.addTab(self.child, "修改密码")
            self.tabWidget.setCurrentWidget(self.child)
        elif str(currentitem.text()) == "修改个人资料":
            self.child = ChildrenForm_Changeinfo()
            self.tabWidget.addTab(self.child, "修改个人资料")
            self.tabWidget.setCurrentWidget(self.child)


class ChildrenForm_Colists(QtWidgets.QWidget, CoLists):
    def __init__(self):
        super(ChildrenForm_Colists, self).__init__()
        self.setupUi(self)
        self.setStyleSheet(style)
        # 搜索公司
        self.pushButton.clicked.connect(self.search)
        self.pushButton_2.clicked.connect(self.reset)
        # 获取全部公司
        self.c_list = list(select_all())
        self.init_tablewidget()

    def apply_cp(self):
        reply = QMessageBox.question(self, "确认", "确定申请该公司？", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            row_index = self.tableWidget.currentIndex().row()
            print(row_index)
            cp_id = self.tableWidget.item(row_index, 4).text()
            print(cp_id)
            if apply_company(staff[0], cp_id):
                QMessageBox.information(self, "提示", "已申请成功，请耐心等待审批", QMessageBox.Yes)
            else:
                QMessageBox.warning(self, "警告", "申请失败，请重试", QMessageBox.Yes)

    # 搜索
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
                apply_btn.setFixedHeight(36)
                apply_btn.setFixedWidth(72)
                apply_btn.clicked.connect(self.apply_cp)
                widget = QWidget()
                layout = QHBoxLayout()
                layout.setSpacing(0)
                layout.setContentsMargins(0, 0, 0, 0)
                layout.addWidget(apply_btn)
                widget.setLayout(layout)
                self.tableWidget.insertRow(int(self.tableWidget.rowCount()))
                self.tableWidget.setItem(self.index, 0, col_name)
                self.tableWidget.setItem(self.index, 1, col_type)
                self.tableWidget.setItem(self.index, 2, col_loacation)
                self.tableWidget.setCellWidget(self.index, 3, widget)
                self.tableWidget.setItem(self.index, 4, col_id)
                for j in range(3):
                    self.tableWidget.item(self.index, j).setTextAlignment(QtCore.Qt.AlignCenter)
                    if self.index % 2 == 0:
                        self.tableWidget.item(self.index, j).setBackground(QColor(248, 248, 255))
                self.tableWidget.setColumnHidden(4, True)
                self.tableWidget.setRowHeight(self.index, 54)

                self.index += 1
            self.tableWidget.update()


class ChildrenForm_info_collcetion(QtWidgets.QWidget, Info_collection):
    def __init__(self):
        super(ChildrenForm_info_collcetion, self).__init__()
        self.setupUi(self)


class ChildrenForm_Clock_in(QtWidgets.QWidget, Clock_in):
    def __init__(self):
        super(ChildrenForm_Clock_in, self).__init__()
        self.setupUi(self)


class ChildrenForm_Atd_record(QtWidgets.QWidget, Atd_record):
    def __init__(self):
        super(ChildrenForm_Atd_record, self).__init__()
        self.setupUi(self)


class ChildrenForm_Leave(QtWidgets.QWidget, Leave):
    def __init__(self):
        super(ChildrenForm_Leave, self).__init__()
        self.setupUi(self)


class ChildrenForm_Outside(QtWidgets.QWidget, Outside):
    def __init__(self):
        super(ChildrenForm_Outside, self).__init__()
        self.setupUi(self)


class ChildrenForm_Appeal(QtWidgets.QWidget, Appeal):
    def __init__(self):
        super(ChildrenForm_Appeal, self).__init__()
        self.setupUi(self)


class ChildrenForm_Changepass(QtWidgets.QWidget, changepass):
    def __init__(self):
        super(ChildrenForm_Changepass, self).__init__()
        self.setupUi(self)


class ChildrenForm_Changeinfo(QtWidgets.QWidget, changeinfo):
    def __init__(self):
        super(ChildrenForm_Changeinfo, self).__init__()
        self.setupUi(self)


class ChildrenForm_Atd_record(QtWidgets.QWidget, Atd_record):
    def __init__(self):
        super(ChildrenForm_Atd_record, self).__init__()
        # self.setupUi(self)


# if __name__== '__main__':
#     import sys
#     app=QApplication(sys.argv)
#     MainWindow=QMainWindow()
#     ui = MainForm()
#     ui.show()
#
#     sys.exit(app.exec_())

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
    changepsw = ChildrenForm_updatepwd()
    sys.exit(app.exec_())
