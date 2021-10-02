"""
Longest Common Prefix 
"""

def longestCommonPrefix(words): 
  commonPrefix = words[0]

  if len(words) == 1:
    return words[0]

  for i in range(1, len(words)): 
    word = commonPrefix
    nextWord = words[i] 

    if len(word) == 0 or len(nextWord) == 0:
      return ""

    tempCP = ""
    p = 0
    shortlen = min(len(word), len(nextWord))
    while p < shortlen: 
      if word[p] == nextWord[p]: 
        tempCP += word[p]
      else: 
        break
      p += 1
    
    commonPrefix = tempCP
    
  return commonPrefix

print(longestCommonPrefix(["reflower","flow","flight"]))
