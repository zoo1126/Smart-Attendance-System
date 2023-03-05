from service import *

#提交申请
#type：1请假2出差3补打卡
def submitApply(phone, apply_time,  demand,  start_time, end_time,type):
    # 打开数据库连接
    db, cursor = connect_to_sql()
    # 查询语句
    insert_sql = "insert into message(m_s_phone,m_apply_datetime,m_type,m_demand,m_state,m_begin_datetime," \
                 "m_end_datetime,m_treat_hr_id) values(%s,%s,%s,%s,%s,%s,%s,%s) "
    data = (phone, apply_time, type, demand, 1, start_time, end_time, None)
    try:
        result=cursor.execute(insert_sql, data)
        db.commit()
        cursor.close()
        db.close()
        return result
    except ValueError as e:
        db.rollback()

def searchApply(type,state,phone):
    # 打开数据库连接
    db, cursor = connect_to_sql()
    print(type)
    print(state)
    print(phone)
    sql = ""
    data = ""
    results = []
    if type ==0 and state ==0:
        sql = "select m_type,m_apply_datetime,m_demand,m_state from message where m_s_phone = %s "
        data = phone
    else:
        if state==0:
            sql = "select m_type,m_apply_datetime,m_demand,m_state from message where m_s_phone = %s and m_type=%s"
            data = (phone, type)
        elif type==0:
            sql = "select m_type,m_apply_datetime,m_demand,m_state from message where m_s_phone = %s and m_state=%s"
            data = (phone, state)
        else:
            sql = "select m_type,m_apply_datetime,m_demand,m_state from message where m_s_phone = %s and m_type=%s " \
                  "and m_state=%s "
            data = (phone, type, state)

    try:
        cursor.execute(sql, data)
        db.commit()
        result=cursor.fetchall()
        print(result)
        cursor.close()
        db.close()
        return result
    except ValueError as e:
        db.rollback()

