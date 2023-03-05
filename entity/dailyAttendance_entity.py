from sql.staff_sql import *
from sql.department import *
class dailyAttendance:
    comid=""
    def initatt(self,id,phone,name,datetime,state):
        self.id=id
        self.phone=phone
        self.name=name
        self.datetime=datetime
        self.state=state

    def setId(self,id):
        self.id=id

    def getId(self):
        return self.id

    def sets_Phone(self,phone):
        self.phone=phone
        if self.phone is not None and len(self.phone) != 0:
            gettuple = staffFindunique(self.phone)
            name = gettuple[2]
            dep_id=gettuple[6]
            self.sets_Name(name)
            self.sets_Depid(dep_id)

    def gets_Phone(self):
        return self.phone

    def setDatetime(self,att_datetime):
        self.att_datetime=att_datetime

    def getDatetime(self):
        return self.att_datetime

    def setAttState(self,state):
        self.state=state

    def getAttState(self):
        return self.state

    def sets_Name(self,name):
        self.name=name

    def gets_Name(self):
        return self.name

    def sets_Depid(self,dep_id):
        self.dep_id=dep_id
        if dep_id is not None:
            gettuple=findDepbyId(self.dep_id,self.getcomid())
            self.sets_Depname(gettuple[2])
        else:
            self.sets_Depname(None)


    def gets_Depid(self):
        return self.dep_id

    def sets_Depname(self,dep_name):
        self.dep_name=dep_name

    def gets_Depname(self):
        return self.dep_name

    def setcomid(self,comid):
        self.comid=comid

    def getcomid(self):
        return self.comid