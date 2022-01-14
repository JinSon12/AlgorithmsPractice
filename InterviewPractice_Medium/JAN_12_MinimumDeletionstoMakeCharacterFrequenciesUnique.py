# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

"""
pseudocode 

freq = {}
setToCheckNums = set()

# count the number of chars in the string
for c in string: 
  if c not in freq: 
    freq[c] = 0 
  else: 
    freq[c] += 1 

counter = 0 
for k, v in freq.items(): 
  f = v 
  num = k
  while f in setToCheckNums:
    freq[num] -= 1 
    counter += 1 
  else: 
    setToCheckNums.add(v)

"""


def minDeletions(s):
    freq = {}
    setToCheckNums = set()

    # count the number of chars in the string
    for c in s:
        if c not in freq:
            freq[c] = 1
        else:
            freq[c] += 1

    print(freq)
    counter = 0
    for k, v in freq.items():
        while v in setToCheckNums:
            freq[k] -= 1
            counter += 1
            v -= 1
        setToCheckNums.add(v)

    return counter


print(minDeletions("ceabaacb"))
