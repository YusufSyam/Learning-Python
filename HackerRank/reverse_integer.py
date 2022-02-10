# Reversing integer without converting it to string

n= int(input())

len_n= 0
divider= 10
while True:
    # print(n/divider)
    if n/divider<1:
        break
    else:
        divider*= 10

num_list= []
temp_divider= divider/10
while True:
    temp= n-(n%temp_divider)
    n-= temp

    num_list.append(temp/temp_divider)
    if temp_divider==1:
        break

    temp_divider/= 10

digits= len(num_list)
num_list.reverse()

reversed_n= 0
for i in range(digits-1, -1, -1):
    n+= num_list[digits-i-1]*(10**i)

print(int(n))
