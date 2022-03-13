# level 2



def true_str(p):
    tmp = True
    for i in range(len(p)):
        if p[:i].count('(') <  p[:i].count(')'):
            tmp = False
    return tmp

def slice_str(p):
    for i in range(1, len(p)//2+1):
        if p[0:i*2].count('(') == p[0:i*2].count(')'):
            u = p[0:i*2]
            v = p[i*2:]
            break
    return u, v

def solution(p):
    answer = ''
    if len(p)==0 or true_str(p):
        return p
    u, v = slice_str(p)

    if true_str(u):
        answer += u + solution(v)
    else:
        answer +='(' + solution(v) + ')'
        for i in u[1:-1]:
            if i=='(':
                answer+=')'
            else:
                answer+='('
    return answer




        

