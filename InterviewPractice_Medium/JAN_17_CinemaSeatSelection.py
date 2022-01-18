"""
Cinema Seat Allocation

https://leetcode.com/problems/cinema-seat-allocation/


"""


from collections import defaultdict


def maxNumberOfFamilies_brute(n, reservedSeats):
    # 시작 좌석과 끝좌석 까지 빈 좌석이 있는지 확인한다.
    def checkRows(start, end, r):
        for i in range(start, end):
            # if that seat is not empty
            # we cannot seat in that row
            if mat[r][i] != 0:
                return False

        return True

    mat = [[0 for _ in range(11)] for _ in range(n+1)]

    # mark seats as seated
    for seat in reservedSeats:
        r, c = seat[0], seat[1]
        mat[r][c] = 1

    groupCount = 0
    for r in range(1, len(mat)):
        canSeatLeft = True
        canSeatRight = True
        if checkRows(2, 5+1, r):
            groupCount += 1
        else:
            canSeatLeft = False

        # if mat[r][6] == 0:
        if checkRows(6, 9+1, r):
            groupCount += 1

        else:
            canSeatRight = False

        if (not canSeatLeft and not canSeatRight) and mat[r][4] == 0:
            if checkRows(4, 7+1, r):
                groupCount += 1

    return groupCount


def maxNumberOfFamilies_dictionary_set(n, reservedSeats):
    # k = row, v = occupied zones
    d = defaultdict(set)
    z1 = {2, 3, 4, 5}
    z2 = {4, 5, 6, 7}
    z3 = {6, 7, 8, 9}

    for seat in reservedSeats:
        k = seat[0]
        v = seat[1]

        if v in z1:
            d[k].add(1)
        if v in z2:
            d[k].add(2)
        if v in z3:
            d[k].add(3)

    count = 2 * n
    for k in d.keys():
        if len(d[k]) == 3:
            count -= 2
        #
        else:
            count -= 1

    return count


print(maxNumberOfFamilies_dictionary_set(
    3, [[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]]))
