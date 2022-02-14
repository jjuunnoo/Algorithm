T = int(input())
for i in range(T):
    # print(('*'*(i+1)).rjust(T))
    print(f"{'*'*(i+1):>{T}}")
    # print(" " * (T-i-1) + "*" * (i+1))

