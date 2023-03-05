import pymysql

from sql.mysqltest import *
from sql.department import *

allStaffFind_sql="select * from staff where s_com_id=%s"
staffFindunique_sql='select * from staff where s_phone=%s'
staffFindbyPhone_sql="select * from staff where s_phone=%s and s_com_id=%s"
staffFindbyName_sql="select * from staff where s_name REGEXP %s and s_com_id=%s"
staffFindbyDep_sql='select * from staff where s_depart_id=%s and s_com_id=%s'
staffFindbyPhoneandName_sql="select * from staff where s_phone=%s and s_name REGEXP %s and s_com_id=%s"
staffFindbyPhoneandDep_sql="select * from staff where s_phone=%s and s_depart_id=%s and s_com_id=%s"
staffFindbyDepandName_sql="select * from staff where s_depart_id=%s and s_name REGEXP %s and s_com_id=%s"
staffFindbyallselect_sql="select * from staff where s_phone=%s and s_depart_id=%s and s_name REGEXP %s and s_com_id=%s"

countAllstaff_sql='select count(*) as s_num from staff where staff.s_com_id=%s'
countDepstaff_sql='select count(*) as s_num from staff where staff.s_depart_id=%s and staff.s_com_id=%s'

updatestaffdep_sql='update staff set s_dep_id=%s where s_phone=%s and s_com_id=%s'
updatestaffcom_sql='update staff set s_com_id=%s where s_phone=%s'

updatestaffid_sql='update staff set s_id=%s where s_phone=%s and s_com_id=%s'
updatestaffdepartid_sql='update staff set s_depart_id=%s where s_phone=%s and s_com_id=%s'
updatestaffposition_sql='update staff set s_position=%s where s_phone=%s and s_com_id=%s'
updatestaffsalary_sql='update staff set s_salary=%s where s_phone=%s and s_com_id=%s'

deletestaff_sql='update staff set s_com_id= NULL , s_id= NULL ,s_depart_id=NULL, s_position=NULL , s_salary=NULL where s_phone=%s'





def allStaffFind(com_id):
    db=connect()
    cursor=getcursor(db)
    try:
        cursor.execute(allStaffFind_sql,com_id)
     #   db.commit()
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchall()
        print(data)
        cursor.close()
        db.close()
        return data
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (allStaffFind_sql, e))
        return None

def staffFindbyPhone(phone,com_id):
    db=connect()
    cursor=getcursor(db)
    try:
        cursor.execute(staffFindbyPhone_sql,(phone,com_id))
     #   db.commit()
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchall()
        print(data)
        cursor.close()
        db.close()
        return data
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (staffFindbyPhone_sql, e))
        return None

def staffFindunique(phone):
    db=connect()
    cursor=getcursor(db)
    try:
        cursor.execute(staffFindunique_sql,phone)
     #   db.commit()
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchone()
        cursor.close()
        db.close()
        return data
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (staffFindunique_sql, e))
        return None

def staffFindbyName(name,com_id):
    db=connect()
    cursor=getcursor(db)

    if len(name)==0 or name.isspace():
        return None
    name = name.strip()
    namelist=str(name).split(" ")
    data=()
    try:
        for i in namelist:
            cursor.execute(staffFindbyName_sql,(i,com_id))
            data = data + cursor.fetchall()
        print(data)
        cursor.close()
        db.close()
        return data
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (staffFindbyName_sql, e))

def staffFindbyDep(depname,com_id):
    db=connect()
    cursor=getcursor(db)
    data=findDepbyName(depname,com_id)
    list=()
    try:
        for i in data:
            cursor.execute(staffFindbyDep_sql,(i[0],com_id))
     #   db.commit()
        # 使用 fetchone() 方法获取单条数据.
            t = cursor.fetchall()
            list = list + t
        cursor.close()
        db.close()
        return list
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (staffFindbyDep_sql, e))
        return None

def staffFindbyDepid(dep_id,com_id):
    db=connect()
    cursor=getcursor(db)
    try:
        cursor.execute(staffFindbyDep_sql,(dep_id,com_id))
        list = cursor.fetchall()
        cursor.close()
        db.close()
        return list
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (staffFindbyDep_sql, e))
        return None

def staffFindbyPhoneandName(phone,name,com_id):
    db=connect()
    cursor=getcursor(db)
    try:
        cursor.execute(staffFindbyPhoneandName_sql,(phone,name,com_id))
     #   db.commit()
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchall()
        print(data)
        cursor.close()
        db.close()
        return data
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (staffFindbyPhoneandName_sql, e))
        return None

