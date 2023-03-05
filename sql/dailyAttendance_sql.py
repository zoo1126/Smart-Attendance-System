import pymysql
from sql.mysqltest import *
from sql.staff_sql import *

from entity.dailyAttendance_entity import *

findAllDailyAtt_sql='select * from dailyAttendance where att_s_phone=%s'
findDailyAttbyId_sql='select * from dailyAttendance where att_id=%s'
findDailyAttbydatetime_sql='select * from dailyAttendance where att_datetime between %s and %s and att_s_phone=%s'
countAllDailyAtt_sql='select att_state,count(*) as att_count from dailyAttendance LEFT JOIN staff on att_s_phone=s_phone where s_com_id=%s and att_datetime between %s and %s GROUP BY att_state'
countDepDailyAtt_sql='select att_state,count(*) as att_count from dailyAttendance LEFT JOIN staff on att_s_phone=s_phone where s_com_id=%s and s_depart_id=%s and att_datetime between %s and %s GROUP BY att_state'
findIndDailyAtt_sql='select * from dailyAttendance LEFT JOIN staff on att_s_phone=s_phone where s_com_id=%s and att_s_phone=%s and att_datetime between %s and %s'
insertDailyAtt_sql="insert into dailyAttendance (att_s_phone,att_datetime,att_state) values(%s,%s,%s)"
updateDailyAtt_time_sql="update dailyAttendance set att_datetime=%s where att_id=%s"
updateDailyAtt_state_sql='update dailyAttendance set att_state=%s where att_id=%s'
updateDailyAtt_sql='update dailyAttendance set att_state=1 where att_s_phone=%s and att_datetime between %s and %s'
deleteDailyAtt_sql='delete from dailyAttendance where att_id=%s'



def findAllDailyAtt(com_id):
    db = connect()
    cursor = getcursor(db)
    stafflist=allStaffFind(com_id)
    list = []
    try:
        for i in stafflist:
            cursor.execute(findAllDailyAtt_sql, i[0])
            att_list=cursor.fetchall()
            for oneline in att_list:
                one_att=dailyAttendance()
                one_att.setcomid(com_id)
                one_att.setId(oneline[0])
                one_att.sets_Phone(oneline[1])
                one_att.setDatetime(oneline[2])
                one_att.setAttState(oneline[3])
                list.append(one_att)

        cursor.close()
        db.close()
        return list
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (findAllDailyAtt_sql, e))
        return None

def findDailyAttbyId(att_id,com_id):
    db = connect()
    cursor = getcursor(db)

    try:
        cursor.execute(findDailyAttbyId_sql, att_id)
        attone=cursor.fetchone()

        one_att=dailyAttendance()
        one_att.setcomid(com_id)
        one_att.setId(attone[0])
        one_att.sets_Phone(attone[1])
        one_att.setDatetime(attone[2])
        one_att.setAttState(attone[3])

        cursor.close()
        db.close()
        return one_att
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (findDailyAttbyId_sql, e))
        return None

def findDailyAttbydatetime(startdatetime,enddatetime,com_id):
    db = connect()
    cursor = getcursor(db)
    stafflist = allStaffFind(com_id)

    list = []
    try:
        for i in stafflist:
            cursor.execute(findDailyAttbydatetime_sql, (startdatetime,enddatetime,i[0]))
            att_list = cursor.fetchall()

            for oneline in att_list:
                one_att = dailyAttendance()
                one_att.setcomid(com_id)
                one_att.setId(oneline[0])
                one_att.sets_Phone(oneline[1])
                one_att.setDatetime(oneline[2])
                one_att.setAttState(oneline[3])
                list.append(one_att)
        cursor.close()
        db.close()
        return list
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (findDailyAttbydatetime_sql, e))
        return None

def findDailyAttbydatetime_and_dep(startdatetime,enddatetime,dep_name,com_id):
    db = connect()
    cursor = getcursor(db)
    stafflist = staffFindbyDep(dep_name,com_id)

    list = []
    try:
        for i in stafflist:
            cursor.execute(findDailyAttbydatetime_sql, (startdatetime,enddatetime,i[0]))
            att_list = cursor.fetchall()

            for oneline in att_list:
                one_att = dailyAttendance()
                one_att.setcomid(com_id)
                one_att.setId(oneline[0])
                one_att.sets_Phone(oneline[1])
                one_att.setDatetime(oneline[2])
                one_att.setAttState(oneline[3])
                list.append(one_att)
        cursor.close()
        db.close()
        return list
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (findDailyAttbydatetime_sql, e))
        return None

def findDailyAttbyphoneorname(phone_or_name,com_id):
    db = connect()
    cursor = getcursor(db)
    stafflist1 = staffFindbyName(phone_or_name,com_id)
    stafflist2 = staffFindbyPhone(phone_or_name,com_id)
    stafflist=tuple(set(stafflist1+stafflist2))
    list = []
    try:
        for i in stafflist:
            cursor.execute(findAllDailyAtt_sql, i[0])
            att_list = cursor.fetchall()

            for oneline in att_list:
                one_att = dailyAttendance()
                one_att.setcomid(com_id)
                one_att.setId(oneline[0])
                one_att.sets_Phone(oneline[1])
                one_att.setDatetime(oneline[2])
                one_att.setAttState(oneline[3])
                list.append(one_att)
        cursor.close()
        db.close()
        return list
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (findAllDailyAtt_sql, e))
        return None

