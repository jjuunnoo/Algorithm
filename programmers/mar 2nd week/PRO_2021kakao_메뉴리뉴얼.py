# level2
from itertools import combinations

def solution(orders, course):
    answer = []
    combi = {}
    for i in course:
        for j in orders:
            for k in list(combinations(j, i)):
                try:
                    combi[''.join(sorted(k))] += 1
                except:
                    combi[''.join(sorted(k))] =1

    for i in course:
        tmp = []
        for j in combi.keys():
            if len(j) == i:
                tmp.append(combi[j])
        for k in combi.keys():
            if len(k) == i:
                if max(tmp)>=2:
                    if combi[k] == max(tmp):
                        answer.append(k)
    answer.sort()
    return answer