""" 
Given an array arr[] of N elements and the task is to count the number of elements from 
this array which are not at the correct position. 

An element is said to be in an incorrect position if its position changes in the array when the array is sorted.

"""


def countEl(arr):
    s_arr = sorted(arr)
    counter = 0

    for i in range(len(arr)):
        if s_arr[i] != arr[i]:
            counter += 1

    return counter
