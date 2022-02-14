# 크로스워드 만들기
# 10분 소요 
A, B = input().split()

for i in range(len(A)):
    if A[i] in B:
        col = i
        row = B.index(A[i])
        break

for i in range(len(B)):
    if i == row:
        print(A)
    else:
        print('.'*col + B[i] + '.'*(len(A)-1-col))
