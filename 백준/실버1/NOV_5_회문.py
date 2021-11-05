# https://www.acmicpc.net/problem/17609
"""
회문 재풀이 

7
abba
summuus
xabba
xabbay
comcom
comwwmoc
comwwtmoc

2 
xabbay
comcom
"""

import sys 
input = sys.stdin.readline

N = int(input()) 
words = [] 

for i in range(N): 
  words.append(input().rstrip())

def checkPalindromeOneLevelDeeper(word, pl, pr):
  while pl < pr: 
    if word[pl] != word[pr]: 
      return False
    pl += 1 
    pr -= 1 
  
  return True 
    

# two pointer approach 
def checkPalindrome(words):
  res = [] 
  for word in words: 
    pl = 0 
    pr = len(word)-1 

    while pl < pr: 
      if word[pl] == word[pr]: 
        pl += 1 
        pr -= 1 
      else: 
        addLeft = checkPalindromeOneLevelDeeper(word, pl + 1, pr) 
        addRight = checkPalindromeOneLevelDeeper(word, pl, pr-1)

        # if 유사회문: 
        if addLeft or addRight: 
          res.append(1)
        else: 
          res.append(2)
        
        break
    
    if pl >= pr: 
      res.append(0)

  for i in range(len(res)):
    print(res[i])

checkPalindrome(words)
