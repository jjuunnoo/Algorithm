import sys
n = int(sys.stdin.readline().rstrip())
num_list = map(int, sys.stdin.readline().split())

tmp = [True]*(1001)
tmp[0] = False
tmp[1] = False

for i in range(2, 1000):
    for j in range(2, 1000//i + 1):
        tmp[i*j] = False
cnt = 0
for i in num_list:
    if tmp[i]==True:
        cnt+=1

print(cnt)