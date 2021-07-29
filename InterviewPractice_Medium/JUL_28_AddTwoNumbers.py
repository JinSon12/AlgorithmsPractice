# https://itholic.github.io/python-reverse-string/
# 리스트 슬라이싱, reverse slicing...

""" 
한 줄로 끝나버렸으니 여기서 더 단순화할 수 없을 것처럼 보인다.

하지만 파이썬에선 이런것도 가능하다.

s = 'abcde'
print(s[::-1])  # 'edcba'
문자열을 [::-1] 이라는 인덱스로 호출하면,

아주 단순하게 해당 문자열을 뒤집은 결과를 반환한다.

만약 [3:0:-1] 이라는 인덱스로 호출하면,

3번 인덱스부터 1번 인덱스까지(0번 까지가 아님) 역순으로 출력해준다.

s = 'abcde'
print(s[3:0:-1])  # dcb
[3::-1] 과 같이 출력하면 3번 인덱스부터 0번 인덱스까지 역순으로 출력해준다.

T2. 
list1 = [8,0,7,2]
-2 번 인덱스, 포함, 부터 0번까지 역순으로 출력. 
list2 = list1[-2::-1]
print(list2) -> returns 708

"""

# https://leetcode.com/problems/add-two-numbers/
# Add Two Numbers

"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""




from DataStructures.LinkedList.ListNode.ListNode import ListNode
class Solution:
    # slow, 76 ms, faster than 34.39% ~ 68 ms, faster than 77.06%
    # Memory Usage: 14.4 MB, less than 44.62%
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        # returns the reversed ll to string
        def toList(node):
            res = ""

            while node:
                res += str(node.val)
                node = node.next

            return res[::-1]

        # reverse Linked List
        def reverseLL(node):
            curNode, prev = node, None

            while curNode:
                nextNode = curNode.next
                curNode.next = prev

                prev = curNode
                curNode = nextNode

            return prev

        # construct LL (if res = 807, then we need to make it 7 -> 0 -> 8)
        def toLL(res_list):
            prev = None

            for num in res_list:
                node = ListNode(num)
                node.next = prev
                prev = node

            return prev

        val1 = toList(l1)
        val2 = toList(l2)

        int_res = int(val1) + int(val2)

        res = toLL(str(int_res))

        return res

    # using 전가산기 (full adder),
    # fastest solution, and more concise code.

    def addTwoNumbers_full_adder(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = dummy = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            valsum = val1 + val2 + carry
            digit = valsum % 10
            carry = valsum // 10

            dummy.next = ListNode(digit)
            dummy = dummy.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return root.next
