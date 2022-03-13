# level1

import numpy as np

def solution(board, moves):
    answer = 0
    board = np.array(board)
    buc = []
    for i in moves:
        for j, num in enumerate(board[:,i-1]):
            if num!=0:
                buc.append(num)
                board[j][i-1] = 0
                break
        if len(buc)>=2:
            if buc[-1] == buc[-2]:
                buc = buc[:-2]
                answer+=2
    return answer
