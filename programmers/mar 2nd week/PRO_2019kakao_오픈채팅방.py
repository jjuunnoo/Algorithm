# level2

def solution(record):
    answer = []
    result = []
    dic = {}
    for rec in record:
        spl = rec.split()
        if spl[0] == 'Enter':
            result.append([spl[0], spl[1]])
            dic[f'{spl[1]}'] = spl[2]
        elif spl[0]== 'Leave':
            result.append([spl[0], spl[1]])
        else:
            dic[f'{spl[1]}'] = spl[2]

    for i, j in result:
        if i=='Enter':
            answer.append(f'{dic[j]}님이 들어왔습니다.')
        elif i =='Leave':
            answer.append(f'{dic[j]}님이 나갔습니다.')
    
    return answer
