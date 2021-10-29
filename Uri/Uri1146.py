while (True):
    a= int(input())
    if(a==0): break
    else:
        for i in range (a):
            if(i==a-1): print(i+1)
            else: print((i+1),"", end= " ")
