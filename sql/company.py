from datetime import datetime
import pymysql
from sql.mysqltest import *
from service import *

sql_nc = "insert into company(c_id,c_hr_phone,c_name,c_phone,c_type,c_location) values (%s,%s,%s,%s,%s,%s)"
sql_uc = "update company set c_id=%s,c_name=%s,c_phone=%s,c_type=%s,c_location=%s where c_hr_phone=%s"
sql_info = "select * from company where c_hr_phone=%s"
sql_dc = "DELETE FROM company WHERE c_hr_phone=%s"
sql_ac = "select c_name, c_type, c_location, c_id from company"
findCom_idbyhr_id_sql = 'select c_id from company where c_hr_phone=%s'

#新建公司
def new_company(name, id, location, phone, type, hr_phone):
    # 打开数据库连接
    db, cursor = connect_to_sql()
    try:
        cursor.execute(sql_nc, (id, hr_phone, name, phone, type, location))
        db.commit()
        cursor.close()
        db.close()
        return True
    except pymysql.Error as e:
        print(e)
        #错误则回滚
        db.rollback()
        return False
#更新公司信息
def update_company(name, id, location, phone, type, hr_phone):
    # 打开数据库连接
    db, cursor = connect_to_sql()
    try:
        cursor.execute(sql_uc, (id, name, phone, type, location, hr_phone))
        db.commit()
        cursor.close()
        db.close()
        return True
    except pymysql.Error as e:
        print(e)
        # 错误则回滚
        db.rollback()
        return False
#显示公司信息
def show_c_info(hr_phone):
    # 打开数据库连接
    db, cursor = connect_to_sql()
    try:
        cursor.execute(sql_info, (hr_phone))
        result = cursor.fetchone()
        cursor.close()
        db.close()
        return result
    except pymysql.Error as e:
        print(e)
        # 错误则回滚
        db.rollback()
#注销公司
def delete_company(hr_phone):
    # 打开数据库连接
    db, cursor = connect_to_sql()
    try:
        cursor.execute(sql_dc, (hr_phone))
        db.commit()
        cursor.close()
        db.close()
        return True
    except pymysql.Error as e:
        print(e)
        # 错误则回滚
        db.rollback()
        return False
#查找全部公司
def select_all():
    # 打开数据库连接
    db, cursor = connect_to_sql()
    try:
        cursor.execute(sql_ac)
        result = cursor.fetchall()
        cursor.close()
        db.close()
        return result
    except pymysql.Error as e:
        print(e)
        # 错误则回滚
        db.rollback()
#申请加入公司（如果有staff_management.py最好将以下方法放回那里去）
sql_apply = "insert into staff_management(sm_s_phone,sm_c_id,sm_type,sm_state,sm_apply_datetime) value (%s,%s,%s,%s,%s)"
def apply_company(phone,id):
    time = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
    # 打开数据库连接
    db, cursor = connect_to_sql()
    try:
        cursor.execute(sql_apply,(phone, id, 0, 0, time))
        db.commit()
        cursor.close()
        db.close()
        return True
    except pymysql.Error as e:
        print(e)
        # 错误则回滚
        db.rollback()
        return False

sql_hc = "select c_id from company where c_hr_phone = %s"
# 查找HR是否有公司
def has_company(hr_phone):
    # 打开数据库连接
    db, cursor = connect_to_sql()
    try:
        cursor.execute(sql_hc, (hr_phone))
        result = cursor.fetchone()
        if result:
            print(result)
        cursor.close()
        db.close()
        return result
    except pymysql.Error as e:
        print(e)
        # 错误则回滚
        db.rollback()




def findCom_idbyhr_id(hr_phone):
    db = connect()
    cursor = getcursor(db)
    try:
        cursor.execute(findCom_idbyhr_id_sql, hr_phone)
        #   db.commit()
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchall()
        cursor.close()
        db.close()
        return data
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (findCom_idbyhr_id_sql, e))

if __name__ == '__main__':
    time = datetime.now()
    print(time)
    time = datetime.strftime(time, '%Y-%m-%d %H:%M:%S')
    print(time)

