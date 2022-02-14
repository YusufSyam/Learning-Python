# Reversing integer without converting it to string

num= int(input())
reversed_num= 0

while num:
    # print(f'num= {num}')
    # print(f'reversed_num= {reversed_num}')
    reversed_num*= 10
    reversed_num+= num%10
    num//= 10

print(reversed_num)