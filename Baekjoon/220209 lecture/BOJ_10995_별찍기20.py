# 별찍기 - 20
T = int(input())
for i in range(T):
    print((' '*(i%2) + '* '*(T)))
    # print("* " * T if i % 2 == 0 else " *" * T)