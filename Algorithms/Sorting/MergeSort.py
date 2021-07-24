# https://www.geeksforgeeks.org/merge-sort/

""" 
Divide and Conquer!!! 
Draw and Understand!!! 
"""


def mergesort(list):
    # 종료 조건 : 원소가 1개 있을 때.
    if len(list) < 2:
        return list

    mid = len(list) // 2
    # array slicing 할 때 배열의 복제가 일어난다. 이때문에 memory usage 증가.
    start = mergesort(list[:mid])
    end = mergesort(list[mid:])

    sorted_list = []

    l = r = 0
    while l < len(start) and r < len(end):
        if start[l] < end[r]:
            sorted_list.append(start[l])
            l += 1
        else:
            sorted_list.append(end[r])
            r += 1

    sorted_list += start[l:]
    sorted_list += end[r:]
    print(sorted_list)

    return sorted_list


mergesort([1, 3, 4, 5, 2])
