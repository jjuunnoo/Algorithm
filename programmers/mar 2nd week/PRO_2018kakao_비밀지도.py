# level1

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        a_1 = f'{bin(arr1[i])[2:]:0>{n}}'
        a_2 = f'{bin(arr2[i])[2:]:0>{n}}'
        wall = ''
        for j in range(n):
            if a_1[j] =='1' or a_2[j] == '1':
                wall +='#'
            else:
                wall +=' '
        answer.append(wall)
    return answer

