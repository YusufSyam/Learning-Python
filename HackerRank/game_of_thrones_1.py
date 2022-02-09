#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def gameOfThrones(s):
    alph_dict= {}

    for i in s:
        if(i in alph_dict.keys()):
            alph_dict[i]+=1
        else:
            alph_dict[i]=1

    odd_alph= 0
    for i in alph_dict:
        if(alph_dict[i]%2==1):
            odd_alph+=1

        if(odd_alph>2):
            return 'NO'

    return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
