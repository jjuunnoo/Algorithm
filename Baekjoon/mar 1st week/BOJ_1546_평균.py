import sys
n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().split()))
print(sum(a)/len(a)*100/max(a))