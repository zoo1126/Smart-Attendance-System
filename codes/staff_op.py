from sql.staff_sql import *

def updateStaff(olddep,newdep):

    if olddep.getPhone()!=newdep.getPhone():
        print("不能修改")
    if newdep.getId() is not None:
        print(newdep.getId())
        sign1=True
    else:
        sign1=False
    if newdep.getDepartid() is not None:
        sign2=True
    else:
        sign2=False
    if  newdep.getPosition() is not None:
        sign3=True
    else:
        sign3=False
    if newdep.getSalary() is not None:
        if newdep.getSalary() is not None and is_number(newdep.getSalary()):
            salary=float(newdep.getSalary())
            print(salary)
            if salary<0:
                print("salary is negative")
                return False
            elif salary>999999:
                print("salary is too big")
                return False
            else:
                salary=round(salary,2)
                print(salary)
                print(olddep.getComid())
                print(olddep.getPhone())
                sign4=True
        else:
            salary=None
    else:
        sign4=False
    res=updatestaff(sign1,sign2,sign3,sign4,newdep.getId(),newdep.getDepartid(), newdep.getPosition(),salary, olddep.getComid(), olddep.getPhone())
    return res





def is_number(s):
    try:  # 如果能运行float(s)语句，返回True（字符串s是浮点数）
        float(s)
        return True
    except ValueError:  # ValueError为Python的一种标准异常，表示"传入无效的参数"
        pass  # 如果引发了ValueError这种异常，不做任何事情（pass：不做任何事情，一般用做占位语句）
    try:
        import unicodedata  # 处理ASCii码的包
        unicodedata.numeric(s)  # 把一个表示数字的字符串转换为浮点数返回的函数
        return True
    except (TypeError, ValueError):
        pass
    return False

