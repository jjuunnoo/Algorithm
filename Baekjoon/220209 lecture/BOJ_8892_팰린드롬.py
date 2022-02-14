# 팰린드롬
# 단어가 k개
# k개 중 2개 단어 함침 팰린드롬

# T = int(input())
# results = []
# for _ in range(T):
#     k = int(input())
#     words = [input() for _ in range(k)]
#     number = 0
#     for j in words:
#         for p in words:
#             if j==p:
#                 continue
#             word1 = j+p
#             if word1==word1[::-1]:
#                 print(word1)
#                 number +=1
#                 break
#             word2 = p+j
#             if word2==word2[::-1]:
#                 print(word2)
#                 number +=1
#                 break
#         if number > 0:
#             break
#     if number==0:
#         print(0)



def palindrome_func(k, words):
    for i in range(k-1):
        for j in range(i+1,k):
            word_1 = words[i] + words[j]
            if word_1==word_1[::-1]:
                return word_1
            word_2 = words[j] + words[i]
            if word_2==word_2[::-1]:
                return word_2
    return 0

for _ in range(int(input())):
    k = int(input())
    words = [input() for _ in range(k)]
    print(palindrome_func(k,words))