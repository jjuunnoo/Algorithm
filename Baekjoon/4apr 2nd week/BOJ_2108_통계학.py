import sys
from collections import Counter
n = int(sys.stdin.readline().rstrip())
num_list = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
num_list.sort() 

print(int(round(sum(num_list)/n)))
print(num_list[n//2])


tmp = Counter(num_list).most_common()
tmp
if n > 1:
    if tmp[0][1] == tmp[1][1]:
        print(tmp[1][0])
    else:
        print(tmp[0][0])
else:
    print(tmp[0][0])


print(num_list[-1]-num_list[0])
