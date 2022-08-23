import math

def t(n):
    return 1 if n<=1 else 1+t(math.ceil(n/2))+t(math.floor(n/2))

print(t(int(input())))