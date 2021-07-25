class Solution:
    """ 
    Key Insight: mathematical thinking, especially vectors. 

    """

    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        direc = (0, 1)

        for i in instructions:
            if i == "G":
                x = x + direc[0]
                y = y + direc[1]
            elif i == "L":
                direc = (-direc[1], direc[0])
            else:
                direc = (direc[1], -direc[0])

        # 이렇게 multiple values equality comparison 할때, 괄호에 넣기.
        # 아니면 답이 틀린다.
        return (x, y) == (0, 0) or direc != (0, 1)

    # no tuple.
    def isRobotBounded_Faster(self, instructions: str) -> bool:
        x, y = 0, 0
        # direc can be a tuple
        dx, dy = 0, 1

        for i in instructions:
            if i == "G":
                x = x + dx
                y = y + dy
            elif i == "L":
                dx, dy = -dy, dx

            else:
                dx, dy = dy, -dx
        print(dx, dy)
        print(x, y)
        # 이렇게 multiple values equality comparison 할때, 괄호에 넣기.
        # 아니면 답이 틀린다.
        return (x == 0 and y == 0) or (dx != 0 or dy != 1)
