# https://programmers.co.kr/learn/courses/30/lessons/42860

""" 
REVIEW Req. 

Key Insights : 
- Think about the directions of the movement. 
- 1) Vertical (from A~ or Z~ ) 
- 2) Horizontal (moving left or right)

"""


def solution(name):
    answer = 0

    # calculating the minimum # of up and down movements
    # add +1 to ord(c) as we need to switch from A to Z
    num_vert_change = [
        min(ord(c) - ord("A"), ord("Z") - ord(c) + 1) for c in name]

    print(num_vert_change)
    pos = 0

    # calculating the horizontal movements.
    while True:
        answer += num_vert_change[pos]
        num_vert_change[pos] = 0

        if sum(num_vert_change) == 0:
            break

        left = 1
        right = 1

        while num_vert_change[pos-left] == 0:
            left += 1

        while num_vert_change[pos + right] == 0:
            right += 1

        answer += left if left < right else right
        pos += -left if left < right else right

    return answer
