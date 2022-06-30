#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    t = 0
    k1, k1_jump = (x1, v1) if x1 > x2 else (x2, v2)
    k2, k2_jump = (x1, v1) if x1 < x2 else (x2, v2)

    if k1_jump > k2_jump or k1 != k2 and k1_jump == k2_jump:
        return 'NO'

    while True:
        k1 += k1_jump
        k2 += k2_jump

        if k1 == k2:
            return 'YES'

        if k1 < k2:
            return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
