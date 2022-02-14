# 직사각형 네개의 합집합의 면적 구하기
import sys
tmp = [[0 for _ in range(101)] for _ in range(101)]

for i in range(4):
    x1, y1, x2, y2= map(int, sys.stdin.readline().split())
    for i in range(x1, x2):
        for j in range(y1,y2):
            tmp[i][j] = 1

area = 0
for i in tmp:
    area += i.count(1)
print(area)            
