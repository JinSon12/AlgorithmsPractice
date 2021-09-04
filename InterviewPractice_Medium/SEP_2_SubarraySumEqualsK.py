"""
Subarray Sum equals K 

- prefix sum

"""


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        prefixSum = [0]
        prev = 0

        for i in range(len(nums)):
            prefixSum.append(prefixSum[i] + nums[i])

        start = 0
        if k == 0:
            start = 1
        for i in range(1, len(prefixSum)):
            target = prefixSum[i] - k
            # print(target, prefixSum[i])

            for j in range(i):
                if prefixSum[j] == target:
                    # print(target, i,j)
                    total += 1

        # print(prefixSum, total)
        return total

    # using dict to record the values of the sum of subarray (record prefix sum)
    # find the target (currentIndex Value - k) in the dict (sum of subarray before the current element)
    # add the occurences of the target to total.
    def subarraySum_faster(self, nums: List[int], k: int) -> int:
        total = 0
        prefixSum = {0: 1}
        prev = 0
        cur = 0

        for i in range(len(nums)):
            cur = prev + nums[i]
            target = cur - k

            # print(prefixSum)

            if target in prefixSum:
                total += prefixSum[target]

            if prev + nums[i] not in prefixSum:
                prefixSum[prev + nums[i]] = 1
            else:
                prefixSum[prev + nums[i]] += 1

            prev = cur

        return total

    # same logic as the previous one,
    # but more concise.
    def subarraySum_concise_fast(self, nums, k):
        count = 0
        sums = 0
        d = dict()
        d[0] = 1

        for i in range(len(nums)):
            sums += nums[i]
            # use d.get(v, if not value then return 0)
            count += d.get(sums-k, 0)
            d[sums] = d.get(sums, 0) + 1

        return(count)
