import sys
multi_num = int(sys.stdin.readline().rstrip())*int(sys.stdin.readline().rstrip())*int(sys.stdin.readline().rstrip())
num_list = list(map(int, str(multi_num)))

for i in range(10):
    print(num_list.count(i))
