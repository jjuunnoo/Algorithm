import sys
m, n = map(int, sys.stdin.readline().split())

tmp = [True]*(n+1)
tmp[0] = False
tmp[1] = False

for i in range(2, n):
    for j in range(2, n//i + 1):
        tmp[i*j] = False

for i in range(m, n+1):
    if tmp[i] == True:
        print(i)



