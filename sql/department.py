import pymysql
from sql.mysqltest import *


findDeps_sql='select * from department where dep_com_id=%s'
findDepbyId_sql='select * from department where dep_id=%s and dep_com_id=%s'
findDepbyName_sql='select * from department where dep_name REGEXP %s and dep_com_id=%s'
createDep_sql="insert into department (dep_com_id,dep_name,dep_start_time,dep_end_time) values(%s,%s,%s,%s) "
updateDepName_sql="update department set dep_name=%s where dep_id=%s"
updateDepStart_sql="update department set dep_start_time=%s where dep_id=%s"
updateDepEnd_sql="update department set dep_end_time=%s where dep_id=%s"
deleteDep_sql="delete from department where dep_id=%s"

def findDeps(com_id):
    db=connect()
    cursor=getcursor(db)
    try:
        cursor.execute(findDeps_sql,com_id)
     #   db.commit()
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchall()
        cursor.close()
        db.close()
        return data
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (findDeps_sql, e))

def findDepbyId(dep_id,comid):
    db=connect()
    cursor=getcursor(db)
    try:
        cursor.execute(findDepbyId_sql,(dep_id,comid))
        #   db.commit()
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchone()

        cursor.close()
        db.close()
        return data
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (findDepbyId_sql, e))

def findDepbyName(dep_name,com_id):
    db=connect()
    cursor=getcursor(db)
    if len(dep_name)==0 or dep_name.isspace():
        return None
    dep_name = dep_name.strip()
    namelist=str(dep_name).split(" ")
    data=()
    try:
        for i in namelist:
            cursor.execute(findDepbyName_sql,(i,com_id))
            data = data + cursor.fetchall()
        print(data)
        cursor.close()
        db.close()
        return data
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (findDepbyName_sql, e))

def createDep(com_id,name,starttime,endtime):
    db = connect()
    cursor = getcursor(db)
    try:
        cursor.execute(createDep_sql, (com_id, name, starttime, endtime))
        db.commit()
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchone()
        # print(data)
        cursor.close()
        db.close()
        return True
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (createDep_sql, e))
        return False

def updateDepName(newname,dep_id):
    db = connect()
    cursor = getcursor(db)
    try:
        cursor.execute(updateDepName_sql, (newname,dep_id))
        db.commit()
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchone()
        # print(data)
        cursor.close()
        db.close()
        return True
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (updateDepName_sql, e))
        return False


def updateDepStart(starttime,dep_id):
    db = connect()
    cursor = getcursor(db)
    try:
        cursor.execute(updateDepStart_sql, (starttime,dep_id))
        db.commit()
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchone()
        # print(data)
        cursor.close()
        db.close()
        return True
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (updateDepStart_sql, e))
        return False


def updateDepEnd(endtime,dep_id):
    db = connect()
    cursor = getcursor(db)
    try:
        cursor.execute(updateDepEnd_sql, (endtime,dep_id))
        db.commit()
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchone()
        # print(data)
        cursor.close()
        db.close()
        return True
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (updateDepEnd_sql, e))
        return False

def updateDep(newname,starttime,endtime,dep_id):
    db = connect()
    cursor = getcursor(db)
    try:
        cursor.execute(updateDepName_sql, (newname, dep_id))
        cursor.execute(updateDepStart_sql, (starttime, dep_id))
        cursor.execute(updateDepEnd_sql, (endtime, dep_id))
        db.commit()
        # 使用 fetchone() 方法获取单条数据.

        # print(data)
        cursor.close()
        db.close()
        return True
    except Exception as e:
        db.rollback()
        print("执行MySQL时出错：%s" % e)
        return False


def deleteDep(dep_id):
    db = connect()
    cursor = getcursor(db)
    try:
        cursor.execute(deleteDep_sql, dep_id)
        db.commit()
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchone()
        # print(data)
        cursor.close()
        db.close()
        return True
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (deleteDep_sql, e))
        return False



if __name__ == '__main__':
    findDepbyName('财务部','91110105MA01GHN16Q')