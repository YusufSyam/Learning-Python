#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    s_no_space = s.replace(' ', '')
    len_s_no_space = len(s_no_space)
    sqrt_len_s_no_space = math.sqrt(len_s_no_space)
    lower_bound = math.floor(sqrt_len_s_no_space)
    upper_bound = math.ceil(sqrt_len_s_no_space)

    if lower_bound * upper_bound < len_s_no_space:
        lower_bound += 1

    encrypted_s_1 = []

    temp_idx = 0
    while True:
        added_idx = temp_idx + lower_bound
        encrypted_s_1.append(s_no_space[temp_idx:added_idx])
        if (added_idx >= len_s_no_space):
            break

        temp_idx = added_idx

    print(encrypted_s_1)
    encrypted_s_2_list = [[' ' for j in range(lower_bound)] for i in range(upper_bound)]

    temp_s_idx = 0
    for i in range(lower_bound):
        for j in range(upper_bound):
            try:
                encrypted_s_2_list[j][i] = s[temp_s_idx]
            except:
                pass
            temp_s_idx += 1

    print(encrypted_s_2_list)
    encrypted_s_2 = ''

    for i in encrypted_s_2_list:
        for j in i:
            if j != ' ':
                encrypted_s_2 += j

        encrypted_s_2 += ' '

    return encrypted_s_2


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
