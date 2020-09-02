# https://www.hackerrank.com/challenges/time-conversion/problem
"""

"""

# Approach
"""
Get the s 
Strip any white-spaces in S 
store the hour, min, sec, Am/PM into corresponding variables 
check if s has PM, if it does, h % 12, and add 12 to h 
save the time to result and return 

"""

# Example Solution
"""
time = input().strip()
h, m, s = map(int, time[:-2].split(':'))
p = time[-2:]
h = h % 12 + (p.upper() == 'PM') * 12
print(('%02d:%02d:%02d') % (h, m, s))

"""

# Notes
"""
.strip() : The strip() method removes any leading (spaces at the beginning) 
           and trailing (spaces at the end) characters 
           (space is the default leading character to remove)
           
    txt = ",,,,,rrttgg.....banana....rrr"

    x = txt.strip(",.grt")

    x : banana

.map() : very similar to JS
https://www.geeksforgeeks.org/python-map-function/
** lambda function is different from js usage. 

[1:] = 1 to end 
[1:5] = 1 to 5 (5 not included)
so [: -2] would = start to last two elements in the array (two elements not included)

==== 
String Formatting in Python 
https://www.learnpython.org/en/String_Formatting
%s - String (or any object with a string representation, like numbers)

%d - Integers

%f - Floating point numbers

%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

%x/%X - Integers in hex representation (lowercase/uppercase)

"""

#!/bin/python3


#
# Complete the timeConversion function below.
#




import os
import sys
def timeConversion(s):
    result = ""
    if s != "":
        s.strip()
        AMPM = s[-2:]
        h, m, s = map(int, s[:-2].split(":"))
        if(AMPM.upper() == "PM"):
            h = h % 12 + 12
        if(AMPM.upper() == "AM" and h >= 12):
            h = 0
        result = ('%02d:%02d:%02d' % (h, m, s))
    return result


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
