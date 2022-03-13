import re
def solution(dartResult):
    answer = 0
    split_list = re.findall('\d+[A-Z]\#+|\d+[A-Z]\*+|\d+[A-Z]', dartResult)
    star_list = [1]*3
    minus_list = [1]*3
    SDT_list = [1]*3

    for i, num in enumerate(split_list):
        if re.findall('\*', num) !=[]:
            if re.findall('\*', num)[0]=='*':
                if i==0:
                    star_list[i] *=2
                else:
                    star_list[i-1] *= 2
                    star_list[i] *= 2
        elif re.findall('#', num) !=[]:
            if re.findall('#', num)[0]== '#':
                minus_list[i] *= -1
        if re.findall('[A-Z]', num)[0] == 'D':
            SDT_list[i] = 2
        elif re.findall('[A-Z]', num)[0] == 'T':
            SDT_list[i] = 3

    for i, num in enumerate(split_list):
        answer += (int((re.findall('\d+',num)[0]))**SDT_list[i])*star_list[i]*minus_list[i]

    return answer

