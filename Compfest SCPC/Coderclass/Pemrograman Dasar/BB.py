s= input()

if s[0]=='-' and s[1]!='0':
    print('bilangan bulat negatif')
elif s[0].isdigit() and s[0]!='0':
    print('bilangan bulat positif')
elif s=='0' or s[1]=='0':
    print('nol')
else:
    print('kata')