import sys
inp = sys.stdin.readline().split()
n = ''.join(inp)
if n == '12345678':
    print('ascending')
elif n=='87654321':
    print('descending')
else:
    print('mixed')