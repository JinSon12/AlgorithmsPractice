"""
숨바꼭질

"""
from collections import deque


def findTime_BFS(sb_pos, sis_pos):
    q = deque([[sb_pos, 0]])
    visited = set({sb_pos})
    count = 0

    while q:
        curPos, time = q.popleft()

        if curPos == sis_pos:
            print(time)
            return

        moveRight = curPos + 1
        moveLeft = curPos - 1
        jump = curPos * 2
        # print(moveRight, moveLeft, jump, "time", time + 1, curPos)

        if moveRight not in visited and moveRight <= LIM:
            q.append([moveRight, time + 1])
            visited.add(moveRight)

        if moveLeft not in visited and moveLeft <= LIM:
            q.append([moveLeft, time + 1])
            visited.add(moveLeft)

        if jump not in visited and jump <= LIM:
            q.append([jump, time + 1])
            visited.add(jump)

# 이 방법은 시간은 좀 더 빠르지만 (index 를 직접 access 해서 어떤 거리까지 오는데 걸리는 시간을 기록)
# 공간을 더 차지한다.
# 또한, input의 크기가 반드시 주어져야 한다.


def findTime_BFS_faster(sb_pos, sis_pos):
    time_for_pos = [0] * (LIM + 1)
    q = deque([sb_pos])
    time_for_pos[sb_pos] = 0

    while q:
        cur_pos = q.popleft()

        if cur_pos == sis_pos:
            print(time_for_pos[cur_pos])
            return

        for newx in (cur_pos + 1, cur_pos - 1, cur_pos * 2):
            if 0 <= newx <= LIM and time_for_pos[newx] == 0:
                q.append(newx)
                time_for_pos[newx] = time_for_pos[cur_pos] + 1


LIM = 10 ** 5
SB, SIS = map(int, input().split())
findTime_BFS_faster(SB, SIS)
