import random

import pymysql

from service import *

#判断手机号是否被注册
def ifPhone(phone):
    # 打开数据库连接
    db, cursor = connect_to_sql()
    # 查询语句
    sql1 = "select * from staff where s_phone = {}".format(phone)
    sql2 = "select * from hr where hr_phone = {}".format(phone)
    # 执行查询
    ifExist1 = cursor.execute(sql1)
    ifExist2 = cursor.execute(sql2)
    return ifExist1 or ifExist2

# 注册
def userReg(phone, pwd, type):
    insert_sql=""
    data=()
    # 打开数据库连接
    db, cursor = connect_to_sql()
    if type==1:
        insert_sql = "insert into staff(s_phone,s_passwd,s_depart_id,s_com_id,s_sex) values(%s,%s,%s," \
                     "%s,%s) "
        data = (phone, pwd, None, None, 0)
    else:
        while True:
            str = ''
            hr_id = str.join(random.choice("0123456789") for i in range(12))
            sql3 = "select * from hr where hr_id = {}".format(hr_id)
            ifExist3 = cursor.execute(sql3)
            if not ifExist3:
                break
        insert_sql = "insert into hr(hr_phone,hr_passwd,hr_id,hr_sex) values(%s,%s,%s,%s)"
        data = (phone, pwd, hr_id, 0)
    try:
        result= cursor.execute(insert_sql, data)
        db.commit()
        # 执行sql语句和实现事件、、、
        cursor.close()
        db.close()
        return result

    except ValueError as e:
        db.rollback()

