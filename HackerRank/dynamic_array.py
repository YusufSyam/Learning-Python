#!/bin/python3

import math
import os
import random
import re
import sys  

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    arr= [[] for i in range(n)]
    answer_list= []
    last_answer= 0

    for query in queries:
        query_type, x, y= query

        idx= ((x^last_answer)%n)
        if(query_type==1):
            arr[idx].append(y)
        elif(query_type==2):
            last_answer= arr[idx][y%len(arr[idx])]
            answer_list.append(last_answer)

    return answer_list


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

# n= 2
# queries_num= 5
#
# queries_raw= '''1 0 5
# 1 1 7
# 1 0 3
# 2 1 0
# 2 1 1'''.split('\n')
#
# arr= [[] for i in range(n)]
# queries= [[int(j) for j in i.split()] for i in queries_raw]
# answer_list= []
# last_answer= 0
#
# for query in queries:
#     query_type, x, y= query
#
#     idx= ((x^last_answer)%n)
#     if(query_type==1):
#         arr[idx].append(y)
#     elif(query_type==2):
#         last_answer= arr[idx][y%len(arr[idx])]
#         answer_list.append(last_answer)
#
# print(answer_list)
