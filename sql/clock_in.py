from service import *

sql_ci="insert into dailyattendance(att_s_phone,att_datetime,att_state) values(%s,%s,%s))"

#插入打卡记录
def insert_clock(phone, datetime, state):
    # 打开数据库连接
    db, cursor = connect_to_sql()
    try:
        cursor.execute(sql_ci, (phone, datetime, state))
        db.commit()
        cursor.close()
        db.close()
        return True
    except pymysql.Error as e:
        print(e)
        #错误则回滚
        db.rollback()
        return False