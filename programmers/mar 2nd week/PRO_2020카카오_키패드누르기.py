# level1

import numpy as np


def num_dis(num, left, right, hand):
    result = 0
    left_dis = 0
    right_dis = 0
    pad = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [11, 0, 12]])
    num_index = [np.where(pad==num)[0][0], np.where(pad==num)[1][0]]
    left_index = [np.where(pad==left)[0][0], np.where(pad==left)[1][0]]
    right_index = [np.where(pad==right)[0][0], np.where(pad==right)[1][0]]

    for i, ind in enumerate(num_index):
        left_dis += abs(left_index[i]-ind)
    for i, ind in enumerate(num_index):
        right_dis += abs(right_index[i]-ind)
    if left_dis > right_dis:
        result = 'R'
    if left_dis < right_dis:
        result = 'L'
    if left_dis == right_dis:
        if hand == 'right':
            result = 'R'
        else:
            result = 'L'

    return result


def solution(numbers, hand):
    answer = ''
    left_num = [1, 4, 7]
    right_num = [3, 6, 9]
    left = 11
    right = 12
    for num in numbers:
        if num in left_num:
            left = num
            answer += 'L'
        elif num in right_num:
            right = num
            answer += 'R'
        elif num_dis(num, left, right, hand) == 'R':
            right = num
            answer +='R'
        elif num_dis(num, left, right, hand) == 'L':
            left = num
            answer +='L'
    return answer

numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = 'left'
solution(numbers, hand)