import sys
import datetime

h, m = sys.stdin.readline().split()
t = datetime.datetime.strptime(h+':'+m, '%H:%M')
t -=datetime.timedelta(minutes=45)
print(t.hour, t.minute)