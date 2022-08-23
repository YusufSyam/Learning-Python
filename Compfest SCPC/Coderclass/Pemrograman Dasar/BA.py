s= input().strip()

if '+' in s:
    a, b= map(lambda x: int(x.strip()), s.split('+'))
    print(a+b)
elif '*' in s:
    a, b= map(lambda x: int(x.strip()), s.split('*'))
    print(a*b)
elif '-' in s:
    a, b= map(lambda x: int(x.strip()), s.split('-'))
    print(a-b)
elif '/' in s:
    a, b= map(lambda x: int(x.strip()), s.split('/'))
    print(a//b)
elif '%' in s:
    a, b= map(lambda x: int(x.strip()), s.split('%'))
    print(a%b)