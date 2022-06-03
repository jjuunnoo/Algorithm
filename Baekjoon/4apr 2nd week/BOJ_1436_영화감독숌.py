import sys
n = int(sys.stdin.readline().rstrip())

tmp = 666
cnt = 0
while True:
    if '666' in str(tmp):
        cnt+=1
    if cnt==n:
        print(tmp)
        break
    tmp+=1