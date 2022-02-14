# 세로읽기
import sys
word_list = [list(sys.stdin.readline().rstrip()) for _ in range(5)]
for i in range(15):
    for j in range(5):
        try:
            print(word_list[j][i], end='')
        except:
            pass