def findDailyAttbyphoneorname_and_datetime(phone_or_name, startdatetime, enddatetime, com_id):
    db = connect()
    cursor = getcursor(db)
    stafflist1 = staffFindbyName(phone_or_name,com_id)
    stafflist2 = staffFindbyPhone(phone_or_name,com_id)
    stafflist=tuple(set(stafflist1+stafflist2))
    list = []
    try:
        for i in stafflist:
            cursor.execute(findDailyAttbydatetime_sql, (startdatetime, enddatetime, i[0]))
            att_list = cursor.fetchall()

            for oneline in att_list:
                one_att = dailyAttendance()
                one_att.setcomid(com_id)
                one_att.setId(oneline[0])
                one_att.sets_Phone(oneline[1])
                one_att.setDatetime(oneline[2])
                one_att.setAttState(oneline[3])
                list.append(one_att)
        cursor.close()
        db.close()
        return list
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (findDailyAttbydatetime_sql, e))
        return None

def findDailyAttbydep(dep_name,com_id):
    db = connect()
    cursor = getcursor(db)
    stafflist = staffFindbyDep(dep_name,com_id)

    list = []
    try:
        for i in stafflist:
            cursor.execute(findAllDailyAtt_sql, i[0])
            att_list = cursor.fetchall()

            for oneline in att_list:
                one_att = dailyAttendance()
                one_att.setcomid(com_id)
                one_att.setId(oneline[0])
                one_att.sets_Phone(oneline[1])
                one_att.setDatetime(oneline[2])
                one_att.setAttState(oneline[3])
                list.append(one_att)
        cursor.close()
        db.close()
        return list
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (findAllDailyAtt_sql, e))
        return None

def countAllDailyAtt(com_id,starttime,endtime):
    db = connect()
    cursor = getcursor(db)
    dictionary={}
    try:
        cursor.execute(countAllDailyAtt_sql, (com_id,starttime,endtime))
        att_list=cursor.fetchall()
        for oneline in att_list:
            state=oneline[0]
            num=oneline[1]
            dictionary[state]=num
        cursor.close()
        db.close()
        return dictionary
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (countAllDailyAtt_sql, e))
        return None

def countDepDailyAtt(com_id,depname,starttime,endtime):
    db = connect()
    cursor = getcursor(db)
    dep_list=findDepbyName(depname,com_id)
    dictionary={}
    try:
        for onedep in dep_list:
            cursor.execute(countDepDailyAtt_sql, (com_id,onedep[0],starttime,endtime))
            att_list=cursor.fetchall()
            for oneline in att_list:
                state=oneline[0]
                num=oneline[1]
                dictionary[state]=num
        cursor.close()
        db.close()
        return dictionary
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (countDepDailyAtt_sql, e))
        return None

def findIndDailyAtt(com_id,phone,starttime,endtime):
    db = connect()
    cursor = getcursor(db)
    dictionary=[]
    try:
        cursor.execute(findIndDailyAtt_sql, (com_id,phone,starttime,endtime))
        att_list=cursor.fetchall()
        for oneline in att_list:
            dictionary.append(oneline)
        cursor.close()
        db.close()
        return dictionary
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (findIndDailyAtt_sql, e))
        return None

def updateDailyAtt_time(dep_id, datetime):
    db = connect()
    cursor = getcursor(db)
    try:
        cursor.execute(updateDailyAtt_time_sql, (datetime, dep_id))
        db.commit()
        cursor.close()
        db.close()
        return True
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (updateDailyAtt_time_sql, e))
        return False

def updateDailyAtt_state(dep_id,state):
    db = connect()
    cursor = getcursor(db)
    try:
        cursor.execute(updateDailyAtt_state_sql, (state, dep_id))
        db.commit()
        cursor.close()
        db.close()
        return True
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (updateDailyAtt_state_sql, e))
        return False


def updateDailyAttendance(dep_id,datetime,state):
    db = connect()
    cursor = getcursor(db)
    try:
        cursor.execute(updateDailyAtt_time_sql, (datetime, dep_id))
        cursor.execute(updateDailyAtt_state_sql, (state, dep_id))
        db.commit()
        cursor.close()
        db.close()
        return True
    except Exception as e:
        db.rollback()
        print("执行MySQL时出错：%s" % e)
        return False

def updateDailyAtt(phone, begintime, endtime):
    db = connect()
    cursor = getcursor(db)
    try:
        cursor.execute(updateDailyAtt_sql, (phone, begintime, endtime))
        db.commit()
        cursor.close()
        db.close()
        return True
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (updateDailyAtt_sql, e))
        return False



def insertDailyAtt(phone,datetime,state):
    db = connect()
    cursor = getcursor(db)
    try:
        cursor.execute(insertDailyAtt_sql, (phone,datetime,state))
        db.commit()
        cursor.close()
        db.close()
        return True
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (insertDailyAtt_sql, e))
        return False


def deleteDailyAtt(att_id):
    db = connect()
    cursor = getcursor(db)
    try:
        cursor.execute(deleteDailyAtt_sql, att_id)
        db.commit()
        cursor.close()
        db.close()
        return True
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (deleteDailyAtt_sql, e))
        return False

