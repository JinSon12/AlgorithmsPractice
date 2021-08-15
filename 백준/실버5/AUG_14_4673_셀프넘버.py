def selfNumber(num):
    res = [False for _ in range(0, num+1)]
    res1 = []

    for i in range(1, num + 1):
        temp = 0
        string = str(i)

        for char in string:
            temp += int(char)
        temp += i

        if temp <= num:
            res[temp] = True

    count = -1  # remove 0 (not count) from res
    for i in range(1, len(res)):
        if res[i] == False:
            count += 1
            # print(i)
            res1.append(i)

    # print("count", count)
    return res1


# selfNumber(10000)


def selfnumber_set():
    natural_num = set(range(1, 10001))
    generated_num = set()

    for i in range(1, 10001):
        for j in str(i):
            i += int(j)
        generated_num.add(i)

    # this will leave only the self numbers
    self_num = sorted(natural_num-generated_num)
    for i in self_num:
        print(i)


# https://velog.io/@sch804/파이썬-백준-4673번-셀프넘버
# was modified to be more optimized.
def selfnumber_map():
    res = []
    # 함수 d 구현하기

    def d(n):
        n = n+sum(map(int, str(n)))   # 하이라이트

        return n

    # 생성자가 있는지 확인할 리스트 초기화하기
    a = [0]*10001

    # 생성자 찾기
    for i in range(1, 10001):
        temp = d(i)

        # modification. (instead of storing the temp at a[i], which means that we have to use not in operator for list)
        if temp <= 10000:
            a[temp] = temp

    for i in range(1, 10001):
        # 셀프넘버라면 출력하기
        # 하지만, list 에서 not in (in) 을 하는 것은 시간 저해. rather, if a[i] == 0: ...
        if a[i] == 0:
            res.append(i)
            # print(i)

    return res


# print(selfnumber_map(), selfNumber(10000))

if selfnumber_map() == selfNumber(10000):
    print("true")
else:
    print("false")
