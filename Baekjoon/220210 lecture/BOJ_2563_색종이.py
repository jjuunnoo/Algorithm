# 색종이
# 22분 시작

import sys
n = int(sys.stdin.readline())
tmp = [[0 for _ in range(101)] for _ in range(101)]
tmp
for i in range(n):
    x, y= map(int, sys.stdin.readline().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            tmp[i][j] = 1

area = 0
for i in tmp:
    area += i.count(1)
print(area)

