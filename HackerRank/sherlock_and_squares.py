import math

a= 16
b= 25

lower_boundary= int(a**0.5) if a**0.5 % 1 == 0 else math.floor(a**0.5)+1
higher_boundary= int(b**0.5) if b**0.5 % 1 == 0 else math.floor(b**0.5)

# print(lower_boundary)
# print(higher_boundary)
print(higher_boundary-lower_boundary+1)
# print(math.floor(9**0.5)+1)
# print(isinstance(9**0.5, int))