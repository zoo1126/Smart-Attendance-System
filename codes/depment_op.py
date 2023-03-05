from sql.department import *

from PyQt5 import QtCore, QtGui, QtWidgets


def findDepartment(depart_txt,com_id):
    if depart_txt is None or len(depart_txt)== 0 or depart_txt.isspace():
        print("depart_txt empty")
        return None
    data =()
    if depart_txt.isdigit():
        data = findDepbyId(depart_txt,com_id)
        if data is not None:
            data = data + findDepbyName(depart_txt, com_id)
        else:
            data =findDepbyName(depart_txt, com_id)
    else:
        data = findDepbyName(depart_txt, com_id)
    return data

def deleteDepartment(depart_txt):
    if depart_txt is None or len(depart_txt)== 0 or depart_txt.isspace():
        print("depart_txt empty")
        return None
    res=deleteDep(depart_txt)
    return res

def updateDepartment(olddep,newdep):
    if olddep.getDep_id()!=newdep.getDep_id():
        print("不能修改")
    if olddep.getCom_id()!=newdep.getCom_id():
        print("不能修改")
    if newdep.getDep_name() is None or newdep.getStarttime() is None or newdep.getEndtime() is None:
        return False
    res=updateDep(newdep.getDep_name(),newdep.getStarttime(),newdep.getEndtime(),olddep.getDep_id())

    if res:
        return True
    else:
        return False
