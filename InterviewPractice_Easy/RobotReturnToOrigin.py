# https://leetcode.com/problems/robot-return-to-origin/
from collections import Counter
from collections import defaultdict
import collections


class Solution:
    def judgeCircle_1(self, moves: str) -> bool:
        # R, L , U, D
        init_pos = [0, 0]
        for move in moves:
            if move == "R":
                init_pos[0] += 1
            # 여기서부터 if 보다는 elif 쓰는 것이 속도에 더 유리하다.
            # if 을 하면 계속 evaluate 되기 때문이다.
            # else if 는 맞으면 끝, 아니면 계속 진행.
            elif move == "L":
                init_pos[0] -= 1
            elif move == "U":
                init_pos[1] += 1
            elif move == "D":
                init_pos[1] -= 1

            # print(init_pos)

        if init_pos == [0, 0]:
            return True
        return False

    def judgeCircle_2(self, moves: str) -> bool:
      # 이번 솔루션은 u, d 의 갯수를 세어 뺄, 덧셈으로 계산하여 0,0 이 되는 지 확인하면 된다.
      # defaultDict 와 카운터 사용.
        # R, L , U, D
        init_pos = [0, 0]
        pos_cnt = collections.defaultdict(int)

        if init_pos == [0, 0]:
            return True
        return False
