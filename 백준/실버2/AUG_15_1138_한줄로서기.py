"""
1138. 한줄로서기 

풀이 방법: 
- DFS 
  - 가능한 모든 순열 탐색. 
  - 주어진 조건에 부합한다면, 
  - 정답으로 간주 
  - 단점: 비효율적이다. 

- Greedy 
  - 키가 가장 작은 사람부터 시작하여 자리 선점. 
  - 키가 커지는 순서대로 탐색하기때문에 다음 사람은 항상 앞 사람보다 키가 클 것. 
  - 답은 0으로 초기화 하고, 각 사람마다 빈 자리의 갯수를 확인하면서 답 list 에서 맞는 position 을 찾기. 

Tip: 
- printing out a list([1,2,3,4]) to 1 2 3 4 format: 
  - print(*listName)

"""

N = int(input())
order = list(map(int, input().split()))


def findOrder(order):
    res = [0] * N

    for i in range(N):
        count = 0
        pos = order[i]

        for j in range(N):
            if pos == count and res[j] == 0:
                res[j] = i + 1
                break

            elif res[j] == 0:
                count += 1

    return res


print(*findOrder(order))


# using enumerate
def enumeration(order):
    reversedList = reversed(order)
    line_list = []

    # for val, height in zip(memory_list, range(people_num, 0, -1)):
    # line_list.insert(int(val), height)

    for idx, val in enumerate(reversedList):
        line_list.insert(int(val), N - idx)

    ans = ' '.join(map(str, line_list))
    print(ans)
