# 딕셔너리 연습 문제 1
# 기타자료형 - 자가진단5
import sys
test_dic = {
    "Pokemon" : "Pikachu",
    "Digimon" : "Agumon",
    "Yugioh" : "Black Magician"
}
try:
    print(test_dic[sys.stdin.readline().rstrip()])
except:
    print("I don't know")

# try except 부분 한번에
# print(test_dic.get(sys.stdin.readline().rstrip(), "I don't know"))