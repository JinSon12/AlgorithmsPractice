# https://leetcode.com/problems/reorder-data-in-log-files/
# https://leetcode.com/problems/reorder-data-in-log-files/discuss/352878/Python3-Sort-the-list-use-key

""" 
937. Reorder Data in Log Files

Key insights: How to sort properly! 
- using custom sort function. 
- esp. for python, what would be the key (function) for the custom sort function? 
"""


from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        res = []
        l, d = [], []

        for i in logs:
            split = i.split()
            if split[1].isnumeric():
                d.append(i)
            else:
                l.append(i)

        l.sort(key=self.sortfn)
        return l + d

    def sortfn(self, log):
        split = log.split()
        print(split[1], split)
        return split[1:], split[0]

    """
    Fastest Solution: 

    a: a1      b:  9 2 3 1
    a: g1      b:  act car
    a: zo4    b:  4 7
    a: ab1    b:  off key dog
    a: a8      b:  act zoo

    
    By default, sort(key) means to sort the list by key in increasing order.
    if b[0] is letter: key = (0,b,a)   => In the original code, it would be split[1:] and split[0]
    - This also means that sort by 기준 b first, and if they are the same, move on to sort condition a. 

    If b[0] is not letter: key = (1,None,None) 
    effect of use (None,None) is when you sort letter-logs, the digit-logs remain in the same order.
    (1,) is short for (1,None,None).

    step 1: 0 < 1: so letter-logs come before any digit-log.
    we get:
    ["let1 art can","let2 own kit dig","let3 art zero","dig1 8 1 5 1","dig2 3 6"]

    step 2: b and None The letter-logs are sorted lexicographically by contend(b), the digit-logs remain in the same order
    We get:
    ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

    step3: a and None, The letter-logs are sorted lexicographically by identifier(a), the digit-logs remain in the same order.
    We get:
    ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

    """

    def reorderLogFiles_Fastest(self, logs: List[str]) -> List[str]:
        def keysort(log):
            # ident = act,
            # vals = ['g1', 'act', 'car']
            ident, vals = log.split(" ", maxsplit=1)

            # if log == letter => [0, vals, indent], else [1]
            return [0, vals, ident] if vals[0].isalpha() else [1]

        return sorted(logs, key=keysort)

    # This solution uses lambda function for the key of the sort function.
    def reorderLogFiles_Lambda(self, logs):
        letters, digits = [], []

        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))


stn = Solution()
stn.reorderLogFiles(["a1 9 2 3 1", "g1 act car", "zo4 4 7",
                     "ab1 off key dog", "a8 act zoo"])
