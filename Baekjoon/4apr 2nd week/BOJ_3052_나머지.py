import sys
divide_list = [int(sys.stdin.readline().rstrip())%42 for _ in range(10)]
print(len(set(divide_list)))