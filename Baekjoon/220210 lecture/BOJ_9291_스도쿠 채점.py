# 스도쿠 채점
# sort 해서 1,2,3,4,5,6,7,8,9와 동일한지 확인
import sys
n = int(sys.stdin.readline().rstrip())
correct_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
correct_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}

for x in range(n):
    if x > 0:
        tmp = sys.stdin.readline().rstrip()
    sudoku = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
    correct = 1
    sudoku_trans = list(zip(*sudoku))

    for i in range(9):
        if set(sudoku[i]) != correct_set:
            print(f'Case {x+1}: INCORRECT')
            correct = 0
            break
        else:
            continue

    if correct == 0:
        continue

    for i in range(9):
        if set(sudoku_trans[i]) != correct_set:
            print(f'Case {x+1}: INCORRECT')
            correct = 0
            break
        else:
            continue

    if correct == 0:
        continue

    for mul in range(3):
        rec=[]
        for i in range(3):
            for j in range(3):
                rec.append(sudoku[mul*3+i][mul*3+j])
        if sorted(rec) != correct_list:
            print(f'Case {x+1}: INCORRECT')
            correct = 0
            break
        else:
            continue

    if correct == 1:
        print(f'Case {x+1}: CORRECT')



    # for mul in range(3):
    #     rec = set()
    #     for i in range(3):
    #         rec = rec.union(set(sudoku[mul*3+i][:3]))
    #     if rec != correct_set:
    #         print(f'Case {x+1}: INCORRECT')
    #         correct = 0
    #         break
    #     else:
    #         continue