# 명령 프롬프트
# 15분
import sys
n = int(sys.stdin.readline())
first_name = list(sys.stdin.readline().rstrip())
for _ in range(n-1):
    file_name = list(sys.stdin.readline().rstrip())
    for i, name in enumerate(first_name):
        if name!=file_name[i]:
            first_name[i] = '?'
print(*first_name, sep='')