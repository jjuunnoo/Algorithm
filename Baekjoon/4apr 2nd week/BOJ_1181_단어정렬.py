import sys
n = int(sys.stdin.readline().rstrip())
word_list = [sys.stdin.readline().rstrip() for _ in range(n)]
word_list_no_dup = list(set(word_list))
word_list_no_dup.sort(key=lambda x :(len(x), x))

for i in word_list_no_dup:
    print(i)

