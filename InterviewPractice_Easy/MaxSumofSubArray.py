# https://www.interviewbit.com/problems/max-sum-contiguous-subarray/

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        # using Kadence algo
        cumSum = A[0]
        maxSum = A[0]

        for i in range(1, len(A)):
            cumSum = max(A[i], cumSum + A[i])

            if cumSum > maxSum:
                maxSum = cumSum

        return maxSum
