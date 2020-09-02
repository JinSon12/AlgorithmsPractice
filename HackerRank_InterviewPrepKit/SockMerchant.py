# SockMerchant
# https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

# Notes
"""
.count() => counts the number of unique elements in a list. 

collections.Counter() = counts the number of occurences of an element in a given list 
          stores the elements in the format of dictionary or K,V format.
          Because creating it takes O(n), it is considered to be O(n) (the rest of the operations would be O(1))

"""
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the sockMerchant function below.
# time complexity = O(2n)= O(n)


def sockMerchant(n, ar):
    newDict = (Counter(ar))
    result = 0
    for ele in newDict.values():
        result += ele // 2

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
