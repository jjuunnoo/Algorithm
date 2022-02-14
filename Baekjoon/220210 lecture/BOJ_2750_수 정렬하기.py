# 수 정렬하기
# 15분 시작
# 18분 종료 
import sys
n = int(sys.stdin.readline())
num_list = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
num_list.sort()
print(*num_list, sep='\n')
