a, b, c, x= map(int, input().strip().split(' '))

langkah= 0
start= x
while True:
    langkah+= 1
    teleport= ((a*start)+b)%c

    if teleport==x:
        break

    start= teleport

print(langkah)