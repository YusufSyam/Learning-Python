a, b, c= map(int, input().strip().split(' '))

if (a + b <= c) or (a + c <= b) or (b + c <= a):
    print('bukan segitiga')
else:
    print('segitiga')