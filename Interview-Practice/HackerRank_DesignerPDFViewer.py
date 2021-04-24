#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
# TC = O(word), SC = O(1)
def designerPdfViewer(h, word):
    maxH = 1
    # O(n)
    for i in word:
        val = h[ord(i)-97]
        if(val > maxH):
            maxH = val
    return (len(word) * maxH)

# TC = O(word), SC = O(1)
def designerPdfViewer2(h, word):
    chartoInttoHeight = [h[ord(c) - ord('a')] for c in word]
    return (max(chartoInttoHeight) * len(chartoInttoHeight))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
