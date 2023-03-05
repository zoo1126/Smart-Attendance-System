import pymysql
import sys
from sql.mysqltest import *
from PyQt5.QtCore import QTimer,QDateTime
from sql.staff_sql import *

allStaffManagementFind_sql="select * from staff_management where sm_c_id=%s"
staffManagementFindex_sql='select * from staff_management where sm_id=%s'

staffManagementFindbyPhone_sql="select * from staff_management where sm_s_phone=%s and sm_c_id=%s"
staffManagementFindbyState_sql="select * from staff_management where sm_state=%s and sm_c_id=%s"
staffManagementFindbyDate_sql='select * from staff_management where sm_apply_datetime between %s and %s and sm_c_id=%s'
staffManagementFindbyDate_and_Phone_sql='select * from staff_management where sm_s_phone=%s and sm_apply_datetime between %s and %s and sm_c_id=%s'
staffManagementFindbyDate_and_State_sql='select * from staff_management where sm_state=%s and sm_apply_datetime between %s and %s and sm_c_id=%s'
staffManagementFindbyState_and_Phone_sql='select * from staff_management where sm_s_phone=%s and sm_state=%s and sm_c_id=%s'
staffManagementFindbyDate_and_Phone_and_State_sql='select * from staff_management where sm_s_phone=%s and sm_state=%s and sm_apply_datetime between %s and %s and sm_c_id=%s'

updateStaffManagementState_sql='update staff_management set sm_state=%s where sm_id=%s'
updateStaffManagementtreattime_sql='update staff_management set sm_treat_datetime=%s where sm_id=%s'
updateStaffManagementtreathrid_sql='update staff_management set sm_treat_hr_id=%s where sm_id=%s'

deleteStaffManagement_sql='delete from staff_management where sm_id=%s'


def allStaffManagementFind(com_id):
    db=connect()
    cursor=getcursor(db)
    try:
        cursor.execute(allStaffManagementFind_sql,com_id)
     #   db.commit()
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchall()
        print(data)
        cursor.close()
        db.close()
        return data
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (allStaffManagementFind_sql, e))
        return None

def staffManagementFindex(sm_id):
    db=connect()
    cursor=getcursor(db)
    try:
        cursor.execute(staffManagementFindex_sql,sm_id)
     #   db.commit()
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchone()
        print(data)
        cursor.close()
        db.close()
        return data
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (staffManagementFindex_sql, e))
        return None

def staffManagementFindbyPhone(c_id,sm_phone):
    db=connect()
    cursor=getcursor(db)
    try:
        cursor.execute(staffManagementFindbyPhone_sql,(sm_phone,c_id))
     #   db.commit()
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchall()
        print(data)
        cursor.close()
        db.close()
        return data
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (staffManagementFindbyPhone_sql, e))
        return None

def staffManagementFindbyState(c_id,sm_state):
    db=connect()
    cursor=getcursor(db)
    try:
        cursor.execute(staffManagementFindbyState_sql,(sm_state,c_id))
     #   db.commit()
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchall()
        print(data)
        cursor.close()
        db.close()
        return data
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (staffManagementFindbyState_sql, e))
        return None

def staffManagementFindbyDate(c_id,sm_date):
    db=connect()
    cursor=getcursor(db)
    bdate=sm_date+" 00:00:00"
    edate=sm_date+" 23:59:59"
    try:
        cursor.execute(staffManagementFindbyDate_sql,(bdate,edate,c_id))
     #   db.commit()
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchall()
        print(data)
        cursor.close()
        db.close()
        return data
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (staffManagementFindbyDate_sql, e))
        return None

def staffManagementFindbyDate_and_Phone(c_id,sm_date,phone):
    db=connect()
    cursor=getcursor(db)
    bdate=sm_date+" 00:00:00"
    edate=sm_date+" 23:59:59"
    try:
        cursor.execute(staffManagementFindbyDate_and_Phone_sql,(phone,bdate,edate,c_id))
     #   db.commit()
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchall()
        print(data)
        cursor.close()
        db.close()
        return data
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (staffManagementFindbyDate_and_Phone_sql, e))
        return None

