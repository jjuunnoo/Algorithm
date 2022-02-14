# 평균은 넘겠지
# 40분 시작
# 52분 종료
import sys
C = int(sys.stdin.readline())
for _ in range(C):
    input_list = list(map(int, sys.stdin.readline().split()))
    people = input_list[0]
    score_list = input_list[1:]
    score_mean = sum(score_list) / people
    avg_people = [i for i in score_list if i > score_mean]
    print(f'{(len(avg_people) / people*100):0.3f}%')