""" 
Two Sum Array is Sorted

- use Two Pointers approach 
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        answers = []

        p1 = 0      # original array
        p2 = len(numbers) - 1  # res array

        while p1 <= p2:
            n1 = numbers[p1]
            n2 = numbers[p2]

            if n1 + n2 < target:
                p1 += 1

            elif n1 + n2 > target:
                p2 -= 1

            else:
                answers = [p1 + 1, p2 + 1]
                return answers
