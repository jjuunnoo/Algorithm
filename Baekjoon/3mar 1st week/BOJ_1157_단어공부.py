import sys
import collections
a = list(sys.stdin.readline().upper().rstrip())
b = collections.Counter(a)
c = [i for i, j in b.items() if max(b.values()) == j]
if len(c)==1:
    print(c[0])
else:
    print('?')