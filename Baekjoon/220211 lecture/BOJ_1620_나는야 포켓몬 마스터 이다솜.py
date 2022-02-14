# 실습 3
# 나는야 포켓몬 마스터 이다솜
import sys
n, m = map(int, sys.stdin.readline().split())

dic_poc = {}
for i in range(n):
    dic_poc[i+1] = sys.stdin.readline().rstrip()

dic_poc_reversed = {value:key for key, value in dic_poc.items()}

for _ in range(m):
    inp = sys.stdin.readline().rstrip()
    try:
        print(dic_poc[int(inp)])
    except:
        print(dic_poc_reversed[inp])
