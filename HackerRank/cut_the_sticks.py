#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def get_cut_length(arr):
    sorted_arr = arr.copy()
    sorted_arr = set(sorted_arr)
    sorted_arr = list(sorted_arr)
    sorted_arr.sort()

    for i in sorted_arr:
        if (i > 0):
            return i

    return None


def cutTheSticks(arr):
    len_arr = len(arr)

    sticks_cut_list = []
    while True:
        sticks_cut = 0
        substractor = get_cut_length(arr)

        if (substractor is None):
            break

        for i in range(len_arr):
            if (arr[i] > 0):
                arr[i] -= substractor
                sticks_cut += 1

        sticks_cut_list.append(sticks_cut)

    return sticks_cut_list


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
