#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    counter_dict = {}

    for i in set(arr):
        counter_dict[i] = arr.count(i)

    # print(counter_dict)

    return max(counter_dict, key=(lambda x: counter_dict[x]))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
