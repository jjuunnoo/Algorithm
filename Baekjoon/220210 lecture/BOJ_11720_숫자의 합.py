# 숫자의 합
# 3분
import sys
n = int(sys.stdin.readline().rstrip())
num_sum = 0
for num in input():
    num_sum+=int(num)
print(num_sum)


# 리팩토링
# n = int(sys.stdin.readline().rstrip())
# print(sum(list(map(int, sys.stdin.readline().rstrip()))))