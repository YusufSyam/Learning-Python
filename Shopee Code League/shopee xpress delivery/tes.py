row= 8
col= 8

for i in range(row):
    for j in range(col):
        if((i==0 and j==2) or (i==6 and j==6)):
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()