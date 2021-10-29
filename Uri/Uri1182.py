column= int(input())
choice= input()

arr= []

for i in range(12):
    col= []
    for j in range(12):
        col.append(float(input()))
    arr.append(col)

sum= 0
for i in range(len(arr)):
    sum+= arr[i][column]

if(choice=="S"): print("{:.1f}".format(sum))
elif(choice=="M"): print("{:.1f}".format(sum/12))

