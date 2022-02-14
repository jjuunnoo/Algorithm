# 문자열 반복
# 3:35 시작
n_case = int(input())
for _ in range(n_case):
    n, word = input().split()
    dup_word = ''
    for i in word:
        dup_word += i * int(n)
    print(dup_word)

# for _ in range(int(input())):
#     r, s = input().split()
#     for char in s:
#         print(char * int(r), end="")
#     print()    