#!/bin/python3

import math
import os
import random
import re
import sys
# from collections import Counter

# Complete the countingValleys function below.


def countingValleys(n, s):
    valley = 0
    height = 0
    for i in range(len(s)):
        if s[i] == 'U':
            height += 1
        else:
            if height == 0:
                valley += 1
            height -= 1
    return valley


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
