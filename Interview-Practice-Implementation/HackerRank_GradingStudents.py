# https://www.hackerrank.com/challenges/grading/problem


import math
import os
import random
import re
import sys


def gradingStudents(grades):
    result = []
    for i in grades[1:]:
        if (i >= 38):
            grade = i
            numtoMult = grade // 5 + 1
            if ((numtoMult * 5) - grade < 3):
                grade = 5 * numtoMult
            result.append(grade)
        else:
            result.append(i)
    return result


def gradingStudentsSol(grades):
    n = int(input().strip())
    for a0 in range(n):
        x = int(input().strip())

        if x >= 38:
            if x % 5 > 2:
                while x % 5 != 0:
                    x += 1
    print(x)


def gradingStudentsSol2(grades):
    result = []
    for grade in grades[1:]:
        newGrade = grade
        if (grade >= 38):
            if (grade % 5 >= 3):
                newGrade = (grade // 5) * 5 + 5
        result.append(newGrade)

    return result


print(gradingStudentsSol2([4, 74, 67, 38, 33]))
