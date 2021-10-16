"""
배열 합치기 

https://www.acmicpc.net/problem/11728

"""
A, B = map(int, input().split()) 

listA, listB = [], []

listA = list(map(int, input().split()))
listB = list(map(int, input().split()))

def mergeTwoLists(listA, listB): 
  pA, pB = 0, 0 
  cnt = 0 
  res = [] 

  while pA < len(listA) and pB < len(listB): 
    if listA[pA] < listB[pB]: 
      res.append(listA[pA]) 
      pA += 1 

    else: 
      res.append(listB[pB])
      pB += 1 
    cnt += 1 
  
  # 두 리스트 pA, pB 중 하나는 이미 포인터가 len 의 길이를 넘어갔다. 
  while pA < len(listA): 
    res.append(listA[pA])
    pA += 1 
  
  while pB < len(listB): 
    res.append(listB[pB])
    pB += 1 

  print(*res)


mergeTwoLists(listA, listB)