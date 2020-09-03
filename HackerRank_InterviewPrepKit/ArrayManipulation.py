#!/bin/python3
# https://www.hackerrank.com/challenges/crush/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
# TC = O(n), SC = O(n)


def arrayManipulation(n, queries):
    # O(n)
    result = [0] * (n + 2)
    # loop over queries
    # O(n)
    a = 0
    b = 0
    k = 0
    greatestValue = 0
    value = 0
    for i in range(0, len(queries)):
        a = queries[i][0]
        b = queries[i][1]
        k = queries[i][2]
        result[a] += k
        result[b+1] += -k

    greatestValue = result[1]
    # O(n)
    for j in range(1, len(result)-1):
        value += result[j]
        if value > greatestValue:
            greatestValue = value
    return greatestValue


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
