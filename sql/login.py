import pymysql

from service import *

# 查询语句
sql_s_login = "select * from staff where s_phone = %s and s_passwd = %s"
sql_h_login = "select * from hr where hr_phone = %s and hr_passwd = %s"

def staff_login(phone,psw):
    # 打开数据库连接
    db, cursor = connect_to_sql()
    try:
        cursor.execute(sql_s_login,(phone, psw))
        result = cursor.fetchone()
        cursor.close()
        db.close()
        return result
    except pymysql.Error as e:
        print(e)
        #错误则回滚
        db.rollback()
def hr_login(phone, psw):
    # 打开数据库连接
    db, cursor = connect_to_sql()
    try:
        cursor.execute(sql_h_login, (phone, psw))
        result = cursor.fetchone()
        cursor.close()
        db.close()
        return result
    except pymysql.Error as e:
        print(e)
        # 错误则回滚
        db.rollback()

if __name__ == '__main__':
    staff = list(hr_login("13510289812","123456"))
    print(staff[1])
