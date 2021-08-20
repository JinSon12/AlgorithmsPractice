"""
10799. 쇠막대기 

https://www.acmicpc.net/problem/10799
"""


def findNumRods(s):
    num_rods = 0
    stack = []

    for i in range(len(s)):
        char = s[i]

        if char == "(":
            # 레이저인 경우, 총 막대 길이 += 현재 중첩된 막대 갯수
            if i + 1 < len(s) and s[i+1] == ")":
                num_rods += len(stack)
            else:
                stack.append("(")
                num_rods += 1

        elif char == ")" and s[i-1] != "(":     # 레이저가 아닌 경우만 pop.
            stack.pop()

    return num_rods


print(findNumRods(input()))
