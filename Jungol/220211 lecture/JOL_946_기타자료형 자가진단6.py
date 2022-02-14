# 딕셔너리 연습 문제 2
# 기타자료형 자가진단6
import sys
n = int(sys.stdin.readline())
country_dict={}
for _ in range(n):
    country, capital = sys.stdin.readline().split()
    country_dict[country] = capital

print(country_dict.get(sys.stdin.readline().rstrip(), 'Unknown Country'))
