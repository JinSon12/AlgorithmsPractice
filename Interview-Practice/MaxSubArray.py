# https://www.interviewbit.com/problems/max-non-negative-subarray/

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        result = [] 
        maxVal = -1 
        temp = [] 
        
        for i in range(len(A)) : 
            if(A[i] >= 0):
                temp.append(A[i]) 
                if (sum(temp) > maxVal) : 
                    maxVal = sum(temp) 
                    result = temp
            if(A[i] < 0):
                temp = []
            
        return result 