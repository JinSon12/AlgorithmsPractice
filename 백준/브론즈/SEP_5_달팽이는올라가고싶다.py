"""
달팽이는 올라가고 싶다. 

Key Insight: 
- Loop를 사용하지 않고, 수학적으로 계산하여 달팽이가 올라가는데 걸리는 일자 계산하기. 
"""


def calculateDays(up, down, total):
    if (total - up) % (up - down) == 0:  # 마지막 날 올라가고 남은 거리가 하루 동안 갈 수 있는 거리라면.
        return (total - up) // (up - down) + 1
    else:
        return 1 + (total - up) // (up - down) + 1


up, down, total = map(int, input().split())
print(calculateDays(up, down, total))
