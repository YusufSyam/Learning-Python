#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    satuan = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    puluhan = ['ten', 'twenty', 'thirty']
    belasan = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fiveteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

    minute_time = ''
    o_clock = False

    before_half = False
    if m > 30:
        m = abs(60 - m)
        before_half = True
        h += 1

    # M
    if (m == 0):
        minute_time += 'o\' clock'
        o_clock = True
    elif (m == 30):
        minute_time += 'half'
    elif (m % 15 == 0):
        minute_time += 'quarter'
    elif (m % 10 == 0):
        minute_time += puluhan[(m // 10) - 1] + ' minutes'
    elif (m <= 10):
        minute_time += satuan[m - 1] + ' minute' + ('s' if (m - 1) > 1 else '')
    elif (m <= 20):
        minute_time += belasan[m - 10 - 1] + ' minutes'
    else:
        a = puluhan[math.floor(m / 10) - 1]
        b = satuan[int(str(m)[-1]) - 1]
        minute_time = a + ' ' + b + ' minutes'

    hour_time = ''

    # H
    if (h % 10 == 0):
        hour_time += puluhan[(h // 10) - 1]
    elif (h <= 10):
        hour_time += satuan[h - 1]
    elif (h <= 20):
        hour_time += belasan[h - 10 - 1]

    if o_clock:
        return hour_time + ' ' + minute_time

    return minute_time + ' to ' + hour_time if before_half else minute_time + ' past ' + hour_time


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
