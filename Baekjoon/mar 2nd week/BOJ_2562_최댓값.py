import sys
num=[int(sys.stdin.readline().rstrip()) for i in range(9)]
print(max(num))
print(num.index(max(num))+1)