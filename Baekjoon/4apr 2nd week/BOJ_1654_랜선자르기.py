import sys
k, n = map(int, sys.stdin.readline().split())
lan_list = [int(sys.stdin.readline().rstrip()) for _ in range(k)]

start = 1
end = max(lan_list)

while start<=end:
    center = (start+end)//2
    cnt = sum(list(map(lambda x:x//center, lan_list)))
    if cnt >= n:
        start = center + 1
    else:
        end = center - 1

print(end)
