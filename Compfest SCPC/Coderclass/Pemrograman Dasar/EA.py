x= int(input())

total_factor= 0
for i in range(1,x+1):
    if i==1:
        total_factor+= 1
        continue
    elif i<=3:
        total_factor+= 2
        continue

    factor= 2
    for j in range(2,(i//2)+1):
        if i%j==0:
            factor+= 1

    total_factor+= factor

print(total_factor)