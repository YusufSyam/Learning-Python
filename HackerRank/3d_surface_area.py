#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#

def surfaceArea(H, W, A):
    if (H == 1 and W == 1):
        return (A[0][0]*4) + 2

    # Bottom and Top
    bottom_and_top= (H * W) * 2
    total_surface = bottom_and_top
    print(f'Bottom and Top ({bottom_and_top//2} x 2) :{bottom_and_top}')

    # Front and Rear
    front_and_rear= sum([i[0] for i in A]) + sum([i[-1] for i in A])
    total_surface += front_and_rear
    print(f'Front and Rear: {front_and_rear}')

    # Left Side
    left_side= sum(A[0])
    total_surface += left_side
    print('Left:', left_side)

    # Right Side
    right_side= sum(A[-1])
    total_surface += right_side
    print('Right:', right_side)

    # Additional Side
    if (H > 2):
        for i in range(H - 1):
            for j in range(W):
                total_surface += abs(A[i][j] - A[i + 1][j])

    if (W > 2):
        for i in range(H):
            for j in range(W-1):
                total_surface += abs(A[i][j] - A[i][j+1])

    return total_surface

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(H, W, A)

    fptr.write(str(result) + '\n')

    fptr.close()