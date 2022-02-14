# 리스트3 자가진단7
import sys
success = 0
for i in range(5):
    score = list(map(int,sys.stdin.readline().split()))
    avg_score = sum(score)/len(score)
    if avg_score >= 80:
        success +=1
        print('pass')
    else:
        print('fail')
print(f'Successful : {success}')





