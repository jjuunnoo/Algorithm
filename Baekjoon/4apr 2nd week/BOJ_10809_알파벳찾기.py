import sys
S = sys.stdin.readline().rstrip()

for i in range(ord('a'), ord('z')+1):
    try:
        print(S.index(chr(i)), end=' ')
    except:
        print(-1, end=' ')