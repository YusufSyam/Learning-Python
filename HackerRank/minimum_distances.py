#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(arr):
    num_dict = {}

    for i in range(len(arr)):
        if (arr[i] in num_dict.keys()):
            num_dict[arr[i]].append(i)
        else:
            num_dict[arr[i]] = []
            num_dict[arr[i]].append(i)

    min_distances = []
    for i in num_dict:
        if (len(num_dict[i]) <= 1):
            continue

        for j in range(len(num_dict[i]) - 1):
            curr_num = num_dict[i][j]
            min_distances.append(abs(num_dict[i][j + 1] - curr_num))

    return min(min_distances) if min_distances else -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
