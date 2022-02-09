s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]

# Get max
sum_arr= {}
for i in range(3):
    temp= 0
    for j in range(3):
        # print(i, j)
        print(s[j][i], end=' ')
        temp+= s[j][i]

    sum_arr['col '+str(i+1)]=temp
    print()

for i in range(3):
    temp= 0
    for j in range(3):
        # print(i, j)
        print(s[i][j], end=' ')
        temp+= s[i][j]

    sum_arr['row '+str(i+1)]=temp
    print()

# print(s[0][0], s[1][1], s[2][2])
sum_arr['diag 1']= (s[0][0]+ s[1][1]+ s[2][2])
# print(s[0][2], s[1][1], s[2][0])
sum_arr['diag 2']= (s[0][2]+ s[1][1]+ s[2][0])

print(sum_arr)

cat_dict= {}
for i in range(3):
    category= []
    for j in range(3):
        category.append('row '+str(i+1))
        category.append('col '+str(j+1))
        if(i==j):
            if(i==1):
                category.append('diag 1')
                category.append('diag 2')

            # Next add diag 1 and 2