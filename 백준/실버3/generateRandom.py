"""
Random
"""

import random

"""
code generating random 2d matrix
"""


def generate2D(r, c, rang):
    randInt = random.randint(0, rang)
    mat = [[random.randrange(0, randInt) for j in range(r)] for i in range(c)]

    return mat


# generate2D(3, 4, 4)
