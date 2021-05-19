
def smallerNumbersThanCurrentBruteForce(nums):
    res = []
    counter = 0
    for i in range(0, len(nums)):
        for j in range(0, len(nums)):
            print(nums[i], " ", nums[j])
            if nums[i] > nums[j]:
                counter += 1
                print(counter)
        res.append(counter)
        counter = 0

    print(res)


def smallerNumbersThanCurrentHashMap(nums):
    res = {}

    for i, num in enumerate(sorted(nums)):
        if num not in res:
            res[num] = i

    for i, num in enumerate(nums):
        nums[i] = res[num]

    print(res)


def smallerNumbersThanCurrentCounter(nums):
    li = [0] * (max(nums) + 1)
    print(li)
    for i in nums:
        li[i] = (nums.count(i))
        print(li[i])
    res = [sum(li[:x]) for x in nums]

    print(res)


smallerNumbersThanCurrentCounter([8, 1, 2, 2, 3])
