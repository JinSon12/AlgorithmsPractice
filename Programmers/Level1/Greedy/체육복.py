# https://programmers.co.kr/learn/courses/30/lessons/42862

""" 
Solved Using Greedy approach. 
Key : 
- Does the a person in the lost group borrow from the person with smaller sized clothes? or larger sized clothes? 
- smaller. 
- cf. consider this case.  l = [2, 4] r =	[1, 3, 5] and l = [2,4] r = [3,5] 
  the latter case would have less # of total people participating in the gym class 
  if the people only borrowed from people with larger sized clothes
  

- key insights: Think about various cases more. 
   i.e. what happens if the second person in l can wear both 3, and 5? 

- expanding thoughts and boundaries = important!! 


"""


def solution(n, lost, reserve):
    answer = n - len(lost)

    setr = set(reserve) - set(lost)
    setl = set(lost) - set(reserve)

    print(answer, "len", len(lost), len(setl))

    answer += len(lost) - len(setl)
    print(answer)

    for i in setl:
        if i-1 in setr:
            setr.remove(i-1)
            answer += 1
        elif i+1 in setr:
            setr.remove(i+1)
            answer += 1

    return answer
