#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def compare_binary(x, y):
    known_subject= 0
    
    for i in range(len(x)):
        if x[i]=='1' or y[i]=='1':
            known_subject+= 1
            
    return known_subject

def acmTeam(topic):
    score_dict= {}
    
    for i in range(len(topic)):
        for j in range(i):
            known_subject= compare_binary(topic[i], topic[j])
            
            if known_subject in list(score_dict.keys()):
                score_dict[known_subject]+= 1
            else:
                score_dict[known_subject]= 1
    
            print(f'i={i}, j={j}, same={known_subject}')
    
            
    highest_subject_known= list(sorted(score_dict.keys()))[-1]        
    
    return highest_subject_known, score_dict[highest_subject_known]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
