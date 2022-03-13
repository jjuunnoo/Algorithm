# level2
import re
def solution(str1, str2):
    answer = 0
    str1_list = []
    str1 = str1.lower()
    str2 = str2.lower()
    for i in range(len(str1)-1):
        if ''.join(re.findall('[a-z][a-z]',str1[i:i+2])) ==str1[i:i+2]:
            str1_list.append(str1[i:i+2])

    str2_list = []
    for i in range(len(str2)-1):
        if ''.join(re.findall('[a-z][a-z]',str2[i:i+2])) ==str2[i:i+2]:
            str2_list.append(str2[i:i+2])

    if str1_list ==[] and str2_list ==[]:
        return 65536
    else:
        tmp1 = str1_list.copy()
        result_union = str1_list.copy()
        for i in str2_list:
            if i not in tmp1:
                result_union.append(i)
            else:
                tmp1.remove(i)
        tmp2 = str1_list.copy()
        result_inter = []
        for i in str2_list:
            if i in tmp2:
                result_inter.append(i)
                tmp2.remove(i)
        answer = int(len(result_inter) / len(result_union)*65536)

    return answer

