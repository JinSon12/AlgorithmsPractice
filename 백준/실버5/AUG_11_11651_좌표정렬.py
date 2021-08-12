"""
11651 좌표 정렬 2 

- sorted function 사용하면서 
- key와 lambda func. 사용하여 custom key 로 sort. 


5
0 4
1 2
1 -1
2 2
3 3

"""

import sys
input = sys.stdin.readline

nTC = int(input())

nums = []

for _ in range(nTC):
    x, y = map(int, input().split())
    nums.append((x, y))

nums.sort(key=lambda x: (x[1], x[0]))

for num in nums:
    print(num[0], num[1])


# Method 2
def method2():
    import sys
    input = sys.stdin.readline

    nTC = int(input())

    nums = []

    for _ in range(nTC):
        x, y = map(int, input().split())
        # 2d array 로 만든다; append 의 순서가 중요. x, y 가 아니라, y, x로 한다.
        nums.append([y, x])

    nums.sort()

    # 역시 여기서도 순서가 중요.
    for y, x in nums:
        print(x, y)


# method2()
