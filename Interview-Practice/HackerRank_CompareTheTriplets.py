# https://www.hackerrank.com/challenges/compare-the-triplets/problem
"""
a = [1, 2, 3] 
b = [3, 2, 1] 
For elements *0*, Bob is awarded a point because a[0] .
For the equal elements a[1] and b[1], no points are earned.
Finally, for elements 2, a[2] > b[2] so Alice receives a point.
The return array is [1, 1] with Alice's score first and Bob's second.

"""
import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.


def compareTriplets(a, b):
    result = [0, 0]
    for i in range(0, len(a)):
        if (a[i] > b[i]):
            result[0] += 1
        if (b[i] > a[i]):
            result[1] += 1
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
