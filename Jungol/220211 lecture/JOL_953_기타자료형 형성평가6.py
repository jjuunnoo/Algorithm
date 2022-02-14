# 딕셔너리 연습 문제 3
# 기타자료형 형성평가 6
import sys
poul = list(sys.stdin.readline().split())
dic_poul = {}
count = len(poul)

for i in poul:
    dic_poul[i] = poul.count(i)
    if count > poul.count(i):
        count = poul.count(i)
for i in dic_poul:
    if dic_poul[i] == count:
        print(i)
print(count)
    
