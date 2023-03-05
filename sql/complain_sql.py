import pymysql
from sql.mysqltest import *
from sql.staff_sql import *
from sql.dailyAttendance_sql import *
findcomplainApply_sql='select * from message where m_type=3 and m_s_phone=%s'
findApplybyState_sql='select * from message where m_type=3 and m_state=%s and m_s_phone=%s'
findApplybyTime_sql='select * from message where m_type=3 and m_apply_datetime between %s and %s  and m_s_phone=%s'
findApplybyStateandTime_sql='select * from message where m_type=3 and m_state=%s and m_apply_datetime between %s and %s and m_s_phone=%s'
findApplybyEx_sql="select * from message where m_id=%s"

updateReduseApply_sql="update message set m_state=3 where m_id=%s"
updateAgreeApply_sql="update message set m_state=2 where m_id=%s"
updatetreathrid_sql="update message set m_treat_hr_id=%s where m_id=%s"
deleteApply_sql="delete from message where m_id=%s"

def findAllcomplainApply(com_id):
    db = connect()
    cursor = getcursor(db)
    stafflist=allStaffFind(com_id)
    list = ()
    try:
        for i in stafflist:
            cursor.execute(findcomplainApply_sql, i[0])
            t= cursor.fetchall()
            list=list+t
        cursor.close()
        db.close()
        print(list)
        return list

    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (findcomplainApply_sql, e))
        return None

def findApplybyState(state,com_id):
    db = connect()
    cursor = getcursor(db)
    stafflist = allStaffFind(com_id)
    print(state)
    list = ()
    try:
        for i in stafflist:
            cursor.execute(findApplybyState_sql, (state,i[0]))
            t = cursor.fetchall()
            list = list + t
        cursor.close()
        db.close()
        print(list)
        return list

    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (findApplybyState_sql, e))
        return None

def findApplybyTime(begintime,endtime,com_id):
    db = connect()
    cursor = getcursor(db)
    stafflist = allStaffFind(com_id)

    list = ()
    try:
        for i in stafflist:
            cursor.execute(findApplybyTime_sql, (begintime,endtime,i[0]))
            t = cursor.fetchall()
            list = list + t
        cursor.close()
        db.close()
        print(list)
        return list

    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (findApplybyTime_sql, e))
        return None

def findApplybyStateandTime(state,startdatetime,enddatetime,com_id):
    db = connect()
    cursor = getcursor(db)
    stafflist = allStaffFind(com_id)
    print(state)
    list = ()
    try:
        for i in stafflist:
            cursor.execute(findApplybyStateandTime_sql, (state,startdatetime,enddatetime,i[0]))
            t = cursor.fetchall()
            list = list + t
        cursor.close()
        db.close()
        print(list)
        return list

    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (findApplybyStateandTime_sql, e))
        return None

def findApplybyPhone(phone,com_id):
    db = connect()
    cursor = getcursor(db)
    stafflist = allStaffFind(com_id)
    list = ()
    try:
        for i in stafflist:
            if phone==i[0]:
                cursor.execute(findcomplainApply_sql, phone)
                t = cursor.fetchall()
                list = list + t
        cursor.close()
        db.close()
        print(list)
        return list

    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (findcomplainApply_sql, e))
        return None

def findApplybyEx(m_id):
    db = connect()
    cursor = getcursor(db)
    try:
        cursor.execute(findApplybyEx_sql, m_id)
        list=cursor.fetchone()
        cursor.close()
        db.close()
        return list

    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (findApplybyEx_sql, e))
        return None

def updateRefuseApply(hr_id,m_id):
    db = connect()
    cursor = getcursor(db)
    try:

        cursor.execute(updateReduseApply_sql, m_id)
        cursor.execute(updatetreathrid_sql,(hr_id,m_id))
        db.commit()
        cursor.close()
        db.close()
        return True

    except Exception as e:
        db.rollback()
        print("执行MySQL时出错：%s" %e)
        return False

def updateAgreeApply(phone,begintime,endtime,hr_id,m_id):
    db = connect()
    cursor = getcursor(db)
    try:
        cursor.execute(updateDailyAtt_sql, (phone, begintime, endtime))
        cursor.execute(updateAgreeApply_sql, m_id)
        cursor.execute(updatetreathrid_sql, (hr_id, m_id))
        db.commit()
        cursor.close()
        db.close()
        return True

    except Exception as e:
        db.rollback()
        print("执行MySQL时出错：%s" %e)
        return False

def updatetreathrid(hr_id,m_id):
    db = connect()
    cursor = getcursor(db)
    try:
        t=cursor.execute(updatetreathrid_sql, (hr_id,m_id))
        db.commit()
        cursor.close()
        db.close()
        return True

    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (updatetreathrid_sql, e))
        return False

def deleteApply(m_id):
    db = connect()
    cursor = getcursor(db)
    try:
        t = cursor.execute(deleteApply_sql,  m_id)
        db.commit()
        cursor.close()
        db.close()
        return True

    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (deleteApply_sql, e))
        return False

