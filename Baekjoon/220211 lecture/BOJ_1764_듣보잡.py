# 실습 1
# 듣보잡
import sys

n, m = map(int, sys.stdin.readline().split())

name_list = [sys.stdin.readline().rstrip() for _ in range(n+m)]

dic_name = {}

for name in name_list:
    if name in dic_name:
        dic_name[name] +=1
    else:
        dic_name[name] = 1

print(list(dic_name.values()).count(2))
print(*[i for i in sorted(dic_name) if dic_name[i]==2], sep='\n')






