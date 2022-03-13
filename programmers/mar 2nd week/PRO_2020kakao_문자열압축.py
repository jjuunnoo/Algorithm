# level2
import re
def solution(s):
    answer = len(s)

    for i in range(1, len(s)//2+1):
        aa = ''
        sliced = s[0:i]
        count = 1
        for j in range(i, len(s), i):
            if s[j:j+i] == sliced:
                count += 1
            else:
                aa += str(count) + sliced if count >=2 else sliced
                sliced = s[j:j+i]
                count = 1
        aa += str(count) + sliced if count>=2 else sliced
        answer = min(answer, len(aa))

    return answer
