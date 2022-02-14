# 최소, 최대
# 2분 시작
# 7분 종료 
import sys
n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
print(min(num_list), max(num_list))
