a, b, x, y= map(int, input().strip().split(' '))

kertas= ''
while True:
    if x>y:
        break

    if kertas!='':
        kertas+= '\n'

    kertas+= str(x)

    x= (a*x)+b

print(kertas)
