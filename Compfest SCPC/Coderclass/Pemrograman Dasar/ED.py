for i in range(int(input())):
    s= input().strip()

    print('palindrom' if s==s[::-1] else 'bukan palindrom')