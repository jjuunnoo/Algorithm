# 나는 요리사다
# 19분 시작
# 25분 종료 
import sys
num = 0
score = 0
for i in range(5):
    score_list = list(map(int, sys.stdin.readline().split()))
    if score < sum(score_list):
        score = sum(score_list)
        num = i+1
print(num, score)
