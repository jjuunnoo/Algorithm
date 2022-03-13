import datetime
import numpy as np

def solution(n, t, m, timetable):
    answer = ''
    suttle = {}
    timetable.sort()
    tmp = datetime.datetime.strptime('09:00', '%H:%M')
    for i in range(n):
        if i!=0:
            tmp += datetime.timedelta(minutes=t)
        suttle[tmp.strftime('%H:%M')] = m

    last_time = ''
    for time in timetable:
        for key in suttle.keys():
            if suttle[key] !=0 and time <= key:
                suttle[key] -=1
                break
        if list(suttle.values())[-1] == 0:
            last_time = datetime.datetime.strptime(time, '%H:%M')
            break

    if suttle[list(suttle.keys())[-1]] !=0:
        answer = list(suttle.keys())[-1]

    if last_time !='':
        last_time -= datetime.timedelta(minutes=1)
        answer = last_time.strftime('%H:%M')
    return answer