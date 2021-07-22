from typing import List


class Solution:

    # time limit exceeded
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        i = 0

        while k >= chalk[i]:
            k -= chalk[i]
            i = (i+1) % len(chalk)

        return i

    """
    reflection: 

    - there is a total number of usage of chalks for all the students (sum of all usage of students)
    - that's going to be the usage for each round. 
    - similar to finding the remainder of division, 
    - for the last round of using it, there must be someone to replace the chalk. 
    - at the last round, we can use the remainder after using the chalk for many rounds, 
    - use that remainder to subtract each person's usage and the one who will have negative result will be the one to replace it. 
    - O(n)

    """

    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total_usage = sum(chalk)
        leftover = k % total_usage

        for i in range(len(chalk)):
            if leftover - chalk[i] < 0:
                return i

            leftover -= chalk[i]
