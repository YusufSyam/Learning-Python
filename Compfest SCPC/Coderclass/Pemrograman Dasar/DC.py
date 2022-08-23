n= int(input())
arr= list(input().strip().split(' '))
res= [arr[0]]

step= 1
for i in range(1,n):
    if i%2==1 and i>2:
        step+= 1

    res.append((arr[step*(-1)] if i%2==1 else arr[step]))

print(' '.join(res))