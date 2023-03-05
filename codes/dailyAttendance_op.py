from sql.dailyAttendance_sql import *

def updatedailyAttendance(oldatt,newatt):

    if newatt.getAttState()=='已打卡':
        state = 1
    elif newatt.getAttState()=='迟到':
        state = 2
    elif newatt.getAttState()=='请假':
        state = 3
    elif newatt.getAttState()=='外勤':
        state = 4
    else:
        state = 0
    res2 = updateDailyAttendance(oldatt.getId(),newatt.getDatetime(), state)
    if res2:
        return True
    else:
        return False