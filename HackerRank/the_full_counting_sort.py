#!/bin/python3
import collections


#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def countSort(n, arr):
    arr_dict = {}

    # print(dash_threshold)
    # print(arr)
    for idx, i in enumerate(arr):
        if idx < n // 2:
            i[1] = '-'

        if i[0] in arr_dict.keys():
            arr_dict[i[0]].append(i[1])
        else:
            arr_dict[i[0]] = [i[1]]

    arr_dict = collections.OrderedDict(sorted(arr_dict.items()))

    print(' '.join([' '.join(l) for l in arr_dict.values()]))

    # print(arr_dict)


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(n, arr)