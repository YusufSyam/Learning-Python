#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None


class Stack:
    def __init__(self):
        self.top = None
        self.curr_size = 0

    def push(self, data):
        new_node = Node(data)

        if self.curr_size == 0:
            self.top = new_node
            self.top.next_node = None
        else:
            new_node.next_node = self.top
            self.top = new_node

        self.curr_size += 1

    def pop(self):
        if self.curr_size <= 0:
            return
        else:
            self.top = self.top.next_node

            self.curr_size -= 1

    def get_max(self):
        if self.curr_size == 0:
            return

        curr_node = self.top
        max = curr_node.data
        while True:
            curr_node = curr_node.next_node

            if curr_node is None:
                break

            if max < curr_node.data:
                max = curr_node.data

        return max


def getMax(operations):
    stack = Stack()
    max_node_list = []

    for i in operations:
        queries = i.split(' ')
        query = int(queries[0])

        if query == 1:
            push = int(queries[1])
            stack.push(push)

        elif query == 2:
            stack.pop()

        elif query == 3:
            max_node_list.append(stack.get_max())

    return max_node_list


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
