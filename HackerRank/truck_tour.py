#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#

def truckTour(petrolpumps):
    circle_len = len(petrolpumps)

    possible_start_idx = []
    for idx, i in enumerate(petrolpumps):
        pump, dist = i

        if (pump >= dist):
            possible_start_idx.append(idx)

    if (len(possible_start_idx) == 1):
        return possible_start_idx[0]
    else:
        for i in possible_start_idx:
            curr_pump = 0

            init_idx = i
            idx = init_idx
            through_all_circle = False
            for j in range(circle_len):
                pump, dist = petrolpumps[idx]
                curr_pump += pump

                curr_pump -= dist
                if (curr_pump < 0):
                    break

                idx = idx + 1 if idx < (circle_len - 1) else 0
                if (j == circle_len - 1):
                    through_all_circle = True

            if (through_all_circle):
                return init_idx


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()
