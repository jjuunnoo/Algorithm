# 오타맨 고창영
n_case = int(input())
for _ in range(n_case):
    miss, word = input().split()
    word = word[:int(miss)-1] + word[int(miss):]
    print(word)
