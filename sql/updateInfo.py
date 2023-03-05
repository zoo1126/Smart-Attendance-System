import random

import pymysql

from service import *

#type 1均为staff 2为HR

#旧密码是否正确
def checkOldP(oldpwd,phone,type):
    sql = ""
    #员工
    if type==1:
        sql = "select s_passwd from staff where s_phone = {}".format(phone)
    elif type==2:
        sql = "select hr_passwd from hr where hr_phone = {}".format(phone)
    # 打开数据库连接
    db, cursor = connect_to_sql()
    # 执行查询
    cursor.execute(sql)
    results = cursor.fetchall()
    pwd = ''
    for row in results:
        pwd = row[0]
    return pwd == oldpwd


#修改密码,1员工，2HR
def updatePwd(pwd,phone,type):
    update_sql=""
    data = (pwd, phone)
    #员工
    if type==1:
        update_sql = "update staff set s_passwd=%s where s_phone=%s"
    #HR
    elif type==2:
        update_sql = "update hr set hr_passwd=%s where hr_phone=%s"
    # 打开数据库连接
    db, cursor = connect_to_sql()
    try:
        result=cursor.execute(update_sql, data)
        db.commit()
        # 执行sql语句和实现事件、、、
        cursor.close()
        db.close()
        return result
    except ValueError as e:
        db.rollback()

#修改个人信息_HR
def updateHRInfo(name,email,sex,phone):
    # 打开数据库连接
    db, cursor = connect_to_sql()
    try:
        update_sql = "update hr set hr_name=%s,hr_email=%s,hr_sex=%s where hr_phone=%s"
        data = (name, email, sex, phone)
        result=cursor.execute(update_sql, data)
        db.commit()

        # 执行sql语句和实现事件、、、
        cursor.close()
        db.close()
        return result
    except ValueError as e:
        db.rollback()

#修改个人信息_员工
def updateSInfo(name, email, sex, addr, phone):
    # 打开数据库连接
    db, cursor = connect_to_sql()
    try:
        update_sql = "update staff set s_name=%s,s_email=%s,s_sex=%s,s_addr=%s where s_phone=%s"
        data = (name, email, sex, addr, phone)
        result=cursor.execute(update_sql, data)
        db.commit()
        # 执行sql语句和实现事件、、、
        cursor.close()
        db.close()
        return result
    except ValueError as e:
        db.rollback()

#修改账号（手机号），type1员工2HR
def updatePhone(newphone, oldphone,type):
    update_sql=""
    # 打开数据库连接
    db, cursor = connect_to_sql()
    data = (newphone, oldphone)
    if type==2:
        update_sql = "update hr set hr_phone=%s where hr_phone=%s"
    elif type==1:
        update_sql = "update staff set s_phone=%s where s_phone=%s"
    try:
        result=cursor.execute(update_sql, data)
        db.commit()
        # 执行sql语句和实现事件、、、
        cursor.close()
        db.close()
        return result
    except ValueError as e:
        db.rollback()



