"""
1784. 스택 수열

스택 수열같이 multiple lines of input을 받을 때에는 readline 이 더 빠른 속도를 낸다. 
"""
import sys
input = sys.stdin.readline


N = int(input())

isInvalid = False
stack = [1]
res = ["+"]
lastAdded = stack[-1] + 1

for _ in range(N):
    num = int(input())
    # print(num)
    while num >= lastAdded:
        stack.append(lastAdded)
        res.append("+")
        lastAdded += 1

    if num == stack[-1]:
        stack.pop()
        res.append("-")

    else:
        isInvalid = True
        break

# if len(res) == maxCounter:
#     return res


if isInvalid:
    print("NO")
else:
    for i in res:
        print(i)
