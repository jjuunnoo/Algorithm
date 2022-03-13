# level1

def solution(N, stages):
    answer = []
    dic = {}
    challenger = len(stages)

    for i in range(N):
        challenger = challenger - stages.count(i)
        try:
            dic[i+1] = stages.count(i+1) / challenger
        except:
            dic[i+1] = 0


    for i in sorted(dic.items(), key = lambda x : x[1], reverse = True):
        answer.append(i[0])
    return answer


