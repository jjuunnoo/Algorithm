import sys
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    ox = sys.stdin.readline().rstrip()
    score = 0
    answer = 0
    for i in ox:
        if i=='O':
            score +=1
            answer +=score
        else:
            score = 0
    print(answer)