def staffFindbyPhoneandDep(phone,depname,com_id):
    db=connect()
    cursor=getcursor(db)
    list=findDepbyName(depname,com_id)
    data=()
    try:
        for i in list:
            cursor.execute(staffFindbyPhoneandDep_sql,(phone,i[0],com_id))
            t = cursor.fetchall()
            data=data+t
        print(data)
        cursor.close()
        db.close()
        return data
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (staffFindbyPhoneandDep_sql, e))
        return None

def staffFindbyDepandName(depname,name,com_id):
    db=connect()
    cursor=getcursor(db)
    list=findDepbyName(depname,com_id)
    data=()
    try:
        for i in list:
            cursor.execute(staffFindbyDepandName_sql,(i[0],name,com_id))
            t = cursor.fetchall()
            data=data+t
        print(data)
        cursor.close()
        db.close()
        return data
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (staffFindbyDepandName_sql, e))
        return None

def staffFindbyallselect(phone,depname,name,com_id):
    db=connect()
    cursor=getcursor(db)
    list=findDepbyName(depname,com_id)
    data=()
    try:
        for i in list:
            cursor.execute(staffFindbyallselect_sql,(phone,i[0],name,com_id))
            t = cursor.fetchall()
            data=data+t
        print(data)
        cursor.close()
        db.close()
        return data
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (staffFindbyallselect_sql, e))
        return None


def countAllstaff(com_id):
    db = connect()
    cursor = getcursor(db)
    num=0
    try:
        cursor.execute(countAllstaff_sql, com_id)
        num=cursor.fetchone()[0]
        cursor.close()
        db.close()
        return num
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (countAllstaff_sql, e))
        return 0

def countDepstaff(dep,com_id):
    db = connect()
    cursor = getcursor(db)
    deplist=findDepbyName(dep,com_id)
    if deplist!=None and len(deplist)!=0:
        num=0
        try:
            cursor.execute(countDepstaff_sql,(deplist[0][0] , com_id))
            num=cursor.fetchone()[0]
            cursor.close()
            db.close()
            return num
        except Exception as e:
            db.rollback()
            print("执行MySQL: %s 时出错：%s" % (countDepstaff_sql, e))
            return 0
    else:
        return 0


def updatestaffcom(com,phone):
    db=connect()
    cursor=getcursor(db)
    try:
        cursor.execute(updatestaffcom_sql,(com,phone))
        db.commit()
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchall()
        cursor.close()
        db.close()
        return True
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (updatestaffcom_sql, e))
        return False

def updatestaffid(id,com,phone):
    db=connect()
    cursor=getcursor(db)
    try:
        cursor.execute(updatestaffid_sql,(id,phone,com))
        db.commit()
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchall()
        cursor.close()
        db.close()
        return True
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (updatestaffid_sql, e))
        return False

def updatestaffdepartid(depid,com, phone):
    db = connect()
    cursor = getcursor(db)
    try:
        cursor.execute(updatestaffdepartid_sql, (depid, phone,com))
        db.commit()
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchall()
        cursor.close()
        db.close()
        return True
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (updatestaffdepartid_sql, e))
        return False

def updatestaffposition(pos,com,phone):
    db=connect()
    cursor=getcursor(db)
    try:
        cursor.execute(updatestaffposition_sql,(pos,phone,com))
        db.commit()
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchall()
        cursor.close()
        db.close()
        return True
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (updatestaffposition_sql, e))
        return False

def updatestaffsalary(sal,com,phone):

    db=connect()
    cursor=getcursor(db)
    try:
        cursor.execute(updatestaffsalary_sql,(sal,phone,com))
        db.commit()
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchall()
        cursor.close()
        db.close()
        return True
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (updatestaffsalary_sql, e))
        return False

def updatestaff(sign1, sign2, sign3, sign4, id, depid, pos, sal, com, phone):
    db = connect()
    cursor = getcursor(db)
    try:
        if sign1:
            cursor.execute(updatestaffid_sql, (id, phone, com))

        if sign2:
            cursor.execute(updatestaffdepartid_sql, (depid, phone, com))
        if sign3:
            cursor.execute(updatestaffposition_sql, (pos, phone, com))
        if sign4:
            cursor.execute(updatestaffsalary_sql, (sal, phone, com))
        print(1111)
        db.commit()
        cursor.close()
        db.close()
        return True
    except Exception as e:
        db.rollback()
        print("执行MySQL时出错：%s" % e)
        return False



def deletestaff(phone):
    db=connect()
    cursor=getcursor(db)
    try:
        cursor.execute(deletestaff_sql,phone)
        db.commit()
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchall()
        cursor.close()
        db.close()
        return True
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (deletestaff_sql, e))
        return False

if __name__ == '__main__':
    data=updatestaffsalary('NULL','91110108MA01GHM95K','13046053122')
    if data:
        print("weikong")