def staffManagementFindbyDate_and_State(c_id,sm_date,state):
    db=connect()
    cursor=getcursor(db)
    bdate=sm_date+" 00:00:00"
    edate=sm_date+" 23:59:59"
    try:
        cursor.execute(staffManagementFindbyDate_and_State_sql,(state,bdate,edate,c_id))
     #   db.commit()
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchall()
        print(data)
        cursor.close()
        db.close()
        return data
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (staffManagementFindbyDate_and_State_sql, e))
        return None

def staffManagementFindbyState_and_Phone(c_id,sm_phone,state):
    db=connect()
    cursor=getcursor(db)
    try:
        cursor.execute(staffManagementFindbyState_and_Phone_sql,(sm_phone,state,c_id))
     #   db.commit()
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchall()
        print(data)
        cursor.close()
        db.close()
        return data
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (staffManagementFindbyState_and_Phone_sql, e))
        return None

def staffManagementFindbyDate_and_Phone_and_State(c_id,sm_date,phone,state):
    db=connect()
    cursor=getcursor(db)
    bdate=sm_date+" 00:00:00"
    edate=sm_date+" 23:59:59"
    try:
        cursor.execute(staffManagementFindbyDate_and_Phone_and_State_sql,(phone,state,bdate,edate,c_id))
     #   db.commit()
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchone()
        print(data)
        cursor.close()
        db.close()
        return data
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (staffManagementFindbyDate_and_Phone_and_State_sql, e))
        return None

def updateStaffManagementState(sm_state,sm_id):
    db = connect()
    cursor = getcursor(db)
    try:
        cursor.execute(updateStaffManagementState_sql, (sm_state,sm_id))
        db.commit()
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchone()
        # print(data)
        cursor.close()
        db.close()
        return True
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (updateStaffManagementState_sql, e))
        return False

def updateStaffManagementtreattime(sm_treat_datetime,sm_id):
    db = connect()
    cursor = getcursor(db)
    try:
        cursor.execute(updateStaffManagementtreattime_sql, (sm_treat_datetime,sm_id))
        db.commit()
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchone()
        # print(data)
        cursor.close()
        db.close()
        return True
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (updateStaffManagementtreattime_sql, e))
        return False

def updateStaffManagementtreathrid(sm_treat_hr_id,sm_id):
    db = connect()
    cursor = getcursor(db)
    try:
        cursor.execute(updateStaffManagementtreathrid_sql, (sm_treat_hr_id,sm_id))
        db.commit()
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchone()
        # print(data)
        cursor.close()
        db.close()
        return True
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (updateStaffManagementtreathrid_sql, e))
        return False

def updateStaffManagement(sm_state,sm_treat_datetime,sm_treat_hr_id,sm_id):
    db = connect()
    cursor = getcursor(db)
    try:
        cursor.execute(updateStaffManagementState_sql, (sm_state,sm_id))
        cursor.execute(updateStaffManagementtreattime_sql, (sm_treat_datetime, sm_id))
        cursor.execute(updateStaffManagementtreathrid_sql, (sm_treat_hr_id, sm_id))
        db.commit()
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchone()
        # print(data)
        cursor.close()
        db.close()
        return True
    except Exception as e:
        db.rollback()
        print("执行MySQL时出错：%s" % e)
        return False

def updateStaffManagementwithcom(com,phone,sm_state,sm_treat_datetime,sm_treat_hr_id,sm_id):
    db = connect()
    cursor = getcursor(db)
    try:
        cursor.execute(updatestaffcom_sql, (com, phone))
        cursor.execute(updateStaffManagementState_sql, (sm_state,sm_id))
        cursor.execute(updateStaffManagementtreattime_sql, (sm_treat_datetime, sm_id))
        cursor.execute(updateStaffManagementtreathrid_sql, (sm_treat_hr_id, sm_id))
        db.commit()
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchone()
        # print(data)
        cursor.close()
        db.close()
        return True
    except Exception as e:
        db.rollback()
        print("执行MySQL时出错：%s" % e)
        return False

def deleteStaffManagement(sm_id):
    db = connect()
    cursor = getcursor(db)
    try:
        cursor.execute(deleteStaffManagement_sql, sm_id)
        db.commit()
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchone()
        # print(data)
        cursor.close()
        db.close()
        return True
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (deleteStaffManagement_sql, e))
        return False

#staffManagementFindbyState_and_Phone('13046053122',0)