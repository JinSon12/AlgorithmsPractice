def sort_descending(nums):
    min_val = min(nums)

    res = []

    for num in nums:
        res.append(num - min_val)

    return res


print(sort_descending([2, 3, 4]))
