#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    s_len = len(s)
    t_len = len(t)

    max_len = max([s_len, t_len])
    if (max_len % 2 == 1 and (k - max_len) % 2 == 0) or (max_len % 2 == 0 and (k - max_len - 1) % 2 == 0):
        return 'Yes'
    elif s == t and k % 2 == 0:
        return 'Yes'

    diff_len = 0
    idx = 0
    while True:
        try:
            if s[idx] != t[idx]:
                break
        except:
            break

        idx += 1

    diff_len = (s_len - idx) + (t_len - idx)
    print(diff_len, idx)
    print((max_len - diff_len))

    if diff_len <= k:
        if (diff_len % 2 == 0 and k % 2 == 0) or (diff_len % 2 == 1 and k % 2 == 1):
            return 'Yes'

    return 'No'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
