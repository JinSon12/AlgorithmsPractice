"""
1924. 2007년

월, 일을 주면, 요일을 맞추기 
"""


def findDay(M, D):
    days_31 = set({1, 3, 5, 7, 8, 10, 12})
    days_30 = set({4, 6, 9, 11})
    days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

    num_days = D

    if M != 1:
        for month in range(1, M):
            if month in days_31:
                num_days += 31

            elif month in days_30:
                num_days += 30

            else:
                num_days += 28

    res = days[(num_days % 7)-1]
    print(res)


mon, day = map(int, input().split())
findDay(mon, day)


def findDay_concise():
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    m, d = map(int, input().split())
    day = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

    totalDays = sum(days[:m-1] + d-1)

    print(day[totalDays % 7])
