# https://wayhome25.github.io/python/2017/02/26/py-14-list/
# Basics of lists

"""
1. list.index(value) : find the index in a list using value 
2. list.extend([v1, v2]) : add to the back of the list (more effective and faster than '+' operators)
3. list.insert(ind, val) : add value to the index 
4. list.sort() : sort values ascending order
5. list.reverse() : sort values descending order
"""

list1 = ['a', 'b', 'c', 'd']
print(list1.index('b'))  # 1

list2 = [1, 2, 3]
list1.extend(list2)
print(list1)                 # ['a', 'b', 'q', 'f', 1, 2, 3]

list1. insert(1, 'hi')
print(list1)
