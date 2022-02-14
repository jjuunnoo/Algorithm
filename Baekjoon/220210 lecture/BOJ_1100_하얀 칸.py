# 하얀 칸
# 5분 
import sys
chess_list = [sys.stdin.readline().rstrip() for _ in range(8)]
numbers = 0
for i, row in enumerate(chess_list):
    for j, piece in enumerate(row):
        if (i+j)%2==0 and piece == 'F':
            numbers += 1
print(numbers)

#
# board = [list(input()) for _ in range(8)]
# total = 0
# for i in range(8):
#     for j in range(8):
#         if i %2 == j%2  and board[i][j]=='F':
#             total += 1
# print(total)


# 한줄표현
# print(sum(input()[i%2::2].count("F") for i in range(8)))