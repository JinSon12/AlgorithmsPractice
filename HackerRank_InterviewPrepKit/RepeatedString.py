#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.


def repeatedString(s, n):
    # enumerate https://wikidocs.net/16045
    # O(n)
    indexOccur = [i for i, char in enumerate(s) if char == "a"]
    occInS = len(indexOccur)
    totalOcc = 0

    if occInS == 0:
        return 0

    Q = (n // len(s)) * occInS
    R = n % len(s)

    for i in s[:R]:
        print(i)
        if i == "a" and occInS > 1:
            print(i)
            totalOcc += 1
    totalOcc += Q
    return totalOcc


# optimization
def repreatedString2(s, n):
    Q = s.count("a") * (n // len(s))
    R = s[:n % len(s)].count("a")

    return Q + R


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
