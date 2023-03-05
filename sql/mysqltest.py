import pymysql

def connect():
    # 打开数据库连接
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='123456',
                         database='kaoqin_db')
    return db
def getcursor(db):
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    return cursor