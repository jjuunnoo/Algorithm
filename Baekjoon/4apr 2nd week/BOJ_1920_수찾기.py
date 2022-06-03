import sys
n = int(sys.stdin.readline().rstrip())
n_num = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().rstrip())
m_num = list(map(int, sys.stdin.readline().split()))
n_num.sort()

def search_num(i, n, num_list):
    start = 0
    end = n-1
    if i > num_list[-1]:
        return print(0)
    elif i < num_list[0]:
        return print(0)

    while start <= end:
        mid = (start+end)//2
        if i == num_list[mid]:
            return print(1)
        elif i > num_list[mid]:
            start = mid + 1
        elif i < num_list[mid]:
            end = mid -1
    return print(0)

for i in m_num:
    search_num(i, n, n_num)

