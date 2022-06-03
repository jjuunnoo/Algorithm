# BOJ 2475 검증수
import sys

print(sum([i**2 for i in list(map(int, sys.stdin.readline().split()))])%10)