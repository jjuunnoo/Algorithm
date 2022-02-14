# 나무 조각
# 15분



import sys
num_list = list(map(int, sys.stdin.readline().split()))
while True:
    for i in range(len(num_list)-1):
        if num_list[i] > num_list[i+1]:
            num_list[i], num_list[i+1] = num_list[i+1], num_list[i]
            print(*num_list, sep=' ')
    if num_list == [1, 2, 3, 4, 5]:
        break
