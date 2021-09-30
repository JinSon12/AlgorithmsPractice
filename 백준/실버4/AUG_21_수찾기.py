"""
1920. 수 찾기. 

이분 탐색 

"""


def findNumber_binarySearch(nums1, nums2):

    nums1.sort()

    for i in range(len(nums2)):
        l = 0
        r = len(nums1) - 1
        mid = (l + r) // 2
        num = nums2[i]
        found = False

        # print(nums1[mid], num)
        while l <= r:
            if nums1[mid] > num:
                r = mid - 1
            elif nums1[mid] < num:
                l = mid + 1
            else:
                # print("mid, num", mid, num)
                print(1)
                found = True
                break

            mid = (l + r) // 2

        if not found:
            print(0)


def findNumber_set(nums1, nums2):

    sn = set(nums1)

    for i in range(len(nums2)):
        if nums2[i] in sn:
            print(1)
        else:
            print(0)


N1 = int(input())
nums1 = list(map(int, input().split()))

N2 = int(input())
nums2 = list(map(int, input().split()))

findNumber_set(nums1, nums2)
