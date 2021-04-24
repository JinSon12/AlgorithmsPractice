#!/bin/python3

import math
import os
import random
import re
import sys

# link : https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

# Complete the isValid function below.


def isValid(s):
    sortedString = "".join(sorted(s))
    print(sortedString)

    string = {}

    # length of string == 1, then return yes.
    if len(s) == 1:
        return "YES"

    for c in s:
        print(c)
        if c in string:
            string[c] += 1
        else:
            string[c] = 1

    dictMin = min(string.values())
    dictMax = max(string.values())
    # diff of Min, Max cannot be > 1
    if (dictMax - 1 != dictMin):
        return "No"

    # diff of Min Max is 1, the frequencies of either of the values must be 1.
    # if dictMax is the majority, then dictMin should only occur once
    # if dictMin is the majority, then dictMax should only occur once.
    # all the other cases, return No.
    numMax = sum(value == dictMax for value in string.values())
    numMin = sum(value == dictMin for value in string.values())

    print(numMax - numMin)
    if numMax - numMin <= 1:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
