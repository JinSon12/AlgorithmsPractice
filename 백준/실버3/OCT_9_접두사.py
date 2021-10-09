"""
https://www.acmicpc.net/problem/1141

접두사

"""
import sys 
input = sys.stdin.readline

N = int(input())

wordList = [] 
for _ in range(N): 
  word = input().rstrip()
  wordList.append(word)


def findSubsetSize(wordList): 
  wordList.sort(key=len) 
  counter = 0 

  for i in range(len(wordList)): 
    L = len(wordList[i])
    isHead = False 

    for j in range(i+1, len(wordList)):
        if wordList[j][:L] == wordList[i]:
            isHead=True
            break

        else: 
          continue

    if not isHead: 
      counter += 1 

  print(counter)

# using startswith()
def findSubSetSize():
  n = int(input())

  lst = []

  for i in range(n):
      lst.append(str(input()))
  lst.sort(key=len)

  answer = n

  for i in range(len(lst)):
      for j in range(i+1, len(lst)):
          if lst[j].startswith(lst[i]):
              answer -= 1
              break
  print(answer)


findSubsetSize(wordList)
